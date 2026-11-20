/* ui/review-final/: the Lesson 10 final check's highlights, after the fixes (step 7, 2026-11-20): the shots the Lesson 10
   overview shows beside the 'before' shots taken by the step 7 check (scripts/review_layout.mjs, the same harness).
   Not part of the build.  Usage: node scripts/review_final.mjs */
import { spawn } from 'node:child_process'; import { createServer } from 'node:http'; 
import { mkdtempSync, readFileSync, writeFileSync, mkdirSync } from 'node:fs'; import { tmpdir } from 'node:os';
import { join, normalize, extname } from 'node:path'; import { fileURLToPath } from 'node:url';
const AFTER = join(fileURLToPath(new URL(".", import.meta.url)), ".."), BEFORE = AFTER;
const OUT = join(AFTER, 'ui/review-final'); mkdirSync(OUT, { recursive: true });
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
const SHOTS = [   // [file, page, query, width, height, act]
  ['after-race-browse-1280', 'race-browse', 'race=utmb', 1280, 800, ''],
  ['after-filters-820', 'race-browse', '', 820, 1180, 'sheet'],
  ['after-log-result-1440', 'log-result', '', 1440, 900, ''],
  ['after-race-detail-1440', 'race-detail', 'race=utmb', 1440, 900, ''],
  ['after-results-chosen-1440', 'results-list', 'result=spartan-beast-killington-2025', 1440, 900, ''],
  ['after-log-result-820', 'log-result', '', 820, 1180, ''],
];
for (const [file, page, q, w, h, act] of SHOTS) {
  await send('Emulation.setDeviceMetricsOverride', { width: w, height: h, deviceScaleFactor: 1, mobile: false });
  const l = new Promise(r => wait.push({ m: 'Page.loadEventFired', r })); await send('Page.navigate', { url: base('after') + page + '.html' + (q ? '?' + q : '') }); await Promise.race([l, sl(8000)]);
  await sl(1500);   // a redirect (race-detail on a desktop) loads a second page
  await ev(`document.fonts.ready.then(() => true)`);
  await ev(`new Promise(r => { const f = document.querySelector('iframe.sheet-presenter[src]'); if (!f) return r(1); setTimeout(() => r(1), 5000); const done = () => setTimeout(() => r(1), 800); if (f.contentDocument && f.contentDocument.readyState === 'complete' && f.contentWindow.location.href !== 'about:blank') done(); else f.addEventListener('load', done, { once: true }); })`);
  if (act === 'sheet') await ev(`document.querySelector('.filters-trigger')?.click()`);
  await sl(/race=|result=/.test(q) || act ? 1500 : 400);
  const r = await send('Page.captureScreenshot', { format: 'webp', quality: 70, clip: { x: 0, y: 0, width: w, height: h, scale: 1 } });
  writeFileSync(join(OUT, file + '.webp'), Buffer.from(r.result.data, 'base64'));
}
console.log('review-final: ' + SHOTS.length + ' shots in ui/review-final/');
ws.close(); ch.kill(); for (const v of Object.values(SRV)) v.close(); process.exit(0);
