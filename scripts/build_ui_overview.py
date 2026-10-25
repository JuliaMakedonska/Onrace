"""Build public/ui-overview.html, the Lesson 7 overview (UI assembly), from the repo's own files.

Run from anywhere:  python3 scripts/build_ui_overview.py
Re-run after editing DESIGN.md, concept/concept.md (→ Native iOS), ui/inventory.md, visuals/README.md, CLAUDE.md
(→ UI assembly), ui/kit.css, ui/map.css or build_stand.py; the page is generated, never hand-edited.
Every line on the page is rendered from those files; every count is read from the files it describes. The page
shares the Lesson 6 overview's look and helpers (scripts/build_concept_overview.py, imported, which also rebuilds that
page with the current lessons bar).
"""
import os, re, glob, html
import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_concept_overview as CO
from lessons_nav import bar as lessons_bar
ROOT = CO.ROOT
GH = CO.GH
md, inline, sections, para, esc = CO.md, CO.inline, CO.sections, CO.para, CO.esc
read = lambda p: open(os.path.join(ROOT, p)).read()

DESIGN = read('DESIGN.md')
DS = sections(DESIGN.split('\n---\n', 1)[1] if DESIGN.startswith('---') else DESIGN)
CONCEPT = read('concept/concept.md')
NATIVE = sections(CO.CS['Native iOS (designer rule, 2026-10-18)'], '### ')
INV = read('ui/inventory.md')
IS = sections(INV)
VIS = read('visuals/README.md')
VS = sections(VIS)
CLAUDE = read('CLAUDE.md')
ASSEMBLY = sections(CLAUDE)['UI assembly']

# ---------------------------------------------------------------- counts, read from the files they describe
TOK = ''.join(re.findall(r':root\s*\{(.*?)\n?\}', read('ui/kit.css') + read('ui/map.css'), flags=re.S))
N_TOKENS = len(set(re.findall(r'(?:^|;)\s*--([a-z0-9-]+):', TOK, flags=re.M)))
BS = read('scripts/concept/build_stand.py')
PAIRS = re.findall(r"^\s+\('[^\n]*', '[a-z0-9-]+', '[a-z0-9-]+', '(text|large|ui|exempt|info)'\),$", BS[BS.index('PAIRS = ['):BS.index('rows, failures')], flags=re.M)
PAGES = [p for p in glob.glob(os.path.join(ROOT, 'wireframes/*.html')) if not p.endswith('index.html')]
N_COMPONENTS = len(re.findall(r'^\| \*\*', INV, flags=re.M)) + len(re.findall(r'^- \*\*[A-Z][^*]*\*\* \(`', INV, flags=re.M))
REVIEWS = sorted(glob.glob(os.path.join(ROOT, 'ui/review-*.html'))) + [os.path.join(ROOT, 'visuals/review-round3.html')]
OVF = read('scripts/check_overflow.mjs')
N_PASSES = len(re.findall(r'\[\d+, \d+, \d+\]', OVF[OVF.index('for (const [w, h, text] of'):OVF.index('for (const [w, h, text] of') + 120]))
C_ROWS = re.findall(r'^- \*\*(C\d) ([^:*]+):\*\*', DS['Native iOS'], flags=re.M)
S6 = NATIVE['Step 6: critique fixes (designer priorities, 2026-10-25)']
S7 = NATIVE['Step 7: the final check (designer priorities, 2026-10-25)']
N_S6 = len(re.findall(r'^- \*\*#', S6, flags=re.M))
N_S7 = int(re.search(r'\*\*(\d+) defects, all fixed\*\*', S7).group(1))
assert N_TOKENS and PAIRS and PAGES and N_COMPONENTS and len(C_ROWS) == 7 and N_PASSES == 3

# ---------------------------------------------------------------- sections
def title_of(p):
    h = open(p).read()
    return re.search(r'<title>([^<]+)</title>', h).group(1).strip()
def rel(p):
    return os.path.relpath(p, ROOT)

overview_body = f'''
<div class="stat-row">
  <div class="stat"><span class="stat-n">{len(PAGES)}</span><span class="stat-l">pages, 10 screens and their states, every one on <code>ui/kit.css</code></span></div>
  <div class="stat"><span class="stat-n">{N_TOKENS}</span><span class="stat-l">tokens in <code>ui/kit.css</code> and <code>ui/map.css</code>, each signed on the stand</span></div>
  <div class="stat"><span class="stat-n">{len(PAIRS)}</span><span class="stat-l">contrast pairs checked by the build</span></div>
  <div class="stat"><span class="stat-n">{N_PASSES}</span><span class="stat-l">overflow passes on every state: 390, 320, and 390 at 200% text</span></div>
</div>
{md(ASSEMBLY.split(chr(10) + chr(10), 1)[0])}
'''

design_body = f'''
{md(DS['Overview'])}
<p><a class="btn" href="{GH}DESIGN.md">Open DESIGN.md →</a></p>
'''

inventory_body = f'''
{md(INV.split(chr(10) + '## ', 1)[0].split(chr(10), 1)[1])}
<h3>Shared components</h3>
{md(IS['Shared'])}
<p><a class="btn" href="{GH}ui/inventory.md">Open the inventory →</a></p>
'''

kit_body = f'''
{md(ASSEMBLY.split(chr(10) + chr(10), 1)[1].split('**Visuals', 1)[0])}
<div class="card-grid">
  <a class="card-link" href="ui/kit.html"><span class="si-tag" style="color:var(--accent)">Showcase</span><span class="si-title">ui/kit.html</span><span class="si-desc">Every component in its states →</span></a>
  <a class="card-link" href="ui/shell.html"><span class="si-tag" style="color:var(--patterns)">Shell</span><span class="si-title">ui/shell.html</span><span class="si-desc">Large title and floating tab bar →</span></a>
  <a class="card-link" href="concept/concept.html"><span class="si-tag" style="color:var(--benchmark)">Stand</span><span class="si-title">concept.html</span><span class="si-desc">Every token and contrast pair, signed →</span></a>
  <a class="card-link" href="wireframes/index.html"><span class="si-tag" style="color:var(--job-loc)">Viewer</span><span class="si-title">All 10 screens</span><span class="si-desc">In an iPhone frame, with zone notes →</span></a>
</div>
<h3>The rules</h3>
{md('**The rules:**' + ASSEMBLY.split('**The rules:**', 1)[1].split('**Wireframe / Design toggle', 1)[0].split(chr(10), 1)[1])}
<h3>Wireframe and Design</h3>
{md('**Wireframe / Design toggle' + ASSEMBLY.split('**Wireframe / Design toggle', 1)[1])}
'''

ios_body = md(DS['Native iOS'])

PHOTOS = [m.group(1) for m in re.finditer(r'^\| ([a-z0-9-]+) \| [^|]+ \| \d+% \|', VS['Export (step 7, 2026-10-25)'], flags=re.M)]
thumbs = ''.join(f'<figure class="thumb"><picture><source type="image/avif" srcset="visuals/{p}-684.avif"><source type="image/webp" srcset="visuals/{p}-684.webp"><img src="visuals/{p}-684.jpg" alt="" width="684" height="228" loading="lazy"></picture><figcaption>{p}</figcaption></figure>' for p in PHOTOS)
visuals_body = f'''
<div class="thumbs">{thumbs}</div>
{md(VIS.split(chr(10) + '## ', 1)[0].split(chr(10), 1)[1])}
<h3>Tool</h3>
{md(VS['Tool'])}
<h3>Workflow</h3>
{md(VS['Workflow'])}
<h3>Export</h3>
{md(VS['Export (step 7, 2026-10-25)'])}
<p><a class="btn" href="{GH}visuals/README.md">Open visuals/README.md →</a> <a class="btn" href="visuals/review-round3.html">Round 3 retouching review →</a></p>
'''

def native(title):
    return f'<h3>{inline(title)}</h3>\n{md(NATIVE[title])}'
assembly_body = '\n'.join(native(t) for t in ['Step 3b: native iOS pass in the kit (2026-10-19)', 'Step 5, Discovery: Race detail on the kit (2026-10-22)',
                                               'Step 5, Archive and Infrastructure on the kit (2026-10-22)', 'Consolidation (2026-10-23)'])
markup_body = '\n'.join(native(t) for t in ['Markup pass (2026-10-23)', 'Markup pass, round 2 (2026-10-23)', 'Race picker pushed (designer, 2026-10-24)'])
checks_body = '\n'.join(native(t) for t in ['Overflow fix: the controls bar (designer report, 2026-10-24)', 'Overflow check, round 2 (designer, 2026-10-25)',
                                             'Step 6: critique fixes (designer priorities, 2026-10-25)']) + '\n' + \
    f'<h3>{inline("Step 7: the final check (designer priorities, 2026-10-25)")}</h3>\n' + md(S7.split('**Still deferred', 1)[0])

reviews_body = '<div class="card-grid">' + ''.join(
    f'<a class="card-link" href="{rel(p)}"><span class="si-tag" style="color:var(--accent)">Before / after</span><span class="si-title">{esc(title_of(p))}</span><span class="si-desc">{rel(p)} →</span></a>'
    for p in REVIEWS) + '</div>'

open_body = md('**Still deferred' + S7.split('**Still deferred', 1)[1])

# ---------------------------------------------------------------- page (the Lesson 6 overview's look)
STYLE = re.search(r'<style>(.*?)</style>', CO.PAGE, re.S).group(1)
STYLE += '''
  .thumbs{display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,220px),1fr)); gap:12px; margin:8px 0 18px}
  .thumb{margin:0}
  .thumb img{display:block; width:100%; height:auto; border-radius:6px; filter:grayscale(1) contrast(1.12) brightness(.85)}
  .thumb figcaption{margin:6px 0 0; font-size:12.5px; color:var(--text-faint)}
'''
NAV = [('overview', 'Overview'), ('design', 'DESIGN.md'), ('inventory', 'Inventory'), ('kit', 'Kit'), ('ios', 'Native iOS'), ('visuals', 'Visuals'),
       ('assembly', 'Assembly'), ('markup', 'Markup'), ('checks', 'Checks'), ('reviews', 'Reviews'), ('open', 'Open')]
section = CO.section
NAVJS = re.findall(r'<script>\n(\(function\(\)\{.*?)</script>', CO.PAGE, re.S)[-1]

PAGE = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Onrace — UI assembly</title>
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<style>{STYLE}</style>
</head>
<body>
{lessons_bar('ui-overview.html')}
<nav>
  <div class="nav-inner">
    <a href="#top" class="brand" style="text-decoration:none">ON<span>RACE</span> · UI assembly</a>
    <div class="navlinks">
      {''.join(f'<a href="#{i}">{n}</a>' for i, n in NAV)}
    </div>
  </div>
</nav>
<a id="top"></a>
<header class="hero">
  <p class="kicker">Lesson 7 · UI assembly</p>
  <h1>One kit, every screen, native iOS</h1>
  <p class="hero-desc">Rendered from <code>CLAUDE.md</code> (UI assembly), <code>DESIGN.md</code>, <code>ui/inventory.md</code>, <code>visuals/README.md</code> and <code>concept/concept.md</code> → Native iOS. The counts are read from <code>ui/kit.css</code>, <code>ui/map.css</code>, the build and the overflow check.</p>
  <div class="meta-row">
    <span class="pill">{len(PAGES)} pages on the kit</span>
    <span class="pill">{N_TOKENS} tokens, all signed</span>
    <span class="pill">{len(PAIRS)} contrast pairs</span>
    <span class="pill">C1–C7 decided</span>
    <span class="pill">Step 6: {N_S6} rows closed</span>
    <span class="pill">Step 7: {N_S7} defects, all fixed</span>
  </div>
  <div class="card-grid">
    <a class="card-link" href="ui/kit.html"><span class="si-tag" style="color:var(--accent)">Kit</span><span class="si-title">The showcase</span><span class="si-desc">Every component in its states →</span></a>
    <a class="card-link" href="wireframes/index.html"><span class="si-tag" style="color:var(--patterns)">Screens</span><span class="si-title">The viewer</span><span class="si-desc">10 screens, {len(PAGES)} states →</span></a>
    <a class="card-link" href="{GH}DESIGN.md"><span class="si-tag" style="color:var(--benchmark)">System</span><span class="si-title">DESIGN.md</span><span class="si-desc">Documented from the code →</span></a>
    <a class="card-link" href="ui/review-step7.html"><span class="si-tag" style="color:var(--job-loc)">Check</span><span class="si-title">The final check</span><span class="si-desc">Before and after →</span></a>
  </div>
</header>
<main>
{section('overview', 'Overview', 'tag-p', 'What Lesson 7 built', overview_body)}
{section('design', 'System', 'tag-d', 'DESIGN.md, from the code', design_body)}
{section('inventory', 'Inventory', 'tag-f', 'Every component of the 10 screens', inventory_body)}
{section('kit', 'Kit', 'tag-m', 'Where the kit lives, and its rules', kit_body)}
{section('ios', 'Native iOS', 'tag-t', 'The HIG rule and the decided conflicts', ios_body)}
{section('visuals', 'Visuals', 'tag-o', 'The race photos, and how they were made', visuals_body)}
{section('assembly', 'Steps 3b–5', 'tag-p', 'Assembly, group by group', assembly_body)}
{section('markup', 'Markup', 'tag-d', 'The markup passes', markup_body)}
{section('checks', 'Steps 6–7', 'tag-m', 'The critique and the final check', checks_body)}
{section('reviews', 'Reviews', 'tag-t', 'Every review page', reviews_body)}
{section('open', 'Open', 'tag-f', "What's still deferred or provisional", open_body)}
</main>
<footer>Generated by <code>scripts/build_ui_overview.py</code> from <a href="{GH}CLAUDE.md">CLAUDE.md</a>, <a href="{GH}DESIGN.md">DESIGN.md</a>, <a href="{GH}ui/inventory.md">ui/inventory.md</a>, <a href="{GH}visuals/README.md">visuals/README.md</a> and <a href="{GH}concept/concept.md">concept/concept.md</a>.</footer>
<script>
{NAVJS}</script>
</body>
</html>
'''
open(os.path.join(ROOT, 'public/ui-overview.html'), 'w').write(PAGE)
print('pages', len(PAGES), 'tokens', N_TOKENS, 'pairs', len(PAIRS), 'components', N_COMPONENTS, 'reviews', len(REVIEWS), 'photos', len(PHOTOS), 'bytes', len(PAGE))
