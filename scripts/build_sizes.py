"""The photos' `sizes`, generated from the tokens and the slot each photo really fills (Lesson 10 step 7, 2026-11-20).

A `sizes` attribute is a media condition and a width written in a screen's markup, where no var() reaches. Until step 7
each page wrote its own by hand ("calc(100vw - 32px)" for a race card that is 342px wide in a 358px list card on a
desktop, the retired tablet breakpoint in Race detail's), so the browser chose the 1026 file for a 342 slot. Now every
<picture> on a screen, a pattern or an example names its slot (data-slot), SLOTS below says what that slot is in tokens
(--bp-desktop, --pane-w, --container-max, the gutters …), and this script writes the numbers into every <source> and
<img> of it. scripts/check_kit.py imports expected() and stops the build when a page's `sizes` differs, or a picture
has no slot, so a page can't drift from the tokens or keep a breakpoint of its own.

Usage: python3 scripts/build_sizes.py   (build_stand.py runs it before the checks)
"""
import glob, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOK = open(os.path.join(ROOT, 'design-system/tokens/tokens.css')).read()

def tok(name):   # a token's value as written (px or rem), following var() to a primitive
    v = re.search(r'^\s*--' + re.escape(name) + r':\s*([^;]+);', TOK, flags=re.M).group(1).strip()
    m = re.fullmatch(r'var\(--([a-z0-9-]+)\)', v)
    return tok(m.group(1)) if m else v

def px(name):    # a px token's number
    v = tok(name); assert v.endswith('px'), (name, v); return float(v[:-2])

def n(x):        # 48.0 -> "48"
    return ('%g' % x)

# Each slot: [(media or None, width)], first match wins, as `sizes` reads. Widths are what the photo is drawn at, in the
# components' own terms: a gutter is --space-4 a side, the race card's inset --space-2 a side, the result card's --space-5.
BP = tok('bp-desktop'); PANE = tok('pane-w'); CMAX = tok('container-max'); CMAXW = tok('container-max-wide')
G, IN, RES, COLGAP = px('space-4'), px('space-2'), px('space-5'), px('space-6')
PHONE_CARD = f'calc(min(100vw, {CMAX}) - {n(2 * G + 2 * IN)}px)'          # the list column (capped), less the gutters and the card's inset
PHONE_PAGE = f'calc(min(100vw, {CMAX}) - {n(2 * G)}px)'                   # a detail screen's column, less its gutters
SLOTS = {
    # Race browse: the list card on a desktop is a phone-width pane (split-view.css), its list in it with the phone's gutters
    'race-card': [(f'(min-width: {BP})', f'calc({PANE} - {n(2 * G + 2 * IN)}px)'), (None, PHONE_CARD)],
    # Saved races: on a desktop the list is two fifths of the wide container less its column gap (split-view.css: 2fr 3fr)
    'race-card-list': [(f'(min-width: {BP})', f'calc((min(100vw, {CMAXW}) - {n(COLGAP)}px) * 2 / 5 - {n(2 * G + 2 * IN)}px)'), (None, PHONE_CARD)],
    # Race detail: on a desktop it is Race browse's race card (a phone-width pane; design-system/tokens/desktop.js sends the page there)
    'race-photo': [(f'(min-width: {BP})', f'calc({PANE} - {n(2 * G)}px)'), (None, PHONE_PAGE)],
    # Race detail's states on their own: the screen's column at every width
    'race-photo-page': [(None, PHONE_PAGE)],
    # Result detail: drawn only in the desktop's result card, three fifths of the wide container less the column gap and the card's padding
    'result-photo': [(f'(min-width: {BP})', f'calc((min(100vw, {CMAXW}) - {n(COLGAP)}px) * 3 / 5 - {n(2 * RES)}px)'), (None, PHONE_PAGE)],
    # Results list: a row's thumbnail on a desktop, a --thumb-w square
    'thumb': [(None, tok('thumb-w'))],
    # the sign-in screens' photo half on a desktop
    'gate-art': [(None, '50vw')],
}

def expected(slot):
    return ', '.join((m + ' ' + w) if m else w for m, w in SLOTS[slot])

PAGES = sorted(p for p in glob.glob(os.path.join(ROOT, 'wireframes/*.html')) if not p.endswith('index.html')) \
      + sorted(glob.glob(os.path.join(ROOT, 'design-system/patterns/*.html'))) + sorted(glob.glob(os.path.join(ROOT, 'design-system/examples/*.html')))
PIC = re.compile(r'<picture\b([^>]*)>(.*?)</picture>', re.S)

def pictures(text):   # (slot or None, the picture's inner markup, its span)
    for m in PIC.finditer(text):
        s = re.search(r'data-slot="([^"]+)"', m.group(1))
        yield (s.group(1) if s else None), m.group(2), m.span()

def problems():       # what check_kit.py reports: a picture with no slot, an unknown slot, a sizes that isn't the slot's
    out = []
    for p in PAGES:
        rel = os.path.relpath(p, ROOT)
        for slot, inner, _ in pictures(open(p).read()):
            if slot is None: out.append(f'{rel}: a <picture> with no data-slot (scripts/build_sizes.py → SLOTS)'); continue
            if slot not in SLOTS: out.append(f'{rel}: data-slot="{slot}" isn\'t a slot in scripts/build_sizes.py'); continue
            for got in re.findall(r'\bsizes="([^"]*)"', inner):
                if got != expected(slot): out.append(f'{rel}: sizes="{got}" on a {slot} photo; the tokens say "{expected(slot)}"')
    return out

def write():
    changed = 0
    for p in PAGES:
        t = open(p).read()
        def fix(m):
            s = re.search(r'data-slot="([^"]+)"', m.group(1))
            if not s or s.group(1) not in SLOTS: return m.group(0)
            return '<picture' + m.group(1) + '>' + re.sub(r'\bsizes="[^"]*"', 'sizes="' + expected(s.group(1)) + '"', m.group(2)) + '</picture>'
        u = PIC.sub(fix, t)
        if u != t: open(p, 'w').write(u); changed += 1
    return changed

if __name__ == '__main__':
    c = write(); bad = problems()
    for b in bad: print('build_sizes: ' + b)
    print(f'build_sizes: {"FAIL" if bad else "pass"} · {len(SLOTS)} slots, {c} pages rewritten')
    raise SystemExit(1 if bad else 0)
