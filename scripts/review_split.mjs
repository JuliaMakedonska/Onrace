/* ui/review-split.html's shots (Lesson 10 step 5, 2026-11-17): Race browse and Results list as split views at 820 and
   1440, their states, a detail that fails inside its pane, and the phone unchanged, before (a tree at the commit before
   the step) and after (this tree), dark. Not part of the build.
   Usage: node scripts/review_split.mjs <before-tree> [out-dir, default ui/review-split] */
import { spawn } from 'node:child_process'; import { createServer } from 'node:http';
import { mkdtempSync, readFileSync, writeFileSync, mkdirSync } from 'node:fs'; import { tmpdir } from 'node:os';
import { join, normalize, extname } from 'node:path'; import { fileURLToPath } from 'node:url';
const AFTER = join(fileURLToPath(new URL('.', import.meta.url)), '..'), BEFORE = process.argv[2] || AFTER;
const OUT = (process.argv[3] || '').startsWith('/') ? process.argv[3] : join(AFTER, process.argv[3] || 'ui/review-split'); mkdirSync(OUT, { recursive: true });
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const T = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.svg': 'image/svg+xml', '.jpg': 'image/jpeg', '.webp': 'image/webp', '.avif': 'image/avif' };
const serve = root => new Promise(r => { const s = createServer((q, res) => { const p = normalize(join(root, decodeURIComponent(new URL(q.url, 'http://x').pathname))); try { const b = readFileSync(p); res.writeHead(200, { 'content-type': T[extname(p)] || 'application/octet-stream' }).end(b); } catch { res.writeHead(404).end(); } }); s.listen(0, '127.0.0.1', () => r(s)); });
const SRV = { before: await serve(BEFORE), after: await serve(AFTER) };
const base = side => `http://127.0.0.1:${SRV[side].address().port}/wireframes/`;
const prof = mkdtempSync(join(tmpdir(), 'rvsp-')); const ch = spawn(CHROME, ['--headless=new', '--disable-gpu', '--hide-scrollbars', '--remote-debugging-port=0', '--user-data-dir=' + prof, 'about:blank'], { stdio: 'ignore' });
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
const CLICK = sel => `document.querySelector(${JSON.stringify(sel)}).click()`;
const SHOTS = [
  ['race-browse-820', 'race-browse.html', 820, 1180, 16, '', 'Race browse, nothing chosen'],
  ['race-browse-820-chosen', 'race-browse.html', 820, 1180, 16, CLICK('.race-card:nth-child(1) .card-link') + '; void 0', 'Race browse, a race chosen'],
  ['race-browse-1440', 'race-browse.html', 1440, 900, 16, '', 'Race browse, nothing chosen'],
  ['race-browse-1440-chosen', 'race-browse.html?race=utmb', 1440, 900, 16, '', 'Race browse, ?race=utmb'],
  ['results-list-820', 'results-list.html', 820, 1180, 16, '', 'Results list, nothing chosen'],
  ['results-list-1440-chosen', 'results-list.html?result=hyrox-london-2025', 1440, 900, 16, '', 'Results list, ?result=hyrox-london-2025'],
  ['race-browse-loading-1440', 'race-browse-loading.html', 1440, 900, 16, '', 'Race browse, loading'],
  ['race-browse-empty-820', 'race-browse-empty.html?sport=triathlon', 820, 1180, 16, '', 'Race browse, empty'],
  ['results-list-error-1440', 'results-list-error.html', 1440, 900, 16, '', 'Results list, error'],
  ['detail-error-1440', 'results-list.html?result=valencia-half-2025&fail=1', 1440, 900, 16, '', 'Results list, a detail that failed'],
  ['race-browse-390', 'race-browse.html', 390, 844, 16, '', 'Race browse, phone'],
  ['race-browse-320-200', 'race-browse.html?race=utmb', 320, 568, 32, '', 'Race browse, 320 with 200% text'],
];
const shots = [];
for (const [key, page, w, h, text, act, cap] of SHOTS) for (const side of ['before', 'after']) {
  await go(base(side) + page, w, h, text);
  if (act) { await ev(act); }
  await sl(900);
  await snap(`${key}-${side}`); shots.push({ key, side, w, h, text, cap });
}
writeFileSync(join(OUT, 'shots.json'), JSON.stringify(shots, null, 1));
ws.close(); ch.kill(); for (const s of Object.values(SRV)) s.close(); process.exit(0);
