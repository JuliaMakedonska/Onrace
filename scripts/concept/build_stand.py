"""Generate concept/concept.html (the concept stand).

Usage, from the repo root:  python3 scripts/concept/build_stand.py
The page holds no style values: it links tokens.css and components.css. Every
contrast ratio is computed here from the hex values in concept/tokens.css, and
the build stops if any text pair fails WCAG AA. Re-run after changing a token,
then copy concept.html, tokens.css and components.css to public/concept/."""
import sys, os, re
sys.path.insert(0, os.path.dirname(__file__))
from colorlib import cr

HERE = os.path.dirname(os.path.abspath(__file__))
ICONS = os.path.join(HERE, 'icons')
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
TOK = open(os.path.join(ROOT, 'concept/tokens.css')).read() + open(os.path.join(ROOT, 'concept/map.css')).read()

def tok(name):
    m = re.search(r'--' + re.escape(name) + r':\s*([^;]+);', TOK)
    v = m.group(1).strip()
    r = re.match(r'var\(--([a-z0-9-]+)\)', v)
    return tok(r.group(1)) if r else v

def svg(name, cls='icon'):
    s = open(f'{ICONS}/{name}-bold.svg').read().strip()
    return s.replace('<svg ', f'<svg class="{cls}" aria-hidden="true" focusable="false" ', 1).replace(' width="1em" height="1em"', '')

def sw(t): return f'<span class="swatch swatch--{t}"></span>'

_wrap_n = [0]
def wrap(label, table):
    return f'<div class="spec-wrap" tabindex="0" role="region" aria-label="{label}">{table}</div>'

# ---------------------------------------------------------------- contrast
PAIRS = [  # label, text token, background token, kind: 'text' | 'large' | 'ui' | 'exempt'
    ('Titles, body, finish time on the page', 'text-1', 'bg-0', 'text'),
    ('Titles, item titles, finish time on a card', 'text-1', 'bg-1', 'text'),
    ('Secondary button label', 'text-1', 'bg-2', 'text'),
    ('Active filter chip label (transparent chip, on the page)', 'text-1', 'bg-0', 'text'),
    ('Selected List/Map segment, hover and open fills', 'text-1', 'bg-3', 'text'),
    ('Unselected List/Map segment on hover', 'text-2', 'bg-3', 'text'),
    ('Meta on the page (counts, sort)', 'text-2', 'bg-0', 'text'),
    ('Meta on a card (month and year, location, proof line)', 'text-2', 'bg-1', 'text'),
    ('Search placeholder', 'text-2', 'bg-1', 'text'),
    ('Date day on the tile', 'text-1', 'bg-2', 'text'),
    ('Date month and year on the tile', 'text-2', 'bg-2', 'text'),
    ('Unselected List/Map segment', 'text-2', 'bg-2', 'text'),
    ('Inactive tab label', 'text-2', 'bg-bar', 'text'),
    ('Current tab label (accent)', 'accent', 'bg-bar', 'text'),
    ('Format chip label', 'chip-text', 'bg-2', 'text'),
    ('Primary button label', 'on-accent', 'accent', 'text'),
    ('Primary button label, hover', 'on-accent', 'accent-hover', 'text'),
    ('Error title and icon', 'error', 'error-bg', 'text'),
    ('Error body', 'text-1', 'error-bg', 'text'),
    ('Inline error text on a card', 'error', 'bg-1', 'text'),
    ('Success title and icon', 'success', 'success-bg', 'text'),
    ('Success body', 'text-1', 'success-bg', 'text'),
    ('Warning title, icon and body', 'warning', 'warning-bg', 'text'),
    ('Stand panels: secondary text', 'text-2', 'bg-bar', 'text'),
    ('Focus ring against the page (non-text, 3:1)', 'focus', 'bg-0', 'ui'),
    ('Focus ring against a card (non-text, 3:1)', 'focus', 'bg-1', 'ui'),
    ('Filter chip outline against the page (non-text, 3:1)', 'text-2', 'bg-0', 'ui'),
    ('Search field outline against its own fill (non-text, 3:1)', 'field-line', 'bg-1', 'ui'),
    ('Search field outline against the page (non-text, 3:1)', 'field-line', 'bg-0', 'ui'),
    ('Disabled button label', 'text-disabled', 'bg-2', 'exempt'),
    ('Result count number', 'text-1', 'bg-0', 'text'),
    ('Result count text, Sort: label', 'text-2', 'bg-0', 'text'),
    ('Sort value (Soonest first)', 'text-1', 'bg-0', 'text'),
    ('Sort chevron (non-text, 3:1)', 'text-1', 'bg-0', 'ui'),
    ('Filters label and icon on the secondary button', 'text-1', 'bg-2', 'text'),
    ('Empty and error state heading', 'text-1', 'bg-0', 'text'),
    ('Empty and error state body', 'text-2', 'bg-0', 'text'),
    ('Error icon in the state heading (non-text, 3:1)', 'error', 'bg-0', 'ui'),
    ('Disabled sort while loading', 'text-disabled', 'bg-0', 'exempt'),
    ('Skeleton bar on a card', 'bg-2', 'bg-1', 'info'),
    ('Race browse · Filters sheet heading, checkbox labels', 'text-1', 'bg-1', 'text'),
    ('Race browse · Filters sheet field labels and legend', 'text-2', 'bg-1', 'text'),
    ('Race browse · Filters sheet field value (select, dates)', 'text-1', 'bg-0', 'text'),
    ('Race browse · Filters sheet field outline (non-text, 3:1)', 'field-line', 'bg-1', 'ui'),
    ('Race browse · checkbox against the sheet (non-text, 3:1)', 'text-1', 'bg-1', 'ui'),
    ('Race browse · Cancel (secondary) in the sheet', 'text-1', 'bg-2', 'text'),
    ('Race browse · Map placeholder caption', 'text-2', 'bg-1', 'text'),
    ('Race browse · Map pin label', 'text-1', 'bg-2', 'text'),
    ('Race browse · Map pin dot on its label (non-text, 3:1)', 'text-1', 'bg-2', 'ui'),
    ('Race browse · Map placeholder outline (non-text, 3:1)', 'field-line', 'bg-0', 'ui'),
    ('Race browse · Map caption on water', 'text-2', 'bg-bar', 'text'),
    ('Race browse · Map pin dot on land (non-text, 3:1)', 'text-1', 'bg-1', 'ui'),
    ('Race browse · Map pin dot on water (non-text, 3:1)', 'text-1', 'bg-bar', 'ui'),
    ('Race browse · Map leader line on land (non-text, 3:1)', 'text-2', 'bg-1', 'ui'),
    ('Race browse · Map leader line on water (non-text, 3:1)', 'text-2', 'bg-bar', 'ui'),
    ('Race browse · Map state panel text (empty, error) on its panel', 'text-1', 'bg-1', 'text'),
    ('Race browse · coastlines and borders on land', 'bg-3', 'bg-1', 'info'),
    ('Results list · saved confirmation text ("Saved: HYROX London"), neutral surface', 'text-1', 'bg-1', 'text'),
    ('Results list · saved confirmation icon, neutral (non-text, 3:1)', 'text-2', 'bg-1', 'ui'),
    ('Results list · "Newest first" after the count', 'text-2', 'bg-0', 'text'),
    ('Results list · Log result stepped down to secondary (empty, error)', 'text-1', 'bg-2', 'text'),
    ('Results list · count separator hairline', 'line', 'bg-0', 'info'),
    ('Skeleton count bar on the page', 'bg-2', 'bg-0', 'info'),
    ('Race browse · filter chip remove icon, close-circle (non-text, 3:1)', 'text-2', 'bg-0', 'ui'),
    ('Race browse · Filters sheet calendar icon in a date field (non-text, 3:1)', 'text-1', 'bg-0', 'ui'),
]
rows, failures = [], []
for label, fg, bg, kind in PAIRS:
    f, b = tok(fg), tok(bg)
    r = cr(f, b)
    need = {'text': 4.5, 'large': 3.0, 'ui': 3.0, 'exempt': 0, 'info': 0}[kind]
    ok = r >= need
    if kind not in ('exempt', 'info') and not ok:
        failures.append((label, r))
    verdict = ('<span class="exempt">exempt (disabled, WCAG 1.4.3)</span>' if kind == 'exempt'
               else '<span class="exempt">no requirement (decorative placeholder, aria-hidden)</span>' if kind == 'info'
               else f'<span class="pass">pass</span> · needs {need:g}:1' if ok else f'<b>fail</b> · needs {need:g}:1')
    rows.append(f'<tr><td>{label}</td><td class="sample">{sw(fg)}<code>--{fg}</code> {f}</td>'
                f'<td class="sample">{sw(bg)}<code>--{bg}</code> {b}</td><td class="num">{r:.2f}:1</td><td>{verdict}</td></tr>')
assert not failures, failures
CONTRAST = ('<div class="spec-wrap" tabindex="0" role="region" aria-label="Contrast table"><table class="spec"><thead><tr><th>Where</th><th>Text</th><th>Background</th><th>Ratio</th><th>WCAG AA</th></tr></thead><tbody>'
            + ''.join(rows) + '</tbody></table></div>')

# cache-busting: stylesheet links carry a short hash of tokens.css + map.css + components.css
import hashlib
CSS_V = hashlib.sha1(''.join(open(os.path.join(ROOT, f'concept/{n}.css')).read() for n in ('tokens', 'map', 'components')).encode()).hexdigest()[:8]
def _stamp(path):
    html = re.sub(r'href="((?:\.\./concept/)?(?:tokens|map|components))\.css(\?v=[0-9a-f]+)?"', lambda m: f'href="{m.group(1)}.css?v={CSS_V}"', open(path).read())
    open(path, 'w').write(html)
for _p in ['concept/first-screen.html'] + [f'wireframes/{s}{x}.html' for s in ('race-browse', 'results-list') for x in ('', '-empty', '-error', '-loading')]:
    _stamp(os.path.join(ROOT, _p))

# ---------------------------------------------------------------- color rules (concept.md → Color rules)
import math
from colorlib import lab, de2000, hue as lab_hue
CSS = open(os.path.join(ROOT, 'concept/components.css')).read()
CSS_RULES = [(sel.strip(), body) for sel, body in re.findall(r'([^{}]+)\{([^{}]*)\}', re.sub(r'/\*.*?\*/', '', CSS, flags=re.S))]

def selectors_using(*tokens):
    out = []
    for sel, body in CSS_RULES:
        if any(f'var(--{t})' in body for t in tokens):
            out += [x.strip() for x in sel.split(',')]
    return out

# Rule 1: amber only where you can act or where you are
ACCENT_OK = [r'^\.btn--primary(:hover)?$', r'^\.header-action(:hover)?$', r'^\.state-action:not\(\.secondary\)(:hover)?$',
             r'^\.bottom-nav a\[aria-current="page"\]$', r'^\.sheet-actions button\[type="submit"\](:hover)?$',
             r'^\.swatch--accent(-hover)?$', r'^\.swatch--on-accent$']
accent_sel = selectors_using('accent', 'accent-hover')
accent_bad = [x for x in accent_sel if not any(re.match(p, x) for p in ACCENT_OK)]
assert not accent_bad, ('Color rule 1: accent on a disallowed selector', accent_bad)

# Rule 2: no success color on results
SUCCESS_OK = [r'^\.status--success( \.icon| strong)?$', r'^\.swatch--success(-bg)?$']   # stand specimen only; no product screen uses success color
success_sel = selectors_using('success', 'success-bg')
success_bad = [x for x in success_sel if not any(re.match(p, x) for p in SUCCESS_OK)]
assert not success_bad, ('Color rule 2: success color outside the stand specimen', success_bad)

# Rule 3a: depth of dark, not #000
BG_LEVELS = ['bg-bar', 'bg-0', 'bg-1', 'bg-2', 'bg-3']
L_MIN, L_MAX, C_MAX, STEP_MIN = 4.5, 20.0, 6.0, 1.5
bg_rows, prev = [], None
for t in BG_LEVELS:
    L, a, b = lab(tok(t)); C = math.hypot(a, b)
    ok = L_MIN <= L <= L_MAX and C <= C_MAX and (prev is None or L - prev >= STEP_MIN)
    assert ok, ('Color rule 3a: background level out of range', t, round(L, 2), round(C, 2))
    bg_rows.append((t, L, C, None if prev is None else L - prev)); prev = L

# Rule 3a, usage: --line and --field-line are hairlines, never a fill (their L* is above the background range)
line_fill = [x for sel, body in CSS_RULES if re.search(r'background(-color)?:\s*var\(--(field-)?line\)', body)
             for x in sel.split(',') if not x.strip().startswith('.swatch--') and x.strip() != '.sheet-handle']   # the handle is a drawn 4px line, not a surface
assert not line_fill, ('Color rule 3a: a hairline token used as a fill', [x.strip() for x in line_fill])

# Rule 3b: amber, not HYROX yellow (reported, not blocking: the designer keeps the amber knowingly)
HYROX_REFS = [('RoxFit', '#FFEC00', 'roxfit-how-it-works.png, 5,786 px'), ('RoxMatchUp', '#F5E401', 'roxmatchup-home.png, 2,770 px')]
HUE_MIN, DE_MIN = 25.0, 24.0
def hue_dist(x, y):
    d = abs(lab_hue(x) - lab_hue(y)); return min(d, 360 - d)
hyrox_rows = [(n, c, src, hue_dist(tok('accent'), c), de2000(tok('accent'), c)) for n, c, src in HYROX_REFS]
HYROX_PASS = all(h >= HUE_MIN and d >= DE_MIN for _, _, _, h, d in hyrox_rows)
# Designer override (concept.md → Color rules → 3b), valid only for this exact accent
RULE_3B_OVERRIDE = {'accent': '#F5B649', 'date': '2026-10-14',
                    'reason': 'the accent is scarce (1–2 uses per screen), the ground is graphite, not black, and the chips are neutral'}
HYROX_ACCEPTED = (not HYROX_PASS) and tok('accent').upper() == RULE_3B_OVERRIDE['accent']
HYROX_STATUS = 'pass' if HYROX_PASS else 'accepted by designer' if HYROX_ACCEPTED else 'FAIL'

# results never carry a success mark (checked on the generated markup at the end)
print('Color rule 1 (accent placement): pass ·', len(accent_sel), 'selectors')
print('Color rule 2 (no success on results): pass ·', len(success_sel), 'selectors')
print('Color rule 3a (depth of dark): pass ·', ', '.join(f'{t} L*{L:.2f} C*{C:.2f}' for t, L, C, _ in bg_rows))
print('Color rule 3b (amber vs HYROX yellow):', HYROX_STATUS if HYROX_STATUS != 'FAIL' else 'FAIL (no designer override for this accent; reported, not blocking)', '·',
      '; '.join(f'{n} {c}: {h:.1f}° ΔE {d:.1f}' for n, c, _, h, d in hyrox_rows))

def decisions_section():
    return f'''
  <section class="stand-section" id="decisions" aria-labelledby="dec-h">
    <h2 id="dec-h">Decided</h2>
    <div class="stand-grid">
      <div class="stand-panel">
        <h3>Accent · <code>{tok("accent")}</code>, kept</h3>
        <p class="stand-why">Compared side by side against a halfway version (<code>{ACCENT_HALF}</code>) and a warmer one that just passes rule 3b (<code>{ACCENT_PASS}</code>). The designer kept the current amber, overriding rule 3b (see Color rules). Text on the accent: {cr(tok("on-accent"), tok("accent")):.2f}:1.</p>
      </div>
      <div class="stand-panel">
        <h3>Photo band · 3:1, {BAND["short"]["band"]}px</h3>
        <p class="stand-why">Compared with 16:7 ({BAND["current"]["band"]}px band, {BAND["current"]["card"]}px card: 1 full card + {BAND["current"]["def"][1]}% of the next). At 3:1 the card is {FS["card_h"]}px: {FS["base"]["full"]} full cards with no filters, {FS["filtered"]["full"]} full + {FS["filtered"]["next"]}% with two filters on. Attribute b: a calendar, not a poster. Same photos and anatomy.</p>
      </div>
    </div>
  </section>
'''

def rules_section():
    bg = ''.join(f'<tr><td><code>--{t}</code> {tok(t)}</td><td class="num">{L:.2f}</td><td class="num">{C:.2f}</td><td class="num">{"base" if st is None else f"+{st:.2f}"}</td><td><span class="pass">pass</span></td></tr>' for t, L, C, st in bg_rows)
    hy = ''.join(f'<tr><td>{n} <code>{c}</code><br>{src}</td><td class="num">{h:.1f}°</td><td class="num">{d:.1f}</td><td>{"<span class=pass>pass</span>" if h >= HUE_MIN and d >= DE_MIN else "below threshold · accepted by designer" if HYROX_ACCEPTED else "<b>fail</b>"}</td></tr>' for n, c, src, h, d in hyrox_rows)
    return f'''
  <section class="stand-section" id="color-rules" aria-labelledby="rules-h">
    <h2 id="rules-h">Color rules, checked by the build</h2>
    <p>From <code>concept.md</code> → Color rules. <code>scripts/concept/build_stand.py</code> checks them on every build: rules 1, 2 and 3a stop the build when broken; 3b is reported here and does not block (the current amber is accepted by the designer).</p>
    <div class="stand-grid">
      <div class="stand-panel">
        <h3>1 · Accent placement · pass</h3>
        <p class="stand-why">Amber only where you can act or where you are. The build found the accent on {len(accent_sel)} selectors, all allowed: the primary button and its hover, <code>.header-action</code>, the primary <code>.state-action</code>, the current tab, and the specimen swatches. It is never on a result, a finish time, a count or a status.</p>
      </div>
      <div class="stand-panel">
        <h3>2 · No success color on results · pass</h3>
        <p class="stand-why">Results are self-reported; Onrace can't verify them. No product screen uses <code>--success</code>: the saved confirmation on Results list is neutral (a surface and a "save" glyph), because a green check next to a race name reads as a "verified" stamp. The build allows success color only on this stand's specimen. The proof line stays Text 2 (attribute d), and even this page's "pass" labels are Text 1, not green.</p>
      </div>
    </div>
    <div class="stand-panel">
      <h3>3a · Depth of dark, not #000: L* {L_MIN:g}–{L_MAX:g}, C* ≤ {C_MAX:g}, each level ≥ {STEP_MIN:g} L* above the last</h3>
      {wrap('Dark depth check', f'<table class="spec"><thead><tr><th>Level</th><th>L*</th><th>C*</th><th>Step</th><th>Result</th></tr></thead><tbody>{bg}</tbody></table>')}
      <p class="stand-why">For reference, #000 is L* 0 and the guardrail <code>#0B0C0E</code> is L* 3.30; both fall outside the range.</p>
    </div>
    <div class="stand-panel">
      <h3>3b · Amber, not HYROX yellow: hue distance ≥ {HUE_MIN:g}° and ΔE2000 ≥ {DE_MIN:g} · {HYROX_STATUS}</h3>
      {wrap('HYROX distance check', f'<table class="spec"><thead><tr><th>HYROX yellow [~], measured in research/screens/</th><th>Hue distance</th><th>ΔE2000</th><th>Result</th></tr></thead><tbody>{hy}</tbody></table>')}
      <p class="stand-why">The threshold is "at least as far as named orange": CSS <code>orange</code> <code>#FFA500</code> is 24.6° and ΔE 24.0 from <code>#FFEC00</code>. There is no screenshot of HYROX's own site in <code>research/screens/</code>, so the reference is the HYROX-ecosystem apps. <b>Overridden by the designer on {RULE_3B_OVERRIDE["date"]}:</b> the amber <code>{RULE_3B_OVERRIDE["accent"]}</code> stays because {RULE_3B_OVERRIDE["reason"]}. The override covers this exact hex; any other accent is checked against the threshold again.</p>
    </div>
  </section>
'''

# ---------------------------------------------------------------- decision 1: accent versions (computed)
from colorlib import lch_to_hex, chroma as lab_chroma
def _rotate_until_pass():
    A = tok('accent'); L, a, b = lab(A); C0 = math.hypot(a, b); h0 = lab_hue(A)
    def col(h):
        C = C0
        while lch_to_hex(L, C, h) is None: C -= 0.1     # keep lightness; lower chroma only as the gamut requires
        return lch_to_hex(L, C, h)
    ok = lambda c: all(hue_dist(c, y) >= HUE_MIN and de2000(c, y) >= DE_MIN for _, y, _ in HYROX_REFS)
    h = h0
    while not ok(col(h)): h -= 0.1                   # warmer = toward orange
    return col((h0 + h) / 2), col(h)
ACCENT_HALF, ACCENT_PASS = _rotate_until_pass()
ACCENT_VERSIONS = [('Current amber', tok('accent')), ('Halfway', ACCENT_HALF), ('Warmer, just passes 3b', ACCENT_PASS)]
print('Accent versions:', ', '.join(f'{n} {c}' for n, c in ACCENT_VERSIONS))

# ---------------------------------------------------------------- decision 2: photo band (measured in the browser)
# first-screen.html at 390×844 on 2026-10-14. Boundary found by search: ratio 2.8638 → band 114px, card 219px, 2 full cards with 0px to spare.
BAND = {'current': {'ratio': '16/7', 'band': 143, 'card': 247, 'def': (1, 77), 'filt': (1, 54)},
        'short':   {'ratio': '3/1',  'band': 109, 'card': 213, 'def': (2, 0),  'filt': (1, 79)},
        'boundary': {'ratio': '2.86/1', 'band': 114, 'card': 219}}

# measured in the browser with first-screen.html at 390×844 on 2026-10-14 after step 5 (box-sizing, 68px date column), --photo-ratio 3 / 1 from tokens.css
FS = {'card_h': 215, 'band': 114, 'tab': 747, 'base': {'top': 290, 'full': 2, 'next': 2}, 'filtered': {'top': 346, 'full': 1, 'next': 81}}
# the real screen, wireframes/race-browse.html, measured 2026-10-14 (step 5)
FS_REAL = {'viewer': {'h': 757, 'tab': 693, 'base': (243, 2, 0, 8.6), 'filtered': (299, 1, 78, None)},
           'direct': {'h': 844, 'tab': 780, 'base': (243, 2, 39, None), 'filtered': (299, 2, 13, None)}}

# ---------------------------------------------------------------- shared markup (wireframe text and structure)
def race_card(name, tag, iso, date, loc, src, pos, alt):
    return f'''<article class="race-card">
          <img class="photo {pos}" src="{src}" alt="{alt}" width="900" height="600">
          <a class="card-link" href="#components">
            <h3>{name}</h3>
            <p class="card-meta"><span class="sport-tag">{tag}</span> <time datetime="{iso}">{date}</time></p>
            <p class="card-location">{loc}</p>
          </a>
        </article>'''

CARD_LONDON = race_card('HYROX London', 'HYROX', '2026-12-06', '6 Dec 2026', 'London, UK',
                        'https://images.unsplash.com/photo-1743993414654-0be2b73a9620?w=900&q=75&fm=jpg', 'photo--low',
                        'A row of athletes leaning on loaded sleds at the start line of an indoor fitness race')
CARD_BERLIN = race_card('Berlin Marathon', 'Marathon', '2026-09-27', '27 Sep 2026', 'Berlin, Germany',
                        'https://images.unsplash.com/photo-1452626038306-9aae5e071dd3?w=900&q=75&fm=jpg', 'photo--mid',
                        'Runners filling a tree-lined city avenue during a road race, seen from above')

RESULT_ROW = '''<article class="result-card">
          <a class="card-link" href="#components">
            <div class="card-top">
              <h2>HYROX London</h2>
              <span class="finish-time">1:18:42</span>
            </div>
            <p class="card-meta"><span class="sport-tag">HYROX</span> <time datetime="2025-12-06">6 Dec 2025</time></p>
            <p class="proof-label">Self-reported · via results.hyrox.com</p>
          </a>
        </article>'''

def tabbar(current):
    items = [('Discover', 'compass'), ('My Results', 'stopwatch'), ('Profile', 'user')]
    cur = ' aria-current="page"'
    lis = ''.join(f'<li><a href="#language"{cur if l == current else ""}>{svg(i, "tab-icon")}<span>{l}</span></a></li>' for l, i in items)
    return f'<nav class="bottom-nav" aria-label="Global navigation"><ul>{lis}</ul></nav>'

BUTTONS = f'''<div class="stand-row">
            <a class="btn btn--primary" href="#components">{svg("add-circle")}Log result</a>
            <button type="button" class="btn btn--secondary">{svg("tuning-2")}Filters · 2</button>
            <button type="button" class="btn btn--tertiary">Clear all filters</button>
          </div>'''

SEARCH = '''<form class="race-search" role="search" onsubmit="return false">
            <label class="visually-hidden" for="race-q">Search races by name or city</label>
            <input type="search" id="race-q" name="q" placeholder="Race name or city" autocomplete="off" enterkeyhint="search">
          </form>'''

def why(*parts): return '<p class="stand-why"><b>Why:</b> ' + ' · '.join(parts) + '</p>'

# ---------------------------------------------------------------- color rows
COLOR_ROWS = [
    ('bg-bar', 'Tab bar', 'The tab bar, the frame around a screen.', 'Never inside content.', 'Taste: dark with depth, not pure #000 (Tension C)'),
    ('bg-0', 'Ground', 'The page behind every screen.', 'Not on cards (cards sit one level up).', 'Attribute e: dark, intense · Taste: not #000'),
    ('bg-1', 'Surface', 'Race cards, result rows, the search field.', 'Not for controls you press (those are raised).', 'Attribute a: cards stay quiet so the time can lead'),
    ('bg-3', 'Raised, pressed', 'Hover, open and pressed fills on raised controls: the selected List/Map segment, Filters while its sheet is open.', 'Never at rest, never a card.', 'Color rule 3a: Line is a hairline, so pressed fills get their own level'),
    ('bg-2', 'Raised', 'Secondary button, format chip, the date tile, segmented track, skeletons, disabled buttons.', 'Never for the primary action.', 'Hierarchy rule 3: secondary is tonal'),
    ('line', 'Line', 'Hairline dividers.', 'Not as a boundary someone must see (fields use Field line), not as a frame around every card.', 'Attribute a: the frame stays quiet'),
    ('field-line', 'Field line', 'The boundary of the search field and other inputs.', 'Not on cards or chips.', 'WCAG 1.4.11: an input boundary needs 3:1 (critique fix)'),
    ('text-1', 'Text 1', 'Screen titles, item titles, finish times, body.', 'Not for meta (date month, location, proof).', 'Hierarchy rule 4: three levels'),
    ('text-2', 'Text 2', 'Meta: month and year, location, proof line, counts, inactive tab.', 'Not for titles or the finish time.', 'Attribute d: proof stated, not stamped (a quiet line)'),
    ('chip-text', 'Chip text', 'The format chip label only.', 'Not on filter chips (those are Text 1).', 'Hierarchy rule 2: chips are metadata'),
    ('text-disabled', 'Disabled', 'Disabled controls only.', 'Never for content someone must read.', 'WCAG 1.4.3 exempts disabled controls'),
    ('accent', 'Accent (sodium amber)', 'The primary button fill (Log result, Register on &lt;domain&gt;) and the current tab. At most two per screen.', 'Not on finish times, chips, filter chips, links, focus rings, icons in content, or state messages.', 'Hierarchy rule 1: accent is scarce · Taste: a high-contrast accent (round 1 Direction 3)'),
    ('accent-hover', 'Accent, hover', 'The primary button under the pointer.', 'Anywhere at rest.', 'Hierarchy rule 3: one primary, with a hover state'),
    ('on-accent', 'On accent', 'Text and icons on the accent.', 'Anywhere else.', f'Contrast: {cr(tok("on-accent"), tok("accent")):.2f}:1 on the accent'),
    ('error', 'Error (soft coral)', 'Error titles and icons: "Couldn’t load races".', 'Not for emphasis, not for deleting, never as a fill for a whole card.', 'Taste: no aggressive red (not the #FF4D2E family)'),
    ('error-bg', 'Error tint', 'Behind an error message.', 'Not behind a card or a field.', 'States: color second, after icon and text'),
    ('success', 'Success', 'The status specimen on this stand only. No product screen uses it: the saved confirmation is neutral (Color rule 2).', 'Not on a result, not on Results list at all, not for "verified" or any claim about a result.', 'Voice principle 1: claim only what Onrace can know'),
    ('success-bg', 'Success tint', 'The status specimen on this stand only.', 'Not behind results, proof lines or the saved confirmation.', 'Voice principle 1: no verified look'),
    ('warning', 'Warning (no hue)', 'Icon plus text on a raised surface with an outline. No warning state exists in the wireframes yet.', 'No amber or yellow: every warm candidate is within ΔE 7.7–13 of the accent and would read as an action.', 'Hierarchy rule 1: keep the accent the only warm hue'),
    ('warning-bg', 'Warning surface', 'Behind a warning: the raised level.', 'Not a tint of any hue.', 'Hierarchy rule 1'),
    ('warning-line', 'Warning outline', 'Around a warning, so it differs from a secondary button.', 'Not around cards.', 'States need a shape cue when they have no hue'),
]
color_trs = ''.join(f'<tr><td>{sw(t)}{n}<br><code>--{t}</code> {tok(t)}</td><td>{u}</td><td>{nu}</td><td>{w}</td></tr>' for t, n, u, nu, w in COLOR_ROWS)
COLOR_TABLE = wrap('Color tokens', f'<table class="spec"><thead><tr><th>Token</th><th>Used</th><th>Not used</th><th>Why</th></tr></thead><tbody>{color_trs}</tbody></table>')

# ---------------------------------------------------------------- type rows
TYPE_ROWS = [
    ('size-title', 'display', 'Discover', 'Screen title (level 1)', 'Hierarchy rule 4 · Taste: Nike Run Club, bold but refined'),
    ('size-time', 'display', '1:18:42', 'Finish time, the loudest thing on the row', 'Attribute a · Hierarchy rule 5'),
    ('size-day', 'display', '27', 'Date day, the first thing read on a race card', 'Attribute b: a calendar, not a poster'),
    ('size-item', 'text-strong', 'HYROX London', 'Item title (level 2): race name', 'Hierarchy rule 4'),
    ('size-body', 'text', 'Registration and payment happen on hyrox.com.', 'Body text, primary and secondary buttons, search', 'Voice principle 3: plain words'),
    ('size-meta', 'text-2', 'London, UK', 'Meta (level 3): location, counts; tertiary text links', 'Hierarchy rule 4'),
    ('size-proof', 'text-2', 'Self-reported · via results.hyrox.com', 'Proof line, month and year under the day', 'Attribute d: proof stated, not stamped'),
    ('size-label', 'label', 'Half marathon', 'Format chip (uppercase by CSS), tab label', 'Decision A: markup keeps the name, CSS uppercases'),
]
TYPE_CLASS = {'size-title': 'type-sample--display type-sample--title', 'size-time': 'type-sample--display type-sample--time',
              'size-day': 'type-sample--display type-sample--day', 'size-item': 'type-sample--item', 'size-body': 'type-sample--body',
              'size-meta': 'type-sample--meta', 'size-proof': 'type-sample--proof'}
def type_sample(kind, text, t):
    if kind == 'label':
        return f'<span class="sport-tag">{text}</span>'
    return f'<span class="type-sample {TYPE_CLASS[t]}">{text}</span>'
type_trs = ''.join(f'<tr><td><code>--{t}</code> {tok(t)}<br>{"Schibsted Grotesk 800" if k == "display" else "Hanken Grotesk"}</td><td>{type_sample(k, x, t)}</td><td>{lvl}</td><td>{w}</td></tr>' for t, k, x, lvl, w in TYPE_ROWS)

# ---------------------------------------------------------------- shape rows
SPACE_USE = {1: 'Icon to label, title to chip, tile padding sides', 2: 'Card inset around the photo, chip padding, button icon gap',
             3: 'Date column to text column, row gaps, tile padding top and bottom', 4: 'Result row sides, section stacks',
             5: 'Button sides, stand panels', 6: 'Between stand blocks; tab bar bottom (home indicator)', 7: 'Reserved: screen sections',
             8: 'Stand page top', 9: 'Between stand sections'}
SPACE = ''.join(f'<tr><td><code>--space-{i}</code> {tok(f"space-{i}")}</td><td><span class="space-bar space-bar--{i}"></span></td><td>{SPACE_USE[i]}</td></tr>' for i in range(1, 10))
METRICS = [('chip-height', 'Format chip height', 'Metadata stays small beside the 17px title', 'Hierarchy rule 2'),
           ('filter-chip-height', 'Active filter chip height (44px tap area via ::after)', 'Removable, so a bigger target than the metadata chip', 'Critique fix: touch targets'),
           ('date-col', 'Date column width', 'Fits "Sep 2026" on one line under the day', 'Attribute b: the date leads'),
           ('photo-ratio', 'Photo band ratio in the card', '3:1, 109px at 390 wide (decided 2026-10-14)', 'Attribute b: two full cards on the first screen'),
           ('icon-s', 'Icons in meta (location, proof line)', 'Matches 13–14px meta text', 'Hierarchy rule 4: meta is level 3'),
           ('icon-m', 'Icons in buttons, search, states', 'Matches 15px button text', 'Hierarchy rule 3'),
           ('icon-l', 'Tab bar icons', 'iOS tab bar size', 'Wireframe conventions: iOS chrome'),
           ('weight-display', 'Display weight', 'Heavy, with refined detailing', 'Taste: Nike Run Club, bold but refined'),
           ('weight-strong', 'Item titles, buttons, labels', 'One step under display', 'Hierarchy rule 4'),
           ('tracking-display', 'Display tracking', 'Tight, not crushed', 'Taste: bold but refined'),
           ('tracking-label', 'Chip label tracking', 'Uppercase needs air', 'Decision A: uppercase via CSS'),
           ('leading-body', 'Body line height', 'Readable running text', 'Voice principle 3: plain words'),
           ('measure', 'Longest text line', '65 characters', 'Critique fix: line length'),
           ('leading-tight', 'Display lines (title, time, day)', 'Line height 1: big numbers sit tight', 'Taste: bold but refined'),
           ('leading-item', 'Item titles, the date column', 'Line height 1.2', 'Hierarchy rule 4: level 2 stays compact'),
           ('weight-regular', 'Body and meta', 'Regular 400', 'Hierarchy rule 4: meta steps back by weight too'),
           ('tap-pad', 'Invisible tap area around filter chips', 'Extends the 32px chip to 44px', 'Critique fix: touch targets'),
           ('photo-focus-low', 'Crop focus for photos whose subject sits low', 'Keeps the athletes in the 3:1 band', 'Attribute b: the band shows the race, not the sky'),
           ('photo-focus-mid', 'Crop focus for photos with a centered subject', 'Keeps the athletes in the 3:1 band', 'Attribute b'),
           ('ease-out', 'Easing for hover and press', 'Fast start, soft stop', 'Attribute e: intense, not jittery'),
           ('stand-max', 'Stand page width (stand only)', 'Never used in the product', 'Stand layout'),
           ('phone-width', 'Phone frame on the stand (stand only)', '390px screen + border', 'Stand layout'),
           ('dur-fast', 'Hover and press transitions', 'Quick, ease-out; 0ms under prefers-reduced-motion', 'Attribute e: intense, not jittery · WCAG 2.3.3: motion can be turned off'),
           ('dur-sheet', 'Filters sheet slides up, backdrop fades in', 'Long enough to read as a sheet arriving from below; 0ms under prefers-reduced-motion', 'Wireframe conventions: modal sheets · WCAG 2.3.3'),
           ('font-display', 'Display face: screen title, finish time, date day', 'Schibsted Grotesk 800, Hanken as fallback', 'Taste: Nike Run Club, bold but refined'),
           ('font-text', 'Text face: everything else', 'Hanken Grotesk 400 and 600 (the only weights loaded)', 'Taste: no single heavy condensed face for everything'),
           ('font-mono', 'Code samples on this stand only', 'System monospace, nothing to load', 'Stand layout: never in the product'),
           ('hidden-size', 'Visually hidden text for screen readers', '1px box, clipped', 'voice.md → Loading: “Loading races…” is read, not shown'),
           ('photo-focus-lower', 'Crop focus, DEKA STRONG Chicago', 'Lower band: keeps the other event’s banner out of frame', 'Attribute c: no other brand on our card (designer, step 5)'),
           ('photo-focus-center', 'Crop focus, Spartan Beast Killington', 'Subject in the middle of a tall photo', 'Attribute b: the band shows the race, not the sky'),
           ('photo-focus-high', 'Crop focus, Boston Marathon', 'Subject (race bibs) at the top edge', 'Attribute b'),
           ('screen-w', 'Screen pages: the page width inside the viewer', 'iPhone logical width', 'Wireframe conventions: iOS-structured, 390pt'),
           ('tabbar-h', 'Tab bar height on the screen pages', '44px targets + 26px icon + label, no home-indicator padding (the viewer draws it); the stand’s bar adds that padding, so it is taller', 'Wireframe conventions: iOS chrome · Critique fix: 44px targets'),
           ('safe-bottom', 'Home-indicator inset under the sheet’s buttons', 'env(safe-area-inset-bottom), 0 inside the viewer', 'iOS chrome: buttons stay above the home indicator'),
           ('sheet-max', 'Filters sheet maximum height', 'Three quarters: the list stays visible above it', 'Wireframe conventions: a sheet, not a new screen'),
           ('scrim', 'Behind the Filters sheet', 'Black at 60%: the page dims, its colors stay', 'Depth comes from levels and one scrim, not from color · Hierarchy rule 1'),
           ('fade-end', 'Active filter chips row: its end fades out', 'Mask, last 24px', 'Says the row scrolls without a scrollbar · Critique fix: hidden overflow'),
           ('stand-col-min', 'Stand columns (stand only)', 'Narrowest panel before the grid wraps', 'Stand layout')]
SKEL = [('skel-line', 'Meta bars (date, location, proof)', 'Same height as 12–13px meta text'),
        ('skel-title', 'Title bar height', 'Same height as the 17px item title'),
        ('skel-title-w', 'Race card title bar width', 'A typical race name'),
        ('skel-tag-w', 'Format chip bar width', 'A typical chip'),
        ('skel-loc-w', 'Location bar width', 'A typical “City, Country”'),
        ('skel-count-w', 'Result count bar width', 'A typical “7 races”'),
        ('skel-row-title-w', 'Result row title bar width', 'A typical race name beside the time'),
        ('skel-time-w', 'Finish time bar width', 'Width of “1:18:42” at 32px'),
        ('skel-time-h', 'Finish time bar height', 'The finish time’s own size, so the row doesn’t shift when it loads'),
        ('skel-date-w', 'Result row date bar width', 'Width of “6 Dec 2025”'),
        ('skel-proof-w', 'Proof line bar width', 'A typical “Self-reported · via …”')]
SKEL_TRS = ''.join(f'<tr><td><code>--{t}</code> {tok(t)}</td><td>{u}</td><td>{d}</td><td>voice.md → Loading: the skeleton has the content’s shape · impeccable: no layout shift</td></tr>' for t, u, d in SKEL)
MAP_PINS = [('berlin-marathon', 'Berlin'), ('hyrox-london', 'London'), ('utmb', 'Chamonix'), ('hyrox-dallas', 'Dallas'),
            ('deka-strong-chicago', 'Chicago'), ('spartan-beast-killington', 'Killington'), ('boston-marathon', 'Boston')]
MAP_TRS = ''.join(f'<tr><td><code>--{t}</code> {v}</td><td>{u}</td><td>{w}</td></tr>' for t, v, u, w in [
    ('map-water', f'= <code>--bg-bar</code> {tok("map-water")}', 'Water: the darkest level', 'Hierarchy rule 1: no accent on the map · Color rule 3a levels only'),
    ('map-land', f'= <code>--bg-1</code> {tok("map-land")}', 'Land: the card surface', 'Color rule 3a'),
    ('map-lines', f'= <code>--bg-3</code> {tok("map-lines")}', 'Coastlines and borders (decorative)', 'Attribute a: the frame stays quiet'),
    ('map-pin-dot', tok('map-pin-dot'), 'The dot on a race’s coordinate', 'Designer: pins at real coordinates'),
    ('pin-h', tok('pin-h'), 'Pin label height', 'Sized to the 11px label'),
    ('pin-gap', tok('pin-gap'), 'Shortest leader line from label to dot', 'Designer: labels may move, dots don’t'),
    ('map-ratio', tok('map-ratio'), 'Map height ÷ width', 'Generated by build_map.py from the Mercator crop'),
    ('map-land-mask', 'SVG mask', 'Land shape', 'Natural Earth 1:110m, public domain · designer: static map'),
    ('map-lines-mask', 'SVG mask', 'Coastline and border shape', 'Same source; colors come from the tokens above')]) + ''.join(
    f'<tr><td><code>--pin-{slug}-x</code> {tok(f"pin-{slug}-x")}<br><code>--pin-{slug}-yf</code> {tok(f"pin-{slug}-yf")}<br><code>--pin-{slug}-dy</code> {tok(f"pin-{slug}-dy")}</td><td>{city}: x and y from the real latitude and longitude; dy moves the label off its neighbours</td><td>Designer: pins at real coordinates, with leader lines</td></tr>' for slug, city in MAP_PINS)
METRIC_TRS = ''.join(f'<tr><td><code>--{t}</code> {tok(t)}</td><td>{u}</td><td>{d}</td><td>{w}</td></tr>' for t, u, d, w in METRICS)
SHAPE = f'''<div class="spec-wrap" tabindex="0" role="region" aria-label="Radii, borders and shadows"><table class="spec"><thead><tr><th>Token</th><th>Value</th><th>Used for</th><th>Why</th></tr></thead><tbody>
<tr><td><code>--radius-1</code></td><td>{tok("radius-1")}</td><td>Inner shapes: the photo inside a card, chips, segments.</td><td>Taste: slightly rounded, small radius · inner shapes one step tighter than outer (4 inside 6)</td></tr>
<tr><td><code>--radius-2</code></td><td>{tok("radius-2")}</td><td>Outer shapes: cards, buttons, the search field.</td><td>Taste: "no radius looks like a wireframe" · one small value, not pills</td></tr>
<tr><td><code>--radius-3</code></td><td>{tok("radius-3")}</td><td>Stand panels only, never in the product.</td><td>Keeps the product's shapes at 4 and 6</td></tr>
<tr><td><code>--border</code></td><td>{tok("border")}</td><td>Hairlines: field outline, dividers, filter chip outline.</td><td>Attribute a: the frame stays quiet</td></tr>
<tr><td><code>--focus-ring</code></td><td>{tok("focus-ring")}</td><td>Keyboard focus, in Text 1, never the accent.</td><td>Hierarchy rule 1: focus is not an accent use</td></tr>
<tr><td><code>--shadow-sheet</code></td><td>{tok("shadow-sheet")}<div class="shadow-demo">A sheet floats; cards don\'t.</div></td><td>Sheets and menus that float (the Filters sheet). Cards are flat.</td><td>Depth comes from background levels, not shadows · Taste: dark with depth</td></tr>
<tr><td><code>--target</code></td><td>{tok("target")}</td><td>Minimum height of every control or its tap area.</td><td>Critique fix (round 2): touch targets</td></tr>
</tbody></table></div>
<div class="spec-wrap" tabindex="0" role="region" aria-label="Spacing scale"><table class="spec"><thead><tr><th>Spacing scale</th><th>Size</th><th>Used for</th></tr></thead><tbody>{SPACE}</tbody></table></div>
<p class="stand-why"><b>Why:</b> one 4px-based scale for every gap · Hierarchy rule 4: more space between groups than inside them</p>
<div class="spec-wrap" tabindex="0" role="region" aria-label="Component metrics"><table class="spec"><thead><tr><th>Component metric</th><th>Used for</th><th>Sizing</th><th>Why</th></tr></thead><tbody>{METRIC_TRS}</tbody></table></div>
<div class="spec-wrap" tabindex="0" role="region" aria-label="Skeleton sizes"><table class="spec"><thead><tr><th>Skeleton (loading)</th><th>Used for</th><th>Sizing</th><th>Why</th></tr></thead><tbody>{SKEL_TRS}</tbody></table></div>
<div class="spec-wrap" tabindex="0" role="region" aria-label="Map tokens"><table class="spec"><thead><tr><th>Map · <code>map.css</code> (Race browse only)</th><th>Used for</th><th>Why</th></tr></thead><tbody>{MAP_TRS}</tbody></table></div>'''

# ---------------------------------------------------------------- icons
ICON_PLAN = [  # where, Solar name, token (None: inline on the stand or not built yet), use, status
    ('Tab bar', 'compass', 'icon-compass', 'Discover', 'in use'), ('Tab bar', 'stopwatch', 'icon-stopwatch', 'My Results', 'in use'), ('Tab bar', 'user', 'icon-user', 'Profile', 'in use'),
    ('Filters sheet · date fields', 'calendar', 'icon-calendar', 'Replaces the browser’s calendar glyph in the From and To date fields (step 7). In the race card the date column itself is the cue, so no icon there.', 'in use'),
    ('Card meta · location', 'map-point', 'icon-pin', 'Before the city on every race card (CSS mask, no markup change).', 'in use'),
    ('Format chip', None, None, 'No icon and no dot: the same neutral chip for every format (dot option dropped 2026-10-13).', 'none'),
    ('Proof line', 'link-round', 'icon-link', 'One link icon before "Self-reported · via …" (Hierarchy rule 6).', 'in use'),
    ('Search field', 'magnifer', 'icon-search', 'Inside the field, Text 2.', 'in use'),
    ('Button · primary', 'add-circle', None, 'Log result.', 'in use'),
    ('Button · external', 'arrow-right-up', None, 'Register on &lt;domain&gt;, Open official result: the arrow says it leaves Onrace (voice principle 2).', 'in use'),
    ('Button · secondary', 'tuning-2', 'icon-filters', 'Filters, before the label (CSS mask, no markup change).', 'in use'),
    ('Sort, sheet selects', 'alt-arrow-down', 'icon-chevron', 'After the sort value and in the sheet’s Region select (CSS mask).', 'in use'),
    ('Filters sheet · checkbox', 'check', 'icon-check', 'The tick in a checked sport type, on Text 1 (neutral, never the accent).', 'in use'),
    ('Filter chip · remove', 'close-circle', 'icon-close', 'Drawn by CSS over the chip’s text "×" (step 7); the text stays in the markup, aria-hidden, until Lesson 7.', 'in use'),
    ('State · empty', 'inbox', None, 'Results list empty state, above "Log your first result". Race browse empty uses no icon: the filters above are the context.', 'planned'),
    ('State · error', 'danger-circle', 'icon-error', 'Before the error heading ("Couldn’t load races"), in the error color (CSS mask).', 'in use'),
    ('Saved confirmation', 'diskette', 'icon-saved', 'Results list after Save, in Text 2: neutral, not a success check (Color rule 2).', 'in use'),
    ('State · success', 'check-circle', None, 'This stand’s success specimen only; no product screen uses it.', 'specimen'),
    ('State · warning', 'danger-triangle', None, 'Warning messages, when one exists.', 'planned'),
    ('State · loading', None, None, 'No icon and no spinner: skeleton cards plus "Loading races…" for screen readers (voice.md → Loading).', 'none'),
]
icon_trs = ''.join(f'<tr><td>{p}</td><td>{("<span class=icon-cell>" + svg(n) + f"<code>{n}</code></span>") if n else "None"}</td><td>{f"<code>--{t}</code>" if t else "None"}</td><td>{u}</td><td>{s}</td></tr>' for p, n, t, u, s in ICON_PLAN)

STATUS = f'''<div class="stand-stack">
            <div class="status status--error">{svg("danger-circle")}<p><strong>Couldn’t load races</strong><br>The connection may have dropped. Check it, then try again. Your filters stay as they are.</p></div>
            <div class="status status--success">{svg("check-circle")}<p><strong>Success style</strong> (specimen only; the saved confirmation on Results list is neutral)</p></div>
            <div class="status status--warning">{svg("danger-triangle")}<p><strong>Warning style</strong> (no warning copy exists in the wireframes yet)</p></div>
          </div>'''

page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Onrace concept stand</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@800&family=Hanken+Grotesk:wght@400;600&display=swap">
<link rel="stylesheet" href="tokens.css?v={CSS_V}">
<link rel="stylesheet" href="components.css?v={CSS_V}">
</head>
<body class="onrace">
<main class="stand">

  <header class="stand-head">
    <h1>Onrace concept · Podium</h1>
    <p>Direction A, chosen 2026-10-13 (<code>concept.md</code> → Directions). Every value on this page comes from <code>tokens.css</code>; every component from <code>components.css</code>. The page itself holds no style values. Each decision below is signed with its reason: an attribute (a–e), the designer's taste, or a hierarchy rule. The full comparison is in <a class="stand-link" href="directions.html">directions.html</a>.</p>
  </header>

  <section class="stand-section" id="language" aria-labelledby="language-h">
    <h2 id="language-h">The language in action</h2>
    <div class="stand-grid">
      <div class="phone-frame">
        <div class="stand-stack">
          <p class="stand-label">Race card with photo</p>
          {CARD_LONDON}
          <p class="stand-label">Results list row</p>
          {RESULT_ROW}
        </div>
        {tabbar("Discover")}
      </div>
      <div class="stand-stack">
        <div class="stand-panel">
          <h3>Button hierarchy · one primary per screen</h3>
          {BUTTONS}
          <p class="stand-why"><b>Primary</b> filled accent · <b>secondary</b> tonal (raised) · <b>tertiary</b> text link.</p>
          {why("Hierarchy rule 3")}
        </div>
        <div class="stand-panel">
          <h3>The accent, counted</h3>
          <p class="stand-why">On this frame: the current tab only. On Results list: Log result and the current tab. Finish times, chips and links stay neutral.</p>
          {why("Hierarchy rule 1", "Hierarchy rule 5", "Attribute a")}
        </div>
      </div>
    </div>
  </section>

  <section class="stand-section" aria-labelledby="color-h">
    <h2 id="color-h">Color</h2>
    <p>Background levels from the frame up, two text levels for content (plus chip text and disabled), one scarce accent, and state colors that never borrow it.</p>
    {COLOR_TABLE}
    <div class="stand-panel">
      <h3>States: icon and text first, color second</h3>
      {STATUS}
      {why("Taste: no aggressive red", "Voice principle 1: success never says verified", "Hierarchy rule 1: warning has no warm hue")}
    </div>
  </section>

  <section class="stand-section" aria-labelledby="type-h">
    <h2 id="type-h">Type</h2>
    <p><b>Schibsted Grotesk</b> (display) for the screen title and the key numbers only: finish time and date day. Big, heavy, tight, with refined detailing. <b>Hanken Grotesk</b> (text) for everything else, in sentence case.</p>
    {why("Taste: Nike Run Club typography, bold but refined", "Taste: no single heavy condensed face for everything", "Hierarchy rule 4")}
    {wrap('Type scale', f'<table class="spec"><thead><tr><th>Token · face</th><th>Sample</th><th>Serves</th><th>Why</th></tr></thead><tbody>{type_trs}</tbody></table>')}
  </section>

  <section class="stand-section" aria-labelledby="shape-h">
    <h2 id="shape-h">Shape</h2>
    {SHAPE}
  </section>

  <section class="stand-section" aria-labelledby="photo-h">
    <h2 id="photo-h">Photos</h2>
    <div class="stand-grid">
      <div class="stand-stack">
        <p>Every photo is black and white: <code>--photo-filter</code> ({tok("photo-filter")}), set inside the card at 3:1 with a 4px radius. Color stays reserved for the accent and the states.</p>
        <p>Source: Unsplash, free license, on topic: hybrid and functional-fitness racing, road races, trail and OCR. No stairs, no generic gym selfies, no posed portraits. Each photo is downloaded and looked at before use, and logged in <code>references.md</code> → Photos.</p>
        {why("Taste: black-and-white race photos (round 1 Direction 1)", "Hierarchy rule 1: photos never compete with the accent", "Attribute c: no single sport's look")}
      </div>
      <div class="stand-stack">{CARD_BERLIN}</div>
    </div>
  </section>

  <section class="stand-section" aria-labelledby="icon-h">
    <h2 id="icon-h">Icons · Solar, bold</h2>
    <p>One library, one style: Solar bold, at 15px in meta, 18px in buttons and fields, 26px in the tab bar. Icons take the color of their text, never the accent on their own.</p>
    {why("Brief: Solar icons", "Hierarchy rule 6: one link icon on the proof line")}
    {wrap('Icon coverage plan', f'<table class="spec"><thead><tr><th>Where</th><th>Icon</th><th>Token</th><th>Use</th><th>Status</th></tr></thead><tbody>{icon_trs}</tbody></table>')}
  </section>

  <section class="stand-section" id="components" aria-labelledby="comp-h">
    <h2 id="comp-h">Components, live</h2>
    <div class="stand-grid">
      <div class="stand-panel">
        <h3>Primary button, with its secondary and tertiary siblings</h3>
        {BUTTONS}
        <p class="stand-label">States: hover on each, Tab for focus (2px Text 1 ring), then disabled and loading.</p>
        <div class="stand-row">
          <button type="button" class="btn btn--primary" disabled>Log result</button>
          <button type="button" class="btn btn--primary" aria-busy="true" aria-disabled="true">Saving…</button>
          <a class="btn btn--primary" href="#components">Register on hyrox.com {svg("arrow-right-up")}</a>
        </div>
        {why("Hierarchy rule 3", "Voice: Button names the result of the tap", "Critique fix: 44px targets", "Disabled falls back to the raised fill and Disabled text, so it reads as unavailable, not as a secondary button")}
      </div>
      <div class="stand-panel">
        <h3>Race card with photo</h3>
        {CARD_LONDON}
        <p class="stand-label">Anatomy borrowed from round 1 "Format colors", layout only, no colors: photo inside the card · date on a tile · title · neutral chip (same for every format) · location with map-point.</p>
        {why("Attribute b: the date leads, on its own tile", "Hierarchy rule 2: chip is metadata", "Taste: black-and-white photos", "Designer: anatomy from round 1 Format colors, layout only")}
      </div>
      <div class="stand-panel">
        <h3>Search field</h3>
        {SEARCH}
        <p class="stand-label">Try it: hover shows a stronger outline; focus shows the 2px Text 1 ring. The outline is Field line ({cr(tok('field-line'), tok('bg-1')):.2f}:1 on the field), the placeholder Text 2 ({cr(tok('text-2'), tok('bg-1')):.2f}:1).</p>
        {why("Hierarchy rule 3: not a button, so it sits on the surface, not raised", "jtbd.md → Hypothesis 7 [?]: search by race name or city")}
      </div>
    </div>
  </section>

  <section class="stand-section" id="race-browse-parts" aria-labelledby="rb-h">
    <h2 id="rb-h">Race browse parts, live</h2>
    <p>Everything Race browse needs besides the card, in the wireframes' own markup and copy, styled only from <code>components.css</code>. The screen can link the same file without markup changes.</p>
    <div class="stand-grid">
      <div class="stand-panel">
        <h3>Controls · Filters, List/Map, active filter chips, result count and sort</h3>
        <div class="controls">
          <div class="control-row">
            <button type="button" class="filters-trigger" aria-haspopup="dialog" aria-expanded="false">Filters · 2</button>
            <div class="view-toggle" role="group" aria-label="Choose view">
              <button type="button" class="view-btn" aria-pressed="true">List</button>
              <button type="button" class="view-btn" aria-pressed="false">Map</button>
            </div>
          </div>
          <div class="chips-bar">
            <ul class="chips-row" aria-label="Active filters">
              <li><button type="button" class="chip" aria-label="Remove filter: HYROX">HYROX <span aria-hidden="true">×</span></button></li>
              <li><button type="button" class="chip" aria-label="Remove filter: Marathon">Marathon <span aria-hidden="true">×</span></button></li>
            </ul>
            <button type="button" class="clear-all">Clear all filters</button>
          </div>
        </div>
        <div class="results-row">
          <p class="results-count"><strong>4</strong> races match your filters</p>
          <div class="sort-control">
            <label for="sort-live">Sort:</label>
            <select id="sort-live" name="sort">
              <option value="soonest" selected>Soonest first</option>
              <option value="farthest">Latest first</option>
            </select>
          </div>
        </div>
        {why("Hierarchy rule 3: Filters is secondary (tonal), Clear all filters is tertiary (text link)", "Hierarchy rule 2: the active chip is a calm outline, not the brightest thing", "Hierarchy rule 1: the selected segment uses Line, not the accent", "Hierarchy rule 4: count and sort are meta", "Critique fix: 44px targets")}
      </div>
      <div class="stand-panel">
        <h3>Loading · skeleton cards, count bar, sort disabled</h3>
        <div class="results-row">
          <p class="results-count"><span class="bar count" aria-hidden="true"></span><span class="visually-hidden">Loading races…</span></p>
          <div class="sort-control">
            <label for="sort-loading">Sort:</label>
            <select id="sort-loading" name="sort" disabled>
              <option value="soonest" selected>Soonest first</option>
              <option value="farthest">Latest first</option>
            </select>
          </div>
        </div>
        <ul class="race-list" aria-busy="true" aria-hidden="true">
          <li><div class="skeleton-card"><div class="bar photo"></div><div class="bar title"></div><div class="skel-meta"><div class="bar tag"></div><div class="bar date"></div></div><div class="bar location"></div></div></li>
          <li><div class="skeleton-card"><div class="bar photo"></div><div class="bar title"></div><div class="skel-meta"><div class="bar tag"></div><div class="bar date"></div></div><div class="bar location"></div></div></li>
        </ul>
        {why("voice.md → Loading: a skeleton plus “Loading races…” for screen readers; no spinner, no invented progress", "Race card anatomy (designer): the skeleton has the card's shape: photo band, date tile, title, chip, location", "No shimmer: nothing moves that isn't real")}
      </div>
      <div class="stand-panel">
        <h3>Empty · no races match</h3>
        <div class="state-message">
          <h2>No races match your current filters</h2>
          <p>Remove a filter above, or try a wider date range, another region, or more sport types.</p>
          <div class="state-actions">
            <button type="button" class="state-action">Change filters</button>
            <button type="button" class="state-action secondary">Clear all filters</button>
          </div>
        </div>
        {why("Hierarchy rule 3: one primary (Change filters), one secondary (Clear all filters)", "Hierarchy rule 4: the heading is the text face, item level, not a display title", "voice.md → Empty: say what happened and the way forward, no motivational line")}
      </div>
      <div class="stand-panel">
        <h3>Error · the catalog didn’t load</h3>
        <div class="state-message is-error">
          <h2>Couldn’t load races</h2>
          <p>The connection may have dropped. Check it, then try again. Your filters stay as they are.</p>
          <div class="state-actions">
            <a class="state-action" href="#race-browse-parts">Try again</a>
          </div>
        </div>
        {why("States: icon and text first, color second; the error color is only on the icon", "Hierarchy rule 3: Try again is the screen's one primary", "voice.md → Error: no Oops, names the problem and the recovery", "On the screen this block has role=alert; the stand leaves the role off so a specimen is not announced on load")}
      </div>
    </div>
  </section>

  <section class="stand-section" id="first-screen" aria-labelledby="fs-h">
    <h2 id="fs-h">First screen · how many race cards on a phone</h2>
    <p>Measured on 2026-10-14 with <code>concept/first-screen.html</code> at 390×844 (iPhone 14/15 viewport, 47px status bar, 34px home indicator): the wireframe's Race browse top with the decided photo card, styled only by <code>tokens.css</code> and <code>components.css</code>. With the decided 3:1 photo band ({FS["band"]}px), a card is {FS["card_h"]}px tall.</p>
    {wrap('First screen measurement', f'<table class="spec"><thead><tr><th>State</th><th>List starts at</th><th>Tab bar at</th><th>Fully visible</th><th>Next card visible</th></tr></thead><tbody>'
      + f'<tr><td>Default (no filters, 7 races)</td><td class="num">{FS["base"]["top"]}px</td><td class="num">{FS["tab"]}px</td><td class="num">{FS["base"]["full"]} cards</td><td class="num">{FS["base"]["next"]}%</td></tr>'
      + f'<tr><td>2 filters on (chips row shown, 4 races)</td><td class="num">{FS["filtered"]["top"]}px</td><td class="num">{FS["tab"]}px</td><td class="num">{FS["filtered"]["full"]} card</td><td class="num">{FS["filtered"]["next"]}%</td></tr></tbody></table>')}
    <h3 class="stand-label">The real screen (step 5): wireframes/race-browse.html</h3>
    {wrap('First screen on the real page', '<table class="spec"><thead><tr><th>Where</th><th>Page height</th><th>List starts at</th><th>Tab bar at</th><th>No filters</th><th>2 filters on</th></tr></thead><tbody>'
      + f'<tr><td>Inside the wireframes viewer (the phone: status bar and home strip are outside the page)</td><td class="num">{FS_REAL["viewer"]["h"]}px</td><td class="num">{FS_REAL["viewer"]["base"][0]}px</td><td class="num">{FS_REAL["viewer"]["tab"]}px</td><td class="num">{FS_REAL["viewer"]["base"][1]} full, {FS_REAL["viewer"]["base"][3]}px to spare</td><td class="num">{FS_REAL["viewer"]["filtered"][1]} full + {FS_REAL["viewer"]["filtered"][2]}%</td></tr>'
      + f'<tr><td>Opened directly at 390×844 (no status bar or home strip)</td><td class="num">{FS_REAL["direct"]["h"]}px</td><td class="num">{FS_REAL["direct"]["base"][0]}px</td><td class="num">{FS_REAL["direct"]["tab"]}px</td><td class="num">{FS_REAL["direct"]["base"][1]} full + {FS_REAL["direct"]["base"][2]}%</td><td class="num">{FS_REAL["direct"]["filtered"][1]} full + {FS_REAL["direct"]["filtered"][2]}%</td></tr></tbody></table>')}
    <p class="stand-why"><b>Why (attribute b, a calendar, not a poster):</b> two full races on the first screen with no filters, so the list reads as a run of dates rather than one poster per screen. With two filters on, the chips row costs one card's worth of the second race (1 full + 79%).</p>
  </section>
{rules_section()}
{decisions_section()}
  <section class="stand-section" aria-labelledby="contrast-h">
    <h2 id="contrast-h">Contrast · every text pair and the key non-text pairs</h2>
    <p>Generated by <code>scripts/concept/build_stand.py</code> from the hex values in <code>tokens.css</code> (WCAG 2 relative luminance); the build stops if a text pair fails. Body text needs 4.5:1; non-text UI (focus ring, outlines) needs 3:1.</p>
    {CONTRAST}
  </section>

</main>
<script>
  // List/Map is live: pressing one releases the other.
  document.querySelectorAll('.view-toggle').forEach(function (group) {{
    group.addEventListener('click', function (e) {{
      var btn = e.target.closest('.view-btn'); if (!btn) return;
      group.querySelectorAll('.view-btn').forEach(function (b) {{ b.setAttribute('aria-pressed', String(b === btn)); }});
    }});
  }});
</script>
</body>
</html>
'''
# Color rule 2 on the generated markup: no result row carries a check icon or "verified"
for block in re.findall(r'<article class="result-card">.*?</article>', page, flags=re.S):
    assert 'check-circle' not in block and 'verified' not in block.lower(), 'Color rule 2: a result carries a success mark'
    assert 'Self-reported · via ' in block, 'Attribute d: the proof line states the source'
# Every token is signed: each one defined in tokens.css or map.css appears on the stand with its reason
_defined = set(re.findall(r'(?:^|;)\s*--([a-z0-9-]+):', TOK, flags=re.M))
_unsigned = sorted(n for n in _defined if not re.search(r'--' + re.escape(n) + r'(?![a-z0-9-])', page))
assert not _unsigned, ('Unsigned tokens (add a row with its reason)', _unsigned)
print('Signed tokens:', len(_defined), 'of', len(_defined))
open(os.path.join(ROOT, 'concept/concept.html'), 'w').write(page)
print('pairs', len(PAIRS), 'min text ratio', min(cr(tok(f), tok(b)) for _, f, b, k in PAIRS if k == 'text'))
