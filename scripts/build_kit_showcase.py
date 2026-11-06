"""The design-system docs, from ui/inventory.md (2026-10-26; restructured into family pages in Lesson 9, 2026-11-05).

Run from anywhere:  python3 scripts/build_kit_showcase.py      (build_stand.py runs it before its checks)
Writes, in design-system/docs/:
- specimens.html, every specimen on one page. The specimens in it are hand-written (the "keep it" rule: a markup
  change goes there and to every screen); this script (re)writes, idempotently, everything around them: a sidebar by
  role with a filter, one intro line, and a card per specimen with its facts from ui/inventory.md → Showcase map, then
  its states side by side. It was ui/kit.html until Lesson 9 step 2, then index.html until the restructure.
- index.html, the start page: what the system is, how it's organised, the families, why.html.
- a page per family (ui/inventory.md → Docs families), each component a section with its own anchor, in one order:
  its name and what it's for; the live specimen; When to use / When not to, side by side, with real screens; the
  anatomy, its parts numbered beside the stage; the other variants, if any; states (step 3); technical details folded
  (classes, the screens that use it, the native counterpart, DESIGN.md, the microcopy.md lines it carries).
  What isn't read from the files (what it's for, the parts, the rule and anti-rule) is ui/inventory.md → Docs map.
- components/<name>.html, one redirect per component to its section (the per-component pages of Lesson 9 step 2).
Every page links design-system/index.css, the file the product links, so a stage can't differ from the screens; the
frame is scripts/docs_shell.py, the documentation's look design-system/docs/doc.css, its script doc.js.
"""
import os, re, sys, glob, json, html as H
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docs_paths import rebase
import docs_shell as DS
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = 'design-system/docs'
P = os.path.join(ROOT, DOCS, 'specimens.html')   # the hand-written specimens
VIEWER = '../../wireframes/index.html'   # the screen viewer, from design-system/docs/
KIT = open(P).read()
KIT = re.sub(r'\n      <!-- kit:states .*?<!-- /kit:states -->', '', KIT, flags=re.S)   # the States grids are generated (below): read without them
INV = open(os.path.join(ROOT, 'ui/inventory.md')).read()
import docs_states as DST

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

# ---------------------------------------------------------------- the patterns (Lesson 9 step 4, 2026-11-06): ui/inventory.md → Patterns map
# A pattern is a composition of existing components that already stands on three or more screens. Each row names the
# classes a screen's page must carry (and, with !, must not); the screens found that way must be exactly the ones the
# row lists, at least three, or the build stops. Each pattern is one file in design-system/patterns/.
_PSEC = re.search(r'^## Patterns map [^\n]*\n(.*?)(?=^## |\Z)', INV, flags=re.M | re.S).group(1)
def _prow(l): return [x.strip() for x in re.split(r'(?<!\\)\|', l.strip().strip('|'))]
def _found(sig):
    need = [c for c in sig if not c.startswith('!')]; no = [c[1:] for c in sig if c.startswith('!')]
    hits = {}
    for page, (tokens, _) in PAGES.items():
        if all(c in tokens for c in need) and not any(c in tokens for c in no):
            hits.setdefault(screen_of(page), []).append(page)
    return {k: sorted(v, key=lambda x: (len(x), x)) for k, v in hits.items()}
PATTERNS, NOT_PATTERNS = [], []
_ptab, _ntab = _PSEC.split('**Not patterns**')
for l in _ptab.split('\n'):
    if not l.startswith('| **'): continue
    c = _prow(l)
    PATTERNS.append({'name': c[0].strip('*'), 'file': c[1].strip('`'), 'for': c[2], 'sig': re.findall(r'`([^`]+)`', c[3]),
                     'on': [x.strip() for x in c[4].split(';')], 'comps': [x.strip() for x in c[5].split(';')], 'use': c[6], 'not': c[7]})
for l in _ntab.split('\n'):
    if not l.startswith('| **'): continue
    c = _prow(l)
    NOT_PATTERNS.append({'name': c[0].strip('*'), 'sig': re.findall(r'`([^`]+)`', c[1]), 'on': [x.strip() for x in c[2].split(';')], 'why': c[3]})
for _p in PATTERNS + NOT_PATTERNS:
    _p['found'] = _found(_p['sig'])
    assert sorted(_p['found']) == sorted(_p['on']), ('ui/inventory.md → Patterns map: the screens carrying ' + ' '.join(_p['sig']) + ' are not the ones listed', _p['name'], sorted(_p['found']), sorted(_p['on']))
for _p in PATTERNS:
    assert len(_p['on']) >= 3, ('a pattern stands on three or more screens', _p['name'], _p['on'])
    assert os.path.exists(os.path.join(ROOT, 'design-system/patterns', _p['file'] + '.html')), ('no pattern file', _p['file'])
def PSTAGE(pt, label=True):   # the live composition: the pattern's own file in a frame; specimens.html labels it, the Patterns page keys it by data-label
    lab = f'{pt["name"]} pattern'
    attr = '' if label else ' data-label="' + H.escape(lab) + '"'
    return (f'<div class="kit-state"{attr}>' + (f'<p class="kit-label">{H.escape(lab)}</p>' if label else '')
            + f'<div class="kit-frame kit-frame--flush"><iframe class="kit-shell" src="../patterns/{pt["file"]}.html" title="{H.escape(lab)}"></iframe></div></div>')

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
assert 'href="doc.css"' in head, 'design-system/docs/specimens.html: no design-system/index.css link to put doc.css after'
# the Shell section went in Lesson 9 step 5 (2026-11-06): ui/shell.html redirects to the Tab screen pattern, the one source,
# shown in the Patterns section below (specimens.html#shell lands there)
tail_from = KIT.index('<!-- /kd -->') + len('<!-- /kd -->') if '<!-- /kd -->' in KIT else KIT.index('</main>') + len('</main>')
tail = re.sub(r'\n<script>\n/\* kd:js.*?</script>', '', KIT[tail_from:], flags=re.S)
tail = re.sub(r'\n<script src="doc\.js"></script>', '', tail)
SPEC_JS = ''.join(m.group(0) + '\n' for m in re.finditer(r'<script>.*?</script>', tail, flags=re.S))   # the specimens' own behaviour (live segments, date pills), carried to every component page

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
    pages = ', '.join(f'<a href="{DS.section_url(n)}">{H.escape(n)}</a>' for n in dict.fromkeys(r['name'] for r in rows))
    parts.append(f'<p class="kd-line"><span class="kd-k">In the docs</span> {pages}</p>')
    if live: parts.append('<p class="kd-line"><span class="kd-k kd-live">Live</span> hover, Tab focus and press work on the specimens below</p>')
    return '<!-- kit:meta (scripts/build_kit_showcase.py) --><div class="kd-meta">' + ''.join(parts) + '</div><!-- /kit:meta -->'
def card(spec):
    b = items[spec]
    b = re.sub(r'\n      <!-- kit:meta.*?<!-- /kit:meta -->', '', b, flags=re.S)
    b = re.sub(r'\n      <details class="kd-notes"><summary>Notes.*?</summary>(.*?)</details><!-- /kd-notes -->', r'\1', b, flags=re.S)
    b = re.sub(r'(</h3>)', r'\1\n      ' + meta(spec).replace('\\', r'\\'), b, count=1)
    # the hand-written notes (the paragraphs between the facts and the states) fold under "Notes"
    m = re.search(r'(<!-- /kit:meta -->)((?:\n      <p>.*?</p>)+)', b, flags=re.S)
    if m:
        b = b[:m.end(1)] + '\n      <details class="kd-notes"><summary>Notes <span class="fold-sub">what it shows and why</span></summary>' + m.group(2) + '</details><!-- /kd-notes -->' + b[m.end():]
    st = states_of_spec(spec)
    if st:
        i = b.index('<div class="kit-states">'); j = element_end(b, i)
        b = b[:j] + '\n      <!-- kit:states (scripts/build_kit_showcase.py: ui/inventory.md → States map) -->' + st + '<!-- /kit:states -->' + b[j:]
    names = ' '.join([title_of(spec)] + [r['name'] for r in rows_of[spec]]).lower()
    return b.replace(f'<div class="kit-item" id="{spec}">', f'<div class="kit-item" id="{spec}" data-names="{H.escape(names)}">', 1) if 'data-names' not in b.split('>', 1)[0] else b

# ---------------------------------------------------------------- the States grids (Lesson 9 step 3): ui/inventory.md → States map
def _cells(line): return [c.strip() for c in re.split(r'(?<!\\)\|', line.strip().strip('|'))]
SMAP = DST.read_map(INV, _cells)
def _stages(spec):
    b, out_ = RAW[spec], []
    for m in re.finditer(r'<div class="kit-state">', b):
        h = b[m.start():element_end(b, m.start())]
        out_.append((H.unescape(re.sub(r'<[^>]+>', '', re.search(r'<p class="kit-label">(.*?)</p>', h, re.S).group(1))).strip(), h))
    return out_
def _unid(h, sfx):
    ids = set(re.findall(r'#([a-zA-Z][\w-]*)', re.sub(r'/\*.*?\*/|\{[^{}]*\}', '', open(os.path.join(ROOT, 'design-system/index.css')).read(), flags=re.S)))
    h = re.sub(r'\b(id|for|aria-labelledby|aria-describedby|aria-controls|list|form)="([^"]+)"', lambda m: f'{m.group(1)}="' + ' '.join(x if x in ids else x + sfx for x in m.group(2).split()) + '"', h)
    return re.sub(r'href="#([^"]+)"', lambda m: f'href="#{m.group(1)}{sfx}"', h)
def _stage(h, sfx, sels, label):   # the docs' stage(): a crop window round the frame, the label kept as data
    h = _unid(h, sfx)
    i = h.index('<div class="kit-frame'); j = element_end(h, i)
    h = h[:i] + f'<div class="an-window" data-crop="{H.escape(json.dumps(sels))}"><div class="an-pan">' + h[i:j] + '</div></div>' + h[j:]
    h = re.sub(r'\s*<p class="kit-label">.*?</p>', '', h, count=1, flags=re.S)
    return h.replace('<div class="kit-state">', f'<div class="kit-state" data-label="{H.escape(label)}">', 1)
def states_grid(name, spec, sfx):
    return DST.grid(name, SMAP[name], _stages(spec), element_end, _stage, _unid, sfx)
def states_of_spec(spec):
    names = [r['name'] for r in rows_of.get(spec, []) if r['name'] in SMAP]
    return ''.join(f'<div class="kd-states"><h4 class="kd-states-h">{H.escape(n)} · States</h4>{states_grid(n, spec, "-s" + slug_c(n))}</div>' for n in names)

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
        '    <nav aria-label="Components by role">']
for r in ROLES:
    side.append(f'      <p class="kd-role"><a href="#{slug(r)}">{r}</a> <span>{len(specs_by_role[r])}</span></p><ul>'
                + ''.join(f'<li><a href="#{s}" data-names="{H.escape(" ".join([title_of(s)] + [x["name"] for x in rows_of[s]]).lower())}">{H.escape(title_of(s))}</a></li>' for s in specs_by_role[r]) + '</ul>')
side.append('      <p class="kd-role"><a href="#role-patterns">Patterns</a> <span>' + str(len(PATTERNS)) + '</span></p><ul>'
            + ''.join(f'<li><a href="#pattern-{pt["file"]}" data-names="{H.escape(pt["name"].lower())} pattern">{H.escape(pt["name"])}</a></li>' for pt in PATTERNS) + '</ul>')
side += ['    </nav>', '    <p class="kd-empty" hidden>No component matches.</p>', '  </div>', '</aside>']
intro = (f'<p class="kd-intro" id="kd-top"><strong>The Onrace kit</strong>: {len(items)} specimens for {N_COMPONENTS} inventory components, '
         f'every state shown on its own, from <a href="../index.css"><code>design-system/index.css</code></a> alone. '
         f'Every specimen on one page, the source the family pages are built from. <a href="index.html">The docs</a> · <a href="why.html">Why the system looks like this</a> · '
         f'<a href="https://github.com/JuliaMakedonska/Onrace/blob/main/ui/inventory.md">The inventory</a> · '
         f'<a href="https://github.com/JuliaMakedonska/Onrace/tree/main/design-system">design-system/ on GitHub</a></p>')
# the theme switch (Lesson 8, 2026-11-01): the stress test from step 5 on every specimen at once. Light is a proof only (C5)
THEME = ('<div class="kd-theme" role="group" aria-label="Theme"><span class="kd-theme-l">Theme</span>'
         '<button type="button" data-kd-theme="dark" aria-pressed="true">Dark</button><button type="button" data-kd-theme="light" aria-pressed="false">Light</button>'
         '<span class="kd-theme-note">Light is the stress test of the semantic roles; Onrace ships dark only.</span></div>')
main = ['<main class="kd-main">', '  ' + intro, '  ' + THEME, '']
for r in ROLES:
    main.append(f'\n  <!-- ================================================================ {r} -->\n'
                f'  <section class="kit-section" id="{slug(r)}" aria-labelledby="{slug(r)}-h">\n    <h2 id="{slug(r)}-h">{r} <span>{len(specs_by_role[r])}</span></h2>\n\n'
                + '\n\n'.join(card(s) for s in specs_by_role[r]) + '\n  </section>')
def _pcard(pt):
    on = ', '.join(f'<a href="{VIEWER}#{pt["found"][k][0]}">{SCREEN[k]}</a>' for k in pt['on'])
    return (f'    <div class="kit-item kd-pattern" id="pattern-{pt["file"]}" data-names="{H.escape(pt["name"].lower())} pattern">\n      <h3>{H.escape(pt["name"])}</h3>\n'
            f'      <div class="kd-meta"><p class="kd-line">{H.escape(pt["for"])}</p><p class="kd-line"><span class="kd-k">Stands on {len(pt["on"])} screens</span> {on}</p>'
            f'<p class="kd-line"><span class="kd-k">In the docs</span> <a href="patterns.html#{pt["file"]}">Patterns</a></p></div>\n'
            f'      <div class="kit-states">{PSTAGE(pt)}</div>\n    </div>')
main.append('\n  <!-- ================================================================ Patterns (ui/inventory.md → Patterns map) -->\n'
            f'  <section class="kit-section" id="role-patterns" aria-labelledby="role-patterns-h"><span id="shell"></span>\n    <h2 id="role-patterns-h">Patterns <span>{len(PATTERNS)}</span></h2>\n\n'
            + '\n\n'.join(_pcard(pt) for pt in PATTERNS) + '\n  </section>')
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
from docs_clean import clean   # no course-process text on a docs page (2026-11-05)
from docs_md import inline, GH   # markdown inline → HTML, a relative link to GitHub (shared with why.html)

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
    return [(lab, h) for lab, h in stages_of(row['spec']) if any(st in lab.lower() for st in sts) and '<div class="kit-frame' in h]   # a stage that is only a note isn't a variant
# an id the product's CSS selects on (dialog.alert #signout-confirm) keeps its name, or the copy would lose its look
CSS_IDS = set(re.findall(r'#([a-zA-Z][\w-]*)', re.sub(r'/\*.*?\*/|\{[^{}]*\}', '', open(os.path.join(ROOT, 'design-system/index.css')).read(), flags=re.S)))
def unid(h, sfx):   # a second copy of a stage on one page: its ids (and what points at them) take a suffix
    h = re.sub(r'\b(id|for|aria-labelledby|aria-describedby|aria-controls|list|form)="([^"]+)"', lambda m: f'{m.group(1)}="' + ' '.join(x if x in CSS_IDS else x + sfx for x in m.group(2).split()) + '"', h)
    return re.sub(r'href="#([^"]+)"', lambda m: f'href="#{m.group(1)}{sfx}"', h)
MAPROW = {}
for line in section(INV, 'Showcase map (2026-10-26)').split('\n'):
    c = cells(line) if line.startswith('| ') and not line.startswith('| Role') and not line.startswith('|---') else None
    if c and len(c) == 6: MAPROW[c[1].strip('*')] = {'states': [x.strip() for x in c[5].split(';') if x.strip()]}

# ---------------------------------------------------------------- the pages (the family restructure, 2026-11-05)
COMP_ROWS = [r for r in MAP if r['spec']]
by_name = {r['name']: r for r in MAP}
in_fams = [n for f in DS.FAMILIES for n in f['comps']]
assert sorted(in_fams) == sorted(r['name'] for r in MAP), ('ui/inventory.md → Docs families must hold every Showcase map component once',
    sorted(set(r['name'] for r in MAP) ^ set(in_fams)), [n for n in in_fams if in_fams.count(n) > 1])
# ui/inventory.md → Docs map: what each section says that can't be read from the files
DMAP = {}
for l in section(INV, 'Docs map (Lesson 9, step 2, 2026-11-04)').split('\n'):
    if not l.startswith('| **'): continue
    c = cells(l)
    m = re.match(r'\*\*([^*]+)\*\* `([^`]+)` (.*)', c[6])
    DMAP[c[0].strip('*')] = {'for': c[1], 'stage': None if c[2] == '—' else c[2],
        'parts': [(m2.group(1), m2.group(2).strip()) for m2 in (re.match(r'`([^`]+)` (.*)', x.strip()) for x in c[3].split('; ')) if m2],
        'design': [x.strip() for x in c[4].split(' + ') if x.strip() and x.strip() != '—'],
        'rule': re.match(r'`([^`]+)` (.*)', c[5]).groups(), 'anti': m.groups() if m else None}

assert all(r['name'] in DMAP for r in COMP_ROWS), ('components with no Docs map row', [r['name'] for r in COMP_ROWS if r['name'] not in DMAP])

def viewer(key):
    base = key.split('?')[0]; scr = screen_of(base)
    state = base[len(scr) + 1:] if base != scr else ''
    return f'<a href="{VIEWER}#{H.escape(key)}">{H.escape(SCREEN[scr])}{" · " + H.escape(state) if state else ""} ↗</a>'
def label_of(h):
    return re.sub(r'<[^>]+>', '', re.search(r'<p class="kit-label">(.*?)</p>', h, re.S).group(1))
def tech(row, vs):   # technical details, folded: classes, the screens that use it, the native counterpart, then the sources
    classes = row['classes']
    code = ' '.join(f'<code>{"&lt;" + c[1:] if c.startswith("<") else "." + c}</code>' for c in classes)
    hits = used_on(classes)
    screens = ', '.join(f'<a href="{VIEWER}#{pages[0]}">{SCREEN[s]}</a>' for s, pages in sorted(hits.items(), key=lambda kv: list(SCREEN).index(kv[0])))
    ios = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1 ↗</a>', row['ios']) if row['ios'] != 'none' else 'none'
    quotes = ''.join(f'<blockquote class="dc-quote"><p>{inline(clean(q), "DESIGN.md")}</p><footer><a href="{GH}DESIGN.md">DESIGN.md</a> → {H.escape(clean(t))}</footer></blockquote>'
                     for t, q in (design_quote(x) for x in DMAP[row['name']]['design']))
    words = {}
    for _, h in vs:
        for line, v in carried(classes, h).items():
            w = words.setdefault(line, {'type': v['type'], 'screens': []})
            w['screens'] += [x for x in v['screens'] if x not in w['screens']]
    mc = ('<div class="tbl-wrap"><table class="dc-mc"><thead><tr><th>Line</th><th>Type</th><th>Screens</th></tr></thead><tbody>'
          + ''.join(f'<tr><td>{H.escape(l)}</td><td>{H.escape(v["type"])}</td><td>{H.escape(", ".join(v["screens"]))}</td></tr>' for l, v in list(words.items())[:12])
          + '</tbody></table></div>') if words else ''
    rows = [('Classes', code),
            (f'Used on {len(hits)} screen{"s" if len(hits) != 1 else ""}' if hits else 'Used on', screens or 'the showcase only'),
            ('Native iOS', ios),
            ('Specimen', f'<a href="specimens.html#{row["spec"]}">{H.escape(title_of(row["spec"]))}</a>, with every state beside it')]
    return ('<details class="dc-tech"><summary>Technical details <span class="fold-sub">classes, screens, iOS</span></summary><div class="dc-tech-body">'
            '<dl>' + ''.join(f'<dt>{k}</dt><dd>{v}</dd>' for k, v in rows) + '</dl>'
            + (f'<h4>From DESIGN.md</h4>{quotes}' if quotes else '') + (f'<h4>The words it carries</h4>{mc}' if mc else '') + '</div></details>')

def stage(h, sfx, sels, label):
    """One stage for a section: its ids suffixed, its label kept as data (the stage check keys on it), and its frame in a
    crop window: doc.js shows the component on its own when its parts cover a small share of the stage. The stage
    inside keeps its width and every style; the window only hides the rest."""
    h = unid(h, sfx)
    i = h.index('<div class="kit-frame'); j = element_end(h, i)
    h = h[:i] + f'<div class="an-window" data-crop="{H.escape(json.dumps(sels))}"><div class="an-pan">' + h[i:j] + '</div></div>' + h[j:]
    h = re.sub(r'\s*<p class="kit-label">.*?</p>', '', h, count=1, flags=re.S)
    return h.replace('<div class="kit-state">', f'<div class="kit-state" data-label="{H.escape(label)}">', 1)

def component(row):
    name, d = row['name'], DMAP[row['name']]
    sl = slug_c(name)
    vs = variants(row)
    assert vs, f'{name}: no stage matches its States'
    top_i = next((i for i, (lab, _) in enumerate(vs) if d['stage'] and d['stage'].lower() in lab.lower()), 0)
    sels = [sel for sel, _ in d['parts']]
    others = [(lab, h) for i, (lab, h) in enumerate(vs) if i != top_i]
    legend = ''.join(f'<li><button type="button" class="an-part" data-part="{n}" aria-pressed="false"><span>{H.escape(label)}</span> <code>{H.escape(sel)}</code></button></li>'
                     for n, (sel, label) in enumerate(d['parts']))
    rkey, rtext = d['rule']
    other, akey, atext = d['anti']
    out = [f'<section class="dc" id="{sl}" aria-labelledby="{sl}-h">',
           f'<h2 id="{sl}-h">{H.escape(name)}</h2>',
           f'<p class="dc-for">{H.escape(d["for"])}</p>',
           f'<div class="dc-spec" data-anatomy="{H.escape(json.dumps(d["parts"]))}">{stage(vs[top_i][1], "-" + sl, sels, vs[top_i][0])}</div>',
           f'<ul class="an-legend" aria-label="Parts of the {H.escape(name.lower())}">{legend}</ul>',
           '<div class="dc-rules">'
           f'<div class="dc-do"><h3>When to use</h3><p>{H.escape(rtext)}</p><p class="dc-see">See it: {viewer(rkey)}</p></div>'
           f'<div class="dc-dont"><h3>When not to</h3><p>{H.escape(atext)} Use <a href="{DS.section_url(other)}">{H.escape(other)}</a>.</p><p class="dc-see">See it: {viewer(akey)}</p></div>'
           '</div>']
    if others:
        out += [f'<h3 class="dc-h" id="{sl}-variants">Variants</h3>',
                '<div class="dc-variants">' + ''.join(f'<figure class="dc-variant">{stage(h, f"-{sl}-v{i}", sels, lab)}<figcaption>{H.escape(lab)}</figcaption></figure>'
                                                    for i, (lab, h) in enumerate(others)) + '</div>']
    st = ''
    if name in SMAP:   # every component you act on (ui/inventory.md → States map)
        st = states_grid(name, row['spec'], '-' + sl + '-st')
        out += [f'<h3 class="dc-h" id="{sl}-states">States</h3>', st]
    out += [tech(row, vs), '</section>']
    return '\n'.join(out), 'map-placeholder' in vs[top_i][1] + ''.join(h for _, h in others) + st

def retired(row):
    sl = slug_c(row['name'])
    why = MAPROW[row['name']]['states'][0]
    inv = ''.join(f'<p class="kd-line"><span class="kd-k">{k}</span> {inline(clean(v), "ui/inventory.md")}</p>' for k, v in inv_row(row['name']))
    return (f'<section class="dc dc--retired" id="{sl}" aria-labelledby="{sl}-h"><h2 id="{sl}-h">{H.escape(row["name"])} <span class="dc-tag">Retired</span></h2>'
            f'<p class="dc-for">{H.escape(why[0].upper() + why[1:])}.</p><div class="kd-meta">{inv}</div></section>')

written = set()
def write(rel, html_):
    open(os.path.join(ROOT, DOCS, rel), 'w').write(html_); written.add(rel)
for f in DS.FAMILIES:
    parts, needs_map = [], False
    for n in f['comps']:
        row = by_name[n]
        if row['spec']:
            h, m = component(row); parts.append(h); needs_map = needs_map or m
        else:
            parts.append(retired(row))
    main = (f'<p class="ds-crumb">{H.escape(f["role"])}</p><h1>{H.escape(f["name"])}</h1><p class="ds-lede">{H.escape(f["line"])}</p>\n' + '\n'.join(parts))
    write(f['page'] + '.html', DS.page(f'{f["name"]} · Onrace design system', f['page'], main, [(slug_c(n), n) for n in f['comps']],
                                       DS.MAP_DATA if needs_map else '', SPEC_JS))

# the Patterns page (Lesson 9 step 4, 2026-11-06): each pattern live from its file, the screens it stands on, when to use it
def pattern(pt):
    sl = pt['file']
    rows = ''.join(f'<tr><td>{viewer(pt["found"][k][0])}</td><td>' + ' '.join(f'<code>{H.escape(x)}</code>' for x in pt['found'][k]) + '</td></tr>' for k in pt['on'])
    comps = ', '.join(f'<a href="{DS.section_url(n)}">{H.escape(n)}</a>' for n in pt['comps'])
    cls = ' '.join(f'<code>{"not " if c.startswith("!") else ""}.{H.escape(c.lstrip("!"))}</code>' for c in pt['sig'])
    return '\n'.join([f'<section class="dc" id="{sl}" aria-labelledby="{sl}-h">', f'<h2 id="{sl}-h">{H.escape(pt["name"])}</h2>',
        f'<p class="dc-for">{H.escape(pt["for"])}</p>',
        f'<div class="dc-spec">{PSTAGE(pt, label=False)}</div>',
        '<div class="dc-rules">'
        f'<div class="dc-do"><h3>Use the pattern</h3><p>{H.escape(pt["use"])}</p></div>'
        f'<div class="dc-dont"><h3>Use the components</h3><p>{H.escape(pt["not"])}</p><p class="dc-see">Composed of {comps}</p></div></div>',
        f'<h3 class="dc-h" id="{sl}-on">Stands on {len(pt["on"])} screens</h3>',
        f'<div class="tbl-wrap"><table class="dc-mc"><thead><tr><th>Screen</th><th>Pages that carry {cls}</th></tr></thead><tbody>{rows}</tbody></table></div>',
        f'<p class="dc-see">The file: <code>design-system/patterns/{sl}.html</code></p>', '</section>'])
_np = ''.join(f'<tr><td>{H.escape(n["name"])}</td><td>' + ', '.join(viewer(n['found'][k][0]) for k in n['on']) + f'</td><td>{H.escape(n["why"])}</td></tr>' for n in NOT_PATTERNS)
_pmain = ('<p class="ds-crumb">Patterns</p><h1>Patterns</h1><p class="ds-lede">A pattern is a composition of existing components that already stands on three or more screens. '
          'Each is one file in <code>design-system/patterns/</code>, with no style of its own.</p>\n'
          + '\n'.join(pattern(pt) for pt in PATTERNS)
          + '\n<section class="dc" id="not-patterns" aria-labelledby="not-patterns-h"><h2 id="not-patterns-h">Not patterns</h2>'
          '<p class="dc-for">Each stays its components.</p>'
          f'<div class="tbl-wrap"><table class="dc-mc"><thead><tr><th>Candidate</th><th>Stands on</th><th>Why not</th></tr></thead><tbody>{_np}</tbody></table></div></section>')
write('patterns.html', DS.page('Patterns · Onrace design system', 'patterns', _pmain, [(pt['file'], pt['name']) for pt in PATTERNS] + [('not-patterns', 'Not patterns')], '', SPEC_JS))

# the start page: what the system is, how it's organised, the families, why.html
cards = []
for role in DS.ROLES:
    cards.append(f'<section class="ds-group" aria-labelledby="g-{slug_c(role)}"><h2 id="g-{slug_c(role)}">{H.escape(role)}</h2><div class="ds-cards">'
                 + ''.join(f'<a class="ds-card" href="{f["page"]}.html"><span class="ds-card-t">{H.escape(f["name"])}</span><span class="ds-card-l">{H.escape(f["line"])}</span>'
                           f'<span class="ds-card-n">{len(f["comps"])} component{"s" if len(f["comps"]) != 1 else ""}</span></a>' for f in DS.FAMILIES if f['role'] == role)
                 + '</div></section>')
start = (f'<h1>Onrace design system</h1><p class="ds-lede">{inline(DS.START, "ui/inventory.md")}</p>'
         '<p class="ds-links"><a href="why.html">Why the system looks like this</a> · <a href="patterns.html">Patterns</a> · <a href="specimens.html">Every specimen on one page</a> · '
         f'<a href="{GH}DESIGN.md">DESIGN.md</a> · <a href="{GH}design-system/README.md">The folder on GitHub</a></p>' + ''.join(cards))
# yesterday's start page was the specimen sheet: an old link to one of its cards (index.html#race-card) goes there
OLD = json.dumps(sorted(set(RAW) | {'shell'}))
write('index.html', DS.page('Onrace design system', 'index', start,
      scripts=f'<script>(function () {{ var id = location.hash.slice(1); if ({OLD}.indexOf(id) > -1) location.replace("specimens.html" + location.search + location.hash); }})();</script>\n'))

# the per-component pages of step 2: each now redirects to its section, keeping the query (?theme=light)
os.makedirs(os.path.join(ROOT, DOCS, 'components'), exist_ok=True)
for row in MAP:
    to = '../' + DS.section_url(row['name'])
    url, frag = to.split('#')
    write(f'components/{slug_c(row["name"])}.html', f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{H.escape(row['name'])} · Onrace design system</title>
<!-- GENERATED by scripts/build_kit_showcase.py: the component's page until 2026-11-05, now its section of a family page. -->
<script>location.replace('{url}' + location.search + '#{frag}');</script>
<meta http-equiv="refresh" content="0; url={to}">
<link rel="canonical" href="{to}">
</head>
<body>
<p><a href="{to}">{H.escape(row['name'])}</a></p>
</body>
</html>
""")
for f in glob.glob(os.path.join(ROOT, DOCS, '*.html')) + glob.glob(os.path.join(ROOT, DOCS, 'components', '*.html')):   # pages no family names any more
    rel = os.path.relpath(f, os.path.join(ROOT, DOCS))
    if rel not in written and rel not in ('specimens.html', 'why.html'): os.remove(f)
print('docs:', len(DS.FAMILIES), 'family pages,', len(COMP_ROWS), 'components (and', len(MAP) - len(COMP_ROWS), 'retired), the start page,', len(MAP), 'redirects')
print('kit showcase:', ', '.join(f'{r} {len(specs_by_role[r])}' for r in ROLES), '·', len(items), 'specimens,', N_COMPONENTS, 'components')
