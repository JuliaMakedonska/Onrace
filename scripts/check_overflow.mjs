#!/usr/bin/env node
/* Horizontal overflow check (2026-10-24): every wireframe page and state, at 390×844 and 320×568 (iPhone SE), fails
   on any horizontal overflow. Dependency-free: it starts the installed Google Chrome headless and drives it over the
   DevTools protocol (Node 18+: fetch and WebSocket built in).

   Fails when, in any state:
   - a rendered element reaches past the screen's left or right edge (outside a container built to scroll sideways);
   - any element scrolls sideways (scrollWidth > clientWidth) that isn't built to: the one sideways scroller by design
     is the active filter chips row (.chips-row), and its own box must still fit the screen.

   Race browse is also checked with 0, 1, 2, 3 and 5 active filters, using the longest chip texts in microcopy.md
   (the region "North America", the sport type "DEKA / functional fitness", a date range across two years) and a
   search chip, in List view, Map view and with the Filters sheet open.

   Usage: node scripts/check_overflow.mjs [--quiet]      exit code 1 on any overflow, 2 if Chrome can't start.
   build_stand.py runs it on every build. */
import { spawn } from 'node:child_process';
import { mkdtempSync, readFileSync, existsSync, rmSync, readdirSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const W = join(ROOT, 'wireframes');
const QUIET = process.argv.includes('--quiet');
const CHROME = ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '/usr/bin/google-chrome', '/usr/bin/chromium', '/usr/bin/chromium-browser'].find(existsSync);
if (!CHROME) { console.error('check_overflow: Google Chrome not found'); process.exit(2); }

// ---------------------------------------------------------------- the states
// Filter sets for Race browse: 0, 1, 2, 3 and 5 active filters, the longest chip texts (microcopy.md: regions,
// sport types, a date range across two years), plus a search chip.
const FILTERS = {
  0: '',
  1: 'sport=deka',
  2: 'region=North%20America&sport=deka',
  3: 'region=North%20America&sport=deka&from=2026-12-28&to=2027-01-03',
  5: 'region=North%20America&sport=deka&sport=half-marathon&sport=triathlon&from=2026-12-28&to=2027-01-03&q=Killington',
};
const CAUSES = {   // the URL switches each state page reads (as the screenshot runs use them)
  'race-detail': ['', 'race=utmb'], 'race-detail-error': ['', 'cause=registration&race=utmb'],
  'results-list': ['', 'saved=Spartan%20Race%20Beast%20%E2%80%94%20Killington'],
  'log-result': ['', 'catalog=spartan-beast-killington-2025'], 'log-result-error': ['cause=fields', 'cause=link', 'cause=submit'],
  'race-picker': ['', 'q=hyrox', 'catalog=utmb-2026'], 'race-picker-empty': ['q=a%20very%20long%20race%20name%20nobody%20has%20heard%20of'],
  'result-detail': ['', 'result=valencia-half-2025'], 'result-detail-error': ['', 'cause=link&result=valencia-half-2025'],
  'sign-in-sign-up': ['', 'mode=signup', 'reset=done'], 'sign-in-sign-up-check-inbox': ['', 'reason=unconfirmed'],
  'sign-in-sign-up-error': ['cause=signin', 'cause=signup&mode=signup', 'cause=confirm'], 'sign-in-sign-up-loading': ['', 'mode=signup'],
  'reset-password-error': ['', 'cause=rate'],
  'new-password-error': ['cause=submit', 'cause=short', 'cause=same', 'cause=mismatch', 'cause=expired'],
  'profile-error': ['', 'cause=save&field=country&value=France&prev=Italy'],
};
const states = [];
for (const f of readdirSync(W).filter(f => f.endsWith('.html') && f !== 'index.html').sort()) {
  const name = f.replace('.html', '');
  if (name.startsWith('race-browse')) {
    for (const [n, q] of Object.entries(FILTERS)) {
      if (name === 'race-browse-error' && n !== '0') continue;   // the error page keeps its filters out of view
      for (const act of ['', 'map', 'sheet']) states.push({ name, q, act, label: `${name} · ${n} filters${act ? ' · ' + act : ''}` });
    }
  } else {
    for (const q of CAUSES[name] || ['']) states.push({ name, q, act: '', label: name + (q ? '?' + q : '') });
  }
}
states.push({ name: 'profile', q: '', act: 'click:#sign-out', label: 'profile · sign-out alert' });
states.push({ name: 'log-result', q: 'race_name=Spartan%20Race%20Beast%20%E2%80%94%20Killington', act: 'click:[data-cancel]', label: 'log-result · discard confirm' });

// ---------------------------------------------------------------- the check, in the page
const CHECK = `(() => {
  const W = innerWidth, bad = [];
  const scrollerX = el => el.matches('.chips-row');   // the one sideways scroller by design
  const name = el => el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') + (el.classList.length ? '.' + [...el.classList].join('.') : '');
  for (const el of document.querySelectorAll('body, body *')) {
    if (!el.getClientRects().length) continue;
    const cs = getComputedStyle(el);
    if (cs.visibility === 'hidden') continue;
    const r = el.getBoundingClientRect();
    if (r.width <= 1 && r.height <= 1) continue;                     // visually hidden text
    if (el.closest('.visually-hidden')) continue;                     // clipped to 1px with it (a busy button's hidden label)
    if (el.closest('.sheet:not(.open)') || el.closest('dialog:not([open])')) continue;   // off-screen until opened
    const inScroller = el.parentElement && el.parentElement.closest('.chips-row');
    if (!inScroller && (r.right > W + 0.5 || r.left < -0.5)) bad.push(name(el) + ' spans ' + Math.round(r.left) + '–' + Math.round(r.right) + ' on a ' + W + 'px screen');
    if (el.scrollWidth > el.clientWidth + 1 && /(auto|scroll)/.test(cs.overflowX) && !scrollerX(el)) bad.push(name(el) + ' scrolls sideways (' + el.scrollWidth + ' > ' + el.clientWidth + ')');
  }
  if (document.documentElement.scrollWidth > W + 1) bad.push('the page scrolls sideways (' + document.documentElement.scrollWidth + ' > ' + W + ')');
  return [...new Set(bad)].slice(0, 6);
})()`;

// ---------------------------------------------------------------- Chrome over the DevTools protocol
const profile = mkdtempSync(join(tmpdir(), 'onrace-overflow-'));
const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu', '--hide-scrollbars', '--no-first-run', '--no-default-browser-check', '--remote-debugging-port=0', '--user-data-dir=' + profile, 'about:blank'], { stdio: 'ignore' });
const cleanup = () => { try { chrome.kill(); } catch {} try { rmSync(profile, { recursive: true, force: true }); } catch {} };
const sleep = ms => new Promise(r => setTimeout(r, ms));
let port = null;
for (let i = 0; i < 100 && !port; i++) {
  await sleep(100);
  try { port = readFileSync(join(profile, 'DevToolsActivePort'), 'utf8').split('\n')[0]; } catch {}
}
if (!port) { console.error('check_overflow: Chrome did not start'); cleanup(); process.exit(2); }
const targets = await (await fetch(`http://127.0.0.1:${port}/json/list`)).json();
const ws = new WebSocket(targets.find(t => t.type === 'page').webSocketDebuggerUrl);
await new Promise(r => ws.addEventListener('open', r, { once: true }));
let seq = 0; const pending = new Map(); const waiters = [];
ws.addEventListener('message', ev => {
  const m = JSON.parse(ev.data);
  if (m.id && pending.has(m.id)) { pending.get(m.id)(m); pending.delete(m.id); }
  else if (m.method) waiters.filter(w => w.method === m.method).forEach(w => { w.resolve(m); waiters.splice(waiters.indexOf(w), 1); });
});
const send = (method, params = {}) => new Promise(r => { const id = ++seq; pending.set(id, r); ws.send(JSON.stringify({ id, method, params })); });
const once = method => new Promise(resolve => waiters.push({ method, resolve }));
const evaluate = async expr => (await send('Runtime.evaluate', { expression: expr, returnByValue: true, awaitPromise: true })).result?.result?.value;
await send('Page.enable'); await send('Runtime.enable');
await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });

const failures = [];
let checked = 0;
for (const [w, h] of [[390, 844], [320, 568]]) {
  await send('Emulation.setDeviceMetricsOverride', { width: w, height: h, deviceScaleFactor: 1, mobile: false });
  for (const s of states) {
    const url = pathToFileURL(join(W, s.name + '.html')).href + (s.q ? '?' + s.q : '');
    const loaded = once('Page.loadEventFired');
    await send('Page.navigate', { url });
    await Promise.race([loaded, sleep(5000)]);
    await sleep(150);
    if (s.act === 'map') await evaluate(`document.querySelector('.view-btn[data-view="map"]')?.click()`);
    if (s.act === 'sheet') await evaluate(`document.querySelector('.filters-trigger')?.click()`);
    if (s.act.startsWith('click:')) await evaluate(`document.querySelector(${JSON.stringify(s.act.slice(6))})?.click()`);
    if (s.act) await sleep(350);
    const bad = await evaluate(CHECK);
    checked++;
    if (bad && bad.length) failures.push(`${w}px · ${s.label}\n    ${bad.join('\n    ')}`);
  }
}
ws.close(); cleanup();
if (failures.length) {
  console.log(`check_overflow: FAIL, horizontal overflow in ${failures.length} of ${checked} states\n` + failures.join('\n'));
  process.exit(1);
}
if (!QUIET) console.log(`check_overflow: pass, no horizontal overflow in ${checked} states (${states.length} per width, 390 and 320)`);
else console.log(`check_overflow: pass (${checked} states)`);
