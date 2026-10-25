"""Lay out the kit showcase (ui/kit.html) as a component sheet, from ui/inventory.md (2026-10-26).

Run from anywhere:  python3 scripts/build_kit_showcase.py      (build_stand.py runs it before its checks)
The specimens stay hand-written in ui/kit.html (the "keep it" rule: a change goes there and to every screen). This
script only (re)writes, idempotently, everything around them:
- a sticky left sidebar: a quick filter, then the roles (Navigation, Cards and lists, Forms, Feedback, One-off) with every
  specimen under its role, the current one highlighted on scroll; on a phone it folds into a menu;
- one short intro line (what the kit is, the counts, links to ui/inventory.md and ui/kit.css);
- one card per specimen: a compact header in the documentation's own style (name, classes, "Used on N screens" linked to
  the viewer, the HIG link, where interaction is live), the specimen's notes folded, then its states side by side, each on
  its own stage with its label under it.
The documentation's look is ui/kit-doc.css (the artifact pages' style); the stages are ui/kit.css (the product).
"""
import os, re, glob, html as H
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, 'ui/kit.html')
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
unmapped = [i for i in items if i not in role_of]
assert not unmapped, ('specimens with no Showcase map row', unmapped)
head = KIT[:KIT.index('<body')]
head = re.sub(r'\n<link rel="stylesheet" href="kit-doc\.css[^"]*">', '', head)
head = re.sub(r'(<link rel="stylesheet" href="kit\.css[^"]*">)', r'\1\n<link rel="stylesheet" href="kit-doc.css">', head, count=1)   # build_stand.py stamps it
shell = re.search(r'  <section class="kit-section" id="shell".*?\n  </section>\n', KIT, re.S).group(0)
tail_from = KIT.index('<!-- /kd -->') + len('<!-- /kd -->') if '<!-- /kd -->' in KIT else KIT.index('</main>') + len('</main>')
tail = re.sub(r'\n<script>\n/\* kd:js.*?</script>', '', KIT[tail_from:], flags=re.S)
shell = shell.replace('<h2 id="shell-h">Shell</h2>', '<h3 id="shell-h">Shell</h3>')

# ---------------------------------------------------------------- one card per specimen
def title_of(spec):
    return re.sub(r'<[^>]+>', '', re.search(r'<h3>(.*?)</h3>', items[spec], re.S).group(1)).strip()
def meta(spec):
    rows = rows_of[spec]
    classes = list(dict.fromkeys(c for r in rows for c in r['classes']))
    code = ' '.join(f'<code>{"&lt;" + c[1:] if c.startswith("<") else "." + c}</code>' for c in classes)
    hits = used_on(classes)
    screens = ', '.join(f'<a href="../wireframes/index.html#{pages[0]}">{SCREEN[s]}</a>' for s, pages in sorted(hits.items(), key=lambda kv: list(SCREEN).index(kv[0])))
    used = f'<span class="kd-k">Used on {len(hits)} screen{"s" if len(hits) != 1 else ""}</span> {screens}' if hits else '<span class="kd-k">Used on</span> the showcase only'
    ios = list(dict.fromkeys(r['ios'] for r in rows if r['ios'] != 'none'))
    ios_html = ' · '.join(re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1 ↗</a>', x) for x in ios) or 'none'
    comps = ', '.join(dict.fromkeys(r['name'] for r in rows))
    live = re.search(r'<(button|a href|input|select|textarea)\b', items[spec].split('<div class="kit-states">', 1)[-1]) is not None
    parts = ([f'<p class="kd-line kd-comps">{H.escape(comps)}</p>'] if comps != title_of(spec) else []) + [f'<p class="kd-line">{code}</p>', f'<p class="kd-line">{used}</p>',
             f'<p class="kd-line"><span class="kd-k">Native iOS</span> {ios_html}</p>']
    if live: parts.append('<p class="kd-line"><span class="kd-k kd-live">Live</span> hover, Tab focus and press work on the stages below</p>')
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
intro = (f'<p class="kd-intro" id="kd-top"><strong>The Onrace kit</strong>: {len(items)} specimens covering {N_COMPONENTS} inventory components, '
         f'every state on its own stage, styled by <a href="kit.css"><code>ui/kit.css</code></a> alone. '
         f'<a href="https://github.com/JuliaMakedonska/Onrace/blob/main/ui/inventory.md">The inventory</a> · '
         f'<a href="https://github.com/JuliaMakedonska/Onrace/blob/main/ui/kit.css">kit.css on GitHub</a></p>')
main = ['<main class="kd-main">', '  ' + intro, '', '  <div class="kit-item kd-shell" id="shell-card" data-names="shell tab bar large title">', shell.replace('  <section', '  <section', 1), '  </div>']
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
page = head + body + '\n' + JS + tail
open(P, 'w').write(page)
print('kit showcase:', ', '.join(f'{r} {len(specs_by_role[r])}' for r in ROLES), '·', len(items), 'specimens,', N_COMPONENTS, 'components')
