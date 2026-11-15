#!/usr/bin/env node
/* Before/after of the adaptive shell (Lesson 10 step 3, 2026-11-15), for ui/review-shell.html.
   Two trees over local HTTP: BEFORE (a git worktree of the commit before the step) and AFTER (this working copy).
   The three tab screens (Race browse, Results list, Profile) at 390×844, 820×1180 and 1440×900, dark and light; then the
   tab bar's states in each form on Results list (hover and pressed forced by DevTools on the Discover tab, keyboard
   focus by Tab), after only. Writes ui/review-shell/<shot>.webp and ui/review-shell/shots.json.
   Run from the repo root: node scripts/review_shell.mjs <before-tree>. Not part of the build. */
import { spawn } from 'node:child_process'; import { createServer } from 'node:http';
import { mkdtempSync, readFileSync, writeFileSync, mkdirSync } from 'node:fs'; import { tmpdir } from 'node:os'; import { join, normalize, extname } from 'node:path';
import { fileURLToPath } from 'node:url';
const AFTER = join(fileURLToPath(new URL('.', import.meta.url)), '..'), BEFORE = process.argv[2] || AFTER;
const OUT = (process.argv[3] || '').startsWith('/') ? process.argv[3] : join(AFTER, process.argv[3] || 'ui/review-shell'); mkdirSync(OUT, { recursive: true });
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const T = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.svg': 'image/svg+xml', '.jpg': 'image/jpeg', '.webp': 'image/webp', '.avif': 'image/avif' };
const serve = root => new Promise(r => { const s = createServer((q, res) => { const p = normalize(join(root, decodeURIComponent(new URL(q.url, 'http://x').pathname))); try { const b = readFileSync(p); res.writeHead(200, { 'content-type': T[extname(p)] || 'application/octet-stream' }).end(b); } catch { res.writeHead(404).end(); } }); s.listen(0, '127.0.0.1', () => r(s)); });
const SRV = { before: await serve(BEFORE), after: await serve(AFTER) };
const base = side => `http://127.0.0.1:${SRV[side].address().port}/wireframes/`;
const prof = mkdtempSync(join(tmpdir(), 'rvsh-')); const ch = spawn(CHROME, ['--headless=new', '--disable-gpu', '--hide-scrollbars', '--remote-debugging-port=0', '--user-data-dir=' + prof, 'about:blank'], { stdio: 'ignore' });
const sl = ms => new Promise(r => setTimeout(r, ms)); let port; for (let i = 0; i < 100 && !port; i++) { await sl(100); try { port = readFileSync(join(prof, 'DevToolsActivePort'), 'utf8').split('\n')[0]; } catch {} }
const tg = await (await fetch(`http://127.0.0.1:${port}/json/list`)).json(); const ws = new WebSocket(tg.find(t => t.type === 'page').webSocketDebuggerUrl); await new Promise(r => ws.addEventListener('open', r, { once: true }));
let id = 0; const pend = new Map(), wait = []; ws.addEventListener('message', e => { const m = JSON.parse(e.data); if (m.id && pend.has(m.id)) { pend.get(m.id)(m); pend.delete(m.id); } else if (m.method) wait.filter(w => w.m === m.method).forEach(w => { w.r(m); wait.splice(wait.indexOf(w), 1); }); });
const send = (method, params = {}) => new Promise(r => { const i = ++id; pend.set(i, r); ws.send(JSON.stringify({ id: i, method, params })); });
const ev = async x => (await send('Runtime.evaluate', { expression: x, returnByValue: true, awaitPromise: true })).result?.result?.value;
await send('Page.enable'); await send('DOM.enable'); await send('CSS.enable');
await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });
await send('Page.addScriptToEvaluateOnNewDocument', { source: "try { sessionStorage.setItem('onrace-signed-in', '1'); } catch (e) {}" });
async function go(url, w, h) {
  await send('Emulation.setDeviceMetricsOverride', { width: w, height: h, deviceScaleFactor: 1, mobile: false });
  const l = new Promise(r => wait.push({ m: 'Page.loadEventFired', r })); await send('Page.navigate', { url }); await Promise.race([l, sl(8000)]);
  await ev(`document.fonts.ready.then(() => true)`); await sl(250);
}
async function snap(name) {
  const r = await send('Page.captureScreenshot', { format: 'webp', quality: 82 });
  writeFileSync(join(OUT, name + '.webp'), Buffer.from(r.result.data, 'base64'));
}
const WIDTHS = [['phone', 390, 844], ['tablet', 820, 1180], ['desktop', 1440, 900]];
const SCREENS = [['race-browse', 'Race browse'], ['results-list', 'Results list'], ['profile', 'Profile']];
const shots = [];
for (const [scr, label] of SCREENS) for (const [wn, w, h] of WIDTHS) for (const theme of ['dark', 'light']) {
  for (const side of (wn === 'phone' ? ['after'] : ['before', 'after'])) {
    await go(base(side) + scr + '.html?theme=' + theme, w, h);
    await snap(`${scr}-${wn}-${theme}-${side}`);
  }
  shots.push({ kind: 'screen', key: `${scr}-${wn}-${theme}`, screen: label, width: wn, theme });
}
// the states in each form, after only: Discover forced to :hover, then :active; Results (current) by keyboard
for (const [wn, w, h] of WIDTHS) for (const theme of ['dark', 'light']) {
  for (const st of ['rest', 'hover', 'pressed', 'focus']) {
    await go(base('after') + 'results-list.html?theme=' + theme, w, h);
    if (st === 'hover' || st === 'pressed') {
      const doc = await send('DOM.getDocument', { depth: -1 });
      const q = await send('DOM.querySelector', { nodeId: doc.result.root.nodeId, selector: '.bottom-nav a[data-tab="discover"]' });
      await send('CSS.forcePseudoState', { nodeId: q.result.nodeId, forcedPseudoClasses: st === 'hover' ? ['hover'] : ['hover', 'active'] });
      await sl(150);
    }
    if (st === 'focus') {   // a real Tab, as a keyboard does, until the current tab has the focus (:focus-visible)
      for (let i = 0; i < 80 && !(await ev(`document.activeElement === document.querySelector('.bottom-nav a[aria-current]')`)); i++) {
        await send('Input.dispatchKeyEvent', { type: 'keyDown', key: 'Tab', code: 'Tab', windowsVirtualKeyCode: 9 });
        await send('Input.dispatchKeyEvent', { type: 'keyUp', key: 'Tab', code: 'Tab', windowsVirtualKeyCode: 9 });
      }
      await sl(150);
    }
    const box = await ev(`(() => { const r = document.querySelector('.bottom-nav').getBoundingClientRect(); return [r.left, r.top, r.width, r.height]; })()`);
    const pad = 24, [x, y, bw, bh] = box;
    const clip = { x: Math.max(0, x - pad), y: Math.max(0, y - pad), width: Math.min(w, bw + 2 * pad), height: Math.min(h - Math.max(0, y - pad), bh + 2 * pad), scale: 1 };
    const r = await send('Page.captureScreenshot', { format: 'webp', quality: 85, clip });
    writeFileSync(join(OUT, `states-${wn}-${theme}-${st}.webp`), Buffer.from(r.result.data, 'base64'));
  }
  shots.push({ kind: 'states', key: `states-${wn}-${theme}`, width: wn, theme });
}
writeFileSync(join(OUT, 'shots.json'), JSON.stringify(shots, null, 1));
console.log('review_shell:', shots.length, 'shot groups in', OUT);
ws.close(); ch.kill(); for (const s of Object.values(SRV)) s.close(); process.exit(0);
