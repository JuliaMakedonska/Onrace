#!/usr/bin/env node
/* Before/after of every component state (Lesson 9 step 3, 2026-11-05), for ui/review-states.html.
   Two trees, served over local HTTP: BEFORE (a git worktree of the commit before the step) and AFTER (this working copy).
   On each tree's specimens.html, for every component in ui/inventory.md → States map: the named stage's control in its
   real state, forced by Chrome DevTools (CSS.forcePseudoState: :hover and :active on the control and its ancestors, as a
   real pointer does; :focus and :focus-visible on the focus target), or with the real disabled attribute, never the
   docs' stand-ins, so the before is the old CSS's own answer. Then the changed screen states at 390×844. Dark and light.
   Writes ui/review-states/<shot>-<theme>-<before|after>.webp and ui/review-states/shots.json (which pairs differ).
   Run from the repo root: node scripts/review_states.mjs <before-tree> <states-map.json> [out-dir] [screens.json]. Not part of the build. */
import { spawn } from 'node:child_process'; import { createServer } from 'node:http';
import { mkdtempSync, readFileSync, writeFileSync, mkdirSync, rmSync } from 'node:fs'; import { tmpdir } from 'node:os'; import { join, normalize, extname } from 'node:path';
import { fileURLToPath } from 'node:url'; import { createHash } from 'node:crypto';
const AFTER = join(fileURLToPath(new URL('.', import.meta.url)), '..'), BEFORE = process.argv[2], MAP = JSON.parse(readFileSync(process.argv[3], 'utf8'));
const OUT = join(AFTER, process.argv[4] || 'ui/review-states'); mkdirSync(OUT, { recursive: true });   // [out dir] [screens.json]: the Step 3 follow-ups write ui/review-states-2
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const T = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.svg': 'image/svg+xml', '.jpg': 'image/jpeg', '.webp': 'image/webp', '.avif': 'image/avif' };
const serve = root => new Promise(r => { const s = createServer((q, res) => { const p = normalize(join(root, decodeURIComponent(new URL(q.url, 'http://x').pathname))); try { const b = readFileSync(p); res.writeHead(200, { 'content-type': T[extname(p)] || 'application/octet-stream', 'cache-control': 'no-store' }).end(b); } catch { res.writeHead(404).end(); } }); s.listen(0, '127.0.0.1', () => r(s)); });
const SRV = { before: await serve(BEFORE), after: await serve(AFTER) };
const base = side => `http://127.0.0.1:${SRV[side].address().port}/`;
const prof = mkdtempSync(join(tmpdir(), 'rvs-')); const ch = spawn(CHROME, ['--headless=new', '--disable-gpu', '--remote-debugging-port=0', '--user-data-dir=' + prof, 'about:blank'], { stdio: 'ignore' });
const sl = ms => new Promise(r => setTimeout(r, ms)); let port; for (let i = 0; i < 100 && !port; i++) { await sl(100); try { port = readFileSync(join(prof, 'DevToolsActivePort'), 'utf8').split('\n')[0]; } catch {} }
const tg = await (await fetch(`http://127.0.0.1:${port}/json/list`)).json(); const ws = new WebSocket(tg.find(t => t.type === 'page').webSocketDebuggerUrl); await new Promise(r => ws.addEventListener('open', r, { once: true }));
let id = 0; const pend = new Map(), wait = []; ws.addEventListener('message', e => { const m = JSON.parse(e.data); if (m.id && pend.has(m.id)) { pend.get(m.id)(m); pend.delete(m.id); } else if (m.method) wait.filter(w => w.m === m.method).forEach(w => { w.r(m); wait.splice(wait.indexOf(w), 1); }); });
const send = (method, params = {}) => new Promise(r => { const i = ++id; pend.set(i, r); ws.send(JSON.stringify({ id: i, method, params })); });
const ev = async x => (await send('Runtime.evaluate', { expression: x, returnByValue: true, awaitPromise: true })).result?.result?.value;
await send('Page.enable'); await send('DOM.enable'); await send('CSS.enable');
await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });   // no transitions mid-shot
await send('Page.addScriptToEvaluateOnNewDocument', { source: "try { sessionStorage.setItem('onrace-signed-in', '1'); } catch (e) {}" });
async function go(url, w, h) {
  await send('Emulation.setDeviceMetricsOverride', { width: w, height: h, deviceScaleFactor: 2, mobile: false });
  const l = new Promise(r => wait.push({ m: 'Page.loadEventFired', r })); await send('Page.navigate', { url }); await Promise.race([l, sl(8000)]);
  await ev(`(async () => { await document.fonts.ready; for (const f of document.querySelectorAll('iframe')) { for (let i = 0; i < 60 && !(f.contentDocument && f.contentDocument.readyState === 'complete'); i++) await new Promise(r => setTimeout(r, 50)); try { await f.contentDocument.fonts.ready; } catch (e) {} } await new Promise(r => setTimeout(r, 400)); })()`);
}
function findMarked(node, out = {}, path = []) {   // nodes carrying data-rv, with the node ids of their ancestors
  const a = node.attributes || []; for (let i = 0; i < a.length; i += 2) if (a[i] === 'data-rv') for (const k of a[i + 1].split(' ')) out[k] = { id: node.nodeId, path: [...path] };
  const kids = [...(node.children || []), ...(node.contentDocument ? [node.contentDocument] : [])];
  for (const k of kids) findMarked(k, out, [...path, node.nodeId]); return out;
}
const shots = [];
async function shot(name, theme, side, clip) {
  const r = await send('Page.captureScreenshot', { format: 'webp', quality: 90, captureBeyondViewport: true, clip: { ...clip, scale: 1 } });
  const f = `${name}-${theme}-${side}.webp`; writeFileSync(join(OUT, f), Buffer.from(r.result.data, 'base64')); return r.result.data;
}
const STATES = ['At rest', 'Hover', 'Pressed', 'Focus', 'Disabled', 'Invalid'];
const slug = s => s.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
const data = {};
for (const theme of ['dark', 'light']) for (const side of ['before', 'after']) {
  await go(base(side) + `design-system/docs/specimens.html?theme=${theme}`, 1280, 900);
  for (const [name, m] of Object.entries(MAP)) for (const st of STATES) {
    if (st === 'Invalid' && !m.invalid) continue;
    const key = `${slug(name)}-${slug(st)}`;
    // mark the control, its keep and focus target; set disabled; return the clip
    const clip = await ev(`(() => {
      const m = ${JSON.stringify(m)}, st = ${JSON.stringify(st)};
      const lab = (st === 'Invalid' ? m.invalid : m.stage).toLowerCase();
      const stage = [...document.querySelectorAll('#' + m.spec + ' .kit-states > .kit-state')].find(s => s.querySelector('.kit-label').textContent.toLowerCase().includes(lab));
      if (!stage) return { err: 'no stage ' + lab };
      let root = stage.querySelector('.kit-frame'), off = { x: 0, y: 0 };
      const ifr = root.querySelector('iframe'); if (ifr) { const r = ifr.getBoundingClientRect(); off = { x: r.left, y: r.top }; root = ifr.contentDocument; }
      const ctl = root.querySelector(m.control) || (m.control === '.is-destructive' ? root.querySelector('#signout-confirm') : null); if (!ctl) return { err: 'no control ' + m.control };
      const keep = (m.keep && ctl.closest(m.keep)) || ctl;
      const foc = (m.focus && ctl.querySelector(m.focus)) || ctl;
      ctl.setAttribute('data-rv', 'c'); foc.setAttribute('data-rv', (foc === ctl ? 'c ' : '') + 'f');
      window.__undo = [];
      if (st === 'Disabled') {
        const ts = m.disabled && m.disabled.startsWith('*') ? [...keep.querySelectorAll(m.disabled.slice(1))] : [(m.disabled && ctl.querySelector(m.disabled)) || ctl];
        for (const t of ts) { const a = /^(BUTTON|INPUT|SELECT|TEXTAREA)$/.test(t.tagName) ? 'disabled' : 'aria-disabled'; if (!t.hasAttribute(a)) { t.setAttribute(a, a === 'disabled' ? '' : 'true'); window.__undo.push([t, a]); } }
      }
      keep.scrollIntoView({ block: 'center' });
      const ir = ifr ? ifr.getBoundingClientRect() : { left: 0, top: 0 };
      const r = keep.getBoundingClientRect(), P = 12;
      return { x: Math.max(0, r.left + ir.left - P), y: Math.max(0, r.top + ir.top + scrollY - P), width: r.width + 2 * P, height: r.height + 2 * P };
    })()`);
    if (!clip || clip.err) { console.log(name, st, side, theme, clip && clip.err); continue; }
    const doc = (await send('DOM.getDocument', { depth: -1, pierce: true })).result.root;
    const mk = findMarked(doc); const forced = [];
    if (st === 'Hover' || st === 'Pressed') for (const n of [...mk.c.path, mk.c.id]) { await send('CSS.forcePseudoState', { nodeId: n, forcedPseudoClasses: st === 'Hover' ? ['hover'] : ['hover', 'active'] }); forced.push(n); }
    if (st === 'Focus') { await send('CSS.forcePseudoState', { nodeId: mk.f.id, forcedPseudoClasses: ['focus', 'focus-visible'] }); forced.push(mk.f.id); for (const n of mk.f.path) { await send('CSS.forcePseudoState', { nodeId: n, forcedPseudoClasses: ['focus-within'] }); forced.push(n); } }
    await sl(120);
    await shot(key, theme, side, clip);
    // what changed is read from the computed styles of the part shot (and its ::before / ::after), not from pixels:
    // the two pages place it at different subpixel offsets, so the same pixels never quite match
    const sig = await ev(`(() => {
      const P = ['color', 'background-color', 'box-shadow', 'outline-style', 'outline-color', 'outline-width', 'outline-offset', 'opacity', 'border-top-left-radius', 'border-top-color', 'transform', 'text-decoration-color', 'font-weight', 'font-size', 'width', 'height'];
      let k = document.querySelector('[data-rv~="c"]'); let win = window;
      if (!k) for (const f of document.querySelectorAll('iframe')) { try { const x = f.contentDocument.querySelector('[data-rv~="c"]'); if (x) { k = x; win = f.contentWindow; } } catch (e) {} }
      const m = ${JSON.stringify(m)}; const keep = (m.keep && k.closest(m.keep)) || k;
      const out = [];
      for (const el of [keep, ...keep.querySelectorAll('*')]) for (const ps of [null, '::before', '::after']) { const cs = win.getComputedStyle(el, ps); out.push(P.map(p => cs.getPropertyValue(p)).join('|')); }
      return out.join('\\n');
    })()`);
    (data[key] ||= { component: name, state: st, kind: 'component' })[`${theme}-${side}`] = createHash('sha1').update(String(sig)).digest('hex');
    for (const n of forced) await send('CSS.forcePseudoState', { nodeId: n, forcedPseudoClasses: [] });
    await ev(`(() => { (window.__undo || []).forEach(([t, a]) => t.removeAttribute(a)); document.querySelectorAll('[data-rv]').forEach(e => e.removeAttribute('data-rv')); document.querySelectorAll('iframe').forEach(f => { try { f.contentDocument.querySelectorAll('[data-rv]').forEach(e => e.removeAttribute('data-rv')); } catch (e) {} }); })()`);
  }
}
// the screens whose field error, segmented control or disabled state changed
const SCREENS = process.argv[5] ? JSON.parse(readFileSync(process.argv[5], 'utf8')) : [['Log result -error, three fields missing', 'wireframes/log-result-error.html?cause=fields'], ['Log result -error, the link missing', 'wireframes/log-result-error.html'],
  ['New password -error, too short', 'wireframes/new-password-error.html?cause=short'], ['New password -error, no match', 'wireframes/new-password-error.html?cause=mismatch'],
  ['Profile -error, a row didn’t save', 'wireframes/profile-error.html?cause=save&field=country&prev=Italy&value=Spain'], ['Sign in', 'wireframes/sign-in-sign-up.html'],
  ['Log result -loading, the locked form', 'wireframes/log-result-loading.html'], ['Race browse -loading, Sort disabled', 'wireframes/race-browse-loading.html']];
for (const [name, path, H = 844] of SCREENS) for (const theme of ['dark', 'light']) for (const side of ['before', 'after']) {   // [name, path, height]: a taller screen shows what's below the fold
  await go(base(side) + path + (path.includes('?') ? '&' : '?') + 'theme=' + theme, 390, H);
  const key = 'screen-' + slug(name);
  const b64 = await shot(key, theme, side, { x: 0, y: 0, width: 390, height: H });
  (data[key] ||= { component: name, state: 'Screen', kind: 'screen', path })[`${theme}-${side}`] = createHash('sha1').update(b64).digest('hex');
}
// a screen changed: decoded in Chrome and compared pixel by pixel; a pixel counts when a channel moves more than 24 of 255,
// and the screen counts when more than 40 do (or the sizes differ). The encoder's noise stays below that.
await go('about:blank', 400, 400);
async function differs(key, theme) {
  const a = readFileSync(join(OUT, `${key}-${theme}-before.webp`)).toString('base64'), b = readFileSync(join(OUT, `${key}-${theme}-after.webp`)).toString('base64');
  return ev(`(async () => {
    const load = s => new Promise(r => { const i = new Image(); i.onload = () => r(i); i.src = 'data:image/webp;base64,' + s; });
    const [x, y] = await Promise.all([load(${JSON.stringify(a)}), load(${JSON.stringify(b)})]);
    if (x.width !== y.width || x.height !== y.height) return true;
    const px = i => { const c = document.createElement('canvas'); c.width = i.width; c.height = i.height; const g = c.getContext('2d'); g.drawImage(i, 0, 0); return g.getImageData(0, 0, i.width, i.height).data; };
    const p = px(x), q = px(y); let n = 0;
    for (let k = 0; k < p.length; k += 4) if (Math.abs(p[k] - q[k]) > 24 || Math.abs(p[k + 1] - q[k + 1]) > 24 || Math.abs(p[k + 2] - q[k + 2]) > 24) n++;
    return n > 40;   // a screen: the same layout on both sides, so any 40 pixels that move are a change
  })()`);
}
const out = [];
for (const [k, v] of Object.entries(data)) {
  if (!v['dark-before'] || !v['dark-after']) continue;
  const ch = v.kind === 'screen' ? { dark: await differs(k, 'dark'), light: await differs(k, 'light') } : { dark: v['dark-before'] !== v['dark-after'], light: v['light-before'] !== v['light-after'] };
  out.push({ key: k, component: v.component, state: v.state, kind: v.kind, path: v.path, changed: ch });
}
writeFileSync(join(OUT, 'shots.json'), JSON.stringify(out, null, 1));
ws.close(); Object.values(SRV).forEach(s => s.close()); ch.kill(); try { rmSync(prof, { recursive: true, force: true }); } catch {}
console.log(`review_states: ${out.length} shots, ${out.filter(o => o.changed.dark || o.changed.light).length} changed in a theme`);
