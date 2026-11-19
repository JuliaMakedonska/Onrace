/* ui/review-webapp.html's shots (2026-11-19, the new direction: the tablet the phone's, the desktop a web app): Race
   browse in every state at 390, 820 and 1440, its map view, a chosen race, the filters open, a race that fails, and
   Results list and Profile under the new navigation, before (a tree at the commit before) and after (this tree), dark.
   Not part of the build.  Usage: node scripts/review_webapp.mjs <before-tree> [out-dir, default ui/review-webapp] */
import { spawn } from 'node:child_process'; import { createServer } from 'node:http';
import { mkdtempSync, readFileSync, writeFileSync, mkdirSync } from 'node:fs'; import { tmpdir } from 'node:os';
import { join, normalize, extname } from 'node:path'; import { fileURLToPath } from 'node:url';
const AFTER = join(fileURLToPath(new URL('.', import.meta.url)), '..'), BEFORE = process.argv[2] || AFTER;
const OUT = (process.argv[3] || '').startsWith('/') ? process.argv[3] : join(AFTER, process.argv[3] || 'ui/review-webapp'); mkdirSync(OUT, { recursive: true });
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
const MAPV = CLICK('.view-btn[data-view="map"]') + '; void 0';
const FILT = "setTimeout(function () { document.getElementById('filters-open').click(); }, 900); void 0";
const WP = [390, 844], WT = [820, 1180], WD = [1440, 900];
const SHOTS = [];
for (const [k, page, cap, acts] of [
  ['rb', 'race-browse.html', 'Race browse', ''],
  ['rb-map', 'race-browse.html', 'Race browse, Map view', 'map'],
  ['rb-chosen', 'race-browse.html?race=utmb', 'Race browse, a race chosen (?race=utmb)', ''],
  ['rb-filters', 'race-browse.html?race=utmb', 'Race browse, the filters open', 'filters'],
  ['rb-loading', 'race-browse-loading.html', 'Race browse, loading', ''],
  ['rb-empty', 'race-browse-empty.html', 'Race browse, empty (no race matches)', ''],
  ['rb-error', 'race-browse-error.html', 'Race browse, error', ''],
  ['rb-fail', 'race-browse.html?race=spartan-beast-killington&fail=1', 'Race browse, a race that fails to load', ''],
  ['rl', 'results-list.html?result=hyrox-london-2025', 'Results list under the new navigation', ''],
  ['pr', 'profile.html', 'Profile under the new navigation', ''],
]) for (const [w, h] of [WP, WT, WD]) {
  if (acts === 'map' && w === 1440) continue;   // a desktop has no List / Map switch: the map is always there
  if (['rb-fail', 'rl', 'pr'].includes(k) && w === 390) continue;   // unchanged on a phone
  SHOTS.push([`${k}-${w}`, page, w, h, 16, acts === 'map' ? MAPV : acts === 'filters' ? FILT : '', cap]);
}
const shots = [];
for (const [key, page, w, h, text, act, cap] of SHOTS) for (const side of ['before', 'after']) {
  await go(base(side) + page, w, h, text);
  if (act) { await ev(act); }
  await sl(1500);
  await snap(`${key}-${side}`); shots.push({ key, side, w, h, text, cap });
}
writeFileSync(join(OUT, 'shots.json'), JSON.stringify(shots, null, 1));
ws.close(); ch.kill(); for (const s of Object.values(SRV)) s.close(); process.exit(0);
