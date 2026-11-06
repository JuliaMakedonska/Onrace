"""The docs shell: one frame for every page of design-system/docs/ (Lesson 9, 2026-11-05), modeled on Apple HIG and Primer.

page(title, current, main, toc) wraps a page's content in:
- a header: a skip link, the menu button (a phone), the brand back to the start page, a small Light / Dark switch;
- a sticky left nav, roles → families → components (ui/inventory.md → Docs families), with a filter and the current
  page marked; on a phone it folds into the menu;
- a right "On this page" list (the page's sections), on a desk only.
The behaviour (filter, menu, the section on screen, the theme) is design-system/docs/doc.js. Every page links
design-system/index.css, the file the product links, then doc.css. Used by scripts/build_kit_showcase.py (the start
page and the family pages) and scripts/build_docs_why.py.
"""
import os, re, html as H
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INV = open(os.path.join(ROOT, 'ui/inventory.md')).read()
slug_c = lambda n: re.sub(r'[^a-z0-9]+', '-', n.lower()).strip('-')

def _section(md, title):
    m = re.search(r'^## ' + re.escape(title) + r'\n(.*?)(?=^## |\Z)', md, flags=re.M | re.S)
    return m.group(1) if m else ''
_FAM = _section(INV, 'Docs families (Lesson 9, 2026-11-05)')
assert _FAM, 'ui/inventory.md: no Docs families section'
START = re.search(r'^\*\*Start page:\*\* (.*)$', _FAM, flags=re.M).group(1)
FAMILIES = []
for l in _FAM.split('\n'):
    c = [x.strip() for x in l.strip().strip('|').split(' | ')] if l.startswith('| ') and not l.startswith('| Role') else None
    if c and len(c) == 5:
        FAMILIES.append({'role': c[0], 'name': c[1], 'page': c[2].strip('`'), 'line': c[3], 'comps': [x.strip() for x in c[4].split(';') if x.strip()]})
ROLES = list(dict.fromkeys(f['role'] for f in FAMILIES))
FAMILY_OF = {n: f for f in FAMILIES for n in f['comps']}
def section_url(name):   # a component's address: its family page and its own anchor
    return f'{FAMILY_OF[name]["page"]}.html#{slug_c(name)}'

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@800&family=Hanken+Grotesk:wght@400;600&display=swap">')
MAP_DATA = ('\n<link rel="preload" as="style" href="../map-data.css" onload="this.onload=null;this.rel=\'stylesheet\'"><!-- the map\'s masks: not render-blocking -->'
            '\n<noscript><link rel="stylesheet" href="../map-data.css"></noscript>')

def nav(current):
    CUR = ' aria-current="page"'
    out = ['<nav class="ds-tree" aria-label="Design system">',
           '<ul class="ds-top">' + ''.join(f'<li><a href="{p}.html"{CUR if current == p else ""}>{t}</a></li>'
                                           for p, t in (('index', 'Start'), ('why', 'Why it looks like this'), ('patterns', 'Patterns'), ('specimens', 'Every specimen'))) + '</ul>']
    for role in ROLES:
        out.append(f'<p class="ds-role">{H.escape(role)}</p><ul class="ds-fams">')
        for f in [f for f in FAMILIES if f['role'] == role]:
            cur = ' aria-current="page"' if current == f['page'] else ''
            comps = ''.join(f'<li><a href="{f["page"]}.html#{slug_c(n)}" data-names="{H.escape(n.lower())}">{H.escape(n)}</a></li>' for n in f['comps'])
            out.append(f'<li class="ds-fam{" is-current" if cur else ""}"><a class="ds-fam-a" href="{f["page"]}.html"{cur} data-names="{H.escape(f["name"].lower())}">{H.escape(f["name"])}</a>'
                       f'<ul class="ds-comps">{comps}</ul></li>')
        out.append('</ul>')
    out.append('</nav>')
    return ''.join(out)

def page(title, current, main, toc=(), head_extra='', scripts=''):
    toc_html = ('<aside class="ds-toc" aria-labelledby="ds-toc-h"><p class="ds-toc-h" id="ds-toc-h">On this page</p><ul>'
                + ''.join(f'<li><a href="#{i}">{H.escape(t)}</a></li>' for i, t in toc) + '</ul></aside>') if toc else ''
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{H.escape(title)}</title>
{FONTS}
<link rel="stylesheet" href="../index.css">
<link rel="stylesheet" href="doc.css">
<script src="../tokens/theme.js"></script>{head_extra}
</head>
<!-- GENERATED (scripts/docs_shell.py and the script that writes this page). Do not edit. -->
<body class="onrace kit-doc ds-body">
<a class="ds-skip" href="#main">Skip to content</a>
<header class="ds-head">
  <button type="button" class="ds-menu" aria-expanded="false" aria-controls="ds-nav">Menu</button>
  <a class="ds-brand" href="index.html">Onrace design system</a>
  <div class="ds-theme" role="group" aria-label="Theme"><button type="button" data-kd-theme="dark" aria-pressed="true">Dark</button><button type="button" data-kd-theme="light" aria-pressed="false">Light</button></div>
</header>
<div class="ds{" ds--toc" if toc else ""}">
<aside class="ds-nav" id="ds-nav" aria-label="Components">
  <label class="ds-filter-l" for="ds-filter">Filter</label>
  <input type="search" id="ds-filter" class="ds-filter" placeholder="Filter components" autocomplete="off">
  {nav(current)}
  <p class="ds-empty" hidden>No component matches.</p>
</aside>
<main class="ds-main" id="main">
{main}
</main>
{toc_html}
</div>
{scripts}<script src="doc.js"></script>
</body>
</html>
'''
