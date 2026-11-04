"""Lay out the kit showcase as a component sheet, and write a page per component, from ui/inventory.md (2026-10-26;
the showcase moved from ui/kit.html to design-system/docs/index.html and the component pages came in Lesson 9, step 2).

Run from anywhere:  python3 scripts/build_kit_showcase.py      (build_stand.py runs it before its checks)
The specimens stay hand-written in design-system/docs/index.html (the "keep it" rule: a change goes there and to every screen). This
script only (re)writes, idempotently, everything around them:
- a sticky left sidebar: a quick filter, then the roles (Navigation, Cards and lists, Forms, Feedback, One-off) with every
  specimen under its role, the current one highlighted on scroll; on a phone it folds into a menu;
- one short intro line (what the kit is, the counts, links to ui/inventory.md, design-system/tokens/tokens.css and design-system/components/);
- one card per specimen: a compact header in the documentation's own style (name, classes, "Used on N screens" linked to
  the viewer, the HIG link, where interaction is live), the specimen's notes folded, then its states side by side, each on
  its own stage with its label under it.
The documentation's look is design-system/docs/doc.css (the artifact pages' style), its script design-system/docs/doc.js
(the Light / Dark switch, the anatomy markers); the stages are product: design-system/index.css (Lesson 8, step 3).

The component pages (Lesson 9, step 2, 2026-11-04): one per inventory component, in design-system/docs/components/, from
the same Showcase map. Each links design-system/index.css, the file the product links, so its stages can't differ from
the screens. Each shows what we already show (classes, the screens that use it, the native counterpart, the theme), the
anatomy (its first variant live, the parts numbered from ui/inventory.md → Docs map), the variants side by side (every
stage whose label holds one of its States), when to use it (DESIGN.md, quoted by the Docs map's pointer, and the
microcopy.md lines its stages carry), the rule and the anti-rule (the Docs map), and room for its states (step 3).
"""
import os, re, sys, glob, json, html as H
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docs_paths import rebase
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = 'design-system/docs'
P = os.path.join(ROOT, DOCS, 'index.html')
VIEWER = '../../wireframes/index.html'   # the screen viewer, from design-system/docs/
KIT = open(P).read()
INV = open(os.path.join(ROOT, 'ui/inventory.md')).read()

# ---------------------------------------------------------------- the Showcase map
sec = re.search(r'^## Showcase map \(2026-10-26\)\n(.*?)(?=^## |\Z)', INV, flags=re.M | re.S).group(1)
MAP = []
for l in sec.split('\n'):
    if l.startswith('| ') and not l.startswith('| Role') and not l.startswith('|---'):
        c = [x.strip() for x in l.strip().strip('|').split(' | ')]
        MAP.append({'role': c[0], 'name': c[1].strip('*'), 'spec': c[2].strip('`#') if c[2] != '—' else None,
                    'classes': re.findall(r'`([^`]+)`', c[3]), 'ios': c[4]})
ROLES = ['Navigation', 'Cards and lists', 'Forms', 'Feedback', 'One-off']
role_of, rows_of = {}, {}
for r in MAP:
    if r['spec']:
        role_of.setdefault(r['spec'], r['role'])
        rows_of.setdefault(r['spec'], []).append(r)
N_COMPONENTS = len({r['name'] for r in MAP if r['spec']})
slug_c = lambda n: re.sub(r'[^a-z0-9]+', '-', n.lower()).strip('-')   # a component's page: components/<slug>.html

# ---------------------------------------------------------------- which screens use what (wireframes/*.html)
SCREEN = {'race-browse': 'Race browse', 'race-detail': 'Race detail', 'results-list': 'Results list', 'log-result': 'Log result',
          'race-picker': 'Race picker', 'result-detail': 'Result detail', 'sign-in-sign-up': 'Sign in / Sign up',
          'reset-password': 'Reset password', 'new-password': 'New password', 'profile': 'Profile'}
PAGES = {}
for f in sorted(glob.glob(os.path.join(ROOT, 'wireframes/*.html'))):
    name = os.path.basename(f)[:-5]
    if name == 'index': continue
    h = open(f).read()
    PAGES[name] = (set(t for cl in re.findall(r'class="([^"]+)"', h) for t in cl.split()), h)
def screen_of(page):
    return next(s for s in sorted(SCREEN, key=len, reverse=True) if page == s or page.startswith(s + '-'))
def used_on(classes):
    hits = {}
    for page, (tokens, h) in PAGES.items():
        if any((c[1:] in h if c.startswith('<') else c in tokens) for c in classes):
            hits.setdefault(screen_of(page), []).append(page)
    return hits

# ---------------------------------------------------------------- cut the page into its parts
def element_end(s, start, tag='div'):
    depth, i = 0, start
    pat = re.compile(r'<(/?)' + tag + r'\b[^>]*>')
    while True:
        m = pat.search(s, i)
        depth += -1 if m.group(1) else 1
        i = m.end()
        if depth == 0: return i
items = {}
for m in re.finditer(r'    <div class="kit-item" id="([^"]+)"[^>]*>', KIT):
    items[m.group(1)] = KIT[m.start():element_end(KIT, m.start() + 4)]
RAW = dict(items)
unmapped = [i for i in items if i not in role_of]
assert not unmapped, ('specimens with no Showcase map row', unmapped)
head = KIT[:KIT.index('<body')]
head = re.sub(r'\n<link rel="stylesheet" href="doc\.css[^"]*">', '', head)
head = re.sub(r'(<link rel="stylesheet" href="\.\./index\.css[^"]*">)', r'\1\n<link rel="stylesheet" href="doc.css">', head, count=1)   # after the design system (Lesson 8, step 3; one file since Lesson 9, step 1); build_stand.py stamps it
assert 'href="doc.css"' in head, 'design-system/docs/index.html: no design-system/index.css link to put doc.css after'
shell = re.search(r'  <section class="kit-section" id="shell".*?\n  </section>\n', KIT, re.S).group(0)
tail_from = KIT.index('<!-- /kd -->') + len('<!-- /kd -->') if '<!-- /kd -->' in KIT else KIT.index('</main>') + len('</main>')
tail = re.sub(r'\n<script>\n/\* kd:js.*?</script>', '', KIT[tail_from:], flags=re.S)
tail = re.sub(r'\n<script src="doc\.js"></script>', '', tail)
SPEC_JS = ''.join(m.group(0) + '\n' for m in re.finditer(r'<script>.*?</script>', tail, flags=re.S))   # the specimens' own behaviour (live segments, date pills), carried to every component page
shell = shell.replace('<h2 id="shell-h">Shell</h2>', '<h3 id="shell-h">Shell</h3>')

# ---------------------------------------------------------------- one card per specimen
def title_of(spec):
    return re.sub(r'<[^>]+>', '', re.search(r'<h3>(.*?)</h3>', items[spec], re.S).group(1)).strip()
def meta(spec):
    rows = rows_of[spec]
    classes = list(dict.fromkeys(c for r in rows for c in r['classes']))
    code = ' '.join(f'<code>{"&lt;" + c[1:] if c.startswith("<") else "." + c}</code>' for c in classes)
    hits = used_on(classes)
    screens = ', '.join(f'<a href="{VIEWER}#{pages[0]}">{SCREEN[s]}</a>' for s, pages in sorted(hits.items(), key=lambda kv: list(SCREEN).index(kv[0])))
    used = f'<span class="kd-k">Used on {len(hits)} screen{"s" if len(hits) != 1 else ""}</span> {screens}' if hits else '<span class="kd-k">Used on</span> the showcase only'
    ios = list(dict.fromkeys(r['ios'] for r in rows if r['ios'] != 'none'))
    ios_html = ' · '.join(re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1 ↗</a>', x) for x in ios) or 'none'
    comps = ', '.join(dict.fromkeys(r['name'] for r in rows))
    live = re.search(r'<(button|a href|input|select|textarea)\b', H.unescape(items[spec].split('<div class="kit-states">', 1)[-1])) is not None   # unescaped: the tab bar's stages are srcdoc frames
    parts = ([f'<p class="kd-line kd-comps">{H.escape(comps)}</p>'] if comps != title_of(spec) else []) + [f'<p class="kd-line">{code}</p>', f'<p class="kd-line">{used}</p>',
             f'<p class="kd-line"><span class="kd-k">Native iOS</span> {ios_html}</p>']
    pages = ', '.join(f'<a href="components/{slug_c(n)}.html">{H.escape(n)}</a>' for n in dict.fromkeys(r['name'] for r in rows))
    parts.append(f'<p class="kd-line"><span class="kd-k">Pages</span> {pages}</p>')
    if live: parts.append('<p class="kd-line"><span class="kd-k kd-live">Live</span> hover, Tab focus and press work on the specimens below</p>')
    return '<!-- kit:meta (scripts/build_kit_showcase.py) --><div class="kd-meta">' + ''.join(parts) + '</div><!-- /kit:meta -->'
def card(spec):
    b = items[spec]
    b = re.sub(r'\n      <!-- kit:meta.*?<!-- /kit:meta -->', '', b, flags=re.S)
    b = re.sub(r'\n      <details class="kd-notes"><summary>Notes</summary>(.*?)</details><!-- /kd-notes -->', r'\1', b, flags=re.S)
    b = re.sub(r'(</h3>)', r'\1\n      ' + meta(spec).replace('\\', r'\\'), b, count=1)
    # the hand-written notes (the paragraphs between the facts and the states) fold under "Notes"
    m = re.search(r'(<!-- /kit:meta -->)((?:\n      <p>.*?</p>)+)', b, flags=re.S)
    if m:
        b = b[:m.end(1)] + '\n      <details class="kd-notes"><summary>Notes</summary>' + m.group(2) + '</details><!-- /kd-notes -->' + b[m.end():]
    names = ' '.join([title_of(spec)] + [r['name'] for r in rows_of[spec]]).lower()
    return b.replace(f'<div class="kit-item" id="{spec}">', f'<div class="kit-item" id="{spec}" data-names="{H.escape(names)}">', 1) if 'data-names' not in b.split('>', 1)[0] else b

# ---------------------------------------------------------------- the page
slug = lambda r: 'role-' + re.sub(r'[^a-z]+', '-', r.lower()).strip('-')
specs_by_role = {r: [] for r in ROLES}
for r in MAP:
    if r['spec'] and r['spec'] not in specs_by_role[role_of[r['spec']]]:
        specs_by_role[role_of[r['spec']]].append(r['spec'])
items = {k: re.sub(r' data-names="[^"]*"', '', v, count=1) for k, v in items.items()}
side = ['<aside class="kd-side" aria-label="Components">',
        '  <div class="kd-side-head"><a class="kd-brand" href="#kd-top">Onrace kit</a>'
        '<button type="button" class="kd-menu" aria-expanded="false" aria-controls="kd-nav">Components</button></div>',
        '  <div class="kd-nav" id="kd-nav">',
        '    <label class="kd-filter-l" for="kd-filter">Filter components</label>',
        '    <input type="search" id="kd-filter" class="kd-filter" placeholder="Filter by name" autocomplete="off">',
        '    <nav aria-label="Components by role">',
        '      <p class="kd-role">Shell</p><ul><li><a href="#shell" data-names="shell tab bar large title">Shell</a></li></ul>']
for r in ROLES:
    side.append(f'      <p class="kd-role"><a href="#{slug(r)}">{r}</a> <span>{len(specs_by_role[r])}</span></p><ul>'
                + ''.join(f'<li><a href="#{s}" data-names="{H.escape(" ".join([title_of(s)] + [x["name"] for x in rows_of[s]]).lower())}">{H.escape(title_of(s))}</a></li>' for s in specs_by_role[r]) + '</ul>')
side += ['    </nav>', '    <p class="kd-empty" hidden>No component matches.</p>', '  </div>', '</aside>']
intro = (f'<p class="kd-intro" id="kd-top"><strong>The Onrace kit</strong>: {len(items)} specimens for {N_COMPONENTS} inventory components, '
         f'every state shown on its own, from <a href="../index.css"><code>design-system/index.css</code></a> alone. '
         f'Each component has <a href="#role-navigation">its own page</a> (the Pages line on every card). <a href="why.html">Why the system looks like this</a> · '
         f'<a href="https://github.com/JuliaMakedonska/Onrace/blob/main/ui/inventory.md">The inventory</a> · '
         f'<a href="https://github.com/JuliaMakedonska/Onrace/tree/main/design-system">design-system/ on GitHub</a></p>')
# the theme switch (Lesson 8, 2026-11-01): the stress test from step 5 on every specimen at once. Light is a proof only (C5)
THEME = ('<div class="kd-theme" role="group" aria-label="Theme"><span class="kd-theme-l">Theme</span>'
         '<button type="button" data-kd-theme="dark" aria-pressed="true">Dark</button><button type="button" data-kd-theme="light" aria-pressed="false">Light</button>'
         '<span class="kd-theme-note">Light is the stress test of the semantic roles; Onrace ships dark only.</span></div>')
main = ['<main class="kd-main">', '  ' + intro, '  ' + THEME, '', '  <div class="kit-item kd-shell" id="shell-card" data-names="shell tab bar large title">', shell.replace('  <section', '  <section', 1), '  </div>']
for r in ROLES:
    main.append(f'\n  <!-- ================================================================ {r} -->\n'
                f'  <section class="kit-section" id="{slug(r)}" aria-labelledby="{slug(r)}-h">\n    <h2 id="{slug(r)}-h">{r} <span>{len(specs_by_role[r])}</span></h2>\n\n'
                + '\n\n'.join(card(s) for s in specs_by_role[r]) + '\n  </section>')
main.append('</main>')
JS = '''<script>
/* kd:js (scripts/build_kit_showcase.py): the sidebar highlights the card on screen, filters by name, and folds into a menu on a phone */
(function () {
  var links = Array.prototype.slice.call(document.querySelectorAll('.kd-side nav a[href^="#"]'));
  var byId = {};
  links.forEach(function (a) { byId[a.getAttribute('href').slice(1)] = a; });
  var cards = Array.prototype.slice.call(document.querySelectorAll('.kd-main .kit-item[id], .kd-main #shell'));
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        links.forEach(function (a) { a.removeAttribute('aria-current'); });
        var a = byId[e.target.id]; if (a) a.setAttribute('aria-current', 'true');
      });
    }, { rootMargin: '-20% 0px -70% 0px' });
    cards.forEach(function (c) { io.observe(c); });
  }
  var input = document.getElementById('kd-filter'), empty = document.querySelector('.kd-empty');
  input.addEventListener('input', function () {
    var q = input.value.trim().toLowerCase(), shown = 0;
    links.forEach(function (a) {
      if (!a.hasAttribute('data-names')) return;
      var hit = !q || a.getAttribute('data-names').indexOf(q) > -1;
      a.parentNode.hidden = !hit; if (hit) shown++;
      var card = document.getElementById(a.getAttribute('href').slice(1));
      if (card) (card.closest('.kd-shell') || card).hidden = !hit;
    });
    document.querySelectorAll('.kd-side nav ul').forEach(function (ul) {
      var role = ul.previousElementSibling; if (role) role.hidden = !ul.querySelector('li:not([hidden])');
    });
    document.querySelectorAll('.kd-main > .kit-section').forEach(function (s) { s.hidden = !s.querySelector('.kit-item:not([hidden])'); });
    empty.hidden = shown > 0;
  });
  var menu = document.querySelector('.kd-menu'), nav = document.getElementById('kd-nav');
  menu.addEventListener('click', function () {
    var open = menu.getAttribute('aria-expanded') !== 'true';
    menu.setAttribute('aria-expanded', String(open)); nav.classList.toggle('is-open', open);
  });
  nav.addEventListener('click', function (e) {
    if (e.target.closest('a') && window.matchMedia('(max-width: 860px)').matches) { menu.setAttribute('aria-expanded', 'false'); nav.classList.remove('is-open'); }
  });
})();
</script>'''
body = '<body class="onrace kit-doc">\n<div class="kd">\n' + '\n'.join(side) + '\n' + '\n'.join(main) + '\n</div><!-- /kd -->'
page = head + body + '\n' + JS + '\n<script src="doc.js"></script>' + tail
open(P, 'w').write(page)

# ================================================================ the component pages (Lesson 9, step 2, 2026-11-04)
DESIGN = open(os.path.join(ROOT, 'DESIGN.md')).read()
MC = open(os.path.join(ROOT, 'microcopy.md')).read()
def section(md, title):
    m = re.search(r'^## ' + re.escape(title) + r'\n(.*?)(?=^## |\Z)', md, flags=re.M | re.S)
    return m.group(1) if m else ''
def cells(line):
    return [c.strip() for c in re.split(r'(?<!\\)\|', line.strip().strip('|'))]
from docs_md import inline, GH   # markdown inline → HTML, a relative link to GitHub (shared with why.html)

# ---------------------------------------------------------------- ui/inventory.md → Docs map
DMAP = {}
for l in section(INV, 'Docs map (Lesson 9, step 2, 2026-11-04)').split('\n'):
    if not l.startswith('| **'): continue
    c = cells(l)
    name = c[0].strip('*')
    m = re.match(r'\*\*([^*]+)\*\* `([^`]+)` (.*)', c[5])
    DMAP[name] = {'stage': None if c[1] == '—' else c[1],
                  'parts': [(m2.group(1), m2.group(2).strip()) for m2 in (re.match(r'`([^`]+)` (.*)', x.strip()) for x in c[2].split('; ')) if m2],
                  'design': [x.strip() for x in c[3].split(' + ') if x.strip() and x.strip() != '—'],
                  'rule': re.match(r'`([^`]+)` (.*)', c[4]).groups(), 'anti': m.groups() if m else None}

# ---------------------------------------------------------------- the inventory row: where it is and what states it shows
def inv_row(name):
    for t in ('Shared', 'Archive', 'Infrastructure'):
        for l in section(INV, t).split('\n'):
            if l.startswith(f'| **{name}**'):
                c = cells(l)
                return [('Screens', c[1]), ('States', c[2])]
    for l in section(INV, 'One-off').split('\n'):
        if l.startswith(f'- **{name}**'):
            return [('In the inventory', l[2:])]
    return []

# ---------------------------------------------------------------- DESIGN.md: the quote a pointer names
def design_quote(ptr):
    head, _, words = ptr.partition(' › ')
    m = re.search(r'^#{2,3} ' + re.escape(head) + r'[^\n]*\n(.*?)(?=^#{1,3} |\Z)', DESIGN, flags=re.M | re.S)
    assert m, f'DESIGN.md has no heading "{head}" (ui/inventory.md → Docs map)'
    body, title = m.group(1), m.group(0).split('\n', 1)[0].lstrip('#').strip()
    if not words:
        para = next(p for p in body.strip().split('\n\n') if p.strip() and not p.lstrip().startswith('- '))
        return title, para.strip()
    bullets = re.findall(r'^- (.*)$', body, flags=re.M)
    hit = next((b for b in bullets if b.startswith('**' + words)), None) or next((b for b in bullets if words.lower() in b.lower()), None)
    assert hit, f'DESIGN.md → {head}: no bullet with "{words}" (ui/inventory.md → Docs map)'
    return title, hit

# ---------------------------------------------------------------- microcopy.md: the lines a component's stages carry
MC_ROWS = []
for l in section(MC, 'Full table').split('\n'):
    if not re.match(r'\|\s*\d+\s*\|', l): continue
    c = cells(l)
    if len(c) < 9 or '(removed)' in c[4]: continue
    line = c[3] if c[4].strip('* ') == 'unchanged' else c[4]
    line = re.sub(r'\*\*', '', line).strip().strip('"“”')
    if len(line) < 3 or '<' in line or line in ('—', '-'): continue
    if not c[8].startswith('UI copy'): continue   # our own words only: not catalog, reference or user data, nor annotations
    MC_ROWS.append({'screen': c[1], 'line': line, 'type': c[6]})
from html.parser import HTMLParser
class Text(HTMLParser):   # the text of the elements that carry a component's classes (and of their children)
    VOID = {'br', 'img', 'input', 'source', 'wbr', 'meta', 'link', 'hr'}
    def __init__(self, classes):
        super().__init__(); self.classes = classes; self.stack = []; self.on = 0; self.out = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs); hit = tag == 'select' and '<select' in self.classes or bool(set((a.get('class') or '').split()) & set(self.classes))
        if self.on or hit:
            for k in ('aria-label', 'placeholder'):
                if a.get(k): self.out.append(a[k])
        if tag in self.VOID: return
        self.stack.append(hit); self.on += hit
    def handle_endtag(self, tag):
        if tag in self.VOID or not self.stack: return
        self.on -= self.stack.pop()
    def handle_data(self, d):
        if self.on and d.strip(): self.out.append(d)
NORM = lambda t: re.sub(r'\s+', ' ', t.replace('’', "'").replace(' ', ' ')).strip().lower()
def carried(classes, stage_html):
    p = Text(classes); p.feed(H.unescape(stage_html) if 'srcdoc' in stage_html else stage_html)
    text = NORM(' | '.join(p.out))
    seen = {}
    for r in MC_ROWS:
        if NORM(r['line']) in text and (len(r['line']) > 3 or re.search(r'\b' + re.escape(NORM(r['line'])) + r'\b', text)):
            seen.setdefault(r['line'], {'type': r['type'], 'screens': []})
            if r['screen'] not in seen[r['line']]['screens']: seen[r['line']]['screens'].append(r['screen'])
    return seen

# ---------------------------------------------------------------- a specimen's stages
def stages_of(spec):
    b, out = RAW[spec], []
    for m in re.finditer(r'<div class="kit-state">', b):
        h = b[m.start():element_end(b, m.start())]
        lab = H.unescape(re.sub(r'<[^>]+>', '', re.search(r'<p class="kit-label">(.*?)</p>', h, re.S).group(1))).strip()
        out.append((lab, h))
    return out
def variants(row):
    sts = [st.lower() for st in MAPROW[row['name']]['states']]
    return [(lab, h) for lab, h in stages_of(row['spec']) if any(st in lab.lower() for st in sts)]
# an id the product's CSS selects on (dialog.alert #signout-confirm) keeps its name, or the copy would lose its look
CSS_IDS = set(re.findall(r'#([a-zA-Z][\w-]*)', re.sub(r'/\*.*?\*/|\{[^{}]*\}', '', open(os.path.join(ROOT, 'design-system/index.css')).read(), flags=re.S)))
def unid(h, sfx):   # a second copy of a stage on one page: its ids (and what points at them) take a suffix
    h = re.sub(r'\b(id|for|aria-labelledby|aria-describedby|aria-controls|list|form)="([^"]+)"', lambda m: f'{m.group(1)}="' + ' '.join(x if x in CSS_IDS else x + sfx for x in m.group(2).split()) + '"', h)
    return re.sub(r'href="#([^"]+)"', lambda m: f'href="#{m.group(1)}{sfx}"', h)
def here(h):   # a stage from the overview, rebased for a page one folder down
    return rebase(h, DOCS, DOCS + '/components')
MAPROW = {}
for line in section(INV, 'Showcase map (2026-10-26)').split('\n'):
    c = cells(line) if line.startswith('| ') and not line.startswith('| Role') and not line.startswith('|---') else None
    if c and len(c) == 6: MAPROW[c[1].strip('*')] = {'states': [x.strip() for x in c[5].split(';') if x.strip()]}

# ---------------------------------------------------------------- one page
COMP_ROWS = [r for r in MAP if r['spec']]
by_name = {r['name']: r for r in MAP}
assert all(r['name'] in DMAP for r in COMP_ROWS), ('components with no Docs map row', [r['name'] for r in COMP_ROWS if r['name'] not in DMAP])
head_pg = re.sub(r'<title>.*?</title>', '<title>{TITLE}</title>', here(head))
head_pg = re.sub(r'\n<link rel="preload" as="style" href="[^"]*map-data[^"]*"[^>]*>(<!--.*?-->)?\n<noscript>.*?</noscript>', '{MAP}', head_pg, flags=re.S)
assert '{MAP}' in head_pg, 'the overview head: no map-data preload to carry'
MAP_LINKS = re.search(r'\n<link rel="preload" as="style" href="[^"]*map-data[^"]*"[^>]*>(<!--.*?-->)?\n<noscript>.*?</noscript>', here(head), flags=re.S).group(0)
FONTS_ETC = head_pg
def facts(row):
    classes = row['classes']
    code = ' '.join(f'<code>{"&lt;" + c[1:] if c.startswith("<") else "." + c}</code>' for c in classes)
    hits = used_on(classes)
    screens = ', '.join(f'<a href="../{VIEWER}#{pages[0]}">{SCREEN[s]}</a>' for s, pages in sorted(hits.items(), key=lambda kv: list(SCREEN).index(kv[0])))
    used = f'<span class="kd-k">Used on {len(hits)} screen{"s" if len(hits) != 1 else ""}</span> {screens}' if hits else '<span class="kd-k">Used on</span> the showcase only'
    ios = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1 ↗</a>', row['ios']) if row['ios'] != 'none' else 'none'
    return ('<div class="kd-meta">' + f'<p class="kd-line"><span class="kd-k">Classes</span> {code}</p>' + f'<p class="kd-line">{used}</p>'
            + f'<p class="kd-line"><span class="kd-k">Native iOS</span> {ios}</p>'
            + f'<p class="kd-line"><span class="kd-k">In the kit</span> <a href="../index.html#{row["spec"]}">{H.escape(title_of(row["spec"]))}</a>, with every specimen beside it</p></div>')
def viewer(key, text):
    screen = SCREEN[screen_of(key.split('?')[0])]
    return f'<a href="../{VIEWER}#{H.escape(key)}">{H.escape(screen)}{" · " + H.escape(key.split("?")[0][len(screen_of(key.split("?")[0])) + 1:]) if key.split("?")[0] != screen_of(key.split("?")[0]) else ""} ↗</a>'
def page_for(i, row):
    name, spec, d = row['name'], row['spec'], DMAP[row['name']]
    vs = variants(row)
    assert vs, f'{name}: no stage matches its States'
    an = next((h for lab, h in vs if d['stage'] and d['stage'].lower() in lab.lower()), vs[0][1]) if d['stage'] else vs[0][1]
    an_label = re.search(r'<p class="kit-label">(.*?)</p>', an, re.S).group(1)
    an = unid(an, '-an')
    legend = ''.join(f'<li><span class="an-n">{n + 1}</span> {H.escape(label)} <code>{H.escape(sel)}</code></li>' for n, (sel, label) in enumerate(d['parts']))
    anatomy = (f'<div class="an" data-anatomy="{H.escape(json.dumps(d["parts"]))}">' + here(an) + '</div>'
               f'<ol class="an-legend">{legend}</ol>')
    var_html = '<div class="kit-states">' + ''.join(here(h) for _, h in vs) + '</div>'
    inv = ''.join(f'<p class="kd-line"><span class="kd-k">{k}</span> {inline(v, "ui/inventory.md")}</p>' for k, v in inv_row(name))
    quotes = ''.join(f'<blockquote class="dp-quote"><p>{inline(q, "DESIGN.md")}</p><footer><a href="{GH}DESIGN.md">DESIGN.md</a> → {H.escape(t)}</footer></blockquote>' for t, q in (design_quote(x) for x in d['design']))
    words = {}
    for _, h in vs:
        for line, v in carried(row['classes'], h).items():
            w = words.setdefault(line, {'type': v['type'], 'screens': []})
            w['screens'] += [s for s in v['screens'] if s not in w['screens']]
    mc = ('<div class="tbl-wrap"><table class="dp-mc"><thead><tr><th>Line</th><th>Type</th><th>Screens</th></tr></thead><tbody>'
          + ''.join(f'<tr><td>{H.escape(l)}</td><td>{H.escape(v["type"])}</td><td>{H.escape(", ".join(v["screens"]))}</td></tr>' for l, v in list(words.items())[:12])
          + '</tbody></table></div>') if words else '<p class="dp-note">What it shows carries no line of its own from <code>microcopy.md</code>: it shows catalog data, user data or another component\'s words.</p>'
    rkey, rtext = d['rule']
    other, akey, atext = d['anti']
    orow = by_name[other]
    assert orow['spec'], f'{name}: the anti-rule names {other}, which has no specimen'
    ostage = unid(next(iter(variants(orow)))[1], '-alt')
    rule = (f'<div class="dp-rule"><p class="kd-k dp-yes">Rule</p><p>{H.escape(rtext)}</p><p class="kd-line">See it: {viewer(rkey, rtext)}</p></div>'
            f'<div class="dp-rule dp-rule--anti"><p class="kd-k dp-no">Anti-rule · use <a href="{slug_c(other)}.html">{H.escape(other)}</a></p><p>{H.escape(atext)}</p>'
            f'<p class="kd-line">See it: {viewer(akey, atext)}</p><div class="kit-states">{here(ostage)}</div></div>')
    prev_, next_ = COMP_ROWS[i - 1] if i else None, COMP_ROWS[i + 1] if i + 1 < len(COMP_ROWS) else None
    nav = ('<nav class="dp-top" aria-label="Design system docs"><a href="../index.html">All components</a> · <a href="../why.html">Why it looks like this</a></nav>')
    pn = ('<nav class="dp-pn" aria-label="Components">' + (f'<a href="{slug_c(prev_["name"])}.html">‹ {H.escape(prev_["name"])}</a>' if prev_ else '<span></span>')
          + (f'<a href="{slug_c(next_["name"])}.html">{H.escape(next_["name"])} ›</a>' if next_ else '') + '</nav>')
    body = f"""<body class="onrace kit-doc">
<main class="dp">
  {nav}
  <p class="kd-k dp-role">{H.escape(row['role'])}</p>
  <h1>{H.escape(name)}</h1>
  <section class="dp-sec" id="show" aria-labelledby="show-h"><h2 id="show-h">What we already show</h2>
    {facts(row)}
    {THEME}
  </section>
  <section class="dp-sec" id="anatomy" aria-labelledby="anatomy-h"><h2 id="anatomy-h">Anatomy</h2>
    {anatomy}
  </section>
  <section class="dp-sec" id="variants" aria-labelledby="variants-h"><h2 id="variants-h">Variants and sizes <span>{len(vs)}</span></h2>
    {var_html}
    <div class="kd-meta dp-inv">{inv}</div>
  </section>
  <section class="dp-sec" id="use" aria-labelledby="use-h"><h2 id="use-h">When to use</h2>
    {quotes}
    <h3>The words it carries</h3>
    {mc}
  </section>
  <section class="dp-sec" id="rule" aria-labelledby="rule-h"><h2 id="rule-h">Rule and anti-rule</h2>
    <div class="dp-rules">{rule}</div>
  </section>
  <section class="dp-sec dp-states" id="states" aria-labelledby="states-h"><h2 id="states-h">States</h2>
    <p class="dp-note">Hover, pressed, focus, disabled and the rest, each shown on its own: step 3.</p>
  </section>
  {pn}
</main>
{SPEC_JS}<script src="../doc.js"></script>
</body>
</html>
"""
    needs_map = 'map-placeholder' in an + var_html + rule
    h = FONTS_ETC.replace('{TITLE}', H.escape(name) + ' · Onrace design system').replace('{MAP}', MAP_LINKS if needs_map else '')
    return h + body

os.makedirs(os.path.join(ROOT, DOCS, 'components'), exist_ok=True)
written = set()
for i, row in enumerate(COMP_ROWS):
    f = os.path.join(ROOT, DOCS, 'components', slug_c(row['name']) + '.html')
    open(f, 'w').write(page_for(i, row)); written.add(os.path.basename(f))
# a retired component keeps a page that says so and where it went
for row in [r for r in MAP if not r['spec']]:
    f = os.path.join(ROOT, DOCS, 'components', slug_c(row['name']) + '.html')
    why = MAPROW[row['name']]['states'][0]
    open(f, 'w').write(FONTS_ETC.replace('{TITLE}', H.escape(row['name']) + ' · Onrace design system').replace('{MAP}', '')
        + f"""<body class="onrace kit-doc">
<main class="dp">
  <nav class="dp-top" aria-label="Design system docs"><a href="../index.html">All components</a> · <a href="../why.html">Why it looks like this</a></nav>
  <p class="kd-k dp-role">{H.escape(row['role'])}</p>
  <h1>{H.escape(row['name'])}</h1>
  <section class="dp-sec" id="show" aria-labelledby="show-h"><h2 id="show-h">Retired</h2>
    <p class="dp-note">{H.escape(why[0].upper() + why[1:])}.</p>
    <div class="kd-meta">{''.join(f'<p class="kd-line"><span class="kd-k">{k}</span> {inline(v, "ui/inventory.md")}</p>' for k, v in inv_row(row['name']))}</div>
  </section>
</main>
<script src="../doc.js"></script>
</body>
</html>
"""); written.add(os.path.basename(f))
for f in glob.glob(os.path.join(ROOT, DOCS, 'components', '*.html')):   # a page whose component left the inventory goes too
    if os.path.basename(f) not in written: os.remove(f)
print('component pages:', len(written), 'in', DOCS + '/components/')
print('kit showcase:', ', '.join(f'{r} {len(specs_by_role[r])}' for r in ROLES), '·', len(items), 'specimens,', N_COMPONENTS, 'components')
