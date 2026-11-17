/* ui/review-adaptive.html's shots (Lesson 10 step 4, 2026-11-17): the backlog's defects at 320×568 with 200% text, the
   single-column screens at 820 and 1440, and the selected race card and result row, before (a tree at the commit before
   the step) and after (this tree), dark. Not part of the build.
   Usage: node scripts/review_adaptive.mjs <before-tree> [out-dir, default ui/review-adaptive] */
import { spawn } from 'node:child_process'; import { createServer } from 'node:http';
import { mkdtempSync, readFileSync, writeFileSync, mkdirSync } from 'node:fs'; import { tmpdir } from 'node:os';
import { join, normalize, extname } from 'node:path'; import { fileURLToPath } from 'node:url';
const AFTER = join(fileURLToPath(new URL('.', import.meta.url)), '..'), BEFORE = process.argv[2] || AFTER;
const OUT = (process.argv[3] || '').startsWith('/') ? process.argv[3] : join(AFTER, process.argv[3] || 'ui/review-adaptive'); mkdirSync(OUT, { recursive: true });
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const T = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.svg': 'image/svg+xml', '.jpg': 'image/jpeg', '.webp': 'image/webp', '.avif': 'image/avif' };
const serve = root => new Promise(r => { const s = createServer((q, res) => { const p = normalize(join(root, decodeURIComponent(new URL(q.url, 'http://x').pathname))); try { const b = readFileSync(p); res.writeHead(200, { 'content-type': T[extname(p)] || 'application/octet-stream' }).end(b); } catch { res.writeHead(404).end(); } }); s.listen(0, '127.0.0.1', () => r(s)); });
const SRV = { before: await serve(BEFORE), after: await serve(AFTER) };
const base = side => `http://127.0.0.1:${SRV[side].address().port}/wireframes/`;
const prof = mkdtempSync(join(tmpdir(), 'rvad-')); const ch = spawn(CHROME, ['--headless=new', '--disable-gpu', '--hide-scrollbars', '--remote-debugging-port=0', '--user-data-dir=' + prof, 'about:blank'], { stdio: 'ignore' });
const sl = ms => new Promise(r => setTimeout(r, ms)); let port; for (let i = 0; i < 100 && !port; i++) { await sl(100); try { port = readFileSync(join(prof, 'DevToolsActivePort'), 'utf8').split('\n')[0]; } catch {} }
const tg = await (await fetch(`http://127.0.0.1:${port}/json/list`)).json(); const ws = new WebSocket(tg.find(t => t.type === 'page').webSocketDebuggerUrl); await new Promise(r => ws.addEventListener('open', r, { once: true }));
let id = 0; const pend = new Map(), wait = []; ws.addEventListener('message', e => { const m = JSON.parse(e.data); if (m.id && pend.has(m.id)) { pend.get(m.id)(m); pend.delete(m.id); } else if (m.method) wait.filter(w => w.m === m.method).forEach(w => { w.r(m); wait.splice(wait.indexOf(w), 1); }); });
const send = (method, params = {}) => new Promise(r => { const i = ++id; pend.set(i, r); ws.send(JSON.stringify({ id: i, method, params })); });
const ev = async x => (await send('Runtime.evaluate', { expression: x, returnByValue: true, awaitPromise: true })).result?.result?.value;
await send('Page.enable');
await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });
await send('Page.addScriptToEvaluateOnNewDocument', { source: "try { sessionStorage.setItem('onrace-signed-in', '1'); } catch (e) {}" });
async function go(url, w, h, text) {
  await send('Emulation.setDeviceMetricsOverride', { width: w, height: h, deviceScaleFactor: 1, mobile: false });
  await send('Page.setFontSizes', { fontSizes: { standard: text, fixed: Math.round(text * 13 / 16) } });
  const l = new Promise(r => wait.push({ m: 'Page.loadEventFired', r })); await send('Page.navigate', { url }); await Promise.race([l, sl(8000)]);
  await ev(`document.fonts.ready.then(() => true)`); await sl(300);
}
async function snap(name) {
  const r = await send('Page.captureScreenshot', { format: 'webp', quality: 82 });
  writeFileSync(join(OUT, name + '.webp'), Buffer.from(r.result.data, 'base64'));
}
// [key, page, width, height, text size, what to do before the shot, caption]
const MAP = `document.querySelector('.view-btn[data-view="map"]').click()`;
const SCROLL = `(() => { const s = document.querySelector('.phone-screen'); s.scrollTop = 400; s.dispatchEvent(new Event('scroll')); })()`;
const SHOTS = [
  ['new-password-320', 'new-password.html', 320, 568, 32, '', 'New password'],
  ['results-list-320', 'results-list.html', 320, 568, 32, SCROLL, 'Results list, scrolled'],
  ['race-picker-320', 'race-picker.html', 320, 568, 32, '', 'Race picker'],
  ['race-browse-320', 'race-browse.html', 320, 568, 32, '', 'Race browse'],
  ['race-browse-map-320', 'race-browse.html', 320, 568, 32, MAP + `; setTimeout(() => document.querySelector('.map-placeholder').scrollIntoView(), 50)`, 'Race browse, Map'],
  ['result-detail-320', 'result-detail.html', 320, 568, 32, '', 'Result detail'],
  ['profile-320', 'profile.html', 320, 568, 32, `document.querySelector('.rows').scrollIntoView()`, 'Profile'],
  ['race-detail-820', 'race-detail.html', 820, 1180, 16, '', 'Race detail'],
  ['new-password-1440', 'new-password.html', 1440, 900, 16, '', 'New password'],
  ['result-detail-1440', 'result-detail.html', 1440, 900, 16, '', 'Result detail'],
];
const shots = [];
for (const [key, page, w, h, text, act, cap] of SHOTS) for (const side of ['before', 'after']) {
  await go(base(side) + page, w, h, text);
  if (act) { await ev(act); await sl(400); }
  await snap(`${key}-${side}`); shots.push({ key, side, w, h, text, cap });
}
// the selected state, after only: the first card's link marked as the screens will mark it when the panes come
for (const [key, page, sel, cap] of [['selected-race-card', 'race-browse.html', '.race-card .card-link', 'Race card'], ['selected-result-row', 'results-list.html', '.result-card .card-link', 'Result row']]) for (const theme of ['dark', 'light']) {
  await go(base('after') + page + '?theme=' + theme, 390, 844, 16);
  await ev(`document.querySelectorAll(${JSON.stringify(sel)})[1].setAttribute('aria-current', 'page')`); await sl(150);
  const box = await ev(`(() => { const a = document.querySelectorAll(${JSON.stringify(sel)}); const r0 = a[0].closest('article').getBoundingClientRect(), r2 = a[2].closest('article').getBoundingClientRect(); return [r0.left, r0.top, r2.right - r0.left, r2.bottom - r0.top]; })()`);
  const pad = 12, [x, y, bw, bh] = box;
  const r = await send('Page.captureScreenshot', { format: 'webp', quality: 85, clip: { x: x - pad, y: Math.max(0, y - pad), width: bw + 2 * pad, height: Math.min(844 - Math.max(0, y - pad), bh + 2 * pad), scale: 1 } });
  writeFileSync(join(OUT, `${key}-${theme}.webp`), Buffer.from(r.result.data, 'base64')); shots.push({ key, side: theme, cap, selected: true });
}
writeFileSync(join(OUT, 'shots.json'), JSON.stringify(shots, null, 1));
ws.close(); ch.kill(); for (const s of Object.values(SRV)) s.close(); process.exit(0);
