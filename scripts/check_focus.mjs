#!/usr/bin/env node
/* Focus halo and sheet bar (designer, 2026-11-08): every screen state (scripts/screen_states.mjs, the same states as
   check_overflow.mjs) at 320×568 with the default text size and at 390×844 with 200% text, in headless Chrome over local
   HTTP with the real fonts. Fails when, in any state:
   - the sheet bar (.sheet > .top-bar, every open sheet): a capsule leaves the bar's inner edges, its text overflows the
     capsule, two capsules collide, a capsule overlaps the title, or the title wraps or overflows without its "…";
   - the focus halo: Tab walks every focusable element; each one must match :focus-visible and draw a halo (an outline
     on itself, a child, or a ::before / ::after), and no ancestor that clips (hidden, clip, a scroller's content box)
     may cut it, nor the screen's edge.
   Open, not checked (concept/concept.md → Large text and keyboard focus; design-system/backlog.md → Lesson 10): 320 with
   200% text, and a map pin whose label already runs past the map's frame at 200% text (the label is cut with its halo:
   moving the labels is Lesson 10's). A pin whose label fits is checked like everything else.
   Usage: node scripts/check_focus.mjs [--quiet] [--only race-browse,profile]. build_stand.py runs it; exit 1 on a
   failure, 2 if Chrome can't start, 3 if the fonts didn't load (Google Fonts unreachable: scripts/ship.sh retries). */
import { spawn } from 'node:child_process';
import { createServer } from 'node:http';
import { mkdtempSync, readFileSync, existsSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, dirname, normalize, extname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenStates } from './screen_states.mjs';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const QUIET = process.argv.includes('--quiet');
const CHROME = ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '/usr/bin/google-chrome', '/usr/bin/chromium', '/usr/bin/chromium-browser'].find(existsSync);
if (!CHROME) { console.error('check_focus: Google Chrome not found'); process.exit(2); }
const PASSES = [[320, 568, 16], [390, 844, 32]];   // [width, height, default font size]: 32 is 200% text
let states = screenStates(ROOT);
const ONLY = process.argv.includes('--only') ? process.argv[process.argv.indexOf('--only') + 1].split(',') : null;
if (ONLY) states = states.filter(s => ONLY.some(o => s.label.includes(o)));

// ---------------------------------------------------------------- in the page: the sheet bars
const BAR = `(() => {
  const bad = [], info = [];
  const name = el => el.tagName.toLowerCase() + (el.classList.length ? '.' + [...el.classList].join('.') : '') + ' "' + el.textContent.trim().replace(/\\s+/g, ' ').slice(0, 30) + '"';
  for (const bar of document.querySelectorAll('.sheet > .top-bar')) {
    if (!bar.getClientRects().length || bar.closest('[hidden]')) continue;
    const br = bar.getBoundingClientRect(), bcs = getComputedStyle(bar);
    const inner = { l: br.left + parseFloat(bcs.paddingLeft), r: br.right - parseFloat(bcs.paddingRight) };
    const caps = [...bar.children].filter(c => c.matches('a, button') && c.getClientRects().length);
    const title = bar.querySelector('.bar-title'); if (!title) { bad.push('sheet bar: no title'); continue; }
    const tr = title.getBoundingClientRect(), rs = caps.map(c => c.getBoundingClientRect());
    caps.forEach((c, i) => {
      const r = rs[i];
      if (r.left < inner.l - 0.5 || r.right > inner.r + 0.5) bad.push('sheet bar: ' + name(c) + ' leaves the bar');
      if (c.scrollWidth > c.clientWidth + 1) bad.push('sheet bar: ' + name(c) + ' text overflows its capsule');
      if (r.right > tr.left + 0.5 && r.left < tr.right - 0.5) bad.push('sheet bar: ' + name(c) + ' overlaps the title');
    });
    for (let i = 0; i < rs.length; i++) for (let j = i + 1; j < rs.length; j++) if (rs[i].right > rs[j].left + 0.5 && rs[i].left < rs[j].right - 0.5) bad.push('sheet bar: the capsules collide');
    const cs = getComputedStyle(title), cut = title.scrollWidth > title.clientWidth + 0.5;
    if (cut && (cs.textOverflow !== 'ellipsis' || cs.overflowX === 'visible')) bad.push('sheet bar: the title overflows without its ellipsis');
    if (title.getClientRects().length > 1 || tr.height > parseFloat(cs.lineHeight) * 1.5) bad.push('sheet bar: the title wraps');
    info.push('"' + title.textContent.trim() + '" ' + Math.round(tr.width) + 'px' + (cut ? ', truncated' : ''));
  }
  return { bad, info };
})()`;

// ---------------------------------------------------------------- in the page: the focused element's halo
const HALO = `(() => {
  const el = document.activeElement;
  if (!el || el === document.body) return null;
  const txt = el.textContent.trim().replace(/\\s+/g, ' ').slice(0, 30);
  const name = el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') + (el.classList.length ? '.' + [...el.classList].join('.') : '') + (txt ? ' "' + txt + '"' : el.getAttribute('aria-label') ? ' [' + el.getAttribute('aria-label') + ']' : '');
  const fv = el.matches(':focus-visible');
  // the box a pseudo-element is placed in: its own element when that is positioned, or the nearest positioned ancestor
  const block = (c, pos) => { if (pos === 'fixed') return { left: 0, top: 0 }; let b = c;
    while (b && b !== document.documentElement && getComputedStyle(b).position === 'static') b = b.parentElement;
    const r = (b || document.documentElement).getBoundingClientRect(), s = getComputedStyle(b || document.documentElement);
    return { left: r.left + parseFloat(s.borderLeftWidth), top: r.top + parseFloat(s.borderTopWidth) }; };
  let host = null, rect = null, ring = 0, off = 0;
  const cands = [el, ...el.children, el.parentElement, el.parentElement?.parentElement].filter(Boolean);
  for (const c of cands) {
    const cs = getComputedStyle(c);
    if (cs.outlineStyle !== 'none' && parseFloat(cs.outlineWidth) > 0) { host = c; rect = c.getBoundingClientRect(); ring = parseFloat(cs.outlineWidth); off = parseFloat(cs.outlineOffset); break; }
    for (const ps of ['::before', '::after']) {
      const p = getComputedStyle(c, ps);
      if (p.content === 'none' || p.outlineStyle === 'none' || !(parseFloat(p.outlineWidth) > 0)) continue;
      const W = parseFloat(p.width) + parseFloat(p.paddingLeft) + parseFloat(p.paddingRight) + parseFloat(p.borderLeftWidth) + parseFloat(p.borderRightWidth);
      const Hh = parseFloat(p.height) + parseFloat(p.paddingTop) + parseFloat(p.paddingBottom) + parseFloat(p.borderTopWidth) + parseFloat(p.borderBottomWidth);
      const o = block(c, p.position);
      const L = o.left + parseFloat(p.left), T = o.top + parseFloat(p.top);
      rect = { left: L, top: T, right: L + W, bottom: T + Hh }; ring = parseFloat(p.outlineWidth); off = parseFloat(p.outlineOffset); host = c; break;
    }
    if (host) break;
  }
  if (!host) return { name, fv, problem: 'no halo' };
  const e = off + ring, H = { l: rect.left - e, t: rect.top - e, r: rect.right + e, b: rect.bottom + e };
  const out = []; let underScroller = false, labelCut = false;
  for (let a = host.parentElement; a && a !== document.documentElement; a = a.parentElement) {
    const cs = getComputedStyle(a), ox = cs.overflowX, oy = cs.overflowY;
    if (ox === 'visible' && oy === 'visible') continue;
    const r = a.getBoundingClientRect(), cm = ox === 'clip' ? (parseFloat(cs.overflowClipMargin.replace(/^[a-z-]+\\s*/, '')) || 0) : 0;
    const box = { l: r.left + parseFloat(cs.borderLeftWidth) - cm, t: r.top + parseFloat(cs.borderTopWidth) - cm, r: r.right - parseFloat(cs.borderRightWidth) + cm, b: r.bottom - parseFloat(cs.borderBottomWidth) + cm };
    const sx = /(auto|scroll)/.test(ox), sy = /(auto|scroll)/.test(oy);
    // a scroller: what can be scrolled into view counts; hidden or clip: the box as it stands
    const lim = { l: box.l - (sx ? a.scrollLeft : 0), t: box.t - (sy ? a.scrollTop : 0) };
    lim.r = sx ? lim.l + a.scrollWidth : box.r; lim.b = sy ? lim.t + a.scrollHeight : box.b;
    const cut = [];
    if (H.l < lim.l - 0.5) cut.push('left ' + (lim.l - H.l).toFixed(1));
    if (H.r > lim.r + 0.5) cut.push('right ' + (H.r - lim.r).toFixed(1));
    if (H.t < lim.t - 0.5) cut.push('top ' + (lim.t - H.t).toFixed(1));
    if (H.b > lim.b + 0.5) cut.push('bottom ' + (H.b - lim.b).toFixed(1));
    if (cut.length) {
      // a map pin whose label already runs past the frame (Lesson 10): the label is cut too, so it is reported apart
      const hr = host.getBoundingClientRect();
      if (el.matches('.map-pin') && (hr.left < box.l + cm - 0.5 || hr.right > box.r - cm + 0.5)) labelCut = true;
      else out.push('cut by ' + a.tagName.toLowerCase() + (a.id ? '#' + a.id : '') + (a.classList.length ? '.' + [...a.classList].join('.') : '') + ' (' + ox + '/' + oy + '): ' + cut.join(', '));
    }
    if (sx || sy) { underScroller = true; break; }
  }
  if (!underScroller && (H.l < -0.5 || H.r > innerWidth + 0.5)) out.push('past the screen edge');
  return { name, fv, problem: out.join('; '), labelCut };
})()`;

const FACES = ['800 1em "Schibsted Grotesk"', '400 1em "Hanken Grotesk"', '600 1em "Hanken Grotesk"'];
const FONTS = `(async () => { await document.fonts.ready; const f = ${JSON.stringify(FACES)}; await Promise.all(f.map(x => document.fonts.load(x).catch(() => null))); return f.every(x => document.fonts.check(x)); })()`;

// ---------------------------------------------------------------- the pages over HTTP, Chrome over the DevTools protocol
const TYPES = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.mjs': 'text/javascript', '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg', '.webp': 'image/webp', '.avif': 'image/avif', '.woff2': 'font/woff2' };
const server = createServer((req, res) => {
  const path = normalize(join(ROOT, decodeURIComponent(new URL(req.url, 'http://x').pathname)));
  if (!path.startsWith(ROOT)) { res.writeHead(403).end(); return; }
  let body; try { body = readFileSync(path); } catch { res.writeHead(404).end(); return; }
  res.writeHead(200, { 'content-type': TYPES[extname(path)] || 'application/octet-stream' }).end(body);
});
await new Promise(r => server.listen(0, '127.0.0.1', r));
const BASE = `http://127.0.0.1:${server.address().port}/wireframes/`;
const profile = mkdtempSync(join(tmpdir(), 'onrace-focus-'));
const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu', '--hide-scrollbars', '--no-first-run', '--no-default-browser-check', '--remote-debugging-port=0', '--user-data-dir=' + profile, 'about:blank'], { stdio: 'ignore' });
const cleanup = () => { server.close(); try { chrome.kill(); } catch {} try { rmSync(profile, { recursive: true, force: true }); } catch {} };
const sleep = ms => new Promise(r => setTimeout(r, ms));
let port = null;
for (let i = 0; i < 100 && !port; i++) { await sleep(100); try { port = readFileSync(join(profile, 'DevToolsActivePort'), 'utf8').split('\n')[0]; } catch {} }
if (!port) { console.error('check_focus: Chrome did not start'); cleanup(); process.exit(2); }
const targets = await (await fetch(`http://127.0.0.1:${port}/json/list`)).json();
const ws = new WebSocket(targets.find(t => t.type === 'page').webSocketDebuggerUrl);
await new Promise(r => ws.addEventListener('open', r, { once: true }));
let seq = 0; const pending = new Map(), waiters = [];
ws.addEventListener('message', ev => {
  const m = JSON.parse(ev.data);
  if (m.id && pending.has(m.id)) { pending.get(m.id)(m); pending.delete(m.id); }
  else if (m.method) waiters.filter(w => w.method === m.method).forEach(w => { w.resolve(m); waiters.splice(waiters.indexOf(w), 1); });
});
const send = (method, params = {}) => new Promise(r => { const id = ++seq; pending.set(id, r); ws.send(JSON.stringify({ id, method, params })); });
const once = method => new Promise(resolve => waiters.push({ method, resolve }));
const evaluate = async expr => (await send('Runtime.evaluate', { expression: expr, returnByValue: true, awaitPromise: true })).result?.result?.value;
const key = async () => { for (const type of ['keyDown', 'keyUp']) await send('Input.dispatchKeyEvent', { type, key: 'Tab', code: 'Tab', windowsVirtualKeyCode: 9 }); };
await send('Page.enable'); await send('Runtime.enable');
await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });

const bad = [], open = []; let walked = 0, focused = 0, bars = 0, noFonts = 0;
for (const [w, h, text] of PASSES) {
  await send('Emulation.setDeviceMetricsOverride', { width: w, height: h, deviceScaleFactor: 1, mobile: false });
  await send('Page.setFontSizes', { fontSizes: { standard: text, fixed: Math.round(text * 13 / 16) } });
  for (const s of states) {
    const tag = `${w}px${text === 32 ? ', 200% text' : ''} · ${s.label}`;
    let fontsOk = false;
    for (let t = 0; t < 2 && !fontsOk; t++) {   // a page whose fonts didn't load is loaded once more
      const loaded = once('Page.loadEventFired');
      await send('Page.navigate', { url: BASE + s.name + '.html' + (s.q ? '?' + s.q : '') });
      await Promise.race([loaded, sleep(5000)]);
      fontsOk = await evaluate(FONTS);
    }
    if (!fontsOk) { noFonts++; bad.push(tag + ' · the fonts did not load'); continue; }
    await sleep(100);
    if (s.act === 'map') await evaluate(`document.querySelector('.view-btn[data-view="map"]')?.click()`);
    if (s.act === 'sheet') await evaluate(`document.querySelector('.filters-trigger')?.click()`);
    if (s.act.startsWith('click:')) await evaluate(`document.querySelector(${JSON.stringify(s.act.slice(6))})?.click()`);
    if (s.act) await sleep(350);
    walked++;
    const b = await evaluate(BAR);
    bars += b.info.length; b.bad.forEach(x => bad.push(tag + ' · ' + x));
    const seen = new Set();
    for (let i = 0; i < 80; i++) {
      await key(); await sleep(20);
      const r = await evaluate(HALO);
      if (!r) continue;
      if (seen.has(r.name)) break;   // back to the first: every element walked
      seen.add(r.name); focused++;
      if (!r.fv) bad.push(tag + ' · ' + r.name + ' · focused but not :focus-visible');
      else if (r.problem) bad.push(tag + ' · ' + r.name + ' · halo ' + r.problem);
      if (r.labelCut) open.push(tag + ' · ' + r.name);
    }
  }
}
ws.close(); cleanup();
if (noFonts && noFonts === bad.length) { console.log(`check_focus: the fonts did not load on ${noFonts} states (Google Fonts unreachable?): not measured, exit 3`); process.exit(3); }
if (bad.length) { console.log(`check_focus: FAIL (${bad.length})`); bad.forEach(x => console.log('  ' + x)); process.exit(1); }
const pins = [...new Set(open.map(x => x.split(' · ').pop()))];
console.log(`check_focus: pass (${walked} states at 320 and at 390 with 200% text: ${focused} focus stops, each halo whole; ${bars} sheet bars, nothing collides)`
  + (QUIET ? '' : `\n  open (Lesson 10, not checked): map pins whose label runs past the frame at 200% text, ${pins.join(', ') || 'none'}`));
