"""Component states for the docs (Lesson 9 step 3, 2026-11-05): ui/inventory.md → States map, applied to the specimens.

For each component you act on, the named stage of its specimen is cut down to the part it keeps (and the ancestors the
product's selectors need), then shown At rest, Hover, Pressed, Focus and Disabled, in Dark and in Light, and Invalid where
the map names a stage. The states come from the product's own CSS: the stand-ins .is-hover, .is-pressed and .is-focus
sit in the same selectors as :hover, :active and :focus-visible (design-system/components/base.css), Disabled sets the
real attribute, and each theme is data-theme-scope on the stage's frame (design-system/tokens/tokens.css). Nothing here
draws a state by hand, so a state shown in the docs is the state the screens get.
Used by scripts/build_kit_showcase.py for specimens.html and the family pages; the same HTML on both, so
scripts/check_docs_stages.mjs compares them (without widths: a cell's width is the page's layout, not the product's).
"""
import re, html as H, json
from html.parser import HTMLParser

VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr'}
class N:
    def __init__(self, tag=None, attrs=None, text=None, parent=None):
        self.tag, self.attrs, self.text, self.parent, self.kids = tag, list(attrs or []), text, parent, []
    def get(self, k):
        return next((v for a, v in self.attrs if a == k), None)
    def has(self, k): return any(a == k for a, _ in self.attrs)
    def set(self, k, v):
        for i, (a, _) in enumerate(self.attrs):
            if a == k: self.attrs[i] = (k, v); return
        self.attrs.append((k, v))
    def add_class(self, c):
        cl = (self.get('class') or '').split()
        if c not in cl: self.set('class', ' '.join(cl + [c]))
class Tree(HTMLParser):
    def __init__(self, src):
        super().__init__(convert_charrefs=False)
        self.root = N('#root'); self.cur = self.root; self.feed(src); self.close()
    def handle_starttag(self, tag, attrs):
        n = N(tag, attrs, parent=self.cur); self.cur.kids.append(n)
        if tag not in VOID: self.cur = n
    def handle_startendtag(self, tag, attrs):
        self.cur.kids.append(N(tag, attrs, parent=self.cur))
    def handle_endtag(self, tag):
        n = self.cur
        while n is not self.root and n.tag != tag: n = n.parent
        if n is not self.root: self.cur = n.parent
    def _t(self, t): self.cur.kids.append(N(text=t, parent=self.cur))
    def handle_data(self, d): self._t(d)
    def handle_entityref(self, name): self._t(f'&{name};')
    def handle_charref(self, name): self._t(f'&#{name};')
    def handle_comment(self, d): self._t(f'<!--{d}-->')
    def handle_decl(self, d): self._t(f'<!{d}>')
def out(n):
    if n.tag is None: return n.text
    if n.tag == '#root': return ''.join(out(k) for k in n.kids)
    a = ''.join(f' {k}' if v is None else f' {k}="{H.escape(v, quote=True)}"' for k, v in n.attrs)
    return f'<{n.tag}{a}>' + ('' if n.tag in VOID else ''.join(out(k) for k in n.kids) + f'</{n.tag}>')

SEL = re.compile(r'^([a-z][a-z0-9]*)?((?:\.[\w-]+|\[[\w-]+(?:="[^"]*")?\]|#[\w-]+)*)$')
def matches(n, sel):
    if n.tag in (None, '#root'): return False
    if ',' in sel: return any(matches(n, x.strip()) for x in sel.split(','))   # a selector list (2026-11-06: keep the group, or the form, so the error under it stays in the cell)
    m = SEL.match(sel); assert m, f'States map: a selector the docs can\'t read: {sel}'
    if m.group(1) and n.tag != m.group(1): return False
    cl = (n.get('class') or '').split()
    for part in re.findall(r'\.[\w-]+|\[[\w-]+(?:="[^"]*")?\]|#[\w-]+', m.group(2)):
        if part[0] == '.' and part[1:] not in cl: return False
        if part[0] == '#' and n.get('id') != part[1:]: return False
        if part[0] == '[':
            k, _, v = part[1:-1].partition('=')
            if not n.has(k) or (v and n.get(k) != v.strip('"')): return False
    return True
def walk(n):
    for k in n.kids:
        if k.tag is not None: yield k; yield from walk(k)
def first(n, sel): return next((x for x in walk(n) if matches(x, sel)), None)
def closest(n, sel):
    while n is not None and n.tag != '#root':
        if matches(n, sel): return n
        n = n.parent
    return None
def prune(keep, top):   # keep only the path from top to keep, and keep's whole subtree
    n = keep
    while n is not top:
        n.parent.kids = [n]; n = n.parent

STATES = ['At rest', 'Hover', 'Pressed', 'Focus', 'Disabled']
STAND_IN = {'Hover': 'is-hover', 'Pressed': 'is-pressed', 'Focus': 'is-focus'}
def read_map(inv, cells):
    sec = re.search(r'^## States map .*?\n(.*?)(?=^## |\Z)', inv, flags=re.M | re.S).group(1)
    rows = {}
    for l in sec.split('\n'):
        if not l.startswith('| **'): continue
        c = cells(l); d = lambda x: None if x == '—' else x.strip('`')
        rows[c[0].strip('*')] = {'stage': c[1], 'keep': d(c[2]), 'control': d(c[3]), 'focus': d(c[4]), 'disabled': d(c[5]),
                                 'crop': c[6], 'w': c[7], 'invalid': d(c[8])}
    return rows

def build(frame_html, m, state, theme):
    """One state of one component in one theme: the stage's frame, cut down, the state applied, the theme scoped."""
    t = Tree(frame_html); frame = next(k for k in t.root.kids if k.tag)
    frame.set('data-theme-scope', theme.lower())
    ifr = first(frame, 'iframe')
    if ifr is not None and ifr.has('srcdoc'):   # the tab bar: its stage is a frame of its own; the state goes inside it
        inner = Tree(ifr.get('srcdoc')); body = first(inner.root, 'body')
        body.set('data-theme-scope', theme.lower())
        ctl = first(body, m['control']); assert ctl, f'States map: "{m["control"]}" finds nothing in the frame'
        keep = closest(ctl, m['keep']) if m['keep'] else ctl
        apply(ctl, keep, m, state)
        (keep if m['crop'] == 'keep' else ctl).set('data-st-crop', None)
        ifr.set('srcdoc', out(inner.root))
        return out(t.root)
    ctl = first(frame, m['control']); assert ctl, f'States map: "{m["control"]}" finds nothing on "{m["stage"]}"'
    keep = closest(ctl, m['keep']) if m['keep'] else ctl
    assert keep, f'States map: no "{m["keep"]}" round "{m["control"]}"'
    prune(keep, frame)
    apply(ctl, keep, m, state)
    (keep if m['crop'] == 'keep' else ctl).set('data-st-crop', None)
    return out(t.root)
def apply(ctl, keep, m, state):
    if state in ('Hover', 'Pressed'): ctl.add_class(STAND_IN[state])
    if state == 'Focus': ((first(ctl, m['focus']) if m['focus'] else None) or ctl).add_class('is-focus')
    if state == 'Disabled':
        sel = m['disabled']
        targets = [x for x in walk(keep) if matches(x, sel[1:])] if sel and sel.startswith('*') else [((first(ctl, sel) if sel else None) or ctl)]
        for x in targets:
            if x.tag in ('button', 'input', 'select', 'textarea'): x.set('disabled', None)
            else: x.set('aria-disabled', 'true')

def grid(name, m, stages, element_end, stage, unid, sfx):
    """The States block: a row per theme (only the docs' current theme's shows; both are built and checked), a cell per state. stages: (label, html) of the specimen's stages."""
    def frame_of(label_part):
        hit = next(((lab, h) for lab, h in stages if label_part.lower() in lab.lower()), None)
        assert hit, f'States map: {name} has no stage labelled "{label_part}"'
        h = hit[1]; i = h.index('<div class="kit-frame'); return h[i:element_end(h, i)]
    base = frame_of(m['stage'])
    inv = frame_of(m['invalid']) if m['invalid'] else None
    rows = []
    FOCUS_ROW = 'Keyboard focus (iPad keyboard, Full Keyboard Access)'   # designer, 2026-11-08: focus shows only from a keyboard, never after a tap, so it isn't a state of the tap row
    for theme in ('Dark', 'Light'):
        cells, focus = [], []
        for st in STATES + (['Invalid'] if inv else []):
            fr = build(inv if st == 'Invalid' else base, m, 'At rest' if st == 'Invalid' else st, theme)
            label = f'{name} · {st} · {theme}'
            k = f'<div class="kit-state" data-nogeo><p class="kit-label">{H.escape(label)}</p>{fr}</div>'
            k = k.replace('<div class="kit-state" data-nogeo>', '<div class="kit-state">', 1)
            got = stage(k, f"{sfx}-{theme[0].lower()}{STATES.index(st) if st in STATES else 9}", ['[data-st-crop]'], label)
            got = got.replace('<div class="kit-state" data-label=', '<div class="kit-state" data-nogeo data-label=', 1)
            (focus if st == 'Focus' else cells).append(f'<figure class="dc-state">{got}<figcaption>{st}</figcaption></figure>')
        rows.append(f'<div class="dc-states-theme" data-st-theme="{theme.lower()}"><div class="dc-states-row">' + ''.join(cells) + '</div>'
                    f'<p class="dc-states-k">{FOCUS_ROW}</p><div class="dc-states-row">' + ''.join(focus) + '</div></div>')   # one block per theme; the docs' theme switch shows its own (doc.css, 2026-11-07)
    return f'<div class="dc-states" data-w="{m["w"]}">' + ''.join(rows) + '</div>'
