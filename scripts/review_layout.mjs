/* ui/review-layout.html's shots and self-check (Lesson 10 layout pass, 2026-11-18): every screen and every state at 390,
   820 and 1440 (dark), each measured against DESIGN.md → Width → The wide layout. The states are the checks' own
   (scripts/screen_states.mjs: every wireframe page and the states its URL opens, the split view's choices, the sheets
   and alerts, the Saved races example), Race browse at 0 filters, with its sheet and its map. Not part of the build.
   Usage: node scripts/review_layout.mjs [out-dir, default ui/review-layout] */
import { spawn } from 'node:child_process'; import { createServer } from 'node:http'; import { screenStates } from './screen_states.mjs';
import { mkdtempSync, readFileSync, writeFileSync, mkdirSync } from 'node:fs'; import { tmpdir } from 'node:os';
import { join, normalize, extname } from 'node:path'; import { fileURLToPath } from 'node:url';
const AFTER = join(fileURLToPath(new URL(".", import.meta.url)), ".."), BEFORE = AFTER;
const OUT = (process.argv[2] || '').startsWith('/') ? process.argv[2] : join(AFTER, process.argv[2] || 'ui/review-layout'); mkdirSync(OUT, { recursive: true });
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
const WIDTHS = [[390, 844, 0.75], [820, 1180, 0.5], [1440, 900, 0.5]];   // [width, height, the shot's scale]
const states = screenStates(AFTER).filter(s => !s.name.startsWith('../design-system/patterns/'))
  .filter(s => !s.name.startsWith('race-browse') || (s.q === '' && (s.act !== 'map' || s.name === 'race-browse')) || s.act === 'wait');
const ONLY = process.env.ONLY ? process.env.ONLY.split(',') : null;   // a review of some screens only (e.g. ONLY=sign-in,reset-password,new-password for ui/review-gate.html)
const PICK = ONLY ? states.filter(s => ONLY.some(o => s.label.startsWith(o))) : states;
// the spec, measured: every failure is [rule, what was found]
const CHECK = `(() => {
  const f = [], W = innerWidth, H = innerHeight, px = v => parseFloat(v) || 0;
  const wide = matchMedia('(min-width: 48.8125rem)').matches, desk = matchMedia('(min-width: 83.9375rem)').matches;
  const vis = el => el && el.getClientRects().length && getComputedStyle(el).visibility !== 'hidden';
  const rem = px(getComputedStyle(document.documentElement).fontSize);
  const cmax = 42 * rem, paneTop = 16 * rem / 16;
  const se = document.scrollingElement, ps = document.querySelector('body > .phone-screen, .sheet > .phone-screen');
  if (se.scrollWidth > W + 1) f.push(['cropped', 'the page scrolls sideways (' + se.scrollWidth + ' > ' + W + ')']);
  if (ps && ps.scrollWidth > ps.clientWidth + 1) f.push(['cropped', 'the screen scrolls sideways (' + ps.scrollWidth + ' > ' + ps.clientWidth + ')']);
  document.querySelectorAll('.map-placeholder').forEach(m => { if (!vis(m)) return; const r = m.getBoundingClientRect();
    m.querySelectorAll('.map-pin').forEach(p => { if (!vis(p)) return; const q = p.querySelector('span').getBoundingClientRect();
      if (q.left < r.left - 1 || q.right > r.right + 1 || q.top < r.top - 1 || q.bottom > r.bottom + 1) f.push(['cropped', 'the ' + p.textContent.trim() + ' pin is cut by the map']); }); });
  if (!wide) return f;
  const sv = document.querySelector('.split-view'), main = sv && sv.querySelector(':scope > main');
  const split = main && getComputedStyle(main).display === 'grid';
  // one top line: the panes beside the list start where the list's pane starts
  if (split) { const top = main.getBoundingClientRect().top;
    sv.querySelectorAll('.map-area, .split-detail').forEach(p => { if (vis(p) && Math.abs(p.getBoundingClientRect().top - top) > 1 && !sv.querySelector(':scope > .top-bar:not(.top-bar--large)'))
      f.push(['top edge', (p.classList.contains('map-area') ? 'the map' : 'the detail') + ' pane starts at ' + Math.round(p.getBoundingClientRect().top) + ', the list at ' + Math.round(top)]); }); }
  const hd = document.querySelector('body > .phone-screen > main > header');
  if (hd && vis(hd)) { const pt = px(getComputedStyle(hd).paddingTop); if (Math.abs(pt - paneTop) > 1) f.push(['top edge', 'the large title starts ' + pt + 'px below its pane, not --pane-top (' + paneTop + ')']); }
  // the sidebar on the panes' grid
  const nav = document.querySelector('body > .bottom-nav');
  if (desk && nav && vis(nav)) { const r = nav.getBoundingClientRect(), cs = getComputedStyle(nav);
    if (r.left > 1 || r.top > 1 || Math.abs(r.bottom - H) > 1) f.push(['grid', 'the sidebar is inset (' + Math.round(r.left) + ', ' + Math.round(r.top) + ')']);
    if (px(cs.borderRightWidth) < 1) f.push(['grid', 'the sidebar has no divider']);
    if (hd && vis(hd)) { const a = nav.querySelector('a').getBoundingClientRect().top, b = hd.getBoundingClientRect().top + px(getComputedStyle(hd).paddingTop);
      if (Math.abs(a - b) > 2) f.push(['top edge', 'the sidebar first row at ' + Math.round(a) + ', the title at ' + Math.round(b)]); } }
  // no frame inside a pane; no blank map
  if (split) sv.querySelectorAll('.map-placeholder').forEach(m => { if (!vis(m)) return; const cs = getComputedStyle(m);
    if (px(cs.borderTopLeftRadius) > 0 || cs.boxShadow !== 'none') f.push(['frame', 'the map has a frame of its own inside its pane']);
    const mr = m.getBoundingClientRect(), pr = m.parentElement.getBoundingClientRect();
    if (Math.abs(mr.left - pr.left) > 1 || Math.abs(mr.right - pr.right) > 1 || Math.abs(mr.top - pr.top) > 1 || Math.abs(mr.bottom - pr.bottom) > 1) f.push(['frame', 'the map does not fill its pane edge to edge']);
    if (getComputedStyle(m, '::before').content === 'none' && m.getAttribute('aria-busy') !== 'true') f.push(['empty pane', 'the map pane is blank']); });
  // no empty pane without a reason
  const det = sv && sv.querySelector('.split-detail'), emp = det && det.querySelector('.split-empty');
  if (split && vis(det) && vis(emp)) { const cards = sv.querySelectorAll('.list-area .card-link').length, busy = sv.querySelector('.list-area[aria-busy="true"], :scope > main[aria-busy="true"]');
    if (!cards && !busy) f.push(['empty pane', 'the detail pane asks for a choice, with nothing in the list to choose']);
    if (sv.querySelector('.map-area')) f.push(['empty pane', 'an empty detail pane beside the map']); }
  // nothing stretched past --container-max
  const col = document.querySelector('body > .phone-screen > main');
  if (col && !split && col.getBoundingClientRect().width > cmax + 1) f.push(['too wide', 'the column is ' + Math.round(col.getBoundingClientRect().width) + 'px, past --container-max (' + cmax + ')']);
  document.querySelectorAll('.split-content > :not(.action-bar)').forEach(e => { if (vis(e) && e.getBoundingClientRect().width > cmax + 1) f.push(['too wide', 'the detail is ' + Math.round(e.getBoundingClientRect().width) + 'px in its pane']); });
  // gutters: the list keeps the phone's
  if (split) { const la = sv.querySelector('.list-area'); if (vis(la) && Math.abs(px(getComputedStyle(la).paddingLeft) - rem) > 1) f.push(['gutter', 'the list pane gutter is ' + getComputedStyle(la).paddingLeft]); }
  // a form sheet: centred
  const fs = [...document.querySelectorAll('body > .sheet')].find(vis) || (document.body.classList.contains('form-sheet') ? document.body : null);
  if (fs) { const r = fs.getBoundingClientRect(); if (Math.abs(r.left + r.width / 2 - W / 2) > 2) f.push(['sheet', 'the form sheet is off centre by ' + Math.round(r.left + r.width / 2 - W / 2)]); }
  return f;
})()`;
const out = [];
for (const [i, s] of PICK.entries()) for (const [w, h, scale] of WIDTHS) {
  const url = base('after') + s.name + '.html' + (s.q ? '?' + s.q : '');
  await send('Emulation.setDeviceMetricsOverride', { width: w, height: h, deviceScaleFactor: 1, mobile: false });
  const l = new Promise(r => wait.push({ m: 'Page.loadEventFired', r })); await send('Page.navigate', { url }); await Promise.race([l, sl(8000)]);
  await ev(`document.fonts.ready.then(() => true)`); await sl(250);
  if (s.act === 'map') await ev(`document.querySelector('.view-btn[data-view="map"]')?.click()`);
  if (s.act === 'sheet') await ev(`document.querySelector('.filters-trigger')?.click()`);
  if (s.act.startsWith('click:')) await ev(`document.querySelector(${JSON.stringify(s.act.slice(6))})?.click()`);
  await sl(s.act === 'wait' || /race=|result=/.test(s.q) ? 1200 : s.act ? 500 : 150);
  const fails = await ev(CHECK) || [];
  const key = String(i).padStart(3, '0') + '-' + (s.label.replace(/^\.\.\/design-system\//, '').replace(/[^a-z0-9]+/gi, '-').replace(/^-|-$/g, '') ).slice(0, 90) + '-' + w;
  const r = await send('Page.captureScreenshot', { format: 'webp', quality: 70, clip: { x: 0, y: 0, width: w, height: h, scale } });
  writeFileSync(join(OUT, key + '.webp'), Buffer.from(r.result.data, 'base64'));
  out.push({ label: s.label, name: s.name, q: s.q, act: s.act, w, h, key, fails });
}
writeFileSync(join(OUT, 'shots.json'), JSON.stringify(out, null, 1));
console.log(`review-layout: ${out.length} shots, ${out.filter(o => o.fails.length).length} with a failure`);
ws.close(); ch.kill(); for (const v of Object.values(SRV)) v.close(); process.exit(0);
