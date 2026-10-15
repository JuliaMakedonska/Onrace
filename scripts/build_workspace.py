"""Build public/workspace.html: the one shell for the whole project.

Run from anywhere:  python3 scripts/build_workspace.py
A persistent left rail lists all twelve lessons from scripts/lessons_nav.py (done ones link, future ones are
greyed). The content area shows the chosen lesson's own page in a frame, so each lesson stays its own file
with its own generator and still opens on its own.

Links: workspace.html#06 opens a lesson, workspace.html#06/stand a section in it, workspace.html#04/race-browse-empty
a wireframe state. The start page (start.html, the 01–02 overview that used to be this file) is workspace.html,
or #start/<section>. Old links to this file's sections (#competitors, #personas, ...) still land on them.
Styling is the artifact pages' own (ia.html's :root tokens).
"""
import os, json, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lessons_nav import LESSONS
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CSSSRC = open(ROOT + '/public/ia.html').read()
root_css = CSSSRC[CSSSRC.index(':root{'):CSSSRC.index('/* Nav */')].rstrip()
DATA = json.dumps([{'n': n, 'name': name.replace('&amp;', '&'), 'href': href} for href, n, name in LESSONS], ensure_ascii=False)

def rail_item(href, n, name):
    if href:
        return f'<li class="r-lesson" data-n="{n}"><a class="r-link" href="#{n}"><span class="r-n">{n}</span><span class="r-name">{name}</span></a><ul class="r-sections" hidden></ul></li>'
    return f'<li class="r-lesson is-future" data-n="{n}"><span class="r-link" aria-disabled="true"><span class="r-n">{n}</span><span class="r-name">{name}</span><span class="r-soon">Not started</span></span></li>'

RAIL = ''.join(rail_item(*l) for l in LESSONS)

PAGE = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Onrace — Workspace</title>
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<style>
  {root_css}
  html, body{{height:100%}}
  body{{overflow:hidden}}
  .shell{{display:grid; grid-template-columns:var(--rail-w, 264px) minmax(0,1fr); height:100vh; height:100dvh}}
  .shell.is-collapsed{{--rail-w:64px}}

  /* rail */
  .rail{{background:var(--bg-elev); border-right:1px solid var(--border); display:flex; flex-direction:column; min-height:0}}
  .rail-head{{display:flex; align-items:center; justify-content:space-between; gap:8px; padding:16px 12px 14px 20px; border-bottom:1px solid var(--border)}}
  .brand{{font-weight:800; letter-spacing:.02em; text-transform:uppercase; font-size:14px; color:var(--text); text-decoration:none; white-space:nowrap}}
  .brand span{{color:var(--accent)}}
  .icon-btn{{flex:none; width:36px; height:36px; display:grid; place-items:center; background:transparent; border:1px solid var(--border); border-radius:8px; color:var(--text-dim); cursor:pointer; font:inherit; font-size:15px}}
  .icon-btn:hover{{color:var(--text); background:var(--bg-elev-2)}}
  .icon-btn[hidden]{{display:none}}
  .icon-btn:focus-visible, .r-link:focus-visible, .r-sec:focus-visible, .menu-btn:focus-visible{{outline:2px solid var(--text); outline-offset:2px}}
  .rail-scroll{{flex:1; overflow-y:auto; padding:12px 10px 20px}}
  .rail ol, .rail ul{{list-style:none; margin:0; padding:0}}
  .r-group{{padding:14px 10px 6px; font-size:11px; font-weight:800; text-transform:uppercase; letter-spacing:.06em; color:var(--text-faint)}}
  .r-link{{display:flex; align-items:baseline; gap:10px; padding:8px 10px; border-radius:6px; color:var(--text-dim); text-decoration:none; font-size:14px; font-weight:600}}
  a.r-link:hover{{background:var(--bg-elev-2); color:var(--text)}}
  .r-n{{flex:none; width:22px; font-size:12px; font-weight:800; color:var(--text-faint); font-variant-numeric:tabular-nums}}
  .r-name{{min-width:0}}
  .r-link[aria-current="page"]{{background:var(--accent-dim); color:var(--accent)}}
  .r-link[aria-current="page"] .r-n{{color:var(--accent)}}
  .is-future .r-link{{color:var(--text-faint); opacity:.6; cursor:default; flex-wrap:wrap}}
  .r-soon{{flex-basis:100%; padding-left:32px; font-size:11px; font-weight:600; margin-top:-2px}}
  .r-sections{{margin:2px 0 8px 32px !important; border-left:1px solid var(--border)}}
  .r-sec{{display:block; padding:5px 10px; color:var(--text-dim); text-decoration:none; font-size:13px; border-radius:0 6px 6px 0}}
  .r-sec:hover{{color:var(--text); background:var(--bg-elev-2)}}
  .r-sec[aria-current="location"]{{color:var(--text); box-shadow:inset 2px 0 0 var(--accent)}}
  .rail-foot{{padding:12px 20px; border-top:1px solid var(--border); font-size:12px; color:var(--text-faint)}}
  .rail-foot a{{color:var(--text-dim)}}
  .is-collapsed .brand-long, .is-collapsed .r-name, .is-collapsed .r-soon, .is-collapsed .r-sections, .is-collapsed .r-group, .is-collapsed .rail-foot{{display:none !important}}
  .is-collapsed .rail-head{{padding:16px 0 14px; justify-content:center}}
  .is-collapsed .rail-head .brand{{display:none}}
  .is-collapsed .r-link{{justify-content:center; padding:8px 0}}
  .is-collapsed .r-n{{width:auto}}

  /* stage */
  .stage{{min-width:0; min-height:0; position:relative; background:var(--bg)}}
  .stage iframe{{display:block; width:100%; height:100%; border:0; background:var(--bg)}}
  .topbar, .backdrop{{display:none}}

  /* phone: the rail becomes a menu over the page */
  @media (max-width:860px){{
    .shell, .shell.is-collapsed{{grid-template-columns:minmax(0,1fr); grid-template-rows:auto minmax(0,1fr); --rail-w:0px}}
    .topbar{{display:flex; align-items:center; justify-content:space-between; gap:12px; padding:8px 16px; border-bottom:1px solid var(--border); background:var(--bg-elev); min-height:52px}}
    .topbar-title{{min-width:0; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; font-size:13px; font-weight:700; color:var(--text-dim)}}
    .menu-btn{{flex:none; min-height:36px; padding:0 12px; background:var(--bg-elev-2); border:1px solid var(--border); border-radius:8px; color:var(--text); font:inherit; font-size:13px; font-weight:700; cursor:pointer}}
    .rail{{position:fixed; z-index:20; top:0; bottom:0; left:0; width:min(300px, 86vw); transform:translateX(-100%); visibility:hidden; transition:transform .2s ease, visibility 0s linear .2s}}
    .shell.menu-open .rail{{transform:none; visibility:visible; transition:transform .2s ease}}
    .shell.menu-open .backdrop{{display:block; position:fixed; inset:0; z-index:19; background:rgba(0,0,0,.55)}}
    .collapse-btn{{display:none}}
    .is-collapsed .brand-long, .is-collapsed .r-name, .is-collapsed .r-soon, .is-collapsed .r-group, .is-collapsed .rail-foot{{display:revert !important}}
    .is-collapsed .rail-head .brand{{display:inline}}
    .is-collapsed .r-link{{justify-content:flex-start; padding:8px 10px}}
    .is-collapsed .r-sections{{display:block !important}}
    .is-collapsed .r-sections[hidden]{{display:none !important}}
  }}
  @media (prefers-reduced-motion: reduce){{ .rail, .shell.menu-open .rail{{transition:none}} }}
</style>
</head>
<body>
<div class="shell" id="shell">
  <header class="topbar">
    <button type="button" class="menu-btn" id="menu-btn" aria-controls="rail" aria-expanded="false">Lessons</button>
    <span class="topbar-title" id="topbar-title">Start</span>
    <a href="#" class="brand">ON<span>RACE</span></a>
  </header>
  <aside class="rail" id="rail" aria-label="Lessons">
    <div class="rail-head">
      <a href="#" class="brand">ON<span>RACE</span><span class="brand-long"> · Workspace</span></a>
      <button type="button" class="icon-btn collapse-btn" id="collapse-btn" aria-controls="rail" aria-expanded="true" aria-label="Collapse the lesson rail" title="Collapse">«</button>
      <button type="button" class="icon-btn" id="close-btn" aria-label="Close the lesson menu" hidden>×</button>
    </div>
    <nav class="rail-scroll" aria-label="Lessons">
      <ol>
        <li class="r-lesson" data-n="start"><a class="r-link" href="#"><span class="r-n">00</span><span class="r-name">Start · 01–02 overview</span></a><ul class="r-sections" hidden></ul></li>
      </ol>
      <p class="r-group">Lessons</p>
      <ol>{RAIL}</ol>
    </nav>
    <p class="rail-foot">Each lesson is its own page: <a id="open-alone" href="start.html">open this one on its own</a>.</p>
  </aside>
  <div class="backdrop" id="backdrop"></div>
  <main class="stage">
    <iframe id="stage" title="Start · 01–02 overview" src="about:blank"></iframe>
  </main>
</div>
<script>
(function () {{
  var LESSONS = {DATA};
  var START = {{ n: 'start', name: 'Start · 01–02 overview', href: 'start.html' }};
  var byN = {{}}; LESSONS.forEach(function (l) {{ byN[l.n] = l; }});
  var shell = document.getElementById('shell'), frame = document.getElementById('stage');
  var current = null, sections = [], activeSub = '';

  // ---- routing: '' → start; '#06' / '#06/stand' → lesson; '#start/x' → start section; anything else → an old start-page anchor
  function parse(hash) {{
    var h = hash.replace(/^#/, '');
    try {{ h = decodeURIComponent(h); }} catch (e) {{}}
    if (!h) return {{ l: START, sub: '' }};
    var m = /^(\\d\\d|start)(?:\\/(.*))?$/.exec(h);
    if (m && (m[1] === 'start' || byN[m[1]])) return {{ l: m[1] === 'start' ? START : byN[m[1]], sub: m[2] || '' }};
    return {{ l: START, sub: h, legacy: true }};
  }}
  function hashFor(l, sub) {{ return l === START ? (sub ? '#start/' + sub : '') : '#' + l.n + (sub ? '/' + sub : ''); }}
  function setTopHash(l, sub) {{
    var h = hashFor(l, sub);
    if ((location.hash || '') !== h) history.replaceState(null, '', h || location.pathname + location.search);
  }}
  function frameDoc() {{ try {{ return frame.contentWindow.document; }} catch (e) {{ return null; }} }}
  function lessonOfFrame() {{
    try {{
      var p = frame.contentWindow.location.pathname;
      if (/\\/start\\.html$/.test(p)) return START;
      for (var i = 0; i < LESSONS.length; i++) {{
        var href = LESSONS[i].href; if (!href) continue;
        if (p.slice(-href.length - 1) === '/' + href || (href === 'wireframes/index.html' && /\\/wireframes\\/$/.test(p))) return LESSONS[i];
      }}
    }} catch (e) {{}}
    return null;
  }}
  function route() {{
    var r = parse(location.hash);
    if (r.legacy) setTopHash(START, r.sub);
    if (!r.l.href) {{   // a future lesson typed into the URL
      current = r.l; activeSub = ''; sections = [];
      frame.removeAttribute('src');
      frame.srcdoc = '<body style="margin:0;display:grid;place-items:center;height:100vh;background:#0b0c0e;color:#9aa0a8;font:15px -apple-system,Segoe UI,Roboto,sans-serif">Lesson ' + r.l.n + ' · ' + r.l.name + ' hasn&#39;t started yet.</body>';
      paint(); return;
    }}
    frame.removeAttribute('srcdoc');
    var shown = lessonOfFrame();
    if (current === r.l && shown === r.l) {{
      var w = frame.contentWindow;
      if (w.location.hash.replace(/^#/, '') !== r.sub) w.location.hash = r.sub;
    }} else {{
      current = r.l; sections = [];
      frame.src = r.l.href + (r.sub ? '#' + r.sub : '');
    }}
    activeSub = r.sub; paint();
  }}

  // ---- the frame tells the shell where it is (section links change its hash; the viewer fires onrace:route)
  function sync() {{
    var l = lessonOfFrame(); if (!l) return;
    var sub = frame.contentWindow.location.hash.replace(/^#/, '');
    try {{ sub = decodeURIComponent(sub); }} catch (e) {{}}
    current = l; activeSub = sub;
    setTopHash(l, sub); paint();
  }}
  frame.addEventListener('load', function () {{
    var l = lessonOfFrame(); if (!l) {{ paint(); return; }}
    current = l;
    var doc = frameDoc();
    sections = doc ? Array.prototype.map.call(doc.querySelectorAll('.navlinks a[href^="#"], .sidebar-group a[href^="#"]'), function (a) {{
      return {{ id: a.getAttribute('href').slice(1), label: a.textContent.trim() }};
    }}).filter(function (s) {{ return s.id && s.id !== 'top'; }}) : [];
    var w = frame.contentWindow;
    w.addEventListener('hashchange', sync);
    w.addEventListener('onrace:route', sync);
    sync();
  }});

  // ---- rail
  function paint() {{
    Array.prototype.forEach.call(document.querySelectorAll('.r-lesson'), function (li) {{
      var n = li.getAttribute('data-n'), link = li.querySelector('a.r-link'), list = li.querySelector('.r-sections');
      var on = current && (current === START ? n === 'start' : current.n === n);
      if (link) {{ if (on) link.setAttribute('aria-current', 'page'); else link.removeAttribute('aria-current'); }}
      if (!list) return;
      if (on && sections.length) {{
        list.innerHTML = '';
        sections.forEach(function (s) {{
          var a = document.createElement('a'); a.className = 'r-sec'; a.textContent = s.label;
          a.href = hashFor(current, s.id) || '#';
          if (s.id === activeSub) a.setAttribute('aria-current', 'location');
          var item = document.createElement('li'); item.appendChild(a); list.appendChild(item);
        }});
        list.hidden = false;
      }} else {{ list.hidden = true; list.innerHTML = ''; }}
    }});
    if (current) {{
      var name = current === START ? current.name : current.n + ' · ' + current.name;
      document.title = 'Onrace — ' + (current === START ? 'Workspace' : name);
      frame.title = name;
      document.getElementById('topbar-title').textContent = name;
      document.getElementById('open-alone').href = (current.href || 'start.html') + (activeSub && current.href ? '#' + activeSub : '');
    }}
  }}

  // ---- collapse (desktop) and menu (phone)
  var collapseBtn = document.getElementById('collapse-btn'), menuBtn = document.getElementById('menu-btn'), closeBtn = document.getElementById('close-btn');
  function setCollapsed(c) {{
    shell.classList.toggle('is-collapsed', c);
    collapseBtn.setAttribute('aria-expanded', String(!c));
    collapseBtn.setAttribute('aria-label', c ? 'Expand the lesson rail' : 'Collapse the lesson rail');
    collapseBtn.textContent = c ? '»' : '«';
    try {{ localStorage.setItem('onrace-rail-collapsed', c ? '1' : '0'); }} catch (e) {{}}
  }}
  try {{ if (localStorage.getItem('onrace-rail-collapsed') === '1') setCollapsed(true); }} catch (e) {{}}
  collapseBtn.addEventListener('click', function () {{ setCollapsed(!shell.classList.contains('is-collapsed')); }});
  function setMenu(open) {{
    shell.classList.toggle('menu-open', open);
    menuBtn.setAttribute('aria-expanded', String(open));
    closeBtn.hidden = !open;
    if (open) (document.querySelector('.r-link[aria-current="page"]') || closeBtn).focus();
    else if (document.activeElement && document.getElementById('rail').contains(document.activeElement)) menuBtn.focus();
  }}
  menuBtn.addEventListener('click', function () {{ setMenu(true); }});
  closeBtn.addEventListener('click', function () {{ setMenu(false); }});
  document.getElementById('backdrop').addEventListener('click', function () {{ setMenu(false); }});
  document.addEventListener('keydown', function (e) {{ if (e.key === 'Escape' && shell.classList.contains('menu-open')) setMenu(false); }});
  document.getElementById('rail').addEventListener('click', function (e) {{ if (e.target.closest('a')) setMenu(false); }});

  window.addEventListener('hashchange', route);
  route();
}})();
</script>
</body>
</html>
'''
open(ROOT + '/public/workspace.html', 'w').write(PAGE)
print('workspace shell:', len(LESSONS), 'lessons,', sum(1 for l in LESSONS if l[0]), 'done,', len(PAGE), 'bytes')
