#!/usr/bin/env node
/* The docs can't lie (Lesson 9, 2026-11-05): every stage on every page of design-system/docs/ (a page per component since 2026-11-08) against the same
   stage on specimens.html, the hand-written source, in headless Chrome over local HTTP. For every element in a stage's
   frame (frames entered, each loaded and styled first) it compares 23 computed properties: color, type, borders,
   radius, spacing, shadow, outline, opacity, size, display, gap, backdrop. Four passes: 1280 and 390, dark and light.
   The frame itself is the docs layer (borderless on the family pages since 2026-11-05), so the comparison starts at its
   children, the product; a stage cropped to its component keeps its full width inside the crop window, so widths and
   heights are compared too, except in the States cells ([data-nogeo]), whose width is the cell's. Any difference means the documentation's own CSS reached a specimen, and fails. It caught three such leaks while the docs were built (doc.css → Lesson 9 in concept.md).
   Run from the repo root: node scripts/check_docs_stages.mjs [--quiet]. build_stand.py runs it; exit 1 on a difference,
   2 if Chrome isn't there, 3 if a page never settled (fonts or frames didn't load: not measured, so scripts/ship.sh retries). */
import { spawn } from 'node:child_process'; import { createServer } from 'node:http';
import { mkdtempSync, readFileSync, readdirSync, rmSync, existsSync } from 'node:fs'; import { tmpdir } from 'node:os'; import { join, normalize, extname } from 'node:path';
import { fileURLToPath } from 'node:url';
const ROOT = join(fileURLToPath(new URL('.', import.meta.url)), '..'), QUIET = process.argv.includes('--quiet');
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const T = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.svg': 'image/svg+xml', '.jpg': 'image/jpeg', '.webp': 'image/webp', '.avif': 'image/avif' };
const srv = createServer((q, r) => { const p = normalize(join(ROOT, decodeURIComponent(new URL(q.url, 'http://x').pathname))); try { const b = readFileSync(p); r.writeHead(200, { 'content-type': T[extname(p)] || 'application/octet-stream' }).end(b); } catch { r.writeHead(404).end(); } });
await new Promise(r => srv.listen(0, '127.0.0.1', r)); const B = `http://127.0.0.1:${srv.address().port}/design-system/docs/`;
if (!existsSync(CHROME)) { console.log('check_docs_stages: SKIPPED, Chrome not found'); process.exit(2); }
const prof = mkdtempSync(join(tmpdir(), 'stc-')); const ch = spawn(CHROME, ['--headless=new', '--disable-gpu', '--remote-debugging-port=0', '--user-data-dir=' + prof, 'about:blank'], { stdio: 'ignore' });
const sl = ms => new Promise(r => setTimeout(r, ms)); let port; for (let i = 0; i < 100 && !port; i++) { await sl(100); try { port = readFileSync(join(prof, 'DevToolsActivePort'), 'utf8').split('\n')[0]; } catch {} }
const tg = await (await fetch(`http://127.0.0.1:${port}/json/list`)).json(); const ws = new WebSocket(tg.find(t => t.type === 'page').webSocketDebuggerUrl); await new Promise(r => ws.addEventListener('open', r, { once: true }));
let id = 0; const pend = new Map(), wait = []; ws.addEventListener('message', e => { const m = JSON.parse(e.data); if (m.id && pend.has(m.id)) { pend.get(m.id)(m); pend.delete(m.id); } else if (m.method) wait.filter(w => w.m === m.method).forEach(w => { w.r(m); wait.splice(wait.indexOf(w), 1); }); });
const send = (method, params = {}) => new Promise(r => { const i = ++id; pend.set(i, r); ws.send(JSON.stringify({ id: i, method, params })); });
const ev = async x => (await send('Runtime.evaluate', { expression: x, returnByValue: true, awaitPromise: true })).result?.result?.value;
await send('Page.enable'); await send('Network.enable');
if (process.env.ONRACE_BLOCK_FONTS) await send('Network.setBlockedURLs', { urls: ['*fonts.gstatic.com*'] });   // a test of the exit 3: fonts unreachable
await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });
const PROPS = ['color', 'background-color', 'font-family', 'font-size', 'font-weight', 'line-height', 'letter-spacing', 'text-transform', 'border-top-left-radius', 'border-top-color', 'border-top-width', 'padding-top', 'padding-left', 'margin-top', 'box-shadow', 'outline-style', 'text-decoration-line', 'opacity', 'width', 'height', 'display', 'gap', 'backdrop-filter'];
const FACES = ['800 1em "Schibsted Grotesk"', '400 1em "Hanken Grotesk"', '600 1em "Hanken Grotesk"'];   // the product's three faces
const COLLECT = (geometry) => `(async () => { await document.fonts.ready;
  const faces = ${JSON.stringify(FACES)};
  await Promise.all(faces.map(f => document.fonts.load(f).catch(() => null)));
  for (const f of document.querySelectorAll('iframe')) {   // every frame loaded and styled before anything is read
    for (let i = 0; i < 100 && !(f.contentDocument && f.contentDocument.readyState === 'complete' && [...f.contentDocument.styleSheets].length); i++) await new Promise(r => setTimeout(r, 50));
    try { await f.contentDocument.fonts.ready; await Promise.all(faces.map(x => f.contentDocument.fonts.load(x).catch(() => null))); } catch (e) {}
  }
  // settled: every face loaded here and in every frame, and every frame styled (an unstyled frame reads Times)
  const docs = [document, ...[...document.querySelectorAll('iframe')].map(f => f.contentDocument).filter(Boolean)];
  const settled = docs.every(d => faces.every(x => d.fonts.check(x)) && (d === document || d.defaultView.getComputedStyle(d.body).fontFamily.includes('Hanken')));
  await new Promise(r => setTimeout(r, 300));
  const out = {};
  for (const st of document.querySelectorAll('.kit-state')) {
    const lab = st.getAttribute('data-label') || st.querySelector('.kit-label')?.textContent.trim(); const fr = st.querySelector('.kit-frame'); if (!fr || !lab || st.closest('[hidden]')) continue;
    const geo = ${geometry} && !st.hasAttribute('data-nogeo');   // a States cell (Lesson 9 step 3): its width is the page's layout, so widths and heights aren't compared
    const rec = []; const walk = (root, doc) => { for (const el of [root, ...root.querySelectorAll('*')]) {
      if (el.closest('.an-layer')) continue;
      const cs = doc.defaultView.getComputedStyle(el); const s = {};
      for (const p of ${JSON.stringify(PROPS)}) if (geo || (p !== 'width' && p !== 'height')) s[p] = cs.getPropertyValue(p);
      rec.push(el.tagName + '.' + [...el.classList].join('.') + ' ' + JSON.stringify(s));
      if (el.tagName === 'IFRAME' && el.contentDocument?.body) walk(el.contentDocument.body, el.contentDocument); } };
    [...fr.children].forEach(c => walk(c, document));   // the frame is the docs layer (borderless on the family pages); the product starts inside it
    (out[lab + (geo ? '' : ' [no geometry]')] ||= []).push(rec.join('\\n'));
  } return { settled, out }; })()`;
// a page read before its frames and fonts settled would report a leak that isn't there (it happened once, 2026-11-05):
// so a page that isn't settled is loaded again, up to three times; one that never settles wasn't measured: exit 3
async function load(u, geometry) {
  for (let t = 0; t < 3; t++) {
    const l = new Promise(r => wait.push({ m: 'Page.loadEventFired', r })); await send('Page.navigate', { url: u }); await Promise.race([l, sl(8000)]);
    const r = await ev(COLLECT(geometry));
    if (r && r.settled) return r.out;
    await sl(1000);
  }
  console.log(`check_docs_stages: ${u.split('/').pop()} never settled (fonts or frames didn't load): not measured, exit 3`);
  ws.close(); srv.close(); ch.kill(); process.exit(3);
}
let pages = 0, stages = 0; const bad = [];
for (const [WIDTH, THEME] of [[1280, ''], [1280, '?theme=light'], [390, ''], [390, '?theme=light']]) {
await send('Emulation.setDeviceMetricsOverride', { width: WIDTH, height: 900, deviceScaleFactor: 1, mobile: false });
const ref = await load(B + 'specimens.html' + THEME, true);
// the reference without geometry: the same stages with width and height dropped
const noGeo = {}; for (const [k, v] of Object.entries(ref)) noGeo[k + ' [no geometry]'] = v.map(r => r.replace(/,"width":"[^"]*","height":"[^"]*"/g, ''));
// the pages with a stage (2026-11-08: a page per component in components/, the Components index, Patterns); not the redirects
const DOCS_DIR = join(ROOT, 'design-system/docs');
const PAGES = [...readdirSync(DOCS_DIR).filter(f => f.endsWith('.html') && f !== 'specimens.html'), ...readdirSync(join(DOCS_DIR, 'components')).filter(f => f.endsWith('.html')).map(f => 'components/' + f)]
  .filter(f => { const h = readFileSync(join(DOCS_DIR, f), 'utf8'); return h.includes('class="kit-state') && !h.includes('http-equiv="refresh"'); }).sort();
for (const f of PAGES) {
  const got = await load(B + f + THEME, true); if (THEME === '' && WIDTH === 1280) pages++;   // every property, widths and heights included
  for (const [lab, recs] of Object.entries(got)) for (const r of recs) {
    stages++;
    const want = ref[lab] || noGeo[lab];
    if (!want) { bad.push(`${f}: "${lab}" not on specimens.html`); continue; }
    if (!want.includes(r)) {
      const tags = x => x.split('\n').map(l => l.split(' ')[0]).join('|');
      const cand = want.find(w => tags(w) === tags(r)) || want[0];
      const A = cand.split('\n'), Bl = r.split('\n'); const i = Bl.findIndex((x, k) => x !== A[k]);
      let diff = '';
      try { const pa = JSON.parse(A[i].slice(A[i].indexOf(' ') + 1)), pb = JSON.parse(Bl[i].slice(Bl[i].indexOf(' ') + 1));
        diff = Object.keys(pb).filter(k => pa[k] !== pb[k]).map(k => `${k}: ${pa[k]} → ${pb[k]}`).join('; '); } catch { diff = (A[i] || '∅').slice(0, 120) + ' → ' + (Bl[i] || '∅').slice(0, 120); }
      bad.push(`${WIDTH} ${THEME ? 'light' : 'dark'} · ${f}: "${lab.slice(0, 50)}" element ${i} ${(Bl[i] || '').split(' ')[0]}: ${diff}`); }
  }
}
}
ws.close(); srv.close(); ch.kill(); try { rmSync(prof, { recursive: true, force: true }); } catch {}
if (bad.length) { console.log(`check_docs_stages: FAIL, ${bad.length} of ${stages} stage-passes differ from specimens.html (the docs' CSS reached a specimen)`); bad.slice(0, 20).forEach(b => console.log('  ' + b)); process.exit(1); }
console.log(QUIET ? `check_docs_stages: pass (${stages} stage-passes on ${pages} docs pages)` : `check_docs_stages: pass, ${stages} stage-passes (${pages} docs pages × 1280 and 390 × dark and light), each identical to specimens.html`);
