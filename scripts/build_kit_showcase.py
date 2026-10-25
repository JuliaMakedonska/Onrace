"""Arrange the kit showcase (ui/kit.html) by role and write each component's facts, from ui/inventory.md (2026-10-26).

Run from anywhere:  python3 scripts/build_kit_showcase.py      (build_stand.py runs it before its checks)
The specimens themselves stay hand-written in ui/kit.html (the "keep it" rule: a change goes there and to every screen).
This script only (re)writes, idempotently:
- the sticky nav by role (Navigation, Cards and lists, Forms, Feedback, One-off) with the number of components in each;
- the role sections, each holding its specimens in the inventory's Showcase map order (a specimen sits under the role
  of its first map row);
- each specimen's facts, between <!-- kit:meta --> markers under its heading: its components and their classes, the
  screens that use them (found in wireframes/*.html, linked to the viewer), the native iOS counterpart with its HIG
  link, and where interaction is live.
"""
import os, re, glob
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
for m in re.finditer(r'    <div class="kit-item" id="([^"]+)">', KIT):
    items[m.group(1)] = KIT[m.start():element_end(KIT, m.start() + 4)]
unmapped = [i for i in items if i not in role_of]
assert not unmapped, ('specimens with no Showcase map row', unmapped)
head_start = KIT.index('<main class="kit">\n') + len('<main class="kit">\n')
prefix = KIT[:head_start]
header = re.search(r'  <header class="kit-head">.*?</header>\n', KIT, re.S).group(0)
header = re.sub(r'\n    <ul class="kit-toc">.*?</ul>', '', header, flags=re.S)   # the nav below replaces the old contents list
shell = re.search(r'  <!-- =+ Shell -->\n  <section class="kit-section" id="shell".*?\n  </section>\n', KIT, re.S).group(0)
suffix = KIT[KIT.index('</main>'):]

# ---------------------------------------------------------------- each specimen's facts
def meta(spec):
    rows = rows_of[spec]
    comps = ', '.join(dict.fromkeys(r['name'] for r in rows))
    classes = list(dict.fromkeys(c for r in rows for c in r['classes']))
    code = ' '.join(f'<code>{"&lt;" + c[1:] if c.startswith("<") else "." + c}</code>' for c in classes)
    hits = used_on(classes)
    screens = ', '.join(f'<a href="../wireframes/index.html#{pages[0] if s in pages else pages[0]}">{SCREEN[s]}</a>'
                        for s, pages in sorted(hits.items(), key=lambda kv: list(SCREEN).index(kv[0])))
    used = f'{len(hits)} screen{"s" if len(hits) != 1 else ""}: {screens}' if hits else 'the showcase only (no screen yet)'
    ios = list(dict.fromkeys(r['ios'] for r in rows if r['ios'] != 'none'))
    ios_html = ' · '.join(re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', x) for x in ios) or 'none'
    live = re.search(r'<(button|a href|input|select|textarea)\b', items[spec].split('<div class="kit-states">', 1)[-1]) is not None
    lines = [('Components', comps), ('Classes', code), ('Used on', used), ('Native iOS', ios_html)]
    if live: lines.append(('Live', 'hover, Tab focus and press work on the specimens below'))
    dl = ''.join(f'<dt>{k}</dt><dd>{v}</dd>' for k, v in lines)
    return f'<!-- kit:meta (scripts/build_kit_showcase.py) --><dl class="kit-meta">{dl}</dl><!-- /kit:meta -->'
def with_meta(spec):
    b = re.sub(r'\n      <!-- kit:meta.*?<!-- /kit:meta -->', '', items[spec], flags=re.S)
    return re.sub(r'(</h3>)', r'\1\n      ' + meta(spec).replace('\\', r'\\'), b, count=1)

# ---------------------------------------------------------------- the page, by role
slug = lambda r: 'role-' + re.sub(r'[^a-z]+', '-', r.lower()).strip('-')
specs_by_role = {r: [] for r in ROLES}
for r in MAP:
    if r['spec'] and r['spec'] not in specs_by_role[role_of[r['spec']]]:
        specs_by_role[role_of[r['spec']]].append(r['spec'])
nav = '  <nav class="kit-nav" aria-label="Components by role">' + ''.join(
    f'<a href="#{slug(r)}">{r} <span>{len(specs_by_role[r])}</span></a>' for r in ROLES) + '<a href="#shell">Shell</a></nav>\n'
sections = ''
for r in ROLES:
    n = len(specs_by_role[r])
    sections += (f'\n  <!-- ================================================================ {r} -->\n'
                 f'  <section class="kit-section" id="{slug(r)}" aria-labelledby="{slug(r)}-h">\n    <h2 id="{slug(r)}-h">{r}</h2>\n'
                 f'    <p>{n} specimen{"s" if n != 1 else ""}, as <code>ui/inventory.md</code> → Showcase map groups them.</p>\n\n'
                 + '\n\n'.join(with_meta(s) for s in specs_by_role[r]) + '\n  </section>\n')
page = prefix + '\n' + header + '\n' + nav + '\n' + shell + sections + '\n' + suffix
open(P, 'w').write(page)
print('kit showcase:', ', '.join(f'{r} {len(specs_by_role[r])}' for r in ROLES), '·', len(items), 'specimens')
