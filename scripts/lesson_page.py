"""One template for the lesson overview pages (2026-10-26): Lesson 6 (scripts/build_concept_overview.py) and
Lesson 7 (scripts/build_ui_overview.py) build their pages with render(). The look is the artifact pages' own (ia.html's
:root tokens and the lessons bar); every word and number on a page comes from the repo files its builder reads.

Order on every page: the hero ("Lesson N of 12", the dates, the sources of truth), the stats strip, the stage nav,
"What we saw / What we decided", one section per stage, the decision register, "What's open" (mapped to the lesson that
takes each item), and a footer naming the scripts that build the page, the kit and the checks.
"""
import os, re, html, glob
import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lessons_nav import BAR_CSS, bar as lessons_bar, LESSONS
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GH = 'https://github.com/JuliaMakedonska/Onrace/blob/main/'
esc = lambda t: html.escape(t, quote=False)
_IA = open(os.path.join(ROOT, 'public/ia.html')).read()
ROOT_CSS = _IA[_IA.index(':root{'):_IA.index('/* Hero */')]

# The sources of truth, one line on every lesson page (the same map heads README.md and CLAUDE.md)
SOURCES = [('look', 'tokens/tokens.css', 'components/'), ('words', 'microcopy.md'), ('structure', 'wireframes/'), ('decisions', 'concept/concept.md')]
def sources_line():
    return ' · '.join(f'<span class="src{" src-more" if len(ps) > 1 else ""}"><span class="src-k">{k}:</span> ' + ' + '.join(f'<a href="{GH}{p}"><code>{p}</code></a>' for p in ps) + '</span>' for k, *ps in SOURCES)

# ---------------------------------------------------------------- the numbers every lesson page shows (read from the repo)
def repo_stats():
    # Lesson 8 step 4: the values are tokens/tokens.css (+ the generated map data), the classes components/index.css
    tok = ''.join(re.findall(r':root\s*\{(.*?)\n?\}', open(os.path.join(ROOT, 'tokens/tokens.css')).read() + open(os.path.join(ROOT, 'ui/map-data.css')).read(), flags=re.S))
    kit = open(os.path.join(ROOT, 'components/index.css')).read()
    variables = len(set(re.findall(r'(?:^|;)\s*--([a-z0-9-]+):', tok, flags=re.M)))
    rules = re.sub(r':root\s*\{.*?\n?\}', '', re.sub(r'/\*.*?\*/', '', kit, flags=re.S), flags=re.S)
    rules = re.sub(r'url\("[^"]*"\)', '', rules)
    classes = len(set(re.findall(r'\.(-?[a-z][a-z0-9-]*)(?=[^{}]*\{)', rules)))
    pages = [p for p in glob.glob(os.path.join(ROOT, 'wireframes/*.html')) if not p.endswith('index.html')]
    screens = len({re.sub(r'-(empty|error|loading|check-inbox)$', '', os.path.basename(p)[:-5]) for p in pages})
    inv = open(os.path.join(ROOT, 'ui/inventory.md')).read()
    def section(t):
        m = re.search(r'^## ' + re.escape(t) + r'\n(.*?)(?=^## |\Z)', inv, flags=re.M | re.S); return m.group(1) if m else ''
    comps = sum(len(re.findall(r'^\| \*\*', section(t), flags=re.M)) for t in ('Shared', 'Discovery', 'Archive', 'Infrastructure'))
    comps += len([n for n in re.findall(r'^- \*\*([^*]+)\*\*', section('One-off'), flags=re.M) if not n.startswith('On the kit')])
    bs = open(os.path.join(ROOT, 'scripts/concept/build_stand.py')).read()
    pairs = len(re.findall(r"^\s+\('[^\n]*', '[a-z0-9-]+', '[a-z0-9-]+', '(?:text|large|ui|exempt|info)'\),$", bs[bs.index('PAIRS = ['):bs.index('rows, failures')], flags=re.M))
    claude = open(os.path.join(ROOT, 'CLAUDE.md')).read()
    checks = re.search(r'\*\*Checks that stop the build[^\n]*\n\n((?:\d+\. [^\n]*\n)+)', claude).group(1).strip().split('\n')
    return {'screens': screens, 'pages': len(pages), 'variables': variables, 'classes': classes, 'components': comps,
            'pairs': pairs, 'checks': [re.sub(r'^\d+\. ', '', c) for c in checks]}

# ---------------------------------------------------------------- the page
TEMPLATE_CSS = r'''  /* Hero (same as ia.html and voice.html) */
  header.hero{ max-width:var(--maxw); margin:0 auto; padding:64px 24px 40px; }
  .kicker{ font-size:12px; font-weight:800; letter-spacing:.14em; text-transform:uppercase; color:var(--accent); margin:0 0 14px; }
  header.hero h1{ font-size:clamp(36px,6vw,60px); margin:0 0 14px; font-weight:800; letter-spacing:-.02em; }
  .hero-desc{color:var(--text-dim); font-size:18px; max-width:720px; margin:0 0 6px; line-height:1.5}
  .meta-row{display:flex; gap:10px; flex-wrap:wrap; margin:24px 0 0}
  .pill{ font-size:12px; font-weight:700; text-transform:uppercase; letter-spacing:.04em; padding:6px 12px; border-radius:999px; border:1px solid var(--border); color:var(--text-dim); }
  .card-grid{display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:14px; margin:28px 0 0}
  a.card-link{ display:block; background:var(--bg-elev); border:1px solid var(--border); border-radius:var(--radius); padding:16px 18px; text-decoration:none; transition:border-color .15s, transform .15s; }
  a.card-link:hover{border-color:var(--accent); transform:translateY(-1px)}
  .si-tag{font-size:11px; font-weight:800; text-transform:uppercase; letter-spacing:.06em; display:block; margin-bottom:6px}
  .si-title{color:var(--text); font-weight:700; font-size:15px; display:block; margin-bottom:4px}
  .si-desc{color:var(--text-dim); font-size:13px; display:block}
  main{max-width:var(--maxw); margin:0 auto; padding:0 24px 80px}
  section.block{padding:56px 0; border-top:1px solid var(--border); scroll-margin-top:72px}
  .section-tag{ display:inline-flex; font-size:12px; font-weight:800; letter-spacing:.08em; text-transform:uppercase; padding:5px 12px; border-radius:999px; margin-bottom:16px; }
  .tag-p{background:var(--accent-dim); color:var(--accent)}
  .tag-d{background:var(--patterns-dim); color:var(--patterns)}
  .tag-f{background:var(--unconfirmed-dim); color:var(--unconfirmed)}
  .tag-m{background:var(--benchmark-dim); color:var(--benchmark)}
  .tag-t{background:var(--job-loc-dim); color:var(--job-loc)}
  .tag-o{background:var(--ok-dim); color:var(--ok)}
  h2{font-size:28px; margin:0 0 8px; font-weight:800; letter-spacing:-.01em}
  h3{font-size:19px; margin:34px 0 10px; font-weight:700}
  h3[id]{scroll-margin-top:72px}
  .prose p, .prose li{color:var(--text-dim); font-size:15px; max-width:820px}
  .prose strong{color:var(--text)}
  .prose ul, .prose ol{padding-left:20px; margin:0 0 14px}
  .prose li{margin-bottom:6px}
  .prose li ul{margin-top:6px}
  .prose p.rule{font-size:16.5px; color:var(--text); background:var(--bg-elev); border:1px solid var(--border); border-left:3px solid var(--accent); border-radius:8px; padding:12px 16px}
  .prose p.note{font-size:13.5px; color:var(--text-faint)}
  .tbl-wrap{overflow-x:auto; margin:10px 0 20px; border:1px solid var(--border); border-radius:var(--radius)}
  table{border-collapse:collapse; width:100%; font-size:13.5px}
  th{text-align:left; background:var(--bg-elev-2); color:var(--text-faint); font-size:11px; text-transform:uppercase; letter-spacing:.05em; padding:10px 12px; border-bottom:1px solid var(--border); white-space:nowrap}
  td{padding:9px 12px; border-bottom:1px solid var(--border); vertical-align:top; color:var(--text-dim)}
  tr:last-child td{border-bottom:none}
  td strong{color:var(--text)}
  .two-col{display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr)); gap:18px}
  .two-col h3{margin-top:6px}
  .panel{background:var(--bg-elev); border:1px solid var(--border); border-radius:var(--radius); padding:6px 20px 8px}
  .tech-grid, .attr-grid{display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr)); gap:14px; margin:14px 0 8px}
  .tech, .attr{background:var(--bg-elev); border:1px solid var(--border); border-radius:var(--radius); padding:14px 18px}
  .tech p, .attr p{margin:0 0 8px}
  .tech-from{font-size:11px; font-weight:800; text-transform:uppercase; letter-spacing:.06em; color:var(--patterns)}
  .prose .tech-name, .prose .attr-title{color:var(--text); font-weight:700; font-size:15.5px; margin-top:6px}
  .prose .tech-meta, .prose .attr-strength{font-size:13px; color:var(--text-faint)}
  .scope{color:var(--benchmark); font-weight:700}
  a.btn{display:inline-block; background:var(--bg-elev); border:1px solid var(--border); border-radius:8px; padding:10px 14px; color:var(--text); font-weight:700; font-size:14px; text-decoration:none}
  a.btn:hover{border-color:var(--accent)}
  .stat-row{display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); gap:14px; margin:6px 0 18px}
  .stat{background:var(--bg-elev); border:1px solid var(--border); border-radius:var(--radius); padding:16px 18px}
  .stat-n{display:block; font-size:36px; font-weight:800; letter-spacing:-.02em; color:var(--text); line-height:1.1}
  .stat-l{display:block; font-size:13px; color:var(--text-dim); margin-top:6px}
  .phones{display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr)); gap:28px; margin:18px 0}
  .phone-fig{margin:0}
  /* device frame: copied from wireframes/index.html at build time */
{DEVICE_CSS}
  .phone-fig .device-slot{margin:0 auto}
  figcaption{max-width:412px; margin:12px auto 0; font-size:13.5px; color:var(--text-dim)}
  figcaption strong{color:var(--text)}
  .states{color:var(--text-faint)}
  footer{max-width:var(--maxw); margin:0 auto; padding:24px; color:var(--text-faint); font-size:12.5px; border-top:1px solid var(--border)}
  @media (prefers-reduced-motion: reduce){ html{scroll-behavior:auto} a.card-link{transition:none} a.card-link:hover{transform:none} }

  /* lesson template (scripts/lesson_page.py, 2026-10-26) */
  .hero-line{color:var(--text-dim); font-size:15px; margin:10px 0 0; line-height:1.6}
  .hero-line strong{color:var(--text)}
  .src{white-space:nowrap}
  .src-more{white-space:normal}  /* a source with two paths (look: tokens + components) may break between them on a phone */
  .src-k{color:var(--text-faint); font-weight:700; text-transform:uppercase; font-size:11px; letter-spacing:.06em}
  .hero-line a{color:var(--text); text-decoration:none}
  .hero-line a:hover code{color:var(--accent)}
  .stats{display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,160px),1fr)); gap:12px; margin:28px 0 0}
  .stats .stat{padding:14px 16px}
  .stats .stat-n{font-size:30px}
  .stat-sub{display:block; font-size:12px; color:var(--text-faint); margin-top:4px}
  .stages{list-style:none; counter-reset:st; margin:24px 0 0; padding:0; display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,200px),1fr)); gap:8px}
  .stages a{display:flex; gap:10px; align-items:baseline; background:var(--bg-elev); border:1px solid var(--border); border-radius:8px; padding:10px 12px; text-decoration:none; color:var(--text-dim); font-size:13.5px; min-height:44px; box-sizing:border-box}
  .stages a:hover{border-color:var(--accent); color:var(--text)}
  .stages .st-k{flex:none; font-size:11px; font-weight:800; letter-spacing:.06em; text-transform:uppercase; color:var(--accent)}
  .stages .st-l{color:var(--text); font-weight:700}
  .led li strong:first-child{color:var(--text)}
  .reg{display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,340px),1fr)); gap:14px; margin:12px 0}
  .reg--key{grid-template-columns:repeat(auto-fit,minmax(min(100%,460px),1fr))}   /* the key cards: wide, so a summary reads in one or two lines */
  .reg-card{background:var(--bg-elev); border:1px solid var(--border); border-radius:var(--radius); padding:14px 18px; display:grid; gap:6px; align-content:start}
  .reg-q{margin:0; color:var(--text); font-weight:700; font-size:15px}
  .reg-a{margin:0; color:var(--text-dim); font-size:14px}
  .reg-meta{margin:0; font-size:12px; color:var(--text-faint)}
  .reg-meta a{color:var(--text-faint)}
  .lesson-tag{display:inline-block; font-size:11px; font-weight:800; letter-spacing:.06em; padding:3px 8px; border-radius:999px; background:var(--accent-dim); color:var(--accent); white-space:nowrap}
  .prose{overflow-wrap:break-word}   /* long URLs in the rendered text break instead of widening the page */
  .prose code, .hero-line code{overflow-wrap:anywhere}
  .nav-inner{flex-wrap:nowrap; gap:16px}
  .brand{flex:none}
  .navlinks{flex-wrap:nowrap; overflow-x:auto; scrollbar-width:none; min-width:0}   /* one row that scrolls: a lesson has many stages */
  .navlinks::-webkit-scrollbar{display:none}
  .navlinks a{white-space:nowrap; flex:none}
  @media (max-width:560px){ .nav-inner{flex-direction:column; align-items:stretch; gap:6px; padding:10px 16px} .navlinks{margin-left:0} }
  .embed{border:1px solid var(--border); border-radius:var(--radius); overflow:hidden; background:var(--bg-elev); margin:14px 0 18px}
  .embed-bar{display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:8px 16px; padding:10px 14px; border-bottom:1px solid var(--border)}
  .embed-t{font-weight:700; color:var(--text); font-size:14px}
  .embed-t code{font-weight:400}
  .embed-bar a{display:inline-flex; align-items:center; min-height:44px; color:var(--text); font-weight:700; font-size:13.5px; text-decoration:none}
  .embed-bar a:hover{color:var(--accent)}
  .embed iframe{display:block; width:100%; border:0; background:#131518}
  .embed--tall iframe{height:min(82vh, 980px); min-height:560px}
  .embed--phone{max-width:392px}
  .embed--phone iframe{height:760px}
  .embeds{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,392px); gap:18px; align-items:start}
  @media (max-width:900px){ .embeds{grid-template-columns:minmax(0,1fr)} }
  details.fold{border:1px solid var(--border); border-radius:var(--radius); background:var(--bg-elev); margin:12px 0 16px}
  details.fold > summary{cursor:pointer; list-style:none; display:flex; align-items:center; gap:10px; min-height:48px; padding:6px 16px; font-weight:700; color:var(--text); font-size:15px}
  details.fold > summary::-webkit-details-marker{display:none}
  details.fold > summary::before{content:"▸"; color:var(--accent); transition:transform .15s}
  details.fold[open] > summary::before{transform:rotate(90deg)}
  details.fold > summary:focus-visible{outline:2px solid var(--text); outline-offset:2px}
  .fold-sub{font-weight:400; color:var(--text-faint); font-size:13px}
  details.fold > .fold-body{padding:4px 16px 12px}
  @media (prefers-reduced-motion: reduce){ details.fold > summary::before{transition:none} }
  .strip{list-style:none; padding:0; margin:8px 0; display:grid; gap:2px}
  .strip li{display:flex; flex-wrap:wrap; align-items:baseline; gap:4px 10px; min-height:40px; border-bottom:1px solid var(--border); padding:8px 0}
  .strip a{color:var(--text); font-weight:700; text-decoration:none}
  .strip a:hover{color:var(--accent)}
  .lede{font-size:16px; color:var(--text-dim); max-width:820px; margin:0 0 14px}
  footer p{margin:0 0 6px}
  footer a{color:var(--text-dim)}
  @media (max-width:480px){ header.hero{padding:40px 16px 28px} main{padding:0 16px 64px} .nav-inner{padding:0 16px} }
'''

def embed(src, title, kind='tall', note=''):
    """A live page in a framed, scrollable panel, with a link to open it on its own."""
    return (f'<div class="embed embed--{kind}"><div class="embed-bar"><span class="embed-t">{title}</span>'
            f'<a href="{src}" target="_blank" rel="noopener">Open full screen ↗</a></div>'
            f'<iframe src="{src}" title="{esc(re.sub("<[^>]+>", "", title))}, live" loading="lazy"></iframe></div>{note}')

def fold(summary, body, sub=''):
    """A long block, closed by default: the summary carries the count."""
    return f'<details class="fold"><summary>{summary}{f" <span class=fold-sub>{sub}</span>" if sub else ""}</summary><div class="fold-body">{body}</div></details>'

def stat(n, label, sub=''):
    return f'<div class="stat"><span class="stat-n">{n}</span><span class="stat-l">{label}</span>{f"<span class=stat-sub>{sub}</span>" if sub else ""}</div>'

def section(id_, tag, tagcls, title, body):
    return f'<section class="block" id="{id_}"><span class="section-tag {tagcls}">{tag}</span><h2>{esc(title)}</h2><div class="prose">{body}</div></section>\n'

def register(cards):
    """cards: (question, answer_html, date, source_label, source_href)"""
    return '<div class="reg">' + ''.join(
        f'<div class="reg-card"><p class="reg-q">{q}</p><p class="reg-a">{a}</p><p class="reg-meta">{d} · <a href="{h}">{s}</a></p></div>'
        for q, a, d, s, h in cards) + '</div>'

def key_decisions(lesson, inline):
    """The key-decision cards of a lesson, from concept/key-decisions.md: a plain one- or two-line summary written for the
    card, its date, and "Full record ↗" to the entry it summarizes."""
    t = open(os.path.join(ROOT, 'concept/key-decisions.md')).read()
    cards = []
    for l in t.split('\n'):
        c = [x.strip() for x in l.strip().strip('|').split(' | ')] if l.startswith('| ') else None
        if c and len(c) == 5 and c[0] == f'{lesson:02d}':
            cards.append(f'<div class="reg-card"><p class="reg-q">{inline(c[1])}</p><p class="reg-a">{inline(c[2])}</p>'
                         f'<p class="reg-meta">{c[3]} · <a href="{GH}{c[4]}">Full record ↗</a></p></div>')
    assert cards, f'no key decisions for lesson {lesson}'
    return '<div class="reg reg--key">' + ''.join(cards) + '</div>', len(cards)

def strip(items):
    """A row of short links (the "More" area): (label, href, sub)."""
    return '<ul class="strip">' + ''.join(f'<li><a href="{h}">{l}</a>{f" <span class=fold-sub>{s}</span>" if s else ""}</li>' for l, h, s in items) + '</ul>'

def open_table(rows, inline):
    """rows: (item_md, lesson_number or None, note_md)"""
    names = {n: name for _, n, name in LESSONS}
    body = ''.join(f'<tr><td>{inline(item)}</td><td>{f"<span class=lesson-tag>{n} · {names[n]}</span>" if n else "—"}</td><td>{inline(note)}</td></tr>' for item, n, note in rows)
    return f'<div class="tbl-wrap"><table><thead><tr><th>Open</th><th>Taken by</th><th>Where it stands</th></tr></thead><tbody>{body}</tbody></table></div>'

def render(n, name, current, dates, h1, desc, stats, stages, saw, decided, sections_html, register_html, open_html,
           footer_scripts, extra_css='', scripts='', cards='', reg_count=0, open_count=0, first_sections=''):
    total = len(LESSONS)
    stage_nav = '<ol class="stages">' + ''.join(f'<li><a href="#{i}"><span class="st-k">{k}</span><span><span class="st-l">{l}</span></span></a></li>' for i, k, l in stages) + '</ol>'
    lis = lambda xs: ''.join(f'<li>{x}</li>' for x in (xs or []))
    overview = f'''<div class="two-col">
  <div class="panel"><h3>What we saw</h3><ul class="led">{lis(saw)}</ul></div>
  <div class="panel"><h3>What we decided</h3><ul class="led">{lis(decided)}</ul></div>
</div>'''
    navlinks = ''.join(f'<a href="#{i}">{l}</a>' for i, k, l in stages)
    foot = ' · '.join(f'<code>{s}</code>' for s in footer_scripts)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Onrace — {name}</title>
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<style>
  {ROOT_CSS}{BAR_CSS}{TEMPLATE_CSS.replace('{{DEVICE_CSS}}', '')}{extra_css}
</style>
</head>
<body>
{lessons_bar(current)}
<nav>
  <div class="nav-inner">
    <a href="#top" class="brand" style="text-decoration:none">ON<span>RACE</span> · {name}</a>
    <div class="navlinks">{navlinks}</div>
  </div>
</nav>
<a id="top"></a>
<header class="hero">
  <p class="kicker">Lesson {n} of {total} · {name}</p>
  <h1>{h1}</h1>
  <p class="hero-desc">{desc}</p>
  <p class="hero-line"><strong>Lesson {n} of {total}</strong> · {dates} · Sources of truth: {sources_line()}</p>
  <div class="stats">{''.join(stat(*s) for s in stats)}</div>
  {cards}
  {stage_nav}
</header>
<main>
{section('overview', 'Start', 'tag-p', 'What we saw, what we decided', overview) if saw else ''}
{first_sections}
{sections_html}
{section('register', 'Register', 'tag-m', 'Decision register', fold(f'{reg_count} decisions', register_html, 'each with its date and its entry in concept.md')) if register_html else ''}
{section('open', 'Close', 'tag-f', "What's open", fold(f'{open_count} open items', open_html, 'and the lesson that takes each')) if open_html else ''}
</main>
<footer>
  <p>Lesson {n} of {total}. This page is built by {foot}, from the repo files it names; it is never edited by hand.</p>
  <p>The kit is built and checked by <code>scripts/concept/build_stand.py</code> (the stand, the color rules, the contrast pairs, the signed tokens), <code>scripts/check_overflow.mjs</code> (every state at 390, 320 and 200% text) and <code>scripts/check_kit.py</code> (the showcase against the inventory and <code>microcopy.md</code>); <code>scripts/build_kit_showcase.py</code> arranges the showcase.</p>
</footer>
{scripts}
<script>
(function(){{
  var links = Array.prototype.slice.call(document.querySelectorAll('.navlinks a'));
  var byId = {{}};
  links.forEach(function(l){{ byId[l.getAttribute('href').slice(1)] = l; }});
  var sections = Array.prototype.slice.call(document.querySelectorAll('section.block[id]'));
  if(!('IntersectionObserver' in window) || !sections.length) return;
  var io = new IntersectionObserver(function(entries){{
    entries.forEach(function(e){{
      if(e.isIntersecting){{ links.forEach(function(l){{ l.classList.remove('active'); }}); var l = byId[e.target.id]; if(l) l.classList.add('active'); }}
    }});
  }}, {{rootMargin:'-45% 0px -50% 0px'}});
  sections.forEach(function(s){{ io.observe(s); }});
}})();
</script>
</body>
</html>
'''
