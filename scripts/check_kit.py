"""Check the kit showcase (ui/kit.html) against the inventory and microcopy.md (2026-10-26).

Run from anywhere:  python3 scripts/check_kit.py      exit code 1 on any failure.
build_stand.py runs it on every build. It fails when:
- an inventory component (ui/inventory.md: the Shared, Discovery, Archive and Infrastructure tables, and the One-off
  blocks) has no row in the inventory's Showcase map;
- a Showcase map row names a specimen ui/kit.html doesn't have, or a state its specimen doesn't label;
- a word shown in a specimen (text, aria-label, placeholder, alt) appears nowhere in microcopy.md: the showcase uses
  the screens' own words, and every product word is recorded there.
"""
import os, re, sys
from html.parser import HTMLParser
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INV = open(os.path.join(ROOT, 'ui/inventory.md')).read()
KIT = open(os.path.join(ROOT, 'ui/kit.html')).read()
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
items = {m.group(1): m.start() for m in re.finditer(r'<div class="kit-item" id="([^"]+)">', KIT)}
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
        fails.append(f'{r["name"]}: specimen #{r["spec"]} is not in ui/kit.html'); continue
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

if fails:
    print(f'check_kit: FAIL ({len(fails)})\n  ' + '\n  '.join(fails))
    sys.exit(1)
print(f'check_kit: pass ({len(names)} inventory components mapped, {len(MAP)} map rows with their states, {len(p.words)} specimen words in microcopy.md)')
