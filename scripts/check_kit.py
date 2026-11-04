"""Check the kit showcase (design-system/docs/index.html, ui/kit.html until Lesson 9 step 2) and the design-system docs
against the inventory and microcopy.md (2026-10-26; the docs pages since 2026-11-04).

Run from anywhere:  python3 scripts/check_kit.py      exit code 1 on any failure.
build_stand.py runs it on every build. It fails when:
- an inventory component (ui/inventory.md: the Shared, Discovery, Archive and Infrastructure tables, and the One-off
  blocks) has no row in the inventory's Showcase map;
- a Showcase map row names a specimen the showcase doesn't have, or a state its specimen doesn't label;
- a word shown in a specimen (text, aria-label, placeholder, alt) appears nowhere in microcopy.md: the showcase uses
  the screens' own words, and every product word is recorded there;
- (Lesson 8 step 4; Lesson 9 step 1) a screen (wireframes/*.html), the showcase or the shell doesn't link
  design-system/index.css once, links tokens.css or a components file directly, a page with the static map (Race
  browse, the showcase) doesn't link design-system/map-data.css, any of them still links ui/kit.css or ui/map.css,
  a screen has a <style> block or a style attribute, or a screen uses a class (in its markup or set by its script)
  that design-system/components/index.css doesn't define;
- (Lesson 9 step 2) an inventory component has no page in design-system/docs/components/, a docs page doesn't link
  design-system/index.css once (the file the product links, so a page can't show another look), a docs page that
  shows the static map doesn't link design-system/map-data.css, or a word on a docs page (its text, aria-label, alt,
  placeholder, title) appears neither in microcopy.md nor in the source docs: DESIGN.md, concept/concept.md,
  concept/references.md and ui/inventory.md, but not the inventory's own Docs map, whose words must come from the rest.
"""
import os, re, sys
from html.parser import HTMLParser
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INV = open(os.path.join(ROOT, 'ui/inventory.md')).read()
KIT_PATH = os.path.join(ROOT, 'design-system/docs/index.html')
KIT = open(KIT_PATH).read()
MC = open(os.path.join(ROOT, 'microcopy.md')).read()
fails = []

def section(md, title):
    m = re.search(r'^## ' + re.escape(title) + r'\n(.*?)(?=^## |\Z)', md, flags=re.M | re.S)
    return m.group(1) if m else ''

# ---------------------------------------------------------------- the Showcase map
MAP = []
for l in section(INV, 'Showcase map (2026-10-26)').split('\n'):
    c = [x.strip() for x in l.strip().strip('|').split(' | ')] if l.startswith('| ') and not l.startswith('| Role') else None
    if c and len(c) == 6:
        MAP.append({'role': c[0], 'name': re.sub(r'\*\*', '', c[1]), 'spec': c[2].strip('`#') if c[2] != '—' else None,
                    'classes': re.findall(r'`([^`]+)`', c[3]), 'ios': c[4], 'states': [s.strip() for s in c[5].split(';') if s.strip()]})
assert MAP, 'no Showcase map in ui/inventory.md'
MAPPED = {r['name'] for r in MAP}

# ---------------------------------------------------------------- every inventory component is mapped
names = []
for t in ('Shared', 'Discovery', 'Archive', 'Infrastructure'):
    names += re.findall(r'^\| \*\*([^*]+)\*\*', section(INV, t), flags=re.M)
names += [n for n in re.findall(r'^- \*\*([^*]+)\*\*', section(INV, 'One-off'), flags=re.M) if not n.startswith('On the kit')]
for n in names:
    if n.rstrip(':') not in MAPPED:
        fails.append(f'inventory component without a Showcase map row: {n}')

# ---------------------------------------------------------------- every mapped component has its specimen and states
items = {m.group(1): m.start() for m in re.finditer(r'<div class="kit-item" id="([^"]+)"[^>]*>', KIT)}
order = sorted(items.values()) + [len(KIT)]
def block(id_):
    i = items[id_]
    return KIT[i:order[order.index(i) + 1]]
for r in MAP:
    if r['spec'] is None:
        if not r['states'] or not r['states'][0].startswith('retired'):
            fails.append(f'{r["name"]}: no specimen and not marked retired')
        continue
    if r['spec'] not in items:
        fails.append(f'{r["name"]}: specimen #{r["spec"]} is not in the showcase'); continue
    labels = [re.sub(r'<[^>]+>', '', l).replace('&amp;', '&').lower() for l in re.findall(r'<p class="kit-label">(.*?)</p>', block(r['spec']), flags=re.S)]
    for st in r['states']:
        if not any(st.lower() in l for l in labels):
            fails.append(f'{r["name"]} (#{r["spec"]}): no state labelled "{st}"')

# ---------------------------------------------------------------- every word in a specimen is in microcopy.md
WORD = re.compile(r"[A-Za-z][A-Za-z’']*")
norm = lambda w: w.lower().replace('’', "'").strip("'")
MC_WORDS = {norm(w) for w in WORD.findall(MC)}
class Spec(HTMLParser):
    def __init__(self):
        super().__init__(); self.depth = 0; self.stack = []; self.words = []; self.skip = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('script', 'style'): self.skip += 1
        inside = self.depth > 0 or 'kit-frame' in (a.get('class') or '').split()
        if tag not in ('br', 'img', 'input', 'source', 'wbr', 'meta', 'link'):
            self.stack.append(inside)
            if inside: self.depth += 1
        if inside:
            for k in ('aria-label', 'placeholder', 'alt', 'value', 'title'):
                if a.get(k): self.words += [(w, a[k]) for w in WORD.findall(a[k])]
    def handle_endtag(self, tag):
        if tag in ('script', 'style'): self.skip -= 1
        if tag not in ('br', 'img', 'input', 'source', 'wbr', 'meta', 'link') and self.stack:
            if self.stack.pop(): self.depth -= 1
    def handle_data(self, d):
        if self.depth and not self.skip and d.strip():
            self.words += [(w, d.strip()) for w in WORD.findall(d)]
p = Spec(); p.feed(KIT)
missing = {}
for w, ctx in p.words:
    if norm(w) not in MC_WORDS:
        missing.setdefault(norm(w), ctx[:60])
for w, ctx in sorted(missing.items()):
    fails.append(f'word in a specimen, not in microcopy.md: "{w}" (in "{ctx}")')

# ---------------------------------------------------------------- the screens on tokens and components (Lesson 8 step 4)
import glob
_css = re.sub(r'url\("[^"]*"\)', '', re.sub(r'/\*.*?\*/', '', open(os.path.join(ROOT, 'design-system/components/index.css')).read(), flags=re.S))
DEFINED = set(re.findall(r'\.(-?[a-zA-Z_][\w-]*)', ''.join(re.findall(r'([^{}]+)\{', _css))))
SCREENS = sorted(p for p in glob.glob(os.path.join(ROOT, 'wireframes/*.html')) if not p.endswith('index.html'))
ENTRY, MAPDATA = os.path.join(ROOT, 'design-system/index.css'), os.path.join(ROOT, 'design-system/map-data.css')
DOC_PAGES = sorted(glob.glob(os.path.join(ROOT, 'design-system/docs/*.html')) + glob.glob(os.path.join(ROOT, 'design-system/docs/components/*.html')))
for sp in SCREENS + [os.path.join(ROOT, 'ui/shell.html')] + DOC_PAGES:
    h, name = open(sp).read(), os.path.relpath(sp, ROOT)
    head = h[:h.index('</head>')]
    links = [os.path.normpath(os.path.join(os.path.dirname(sp), l)) for l in re.findall(r'href="([\w./-]+?\.css)(?:\?v=[0-9a-f]+)?"', head)]
    shown = [os.path.relpath(l, ROOT) for l in links]
    # Lesson 9 step 1: one entry point, design-system/index.css (tokens + components, generated); never the two halves
    if links.count(ENTRY) != 1:
        fails.append(f'{name}: links design-system/index.css once? found {shown}')
    if any(re.search(r'/design-system/(?:tokens|components)/[\w-]+\.css$', l) for l in links):
        fails.append(f'{name}: links tokens.css or a components file directly (link design-system/index.css): {shown}')
    if ('race-browse' in name or 'map-placeholder' in h) and MAPDATA not in links:
        fails.append(f'{name}: shows the static map but doesn\'t link design-system/map-data.css')
    if re.search(r'(?:kit|/map)\.css', head):
        fails.append(f'{name}: still links ui/kit.css or ui/map.css')
    if sp in SCREENS:
        if re.search(r'<style\b|\sstyle="', h):
            fails.append(f'{name}: a style block or a style attribute (every value comes from the kit)')
        body = re.sub(r'<script\b.*?</script>', '', h, flags=re.S)
        used = {c for a in re.findall(r'class="([^"]*)"', body) for c in a.split()} | set(re.findall(r"classList\.(?:add|toggle|remove)\('([\w-]+)'", h))
        for c in sorted(used - DEFINED):
            fails.append(f'{name}: class .{c} isn\'t defined in design-system/components/index.css')

# ---------------------------------------------------------------- the docs pages (Lesson 9 step 2, 2026-11-04)
slug_c = lambda n: re.sub(r'[^a-z0-9]+', '-', n.lower()).strip('-')
for n in names:
    if not os.path.exists(os.path.join(ROOT, 'design-system/docs/components', slug_c(n.rstrip(':')) + '.html')):
        fails.append(f'inventory component without a page: {n} (design-system/docs/components/{slug_c(n.rstrip(":"))}.html)')
SOURCES = {f: open(os.path.join(ROOT, f)).read() for f in ('DESIGN.md', 'concept/concept.md', 'concept/references.md')}
SOURCES['ui/inventory.md'] = re.sub(r'^## Docs map .*?(?=^## |\Z)', '', INV, flags=re.M | re.S)   # the Docs map's words must come from the rest
VOCAB = MC_WORDS | {norm(w) for t in SOURCES.values() for w in WORD.findall(t)}
class Doc(HTMLParser):   # every word a reader sees on a docs page (scripts and styles aside)
    def __init__(self):
        super().__init__(); self.skip = 0; self.words = []
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style', 'code'): self.skip += 1   # <code> holds selectors and paths, not words
        for k, v in attrs:
            if k in ('aria-label', 'placeholder', 'alt', 'title') and v: self.words += [(w, v) for w in WORD.findall(v)]
            if k == 'srcdoc' and v: d = Doc(); d.feed(v); self.words += d.words
    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'code'): self.skip -= 1
    def handle_data(self, d):
        if not self.skip and d.strip(): self.words += [(w, d.strip()) for w in WORD.findall(d)]
doc_words, doc_missing = 0, {}
for dp in DOC_PAGES:
    d = Doc(); d.feed(open(dp).read()); doc_words += len(d.words)
    for w, ctx in d.words:
        if norm(w) not in VOCAB: doc_missing.setdefault(norm(w), f'{os.path.relpath(dp, ROOT)}: "{ctx[:60]}"')
for w, where in sorted(doc_missing.items()):
    fails.append(f'word on a docs page, in neither microcopy.md nor the source docs: "{w}" ({where})')

if fails:
    print(f'check_kit: FAIL ({len(fails)})\n  ' + '\n  '.join(fails))
    sys.exit(1)
print(f'check_kit: pass ({len(names)} inventory components mapped, {len(MAP)} map rows with their states, {len(p.words)} specimen words in microcopy.md; '
      f'{len(SCREENS)} screens, the shell and {len(DOC_PAGES)} docs pages on design-system/index.css, every screen class defined; '
      f'every component with its page; {doc_words} words on the docs pages, each in microcopy.md or the source docs)')
