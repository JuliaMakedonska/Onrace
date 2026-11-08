"""The docs shell: one frame for every page of design-system/docs/ (Lesson 9, 2026-11-05; the navigation restructure,
designer, 2026-11-08, modeled on Apple HIG's components and shadcn/ui).

page(title, current, main, toc, head_extra, scripts, depth) wraps a page's content in:
- a header: a skip link, the menu button (a phone), the brand back to the start page, a small Light / Dark switch;
- a sticky left nav in two levels, read from ui/inventory.md → Docs navigation: a section (Getting started,
  Foundations, Components, Patterns, Reference), then its pages; the components under their HIG group, alphabetical;
  a filter (an entry shown on another component's page finds that page) and the current page marked; on a phone it
  folds into the menu;
- a right "On this page" list (the page's sections), on a desk only;
- Previous / Next at the bottom, in the nav's order.
A page in docs/components/ passes depth=1, and every link of the shell is written from there. The behaviour (filter,
menu, the section on screen, the theme) is design-system/docs/doc.js. Every page links design-system/index.css, the
file the product links, then doc.css. Used by scripts/build_kit_showcase.py, scripts/build_docs_why.py and
scripts/docs_foundations.py.
"""
import os, re, html as H
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INV = open(os.path.join(ROOT, 'ui/inventory.md')).read()
slug_c = lambda n: re.sub(r'[^a-z0-9]+', '-', n.lower()).strip('-')

def _section(md, title):
    m = re.search(r'^## ' + re.escape(title) + r'\n(.*?)(?=^## |\Z)', md, flags=re.M | re.S)
    return m.group(1) if m else ''
_NAV = _section(INV, 'Docs navigation (designer, 2026-11-08)')
assert _NAV, 'ui/inventory.md: no Docs navigation section'
START = re.search(r'^\*\*Start page:\*\* (.*)$', _NAV, flags=re.M).group(1)
def _table(after):
    """The rows of the first table after a bold label in the Docs navigation section."""
    part = _NAV.split(after, 1)[1]
    rows = []
    for l in part.split('\n')[1:]:
        if not l.strip() and rows: break
        if l.startswith('| ') and not l.startswith('|---'):
            rows.append([x.strip() for x in re.split(r'(?<!\\)\|', l.strip().strip('|'))])
    return rows[1:]   # without the header
GETTING = [{'page': r[0].strip('`'), 'title': r[1]} for r in _table('**Getting started**')]
FOUNDATIONS = [{'page': r[0].strip('`'), 'title': r[1], 'design': [x.strip() for x in r[2].split(';') if x.strip()],
                'groups': [x.strip() for x in r[3].split(';') if x.strip()]} for r in _table('**Foundations**')]
GROUPS = [{'name': r[0], 'comps': [x.strip() for x in r[1].split(';') if x.strip()]} for r in _table('**Components**')]
MERGED = {r[0]: r[1] for r in _table("**Shown on another component's page**")}
OLD_FAMILIES = re.findall(r'`([a-z-]+)`', re.search(r'^\*\*The family pages\*\*.*$', _NAV, flags=re.M).group(0))
COMPONENTS = [n for g in GROUPS for n in g['comps']]
GROUP_OF = {n: g['name'] for g in GROUPS for n in g['comps']}
for g in GROUPS:
    assert g['comps'] == sorted(g['comps'], key=str.lower), ('ui/inventory.md → Docs navigation: a group is alphabetical', g['name'])
assert len(set(COMPONENTS)) == len(COMPONENTS), ('a component sits in one group', [n for n in COMPONENTS if COMPONENTS.count(n) > 1])
assert all(h in COMPONENTS for h in MERGED.values()), ('an entry is shown on a component page', [h for h in MERGED.values() if h not in COMPONENTS])
assert not set(MERGED) & set(COMPONENTS), ('an entry is a component or shown on one, not both', set(MERGED) & set(COMPONENTS))
SHOWN_HERE = {n: [e for e, h in MERGED.items() if h == n] for n in COMPONENTS}

def page_of(name):   # a component's own page, from the docs folder
    return f'components/{slug_c(name)}.html'
def section_url(name):   # where a Showcase map entry is shown: its own page, or its anchor on the page it is shown on
    return page_of(name) if name in GROUP_OF else f'{page_of(MERGED[name])}#{slug_c(name)}'

# the nav's sections and pages, in order: (section, sub-heading or None, page, title, names the filter finds)
_PMAP = re.search(r'^## Patterns map [^\n]*\n(.*?)(?=^## |\Z)', INV, flags=re.M | re.S).group(1).split('**Not patterns**')[0]
PATTERN_ROWS = [(c[1].strip('`'), c[0].strip('*')) for c in ([x.strip() for x in re.split(r'(?<!\\)\|', l.strip().strip('|'))] for l in _PMAP.split('\n') if l.startswith('| **'))]   # [(file, name)] from ui/inventory.md → Patterns map
NAV = ([('Getting started', None, g['page'], g['title'], g['title']) for g in GETTING]
       + [('Foundations', None, f['page'], f['title'], f['title']) for f in FOUNDATIONS]
       + [('Components', None, 'components', 'All components', 'all components')]
       + [('Components', GROUP_OF[n], page_of(n)[:-5], n, ' '.join([n] + SHOWN_HERE[n])) for n in COMPONENTS]
       + [('Patterns', None, 'patterns', 'All patterns', 'all patterns')]
       + [('Patterns', None, f'patterns#{f}', n, n + ' pattern') for f, n in PATTERN_ROWS]
       + [('Reference', None, 'specimens', 'Every specimen', 'every specimen')])
ORDER = list(dict.fromkeys(p for _, _, p, _, _ in NAV if '#' not in p))   # Previous / Next walks the pages, not the anchors
TITLE = {p: t for _, _, p, t, _ in NAV if '#' not in p}

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@800&family=Hanken+Grotesk:wght@400;600&display=swap">')
def map_data(depth=0):
    up = '../' * depth
    return (f'\n<link rel="preload" as="style" href="{up}../map-data.css" onload="this.onload=null;this.rel=\'stylesheet\'"><!-- the map\'s masks: not render-blocking -->'
            f'\n<noscript><link rel="stylesheet" href="{up}../map-data.css"></noscript>')
MAP_DATA = map_data(0)

def nav(current, depth=0):
    up = '../' * depth
    out, sec, sub = ['<nav class="ds-tree" aria-label="Design system">'], None, None
    for s, g, p, t, names in NAV:
        if s != sec:
            if sec: out.append('</ul>')
            out.append(f'<p class="ds-role">{H.escape(s)}</p><ul class="ds-list">'); sec, sub = s, None
        if g and g != sub:
            out.append(f'<li class="ds-sub" aria-hidden="true">{H.escape(g)}</li>'); sub = g
        cur = ' aria-current="page"' if p == current else ''
        href = up + (p.replace('#', '.html#') if '#' in p else p + '.html')
        out.append(f'<li><a href="{href}"{cur} data-names="{H.escape(names.lower())}">{H.escape(t)}</a></li>')
    out.append('</ul></nav>')
    return ''.join(out)

def pager(current, depth=0):
    if current not in ORDER: return ''
    up, i = '../' * depth, ORDER.index(current)
    def a(j, k):
        p = ORDER[j]
        return f'<a class="ds-pager-{k}" href="{up}{p}.html"><span class="ds-pager-k">{"Previous" if k == "prev" else "Next"}</span><span class="ds-pager-t">{H.escape(TITLE[p])}</span></a>'
    return ('<nav class="ds-pager" aria-label="Previous and next">' + (a(i - 1, 'prev') if i > 0 else '<span></span>')
            + (a(i + 1, 'next') if i < len(ORDER) - 1 else '') + '</nav>')

def page(title, current, main, toc=(), head_extra='', scripts='', depth=0):
    up = '../' * depth
    toc_html = ('<aside class="ds-toc" aria-labelledby="ds-toc-h"><p class="ds-toc-h" id="ds-toc-h">On this page</p><ul>'
                + ''.join(f'<li{" class=ds-toc-sub" if len(x) > 2 and x[2] else ""}><a href="#{x[0]}">{H.escape(x[1])}</a></li>' for x in toc) + '</ul></aside>') if toc else ''
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{H.escape(title)}</title>
{FONTS}
<link rel="stylesheet" href="{up}../index.css">
<link rel="stylesheet" href="{up}doc.css">
<script src="{up}../tokens/theme.js"></script>{head_extra}
</head>
<!-- GENERATED (scripts/docs_shell.py and the script that writes this page). Do not edit. -->
<body class="onrace kit-doc ds-body">
<a class="ds-skip" href="#main">Skip to content</a>
<header class="ds-head">
  <button type="button" class="ds-menu" aria-expanded="false" aria-controls="ds-nav">Menu</button>
  <a class="ds-brand" href="{up}index.html">Onrace design system</a>
  <div class="ds-theme" role="group" aria-label="Theme"><button type="button" data-kd-theme="dark" aria-pressed="true">Dark</button><button type="button" data-kd-theme="light" aria-pressed="false">Light</button></div>
</header>
<div class="ds{" ds--toc" if toc else ""}">
<aside class="ds-nav" id="ds-nav" aria-label="Design system">
  <label class="ds-filter-l" for="ds-filter">Filter</label>
  <input type="search" id="ds-filter" class="ds-filter" placeholder="Filter components" autocomplete="off">
  {nav(current, depth)}
  <p class="ds-empty" hidden>No component matches.</p>
</aside>
<main class="ds-main" id="main">
{main}
{pager(current, depth)}
</main>
{toc_html}
</div>
{scripts}<script src="{up}doc.js"></script>
</body>
</html>
'''
