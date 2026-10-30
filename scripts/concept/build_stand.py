"""Generate concept/concept.html (the concept stand).

Usage, from the repo root:  python3 scripts/concept/build_stand.py
The page holds no style values: it links tokens/tokens.css (every value: primitives
and semantic color roles), components/index.css (every component) since Lesson 8
step 4, and concept/specimens.css and concept/stand.css (the docs layer).
Every contrast ratio is computed here from the hex values in tokens/tokens.css, and
the build stops if any text pair fails WCAG AA. Re-run after changing a token;
it stamps the pages that link the kit, checks that no page links a missing file,
and mirrors the stand, the kit and the map to public/."""
import sys, os, re
sys.path.insert(0, os.path.dirname(__file__))
from colorlib import cr

HERE = os.path.dirname(os.path.abspath(__file__))
ICONS = os.path.join(HERE, 'icons')
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
def _read(f): return open(os.path.join(ROOT, f)).read()
# Lesson 8 step 4: the values are tokens/tokens.css (primitives + semantic roles) and the components components/index.css
TOKENS = _read('tokens/tokens.css')
COMPONENTS = _read('components/index.css')
# the tokens: every :root block of tokens/tokens.css (its first block holds every value; the later ones are the Dynamic
# Type, reduced-motion and Reduce Transparency overrides), of ui/map-data.css (the generated map data) and of the docs
# layer (specimens.css, stand.css, kit-doc.css). tok() reads the first definition: the value at rest.
TOK = ''.join(re.findall(r':root\s*\{(.*?)\n?\}', TOKENS + ''.join(_read(f) for f in ('ui/map-data.css', 'concept/specimens.css', 'concept/stand.css', 'ui/kit-doc.css')), flags=re.S))   # tokens only: map-data.css's per-pin rules set local variables, not tokens

# the light theme (step 5): tokens/tokens.css's :root[data-theme="light"] block overrides roles; tok(name, 'light') reads it first
LIGHT = re.search(r':root\[data-theme="light"\]\s*\{(.*?)\n\}', TOKENS, flags=re.S).group(1)
LIGHT_DEF = dict(re.findall(r'^\s*--([a-z0-9-]+):\s*([^;]+);', re.sub(r'/\*.*?\*/', '', LIGHT, flags=re.S), flags=re.M))
THEMES = ('dark', 'light')
def tok(name, theme='dark'):
    if theme == 'light' and name in LIGHT_DEF:
        v = LIGHT_DEF[name].strip()
    else:
        m = re.search(r'--' + re.escape(name) + r':\s*([^;]+);', TOK)
        v = m.group(1).strip()
    r = re.match(r'var\(--([a-z0-9-]+)\)', v)
    if r: return tok(r.group(1), theme)
    return '#' + ''.join(c * 2 for c in v[1:]) if re.fullmatch(r'#[0-9A-Fa-f]{3}', v) else v   # #000 → #000000

def px(name):
    """A type-scaled size as shown on the stand: 'calc(34 * var(--type-unit))' → '34px'."""
    v = tok(name); m = re.match(r'calc\((\d+(?:\.\d+)?) \* var\(--type-unit\)\)', v)
    return f'{m.group(1)}px' if m else v

def svg(name, cls='icon'):
    s = open(f'{ICONS}/{name}.svg' if name.endswith('-linear') else f'{ICONS}/{name}-bold.svg').read().strip()   # small UI glyphs are Solar Linear (step 6, #23)
    return s.replace('<svg ', f'<svg class="{cls}" aria-hidden="true" focusable="false" ', 1).replace(' width="1em" height="1em"', '')

def sw(t): return f'<span class="swatch swatch--{t}"></span>'

_wrap_n = [0]
def wrap(label, table):
    return f'<div class="spec-wrap" tabindex="0" role="region" aria-label="{label}">{table}</div>'

# ---------------------------------------------------------------- contrast
PAIRS = [  # label, text token, background token, kind: 'text' | 'large' | 'ui' | 'exempt'
    ('Titles, body, finish time on the page', 'text-primary', 'page', 'text'),
    ('Titles, item titles, finish time on a card', 'text-primary', 'surface', 'text'),
    ('Secondary button label', 'text-primary', 'raised', 'text'),
    ('Active filter chip label on its tonal capsule (designer, 2026-10-22)', 'text-primary', 'raised', 'text'),
    ('Active filter chip label, hover', 'text-primary', 'pressed', 'text'),
    ('Selected List/Map segment, hover and open fills', 'text-primary', 'pressed', 'text'),
    ('Unselected List/Map segment on hover', 'text-secondary', 'pressed', 'text'),
    ('Meta on the page (counts, sort)', 'text-secondary', 'page', 'text'),
    ('Meta on a card (month and year, location, proof line)', 'text-secondary', 'surface', 'text'),
    ('Search placeholder', 'text-secondary', 'surface', 'text'),
    ('Date day on the tile', 'text-primary', 'raised', 'text'),
    ('Date month and year on the tile', 'text-secondary', 'raised', 'text'),
    ('Unselected List/Map segment', 'text-secondary', 'raised', 'text'),
    ('Format chip label', 'chip-text', 'raised', 'text'),
    ('Primary button label', 'on-accent-fill', 'accent-fill', 'text'),
    ('Primary button label, hover', 'on-accent-fill', 'accent-hover', 'text'),
    ('Error title and icon', 'error', 'error-surface', 'text'),
    ('Error body', 'text-primary', 'error-surface', 'text'),
    ('Inline error text on a card', 'error', 'surface', 'text'),
    ('Success title and icon', 'success', 'success-bg', 'text'),
    ('Success body', 'text-primary', 'success-bg', 'text'),
    ('Warning title, icon and body', 'warning', 'warning-bg', 'text'),
    ('Stand panels: secondary text', 'text-secondary', 'frame', 'text'),
    ('Focus ring against the page (non-text, 3:1)', 'text-primary', 'page', 'ui'),
    ('Focus ring against a card (non-text, 3:1)', 'text-primary', 'surface', 'ui'),
    ('Search field outline against its own fill (non-text, 3:1)', 'boundary', 'surface', 'ui'),
    ('Search field outline against the page (non-text, 3:1)', 'boundary', 'page', 'ui'),
    ('Disabled button label', 'text-disabled', 'raised', 'exempt'),
    ('Result count number', 'text-primary', 'page', 'text'),
    ('Result count text, Sort: label', 'text-secondary', 'page', 'text'),
    ('Sort value (Soonest first)', 'text-primary', 'page', 'text'),
    ('Sort chevron (non-text, 3:1)', 'text-primary', 'page', 'ui'),
    ('Filters label and icon on the secondary button', 'text-primary', 'raised', 'text'),
    ('Empty and error state heading', 'text-primary', 'page', 'text'),
    ('Empty and error state body', 'text-secondary', 'page', 'text'),
    ('Error icon in the state heading (non-text, 3:1)', 'error', 'page', 'ui'),
    ('Kit · top bar: back link, title, Cancel, Save', 'text-primary', 'page', 'text'),
    ('Kit · Save while saving ("Saving…")', 'text-secondary', 'page', 'text'),
    ('Kit · detail facts label (Sport type, Race date)', 'text-secondary', 'page', 'text'),
    ('Kit · inline error and form alert text', 'text-primary', 'error-surface', 'text'),
    ('Kit · error icon in an inline error (non-text, 3:1)', 'error', 'error-surface', 'ui'),
    ('Kit · primary button in the action bar', 'on-accent-fill', 'accent-fill', 'text'),
    ('Kit · text field value and label on a field', 'text-primary', 'surface', 'text'),
    ('Kit · field label and hint on the page', 'text-secondary', 'page', 'text'),
    ('Kit · field boundary against the page (non-text, 3:1)', 'boundary', 'page', 'ui'),
    ('Kit · field error icon on the page (non-text, 3:1)', 'error', 'page', 'ui'),
    ('Kit · Profile row value and note', 'text-secondary', 'surface', 'text'),
    ('Kit · Profile initials on their tile', 'text-primary', 'raised', 'text'),
    ('Kit · confirm alert body', 'text-secondary', 'surface', 'text'),
    ('Kit · small secondary button (Dismiss, Unlink race)', 'text-primary', 'raised', 'text'),
    ('Kit · disabled catalog row label', 'text-disabled', 'surface', 'exempt'),
    ('Disabled sort while loading', 'text-disabled', 'page', 'exempt'),
    ('Skeleton bar on a card', 'raised', 'surface', 'info'),
    ('Race browse · Filters sheet heading, checkbox labels', 'text-primary', 'surface', 'text'),
    ('Race browse · Filters sheet field labels and legend', 'text-secondary', 'surface', 'text'),
    ('Race browse · Filters sheet field value (select, dates)', 'text-primary', 'page', 'text'),
    ('Race browse · Filters sheet field outline (non-text, 3:1)', 'boundary', 'surface', 'ui'),
    ('Race browse · checkbox against the sheet (non-text, 3:1)', 'text-primary', 'surface', 'ui'),
    ('Race browse · Cancel (secondary) in the sheet', 'text-primary', 'raised', 'text'),
    ('Race browse · Map placeholder caption', 'text-secondary', 'surface', 'text'),
    ('Race browse · Map pin label', 'text-primary', 'raised', 'text'),
    ('Race browse · Map pin dot on its label (non-text, 3:1)', 'text-primary', 'raised', 'ui'),
    ('Race browse · Map placeholder outline (non-text, 3:1)', 'boundary', 'page', 'ui'),
    ('Race browse · Map caption on water', 'text-secondary', 'map-water', 'text'),
    ('Race browse · Map pin dot on land (non-text, 3:1)', 'text-primary', 'map-land', 'ui'),
    ('Race browse · Map pin dot on water (non-text, 3:1)', 'text-primary', 'map-water', 'ui'),
    ('Race browse · Map leader line on land (non-text, 3:1)', 'text-secondary', 'map-land', 'ui'),
    ('Race browse · Map leader line on water (non-text, 3:1)', 'text-secondary', 'map-water', 'ui'),
    ('Race browse · Map state panel text (empty, error) on its panel', 'text-primary', 'surface', 'text'),
    ('Race browse · coastlines and borders on land', 'map-lines', 'map-land', 'info'),
    ('Results list · saved confirmation text ("Saved: HYROX London"), neutral surface', 'text-primary', 'surface', 'text'),
    ('Results list · saved confirmation icon, neutral (non-text, 3:1)', 'text-secondary', 'surface', 'ui'),
    ('Results list · "Newest first" after the count', 'text-secondary', 'page', 'text'),
    ('Results list · Log result stepped down to secondary (empty, error)', 'text-primary', 'raised', 'text'),
    ('Results list · count separator hairline', 'hairline', 'page', 'info'),
    ('Skeleton count bar on the page', 'raised', 'page', 'info'),
    ('Race browse · filter chip remove icon on the capsule, close-circle (non-text, 3:1)', 'text-secondary', 'raised', 'ui'),
    ('Race browse · filter chip remove icon on the capsule, hover (non-text, 3:1)', 'text-secondary', 'pressed', 'ui'),
    ('Race browse · Filters sheet calendar icon in a date field (non-text, 3:1)', 'text-primary', 'page', 'ui'),
    ('Empty state icon, muted, on the page (non-text, 3:1)', 'text-secondary', 'page', 'ui'),
    ('Error state icon, coral, on the page (non-text, 3:1)', 'error', 'page', 'ui'),
    ('Empty or error state icon inside the map panel (non-text, 3:1)', 'text-secondary', 'surface', 'ui'),
    ('Profile · Sign out in its row (destructive, coral; G68, designer 2026-10-23)', 'error', 'surface', 'text'),
    ('Profile · Sign out row, hover', 'error', 'raised', 'text'),
    ('Filters sheet · row label and checked sport type on the raised rows (G19, G20)', 'text-primary', 'group', 'text'),
    ('Filters sheet · neutral checkmark on a raised row (non-text, 3:1; G19, C4)', 'text-primary', 'group', 'ui'),
    ('Filters sheet · Region value on a raised row (a native menu, G17)', 'text-secondary', 'group', 'text'),
    ('Filters sheet · Region pop-up chevron on a raised row (non-text, 3:1)', 'text-secondary', 'group', 'ui'),
    ('Filters sheet · date value on its compact-picker pill (G18)', 'text-primary', 'raised', 'text'),
    ('Filters sheet · calendar glyph on the date pill (non-text, 3:1)', 'text-secondary', 'raised', 'ui'),
    ('Race browse · Sort button: the current order and its icon (G21)', 'text-primary', 'page', 'text'),
    ('Race picker · the linked race’s checkmark on its card (non-text, 3:1; G47)', 'text-primary', 'surface', 'ui'),
    ('Log result · the linked race on the sheet: name, facts and Unlink (step 6, #8)', 'text-primary', 'group', 'text'),
    ('Date pill · "Choose a date" when empty (step 6, #26)', 'text-secondary', 'raised', 'text'),
    ('Date pill · the date (step 6, #26)', 'text-primary', 'raised', 'text'),
    ('Log result · the linked race on the sheet: "From the race catalog", the place (step 6, #8)', 'text-secondary', 'group', 'text'),
    ('Profile · an editable value in its row (step 6, #21)', 'text-primary', 'surface', 'text'),
    ('Result detail · Copy link under the official result link (step 6, #10)', 'text-primary', 'page', 'text'),
    ('Race browse · Sort button disabled while loading', 'text-disabled', 'page', 'exempt'),
    ('Results list · Log result stepped down to Text 1 when a state brings its own primary (-error)', 'text-primary', 'page', 'text'),
    ('Kit · invalid field ring against the field (non-text, 3:1)', 'error', 'surface', 'ui'),
    ('Kit · invalid field ring against the page (non-text, 3:1)', 'error', 'page', 'ui'),
    ('Results list · disclosure indicator on a row (non-text, 3:1)', 'text-secondary', 'surface', 'ui'),
    ('Pressed card or row: meta on the pressed level', 'text-secondary', 'pressed', 'text'),
    ('Pressed race card: format chip label (the chip keeps bg-2)', 'chip-text', 'raised', 'text'),
    ('Profile · pop-up chevron on a row, Saving… spinner (non-text, 3:1)', 'text-secondary', 'surface', 'ui'),
]
# ---------------------------------------------------------------- glass (C1): text over glass, against the worst case behind it
def _rgb(h): h = h.lstrip('#'); return [int(h[i:i+2], 16) for i in (0, 2, 4)]
def over(fg, a, bg): return '#' + ''.join(f'{round(a * f + (1 - a) * b):02X}' for f, b in zip(_rgb(fg), _rgb(bg)))   # sRGB "over", as the browser blends
def glass_parts(name, theme='dark'):
    m = re.match(r'color-mix\(in srgb, var\(--([a-z0-9-]+)\) var\(--([a-z0-9-]+)\), transparent\)', tok(name, theme))
    return tok(m.group(1), theme), float(tok(m.group(2), theme).rstrip('%')) / 100, m.group(1), m.group(2)
# the scrim is a mix too since Lesson 8 (color-mix(in srgb, var(--black) var(--alpha-60), transparent)), parsed the same way
SCRIM = {t: glass_parts('scrim', t) for t in THEMES}
SCRIM_BASE, SCRIM_A = SCRIM['dark'][0], SCRIM['dark'][1]
# The worst case behind a glass is what contrasts least with its text.
# Dark: the brightest thing that can scroll under a bar is Text primary (a title); a photo's lightest tone after the
# black-and-white filter is #D9D9D9, below it. Light (step 5): the darkest, and a photo's shadows reach black, below
# Text primary's #131518. Under the sheet the same sits behind the scrim. Measured with no help from the blur (a blurred
# glyph is lighter or darker than its solid color, never further), so this is the floor.
WORST = {'dark': tok('text-primary'), 'light': '#000000'}
UNDER = {t: {'bar': WORST[t], 'ground': WORST[t], 'sheet': over(SCRIM[t][0], SCRIM[t][1], WORST[t])} for t in THEMES}
GLASS = {'bar': 'glass-bar', 'ground': 'glass-ground', 'sheet': 'glass-sheet'}
def glass_bg(where, alpha=None, theme='dark'):
    base, a, _, _ = glass_parts(GLASS[where], theme); return over(base, a if alpha is None else alpha, UNDER[theme][where])
GLASS_PAIRS = [   # label, text token, glass, kind
    ('Tab bar · inactive tab label over content', 'text-secondary', 'bar', 'text'),
    ('Tab bar · current tab (accent) over content', 'accent-ink', 'bar', 'text'),
    ('Action bar · caption over content (“Opens in a new tab.”)', 'text-secondary', 'bar', 'text'),
    ('Controls bar · Clear all filters (the chips are opaque capsules: their pairs are solid)', 'text-primary', 'ground', 'text'),
    ('Top bar · back link, title, Cancel', 'text-primary', 'ground', 'text'),
    ('Top bar · Save, Log result’s one primary (accent text)', 'accent-ink', 'ground', 'text'),
    ('Top bar · Save or Log result under the pointer (step 5: its own role)', 'accent-ink-hover', 'ground', 'text'),
    ('Top bar · “Saving…” with its spinner', 'text-secondary', 'ground', 'text'),
    ('Filters sheet · heading, checkbox labels', 'text-primary', 'sheet', 'text'),
    ('Filters sheet · field labels and legend', 'text-secondary', 'sheet', 'text'),
    ('Filters sheet · checked box, neutral tint (non-text, 3:1)', 'text-primary', 'sheet', 'ui'),
    ('Filters sheet · Apply filters, the sheet’s one primary, in its top bar (accent text; G12)', 'accent-ink', 'sheet', 'text'),
    ('Collapsed title bar · Log result, Results list’s one primary (accent text; G5)', 'accent-ink', 'ground', 'text'),
    ('Log result sheet · title, Cancel, row labels and values', 'text-primary', 'sheet', 'text'),
    ('Confirm alert (glass, G67) · title, Cancel', 'text-primary', 'sheet', 'text'),
    ('Confirm alert (glass, G67) · body', 'text-secondary', 'sheet', 'text'),
    ('Confirm alert (glass, G67) · Sign out, destructive', 'error', 'sheet', 'text'),
]
def min_alpha(where, theme='dark'):   # the lowest fill opacity at which every pair on this glass still passes
    for pct in range(0, 101):
        if all(cr(tok(fg, theme), glass_bg(where, pct / 100, theme)) >= (4.5 if k == 'text' else 3.0) for _, fg, w, k in GLASS_PAIRS if w == where):
            return pct
    return None
GLASS_MIN_T = {t: {w: min_alpha(w, t) for w in GLASS} for t in THEMES}
GLASS_MIN = GLASS_MIN_T['dark']
P = '[?] provisional: Apple’s iOS 26 kit wasn’t read; to be replaced from it (designer, 2026-10-19)'
HIG_DIM = 35   # HIG Materials: "consider adding a dark dimming layer of 35% opacity" under clear Liquid Glass over bright content
for t in THEMES:
    for w in GLASS:
        _, a, _, _ = glass_parts(GLASS[w], t)
        assert GLASS_MIN_T[t][w] is not None and a * 100 >= GLASS_MIN_T[t][w], ('Glass too clear for AA over the worst case', t, w, a, GLASS_MIN_T[t][w])
        assert a * 100 >= HIG_DIM, ('Glass lighter than HIG’s 35% dimming floor', t, w)

NEED = {'text': 4.5, 'large': 3.0, 'ui': 3.0, 'exempt': 0, 'info': 0}
rows, failures, CONTRAST_LOG = [], [], []
def _verdict(kind, oks):
    need = NEED[kind]
    if kind == 'exempt': return '<span class="exempt">exempt (disabled, WCAG 1.4.3)</span>'
    if kind == 'info': return '<span class="exempt">no requirement (decorative placeholder, aria-hidden)</span>'
    return (f'<span class="pass">pass</span> · needs {need:g}:1' if all(oks) else f'<b>fail</b> · needs {need:g}:1')
# Dark-only pairs: the stand's own panels and its state specimens (success, warning) live on the stand, a dark-only docs
# page that never takes the light theme; their tokens have no light value. Every product pair is checked in both themes.
def dark_only(label, fg, bg): return label.startswith('Stand panels') or bool({fg, bg} & {'success', 'success-bg', 'warning', 'warning-bg', 'warning-line'})
for label, fg, bg, kind in PAIRS:   # every pair in both themes (step 5); a failure in either stops the build
    themes = ('dark',) if dark_only(label, fg, bg) else THEMES
    rs = {t: cr(tok(fg, t), tok(bg, t)) for t in THEMES}
    oks = [rs[t] >= NEED[kind] for t in themes]
    for t in themes:
        if kind not in ('exempt', 'info') and rs[t] < NEED[kind]: failures.append((t, label, rs[t]))
    if len(themes) == 2: CONTRAST_LOG.append((fg, bg, kind, rs['dark'], rs['light']))
    rows.append(f'<tr><td>{label}</td><td class="sample">{sw(fg)}<code>--{fg}</code> {tok(fg)} · {tok(fg, "light")}</td>'
                f'<td class="sample">{sw(bg)}<code>--{bg}</code> {tok(bg)} · {tok(bg, "light")}</td><td class="num">{rs["dark"]:.2f}:1</td><td class="num">{f"{rs[chr(108) + chr(105) + chr(103) + chr(104) + chr(116)]:.2f}:1" if len(themes) == 2 else "dark only (the stand)"}</td><td>{_verdict(kind, oks)}</td></tr>')
for label, fg, where, kind in GLASS_PAIRS:
    rs = {t: cr(tok(fg, t), glass_bg(where, None, t)) for t in THEMES}
    need = NEED[kind]; oks = [rs[t] >= need for t in THEMES]
    for t in THEMES:
        if rs[t] < need: failures.append((t, label, rs[t]))
        solid = cr(tok(fg, t), glass_parts(GLASS[where], t)[0])   # Reduce Transparency: the glass turns solid (step 5; this replaced the solid tab bar pairs)
        if solid < need: failures.append((t, label + ' · Reduce Transparency, solid', solid))
    CONTRAST_LOG.append((fg, GLASS[where] + ' over the worst case', kind, rs['dark'], rs['light']))
    base, a, bt, at = glass_parts(GLASS[where])
    lbase, la, lbt, _ = glass_parts(GLASS[where], 'light')
    under = 'the scrim over the worst case' if where == 'sheet' else 'the worst case'
    rows.append(f'<tr><td>{label}</td><td class="sample">{sw(fg)}<code>--{fg}</code> {tok(fg)} · {tok(fg, "light")}</td>'
                f'<td class="sample"><code>--{GLASS[where]}</code> over {under}: dark <code>--{bt}</code> at {a * 100:g}% over Text primary = {glass_bg(where)}; light <code>--{lbt}</code> at {la * 100:g}% over black = {glass_bg(where, None, "light")}</td><td class="num">{rs["dark"]:.2f}:1</td><td class="num">{rs["light"]:.2f}:1</td>'
                f'<td>{_verdict(kind, oks)}</td></tr>')
assert not failures, failures
for t in THEMES:
    print(f'Glass ({t}): bar', glass_bg('bar', None, t), 'min opacity', GLASS_MIN_T[t]['bar'], '% · ground', glass_bg('ground', None, t), 'min', GLASS_MIN_T[t]['ground'], '% · sheet', glass_bg('sheet', None, t), 'min opacity', GLASS_MIN_T[t]['sheet'], '%')

# the contrast record in tokens/tokens.css (step 5): every role pair the build checks, in both themes, as a generated comment
_seen, _lines = set(), []
for fg, bg, kind, rd, rl in CONTRAST_LOG:
    if kind in ('exempt', 'info') or (fg, bg) in _seen: continue
    _seen.add((fg, bg)); _lines.append(f'   --{fg} on --{bg}'.ljust(74) + f'dark {rd:5.2f}  light {rl:5.2f}  needs {NEED[kind]:g}')
_block = ('/* contrast:start (generated by scripts/concept/build_stand.py; do not edit by hand)\n'
          f'   Every semantic text/background pair the build checks, in both themes (WCAG 2 ratios). Glass is measured over its\n'
          f'   worst case: dark, Text primary behind; light, black behind (a photo\'s shadows); the sheet also under its scrim.\n'
          f'   {len(_lines)} pairs; the build stops if one falls below its need in either theme.\n'
          + '\n'.join(_lines) + '\n   contrast:end */')
_tok_text = open(os.path.join(ROOT, 'tokens/tokens.css')).read()
if '/* contrast:start' in _tok_text:
    _new = re.sub(r'/\* contrast:start.*?contrast:end \*/', lambda m: _block, _tok_text, flags=re.S)
else:
    _new = _tok_text.rstrip('\n') + '\n\n' + _block + '\n'
if _new != _tok_text:
    open(os.path.join(ROOT, 'tokens/tokens.css'), 'w').write(_new)
print('Contrast in both themes:', len(_lines), 'role pairs written to tokens/tokens.css')
CONTRAST = ('<div class="spec-wrap" tabindex="0" role="region" aria-label="Contrast table"><table class="spec"><thead><tr><th>Where</th><th>Text (dark · light)</th><th>Background (dark · light)</th><th>Dark</th><th>Light</th><th>WCAG AA, both</th></tr></thead><tbody>'
            + ''.join(rows) + '</tbody></table></div>')

# cache-busting: stylesheet links carry a short hash of the token, component, map and docs-layer files
import hashlib, subprocess
# components/ (Lesson 8, step 3): bundle components/*.css into components/index.css in cascade order, check that no component
# reads a color primitive or writes a hex, px or font name; a failure stops the build
_c = subprocess.run([sys.executable, os.path.join(ROOT, 'scripts/build_components.py')], capture_output=True, text=True)
print(_c.stdout.strip())
if _c.returncode: sys.exit('build_components failed: the build stops')
# DESIGN.md's frontmatter values and .impeccable/design.json, generated from tokens/tokens.css (Lesson 8 step 4): hex lives in one file
_d = subprocess.run([sys.executable, os.path.join(ROOT, 'scripts/build_design_sidecar.py')], capture_output=True, text=True)
print(_d.stdout.strip() or _d.stderr.strip())
if _d.returncode: sys.exit('build_design_sidecar failed: the build stops')
COMPONENTS = _read('components/index.css')   # re-read: build_components.py just rewrote it
CSS_V = hashlib.sha1(''.join(open(os.path.join(ROOT, n)).read() for n in ('ui/kit-doc.css', 'concept/stand.css', 'concept/specimens.css', 'concept/first-screen.css', 'tokens/tokens.css', 'components/index.css', 'ui/map-data.css')).encode()).hexdigest()[:8]
def _stamp(path):
    # also inside a srcdoc attribute (the showcase's tab bar frames), where the quotes are &quot;
    html = re.sub(r'href=("|&quot;)((?:\.\./ui/|\.\./tokens/|\.\./components/|)(?:kit-doc|map-data|stand|specimens|first-screen|tokens|index))\.css(\?v=[0-9a-f]+)?\1',
                  lambda m: f'href={m.group(1)}{m.group(2)}.css?v={CSS_V}{m.group(1)}', open(path).read())
    open(path, 'w').write(html)
STAMPED = ['concept/first-screen.html', 'ui/kit.html', 'ui/shell.html'] + [f'wireframes/{s}{x}.html' for s in ('race-browse', 'results-list') for x in ('', '-empty', '-error', '-loading')]
STAMPED += [f'wireframes/race-detail{x}.html' for x in ('', '-error', '-loading')]   # step 5, Discovery group (2026-10-22)
STAMPED += [f'wireframes/{p}.html' for p in (   # step 5, Archive and Infrastructure groups (2026-10-22)
    'log-result', 'log-result-error', 'log-result-loading', 'race-picker', 'race-picker-empty', 'race-picker-error', 'race-picker-loading',
    'result-detail', 'result-detail-error', 'result-detail-loading',
    'sign-in-sign-up', 'sign-in-sign-up-check-inbox', 'sign-in-sign-up-error', 'sign-in-sign-up-loading',
    'reset-password', 'reset-password-check-inbox', 'reset-password-error', 'reset-password-loading',
    'new-password', 'new-password-error', 'new-password-loading', 'profile', 'profile-error', 'profile-loading')]
import subprocess
# the showcase: arranged by role, each specimen's facts from ui/inventory.md → Showcase map (2026-10-26), before stamping
subprocess.run([sys.executable, os.path.join(ROOT, 'scripts/build_kit_showcase.py')], check=True)
for _p in STAMPED:
    _stamp(os.path.join(ROOT, _p))
# the showcase against the inventory and microcopy.md (2026-10-26): every component mapped, every state labelled, every word recorded
_k = subprocess.run([sys.executable, os.path.join(ROOT, 'scripts/check_kit.py')], capture_output=True, text=True)
print(_k.stdout.strip())
if _k.returncode: sys.exit('check_kit failed: the build stops')

# ---------------------------------------------------------------- color rules (concept.md → Color rules)
import math
from colorlib import lab, de2000, hue as lab_hue
CSS = COMPONENTS + _read('concept/stand.css') + _read('concept/specimens.css')   # every component rule the color rules check (Lesson 8 step 4: the components, not ui/kit.css)
CSS_RULES = [(sel.strip(), body) for sel, body in re.findall(r'([^{}]+)\{([^{}]*)\}', re.sub(r'/\*.*?\*/', '', CSS, flags=re.S))]

def selectors_using(*tokens):
    out = []
    for sel, body in CSS_RULES:
        if any(f'var(--{t})' in body for t in tokens):
            out += [x.strip() for x in sel.split(',')]
    return out

# Rule 1: amber only where you can act or where you are
ACCENT_OK = [r'^\.btn--primary(:hover)?$', r'^\.state-action:not\(\.secondary\)(:hover)?$',
             r'^\.(register|open|submit)-btn(:hover)?$',   # the grayscale screens' one primary (kit, 2026-10-18)
             r'^\.top-bar \.(save-btn|bar-action)(:hover)?$',   # the bar action: Save on Log result (kit feedback, 2026-10-19), Log result on Results list (G5), Apply filters on the sheet (G12; markup pass, 2026-10-23)
             r'^\.bottom-nav a\[aria-current="page"\]$',
             r'^\.swatch--(accent-(fill|ink|hover|ink-hover)|amber-\d+)$']   # the stand's swatches, one per token
# the accent roles (--accent-fill, --accent-ink, --accent-hover, since Lesson 8 step 4) and their amber primitives, so a
# class can't reach the amber around its roles (tokens/tokens.css's :root is not a class and isn't read here)
accent_sel = selectors_using('accent-fill', 'accent-ink', 'accent-hover', 'accent-ink-hover', 'amber-78', 'amber-83', 'amber-40', 'amber-33')
accent_bad = [x for x in accent_sel if not any(re.match(p, x) for p in ACCENT_OK)]
assert not accent_bad, ('Color rule 1: accent on a disallowed selector', accent_bad)

# Rule 2: no success color on results
SUCCESS_OK = [r'^\.status--success( \.icon| strong)?$', r'^\.swatch--success(-bg)?$']   # stand specimen only; no product screen uses success color
success_sel = selectors_using('success', 'success-bg')
success_bad = [x for x in success_sel if not any(re.match(p, x) for p in SUCCESS_OK)]
assert not success_bad, ('Color rule 2: success color outside the stand specimen', success_bad)

# Rules 1 and 2 in both themes (step 5): the classes are the same in both, so the theme can only break a rule through its
# values. In each theme, only the accent roles may resolve to an amber primitive, and no role may resolve to a success color.
ROLES = [n for n in re.findall(r'^\s*--([a-z0-9-]+):', TOKENS.split('     2. SEMANTIC: color roles\n')[1].split('\n}')[0], flags=re.M)]
AMBERS = {tok(n).upper() for n in re.findall(r'--(amber-\d+):', TOKENS)}
ACCENT_ROLES = {'accent-fill', 'accent-ink', 'accent-hover', 'accent-ink-hover'}
SUCCESS = {tok('success').upper(), tok('success-bg').upper()}
for _t in THEMES:
    _amber = sorted(r for r in ROLES if tok(r, _t).upper() in AMBERS)
    assert set(_amber) <= ACCENT_ROLES, ('Color rule 1: an amber value on a non-accent role', _t, sorted(set(_amber) - ACCENT_ROLES))
    assert ACCENT_ROLES <= set(_amber), ('Color rule 1: an accent role without an amber value', _t, sorted(ACCENT_ROLES - set(_amber)))
    _green = sorted(r for r in ROLES if tok(r, _t).upper() in SUCCESS)
    assert not _green, ('Color rule 2: a role takes the success color', _t, _green)

# Rule 3a: depth of dark, not #000
BG_LEVELS = ['frame', 'page', 'surface', 'raised', 'pressed']   # the roles on the five graphite levels; --group shares --pressed's level (graphite-20), and the map roles reuse levels
L_MIN, L_MAX, C_MAX, STEP_MIN = 4.5, 20.0, 6.0, 1.5
bg_rows, prev = [], None
for t in BG_LEVELS:
    L, a, b = lab(tok(t)); C = math.hypot(a, b)
    ok = L_MIN <= L <= L_MAX and C <= C_MAX and (prev is None or L - prev >= STEP_MIN)
    assert ok, ('Color rule 3a: background level out of range', t, round(L, 2), round(C, 2))
    bg_rows.append((t, L, C, None if prev is None else L - prev)); prev = L

# Rule 3a, usage: --hairline and --boundary are lines, never a fill (their L* is above the background range)
line_fill = [x for sel, body in CSS_RULES if re.search(r'background(-color)?:\s*var\(--(hairline|boundary|graphite-22|graphite-46)\)', body)
             for x in sel.split(',') if not x.strip().startswith('.swatch--') and x.strip() != '.sheet-handle']   # the handle is a drawn 4px line, not a surface
assert not line_fill, ('Color rule 3a: a hairline token used as a fill', [x.strip() for x in line_fill])

# Rule 3b: amber, not HYROX yellow (reported, not blocking: the designer keeps the amber knowingly)
HYROX_REFS = [('RoxFit', '#FFEC00', 'roxfit-how-it-works.png, 5,786 px'), ('RoxMatchUp', '#F5E401', 'roxmatchup-home.png, 2,770 px')]
HUE_MIN, DE_MIN = 25.0, 24.0
def hue_dist(x, y):
    d = abs(lab_hue(x) - lab_hue(y)); return min(d, 360 - d)
ACCENT = tok('accent-fill')   # = --amber-78 in both themes; the dark --accent-ink is the same primitive (asserted below)
assert tok('accent-ink') == ACCENT, 'Color rule 3b: --accent-ink and --accent-fill parted in dark; check each against HYROX yellow'
# step 5: every accent value in both themes (fill and ink; the hovers are states, Lesson 9) passes the threshold, or is
# the exact hex the designer's override covers. Reported, not blocking, as before.
def _3b(c): return all(hue_dist(c, y) >= HUE_MIN and de2000(c, y) >= DE_MIN for _, y, _ in HYROX_REFS)
RULE_3B_THEMES = []
for _t in THEMES:
    for _r in ('accent-fill', 'accent-ink'):
        _c = tok(_r, _t).upper()
        RULE_3B_THEMES.append((_t, _r, _c, 'pass' if _3b(_c) else 'accepted by designer' if _c == '#F5B649' else 'FAIL'))
hyrox_rows = [(n, c, src, hue_dist(ACCENT, c), de2000(ACCENT, c)) for n, c, src in HYROX_REFS]
HYROX_PASS = all(h >= HUE_MIN and d >= DE_MIN for _, _, _, h, d in hyrox_rows)
# Designer override (concept.md → Color rules → 3b), valid only for this exact accent
RULE_3B_OVERRIDE = {'accent': '#F5B649', 'date': '2026-10-14',
                    'reason': 'the accent is scarce (1–2 uses per screen), the ground is graphite, not black, and the chips are neutral'}
HYROX_ACCEPTED = (not HYROX_PASS) and ACCENT.upper() == RULE_3B_OVERRIDE['accent']
HYROX_STATUS = 'pass' if HYROX_PASS else 'accepted by designer' if HYROX_ACCEPTED else 'FAIL'

# results never carry a success mark (checked on the generated markup at the end)
print('Color rule 1 (accent placement): pass ·', len(accent_sel), 'selectors')
print('Color rule 2 (no success on results): pass ·', len(success_sel), 'selectors')
print('Color rule 3a (depth of dark): pass ·', ', '.join(f'{t} L*{L:.2f} C*{C:.2f}' for t, L, C, _ in bg_rows))
print('Color rule 3b (amber vs HYROX yellow):', HYROX_STATUS if HYROX_STATUS != 'FAIL' else 'FAIL (no designer override for this accent; reported, not blocking)', '·',
      '; '.join(f'{n} {c}: {h:.1f}° ΔE {d:.1f}' for n, c, _, h, d in hyrox_rows))
print('Color rule 3b, both themes:', '; '.join(f'{t} --{r} {c} {v}' for t, r, c, v in RULE_3B_THEMES))
print('Color rules 1 and 2, both themes: pass ·', len(ROLES), 'roles resolved in each')

def decisions_section():
    return f'''
  <section class="stand-section" id="decisions" aria-labelledby="dec-h">
    <h2 id="dec-h">Decided</h2>
    <div class="stand-grid">
      <div class="stand-panel">
        <h3>Accent · <code>{tok("accent-fill")}</code>, kept</h3>
        <p class="stand-why">Compared side by side against a halfway version (<code>{ACCENT_HALF}</code>) and a warmer one that just passes rule 3b (<code>{ACCENT_PASS}</code>). The designer kept the current amber, overriding rule 3b (see Color rules). Text on the accent: {cr(tok("on-accent-fill"), tok("accent-fill")):.2f}:1.</p>
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
        <p class="stand-why">Amber only where you can act or where you are. The build found the accent on {len(accent_sel)} selectors, all allowed: the primary button and its hover, <code>.header-action</code>, the primary <code>.state-action</code>, the grayscale screens' one primary (<code>.register-btn</code>, <code>.open-btn</code>, <code>.submit-btn</code>), Apply filters in the sheet, Save in Log result's top bar (amber text: that screen has no tab bar and no other amber), the current tab, and the specimen swatches. It is never on a result, a finish time, a count or a status.</p>
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
    A = tok('accent-fill'); L, a, b = lab(A); C0 = math.hypot(a, b); h0 = lab_hue(A)
    def col(h):
        C = C0
        while lch_to_hex(L, C, h) is None: C -= 0.1     # keep lightness; lower chroma only as the gamut requires
        return lch_to_hex(L, C, h)
    ok = lambda c: all(hue_dist(c, y) >= HUE_MIN and de2000(c, y) >= DE_MIN for _, y, _ in HYROX_REFS)
    h = h0
    while not ok(col(h)): h -= 0.1                   # warmer = toward orange
    return col((h0 + h) / 2), col(h)
ACCENT_HALF, ACCENT_PASS = _rotate_until_pass()
ACCENT_VERSIONS = [('Current amber', tok('accent-fill')), ('Halfway', ACCENT_HALF), ('Warmer, just passes 3b', ACCENT_PASS)]
print('Accent versions:', ', '.join(f'{n} {c}' for n, c in ACCENT_VERSIONS))

# ---------------------------------------------------------------- decision 2: photo band (measured in the browser)
# first-screen.html at 390×844 on 2026-10-14. Boundary found by search: ratio 2.8638 → band 114px, card 219px, 2 full cards with 0px to spare.
BAND = {'current': {'ratio': '16/7', 'band': 143, 'card': 247, 'def': (1, 77), 'filt': (1, 54)},
        'short':   {'ratio': '3/1',  'band': 109, 'card': 213, 'def': (2, 0),  'filt': (1, 79)},
        'boundary': {'ratio': '2.86/1', 'band': 114, 'card': 219}}

# measured in the browser with first-screen.html at 390×844 on 2026-10-14 after step 5 (box-sizing, 68px date column), --photo-ratio 3 / 1 from tokens.css
FS = {'card_h': 215, 'band': 114, 'tab': 747, 'base': {'top': 290, 'full': 2, 'next': 2}, 'filtered': {'top': 346, 'full': 1, 'next': 81}}
# the real screen, wireframes/race-browse.html, measured 2026-10-14 (step 5)
# step 3b (2026-10-19): content runs under the floating glass tab bar; C3 sizes. Measured in Chrome at 390 wide.
# (page height, list top, tab bar top, cards clear of the bar: full + % of the next, cards on screen incl. under the glass)
FS_3B = [('Inside the viewer, no filters', 757, 239, 685, (2, 0, 1.7), (2, 29)),
         ('Inside the viewer, two filters', 757, 295, 685, (1, 75, None), (2, 3)),
         ('Direct at 390×844, no filters', 844, 239, 772, (2, 35, None), (2, 69)),
         ('Direct at 390×844, two filters', 844, 295, 772, (2, 10, None), (2, 43))]
FS_REAL = {'viewer': {'h': 757, 'tab': 693, 'base': (243, 2, 0, 8.6), 'filtered': (299, 1, 78, None)},
           'direct': {'h': 844, 'tab': 780, 'base': (243, 2, 39, None), 'filtered': (299, 2, 13, None)}}

# ---------------------------------------------------------------- shared markup (wireframe text and structure)
def race_card(name, tag, iso, date, loc, src, pos, alt):
    return f'''<article class="race-card">
          <picture><source type="image/avif" srcset="{src}-684.avif 684w, {src}-1026.avif 1026w" sizes="342px"><source type="image/webp" srcset="{src}-684.webp 684w, {src}-1026.webp 1026w" sizes="342px"><img class="photo" src="{src}-1026.jpg" srcset="{src}-684.jpg 684w, {src}-1026.jpg 1026w" sizes="342px" alt="{alt}" width="1026" height="342"></picture>
          <a class="card-link" href="#components">
            <h2>{name}</h2>
            <p class="card-meta"><span class="sport-tag">{tag}</span> <time datetime="{iso}"><span class="day">{date.split(' ', 1)[0]}</span> {date.split(' ', 1)[1]}</time></p>
            <p class="card-location">{loc}</p>
          </a>
        </article>'''

CARD_LONDON = race_card('HYROX London', 'HYROX', '2026-12-06', '6 Dec 2026', 'London, UK',
                        '../visuals/hyrox-sled-hall-1', None,
                        'Athletes pushing weighted sleds down parallel lanes in a large indoor hall, spectators behind the barriers')
CARD_BERLIN = race_card('Berlin Marathon', 'Marathon', '2026-09-27', '27 Sep 2026', 'Berlin, Germany',
                        '../visuals/marathon-city-1', None,
                        'A dense field of runners mid-race on a wide sunlit city avenue, seen from slightly above')

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
    items = [('Discover', 'compass'), ('Results', 'stopwatch'), ('Profile', 'user')]
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
COLOR_ROWS = [   # the semantic roles (tokens/tokens.css, level 2), then the stand's state specimens (specimens.css)
    ('frame', 'Frame', 'The void behind an open sheet (<code>body:has(&gt; .sheet &gt; .phone-screen)</code>); the stand panels. The tab bar glass and the map water build from the same primitive, <code>--graphite-5</code>.', 'Never inside content.', 'Taste: dark with depth, not pure #000 (Tension C) · Lesson 8: in iOS light the area behind a sheet stays black while the tab bar doesn’t, so the frame is its own role'),
    ('page', 'Page', 'The page behind every screen.', 'Not on cards (cards sit one level up).', 'Attribute e: dark, intense · Taste: not #000'),
    ('surface', 'Surface', 'Race cards, result rows, row groups, the search field, the saved confirmation.', 'Not for controls you press (those are raised).', 'Attribute a: cards stay quiet so the time can lead'),
    ('raised', 'Raised', 'Secondary button, format chip, the date tile, segmented track, skeletons, disabled buttons, pin labels, the initials.', 'Never for the primary action.', 'Hierarchy rule 3: secondary is tonal'),
    ('pressed', 'Pressed', 'Hover, open and pressed fills: the selected List/Map segment, Filters while its sheet is open, a pressed card (+2).', 'Never at rest, never a card.', 'Color rule 3a: the hairline is a line, so pressed fills get their own level'),
    ('group', 'Group', 'A group of rows one level above its container: the rows in the Filters sheet, the linked race on Log result. Same level as Pressed today.', 'Not a state: a press uses Pressed.', 'Lesson 8: in a light appearance a group rises lighter while a press goes darker, so the two roles part'),
    ('hairline', 'Hairline', 'Hairline dividers.', 'Not as a boundary someone must see (fields use Boundary), not as a frame around every card, never a fill.', 'Attribute a: the frame stays quiet'),
    ('boundary', 'Boundary', 'The edge of the search field and other inputs, the pressed segment, the card hover ring, the map frame.', 'Not on cards or chips, never a fill.', 'WCAG 1.4.11: an input boundary needs 3:1 (critique fix)'),
    ('text-primary', 'Text primary', 'Screen titles, item titles, finish times, body. Also the focus ring and the control tint (checked boxes, checkmarks, <code>accent-color</code>), which were <code>--focus</code> and <code>--control-tint</code> until Lesson 8.', 'Not for meta (date month, location, proof). The control tint is never amber, never green.', 'Hierarchy rule 4: three levels · C4 (designer, 2026-10-18): control tint is neutral · Color rule 1'),
    ('text-secondary', 'Text secondary', 'Meta: month and year, location, proof line, counts, inactive tab.', 'Not for titles or the finish time.', 'Attribute d: proof stated, not stamped (a quiet line)'),
    ('chip-text', 'Chip text', 'The format chip label only.', 'Not on filter chips (those are Text primary).', 'Hierarchy rule 2: chips are metadata'),
    ('text-disabled', 'Disabled', 'Disabled controls only.', 'Never for content someone must read.', 'WCAG 1.4.3 exempts disabled controls'),
    ('accent-fill', 'Accent fill (sodium amber)', 'The primary button fill (Log result, Register on &lt;domain&gt;). With the ink, at most two amber uses per screen.', 'Not on finish times, chips, filter chips, links, focus rings, icons in content, or state messages.', 'Hierarchy rule 1: accent is scarce · Taste: a high-contrast accent (round 1 Direction 3)'),
    ('accent-ink', 'Accent ink', 'Amber as text and icon on a bar: the bar action (Save, Log result, Apply filters) and the current tab.', 'Anywhere in content.', 'Hierarchy rule 1 · Lesson 8: amber text on a light bar would need a darker amber than the fill, so the ink is its own role'),
    ('accent-hover', 'Accent, hover', 'The fill under the pointer.', 'Anywhere at rest; never as text (that is the ink’s hover).', 'Hierarchy rule 3: one primary, with a hover state'),
    ('accent-ink-hover', 'Accent ink, hover', 'The bar action (Save, Log result) under the pointer.', 'Anywhere at rest; never as a fill.', 'Step 5, the theme test: split from Accent, hover. In light the fill’s hover keeps dark text while the ink’s hover is text on a light bar, so one value couldn’t serve both'),
    ('on-accent-fill', 'On accent fill', 'Text and icons on the accent fill. The same primitive as the page.', 'Anywhere else.', f'Contrast: {cr(tok("on-accent-fill"), tok("accent-fill")):.2f}:1 on the accent'),
    ('error', 'Error (soft coral)', 'Error titles and icons: "Couldn’t load races". The invalid field ring (inside the field) and destructive text (Sign out), which were <code>--invalid</code> and <code>--destructive</code> until Lesson 8.', 'Not for emphasis, never as a fill for a whole card, never on a focused-only field (focus is the Text primary ring outside).', 'Taste: no aggressive red (not the #FF4D2E family) · Kit feedback (designer, 2026-10-19): invalid and focus never look alike · HIG Alerts: destructive style'),
    ('error-surface', 'Error surface', 'Behind an error message.', 'Not behind a card or a field.', 'States: color second, after icon and text'),
    ('success', 'Success', 'The status specimen on this stand only. No product screen uses it: the saved confirmation is neutral (Color rule 2).', 'Not on a result, not on Results list at all, not for "verified" or any claim about a result.', 'Voice principle 1: claim only what Onrace can know'),
    ('success-bg', 'Success tint', 'The status specimen on this stand only.', 'Not behind results, proof lines or the saved confirmation.', 'Voice principle 1: no verified look'),
    ('warning', 'Warning (no hue)', 'Icon plus text on a raised surface with an outline. No warning state exists in the wireframes yet.', 'No amber or yellow: every warm candidate is within ΔE 7.7–13 of the accent and would read as an action.', 'Hierarchy rule 1: keep the accent the only warm hue'),
    ('warning-bg', 'Warning surface', 'Behind a warning: the raised level.', 'Not a tint of any hue.', 'Hierarchy rule 1'),
    ('warning-line', 'Warning outline', 'Around a warning, so it differs from a secondary button.', 'Not around cards.', 'States need a shape cue when they have no hue'),
]
color_trs = ''.join(f'<tr><td>{sw(t)}{n}<br><code>--{t}</code> {tok(t)}{"<br>light: " + tok(t, "light") if t in LIGHT_DEF else ""}</td><td>{u}</td><td>{nu}</td><td>{w}</td></tr>' for t, n, u, nu, w in COLOR_ROWS)
COLOR_TABLE = wrap('Color roles', f'<table class="spec"><thead><tr><th>Role</th><th>Used</th><th>Not used</th><th>Why</th></tr></thead><tbody>{color_trs}</tbody></table>')
# level 1: the color primitives, named by hue and L*, each with the roles built on it (read from tokens/tokens.css)
_LEVELS = TOKENS.split('     2. SEMANTIC: color roles\n')   # the section marker inside :root, not the header's mention
assert len(_LEVELS) == 2, 'tokens/tokens.css: the "2. SEMANTIC: color roles" section marker'
_PRIM = re.findall(r'^\s*--((?:graphite|amber|coral)-\d+|black|white|alpha-\d+):\s*([^;]+);\s*/\*\s*(.*?)\s*\*/', _LEVELS[0], flags=re.M)
_SEM = _LEVELS[1]
def _built_on(n):
    dark = [f'<code>--{r}</code>' for r in dict.fromkeys(re.findall(r'^\s*--([a-z0-9-]+):[^;]*var\(--' + re.escape(n) + r'\)', _SEM.split('\n}')[0], flags=re.M))]
    light = [f'<code>--{r}</code> (light)' for r in dict.fromkeys(re.findall(r'^\s*--([a-z0-9-]+):[^;]*var\(--' + re.escape(n) + r'\)', LIGHT, flags=re.M)) if f'<code>--{r}</code>' not in dark]
    return ', '.join(dark + light) or 'None'
prim_trs = ''.join(f'<tr><td>{"" if n.startswith("alpha") else sw(n)}<code>--{n}</code> {v.strip()}</td><td>{c}</td><td>{_built_on(n)}</td></tr>' for n, v, c in _PRIM)
PRIM_TABLE = wrap('Color primitives', f'<table class="spec"><thead><tr><th>Primitive</th><th>L* · DESIGN.md name</th><th>Roles built on it</th></tr></thead><tbody>{prim_trs}</tbody></table>')

# ---------------------------------------------------------------- type rows
TYPE_ROWS = [
    ('size-title', 'display', 'Discover', 'Screen title (level 1) · HIG Large Title', 'Hierarchy rule 4 · Taste: Nike Run Club, bold but refined · C3: 38 → 34 (designer, 2026-10-18)'),
    ('size-time', 'display', '1:18:42', 'Finish time, the loudest thing on the row', 'Attribute a · Hierarchy rule 5'),
    ('size-time-hero', 'display', '1:18:42', 'The finish time leading Result detail, the largest thing on the screen', 'Attribute a: the time is what the screen proves (designer, step 6, #11)'),
    ('size-day', 'display', '27', 'Date day, the first thing read on a race card', 'Attribute b: a calendar, not a poster'),
    ('size-initials', 'display', 'JM', 'Profile initials (split from <code>--size-day</code>, Lesson 8: same value, an avatar letter and a date figure can change apart)', 'Kit feedback (designer, 2026-10-19): iOS avatars'),
    ('size-item', 'text-strong', 'HYROX London', 'Item title (level 2): race name', 'Hierarchy rule 4'),
    ('size-body', 'text', 'Registration and payment happen on hyrox.com.', 'Body text, primary and secondary buttons, search', 'Voice principle 3: plain words'),
    ('size-meta', 'text-2', 'London, UK', 'Meta (level 3): location, counts; tertiary text links · HIG Subheadline', 'Hierarchy rule 4 · C3: 14 → 15, apart from body by color (designer, 2026-10-18)'),
    ('size-proof', 'text-2', 'Self-reported · via results.hyrox.com', 'Proof line, month and year under the day', 'Attribute d: proof stated, not stamped'),
    ('size-label', 'label', 'Half marathon', 'Format chip (uppercase by CSS), tab label', 'Decision A: markup keeps the name, CSS uppercases'),
]
TYPE_CLASS = {'size-title': 'type-sample--display type-sample--title', 'size-time': 'type-sample--display type-sample--time', 'size-time-hero': 'type-sample--display type-sample--time-hero',
              'size-day': 'type-sample--display type-sample--day', 'size-initials': 'type-sample--display type-sample--day', 'size-item': 'type-sample--item', 'size-body': 'type-sample--body',
              'size-meta': 'type-sample--meta', 'size-proof': 'type-sample--proof'}
def type_sample(kind, text, t):
    if kind == 'label':
        return f'<span class="sport-tag">{text}</span>'
    return f'<span class="type-sample {TYPE_CLASS[t]}">{text}</span>'
type_trs = ''.join(f'<tr><td><code>--{t}</code> {px(t)} at the default text size<br>{"Schibsted Grotesk 800" if k == "display" else "Hanken Grotesk"}</td><td>{type_sample(k, x, t)}</td><td>{lvl}</td><td>{w}</td></tr>' for t, k, x, lvl, w in TYPE_ROWS)

# ---------------------------------------------------------------- shape rows
SPACE_USE = {1: 'Icon to label, title to chip, tile padding sides', 2: 'Card inset around the photo, chip padding, button icon gap',
             3: 'Date column to text column, row gaps, tile padding top and bottom', 4: 'Result row sides, section stacks',
             5: 'Button sides, stand panels', 6: 'Between stand blocks; tab bar bottom (home indicator)', 7: 'Reserved: screen sections',
             8: 'Stand page top', 9: 'Between stand sections'}
SPACE = ''.join(f'<tr><td><code>--space-{i}</code> {tok(f"space-{i}")}</td><td><span class="space-bar space-bar--{i}"></span></td><td>{SPACE_USE[i]}</td></tr>' for i in range(1, 10))
METRICS = [('chip-height', 'Format chip height', 'Metadata stays small beside the 17px title', 'Hierarchy rule 2'),
           ('filter-chip-height', 'Active filter chip height (44px tap area via ::after)', 'Removable, so a bigger target than the metadata chip', 'Critique fix: touch targets'),
           ('date-col', 'Date column width', 'Fits "Sep 2026" on one line under the day', 'Attribute b: the date leads'),
           ('type-root', 'Type root: the text size one rem stands for', '16 in browsers, 17 on iOS, where the root takes <code>-apple-system-body</code>', 'G28: sizes follow the system text size (Dynamic Type on iOS, the browser’s text size elsewhere)'),
           ('type-unit', 'One type unit: 1px at the default text size', 'Every <code>--size-*</code> and the date column are a number of these', 'G28: text grows to 200% with the system setting, layout keeps its ratios'),
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
           ('ease-out', 'Easing for hover and press', 'Fast start, soft stop', 'Attribute e: intense, not jittery'),
           ('stand-max', 'Stand page width (stand only)', 'Never used in the product', 'Stand layout'),
           ('phone-width', 'Phone frame on the stand (stand only)', '390px screen + border', 'Stand layout'),
           ('dur-fast', 'Hover and press transitions', 'Quick, ease-out; 0ms under prefers-reduced-motion', 'Attribute e: intense, not jittery · WCAG 2.3.3: motion can be turned off'),
           ('dur-sheet', 'Filters sheet slides up, backdrop fades in', 'Long enough to read as a sheet arriving from below; 0ms under prefers-reduced-motion', 'Wireframe conventions: modal sheets · WCAG 2.3.3'),
           ('font-display', 'Display face: screen title, finish time, date day', 'Schibsted Grotesk 800, Hanken as fallback', 'Taste: Nike Run Club, bold but refined'),
           ('font-text', 'Text face: everything else', 'Hanken Grotesk 400 and 600 (the only weights loaded)', 'Taste: no single heavy condensed face for everything'),
           ('font-mono', 'Code samples on this stand only', 'System monospace, nothing to load', 'Stand layout: never in the product'),
           ('hidden-size', 'Visually hidden text for screen readers', '1px box, clipped', 'voice.md → Loading: “Loading races…” is read, not shown'),
           ('screen-w', 'Screen pages: the page width inside the viewer', 'iPhone logical width', 'Wireframe conventions: iOS-structured, 390pt'),
           ('tabbar-h', 'Tab bar capsule height on the screen pages', '44px targets + 26px icon + label', 'Wireframe conventions: iOS chrome · Critique fix: 44px targets'),
           ('tabbar-inset', 'Floating tab bar: in from the screen edges', 'The 16px gutter (HIG gives no number)', 'G1: on iOS the tab bar floats above content'),
           ('tabbar-gap', 'Floating tab bar: above the bottom safe area', '8px', 'G1, G2'),
           ('radius-tabbar', 'Floating tab bar corners', 'Half its height: a capsule', 'G1 · C7: shapes in the bar chrome are concentric capsules'),
           ('tabbar-clear', 'Scroll padding under the content', 'Bar + gap + safe area: content runs under the glass, the last item still scrolls clear', 'G1: content shows through beneath the tab bar'),
           ('safe-top', 'Top safe area (status bar, Dynamic Island)', 'env(safe-area-inset-top), 0 inside the viewer', 'G6: respect the top safe area'),
           ('safe-bottom', 'Home-indicator inset under the tab bar and the sheet’s buttons', 'env(safe-area-inset-bottom), 0 inside the viewer', 'G2: buttons stay above the home indicator'),
           ('size-time-hero-cap', 'Result detail: the most the leading finish time may grow to', '22% of the screen width', 'Step 7, #2: at 200% text the 56px time would outgrow the screen'),
           ('sheet-gap-top', 'Filters sheet: space left above the large detent', f'12px below the top safe area · {P}', 'G13: the sheet rests at its detent'),
           ('z-under', 'Stacking: behind its own box (the map\'s land and borders)', 'Lowest of the stacking scale', 'Step 6, #37: one scale, no bare z-index in a class'),
           ('z-lift', 'Stacking: above its siblings (map contents, bar buttons over the title)', 'One step up', 'Step 6, #37'),
           ('z-float', 'Stacking: the sticky top bar, map pins', 'Floats over content', 'Step 6, #37'),
           ('z-bar', 'Stacking: tab bar, action bar, a tab screen\'s top bar, a gate\'s bar', 'Bars over the page', 'Step 6, #37'),
           ('z-edge', 'Stacking: the status-bar scroll edge', 'Over every bar', 'Step 6, #37'),
           ('z-scrim', 'Stacking: the dimming layer under a sheet', 'Under the sheet, over the bars', 'Step 6, #37'),
           ('z-sheet', 'Stacking: sheets, alerts, action sheets', 'Highest', 'Step 6, #37'),
           ('sheet-large', 'Filters sheet height: the large detent only', 'Full height less the top safe area and the gap', 'G13 · designer, 2026-10-19: large detent only'),
           ('alpha-85', 'Glass fill on bars (tab bar, top bar, controls bar, status-bar edge); was --glass-opacity', f'Lowest that passes AA over the worst case: {max(GLASS_MIN["bar"], GLASS_MIN["ground"])}%; set with margin. Above HIG’s {HIG_DIM}% dimming layer for clear glass over bright content (HIG Materials, the one Apple number) · {P}', 'C1: glass for bars, in Podium tones · contrast checked below'),
           ('alpha-90', 'Glass fill on the Filters sheet; was --glass-opacity-sheet', f'Lowest that passes AA over the scrim and the worst case: {GLASS_MIN["sheet"]}%; set with margin · {P}', 'C1, C4: the sheet on the raised level'),
           ('glass-bar', 'Tab bar and action bar glass: the Tab bar level at the glass opacity', 'color-mix with transparent; the floating tab bar and the sticky action bar (Race detail, Result detail) stay a shade darker than the page', 'C1: translucent graphite · action bar added by the designer, 2026-10-19'),
           ('glass-ground', 'Glass for bars on the page (controls bar, top bar, status-bar edge): the Ground level at the glass opacity', 'color-mix with transparent; at rest it matches the page, so the bar shows only when content runs under it', 'C1 · G7: a scroll edge, not a custom bar background'),
           ('glass-sheet', 'Sheet glass: Raised level at the sheet opacity', 'color-mix with transparent', 'C1 · C4: the raised graphite level'),
           ('glass-blur', 'Backdrop blur on all glass', f'20px · {P}', 'C1: blur, so content under a bar reads as shape, not text'),
           ('alpha-100', 'Glass under Reduce Transparency: every glass role turns solid', 'The glass roles swap their alpha to 100%', 'C1: Reduce Transparency'),
           ('alpha-8', 'The glass rim’s strength', f'8% · {P}', 'C1, G7'),
           ('alpha-60', 'The scrim’s and the float shadow’s strength', 'Black at 60%', 'Depth comes from levels and one scrim'),
           ('glass-rim', 'The glass rim (in place of a hairline); was --glass-edge', f'Text primary’s primitive at 8% · {P}', 'C1, G7: a scroll edge, not a solid bar border · decorative, no contrast requirement'),
           ('icon-state', 'Icon on top of an empty or error state', '48px, centered above the title', 'Designer, 2026-10-19: the iOS ContentUnavailableView pattern · HIG gives no number'),
           ('dur-spin', 'Busy spinner: one turn', '800ms, linear; keeps turning under reduced motion (HIG: a still indicator reads as stalled)', 'G26'),
           ('spinner-size', 'Busy spinner size', 'Meta icon size, inside the button before its label', 'G26: an activity indicator inside the button'),
           ('ease-in-out', 'Easing for the skeleton pulse', 'Even in, even out', 'C6: a subtle pulse'),
           ('scrim', 'Behind the Filters sheet', 'Black at 60%: the page dims, its colors stay', 'Depth comes from levels and one scrim, not from color · Hierarchy rule 1'),
           ('fade-end', 'Active filter chips row: its end fades out', 'Mask, last 24px', 'Says the row scrolls without a scrollbar · Critique fix: hidden overflow'),
           ('stand-col-min', 'Stand columns (stand only)', 'Narrowest panel before the grid wraps', 'Stand layout'),
           ('leading-box', 'The line box in layout math (the 44pt target offsets, the skeleton proof bar)', '= <code>--leading-body</code>, so they can’t drift', 'Lesson 8: split by use from --leading-body'),
           ('invalid-ring', 'The invalid field ring’s width', '2px, inside the field', 'Split from --focus-ring (Lesson 8): same value, changes apart'),
           ('spinner-stroke', 'The busy spinner’s stroke', '2px', 'Split from --focus-ring (Lesson 8)'),
           ('shadow-y', 'The float shadow: offset down', 'Its color is the role --float-shadow', 'Depth comes from levels; only what floats has a shadow'),
           ('shadow-blur', 'The float shadow: blur', '32px', 'Same'),
           ('shadow-spread', 'The float shadow: spread', '−12px, so it stays under the floating thing', 'Same'),
           ('avatar-size', 'Profile initials', '80px, the iOS profile size, in a circle (<code>--radius-avatar</code>)', 'Kit feedback (designer, 2026-10-19): iOS avatars are circular · DESIGN.md → Shapes, the one circle'),
           ('alert-width', 'The Sign out confirm alert', '270px, the iOS alert width', 'Native iOS (HIG Alerts) · kit, 2026-10-18'),
           ('kit-stage-h', 'Showcase stage for the sheet, the map and the alert (ui/kit.html only)', 'Tall enough for the Filters sheet at its large detent', 'Showcase layout: never in the product')]
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
        ('skel-proof-w', 'Proof line bar width', 'A typical “Self-reported · via …”'),
        ('skel-pulse-dim', 'Skeleton pulse: the low point', 'Opacity 0.55 at mid-breath; still under reduced motion (C6)'),
        ('dur-pulse', 'Skeleton pulse: one breath', '1.6s, so it reads as waiting, not as an alarm (C6, G25)')]
SKEL_TRS = ''.join(f'<tr><td><code>--{t}</code> {tok(t)}</td><td>{u}</td><td>{d}</td><td>voice.md → Loading: the skeleton has the content’s shape · impeccable: no layout shift</td></tr>' for t, u, d in SKEL)
MAP_PINS = [('berlin-marathon', 'Berlin'), ('hyrox-london', 'London'), ('utmb', 'Chamonix'), ('hyrox-dallas', 'Dallas'),
            ('deka-strong-chicago', 'Chicago'), ('spartan-beast-killington', 'Killington'), ('boston-marathon', 'Boston')]
MAP_TRS = ''.join(f'<tr><td><code>--{t}</code> {v}</td><td>{u}</td><td>{w}</td></tr>' for t, v, u, w in [
    ('map-water', f'= <code>--graphite-5</code> {tok("map-water")}', 'Water: the darkest level', 'Hierarchy rule 1: no accent on the map · Color rule 3a levels only'),
    ('map-land', f'= <code>--graphite-12</code> {tok("map-land")}', 'Land: the card surface', 'Color rule 3a'),
    ('map-lines', f'= <code>--graphite-20</code> {tok("map-lines")}', 'Coastlines and borders (decorative)', 'Attribute a: the frame stays quiet'),
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
<tr><td><code>--radius-3</code></td><td>{tok("radius-3")}</td><td>Stand panels only, never in the product. (The Filters sheet had it until step 3b; it now takes <code>--radius-sheet</code>.)</td><td>Keeps the product's shapes at 4 and 6</td></tr>
<tr><td><code>--radius-sheet</code></td><td>{tok("radius-sheet")}</td><td>The Filters sheet's (and Race picker's) top corners. {P}.</td><td>G16 · Native sheet anatomy (designer, 2026-10-18): the system's sheet radius, not a Podium radius</td></tr>
<tr><td><code>--radius-bar-control</code></td><td>{tok("radius-bar-control")} = 22px</td><td>A control inside a bar: the Filters button and the segmented track in the controls bar (Filters added by the designer, 2026-10-19); the search field once it pins to a bar (G8).</td><td>C7: concentric only inside bars; content keeps 4/6</td></tr>
<tr><td><code>--radius-bar-inner</code></td><td>{tok("radius-bar-inner")} = 18px</td><td>A segment inside that track: the outer radius minus the track's 4px padding.</td><td>C7: concentric corners</td></tr>
<tr><td><code>--radius-filter-chip</code></td><td>{tok("radius-filter-chip")} = 16px</td><td>Active filter chips in the controls bar: a capsule, half the 32px chip height.</td><td>C7: a control inside a bar is a capsule (designer, 2026-10-22). Format chips on cards keep 4px</td></tr>
<tr><td><code>--radius-alert</code></td><td>{tok("radius-alert")}</td><td>The confirm alert (Profile, Sign out). {P}.</td><td>G67 (designer, 2026-10-23): the alert as iOS 26 alerts, glass and a larger radius, provisional like the sheet's</td></tr>
<tr><td><code>--radius-avatar</code></td><td>{tok("radius-avatar")}</td><td>Profile initials (a circle); also the busy spinner's ring.</td><td>Kit feedback (designer, 2026-10-19): iOS avatars are circular. The one circle in content (DESIGN.md → Shapes)</td></tr>
<tr><td><code>--border</code></td><td>{tok("border")}</td><td>Hairlines: field outline, dividers.</td><td>Attribute a: the frame stays quiet</td></tr>
<tr><td><code>--focus-ring</code></td><td>{tok("focus-ring")}</td><td>Keyboard focus, in Text primary, never the accent.</td><td>Hierarchy rule 1: focus is not an accent use</td></tr>
<tr><td><code>--float-shadow</code></td><td>{tok("float-shadow")}<div class="shadow-demo">A sheet floats; cards don\'t.</div></td><td>Sheets and menus that float (the Filters sheet). Cards are flat.</td><td>Depth comes from background levels, not shadows · Taste: dark with depth</td></tr>
<tr><td><code>--target</code></td><td>{tok("target")}</td><td>Minimum height of every control or its tap area.</td><td>Critique fix (round 2): touch targets</td></tr>
</tbody></table></div>
<div class="spec-wrap" tabindex="0" role="region" aria-label="Spacing scale"><table class="spec"><thead><tr><th>Spacing scale</th><th>Size</th><th>Used for</th></tr></thead><tbody>{SPACE}</tbody></table></div>
<p class="stand-why"><b>Why:</b> one 4px-based scale for every gap · Hierarchy rule 4: more space between groups than inside them</p>
<div class="spec-wrap" tabindex="0" role="region" aria-label="Component metrics"><table class="spec"><thead><tr><th>Component metric</th><th>Used for</th><th>Sizing</th><th>Why</th></tr></thead><tbody>{METRIC_TRS}</tbody></table></div>
<div class="spec-wrap" tabindex="0" role="region" aria-label="Skeleton sizes"><table class="spec"><thead><tr><th>Skeleton (loading)</th><th>Used for</th><th>Sizing</th><th>Why</th></tr></thead><tbody>{SKEL_TRS}</tbody></table></div>
<div class="spec-wrap" tabindex="0" role="region" aria-label="Map tokens"><table class="spec"><thead><tr><th>Map · <code>tokens/tokens.css</code> (roles, sizes) and <code>ui/map-data.css</code> (generated data, Race browse only)</th><th>Used for</th><th>Why</th></tr></thead><tbody>{MAP_TRS}</tbody></table></div>'''

# ---------------------------------------------------------------- icons
ICON_PLAN = [  # where, Solar name, token (None: inline on the stand or not built yet), use, status
    ('Top bar · back', 'alt-arrow-left-linear', 'icon-back', 'Before the parent screen’s name in a top bar (‹ Discover, ‹ Results, ‹ Log result). Linear, a designer exception for small UI glyphs (step 6, #23).', 'in use'),
    ('Result row · disclosure', 'alt-arrow-right-linear', 'icon-disclosure', 'At the trailing edge of a result row and a navigation row, which drill in (G22, step 3b). Race cards are a collection, so none there. Linear (step 6, #23).', 'in use'),
    ('Tab bar', 'compass', 'icon-compass', 'Discover', 'in use'), ('Tab bar', 'stopwatch', 'icon-stopwatch', 'Results', 'in use'), ('Tab bar', 'user', 'icon-user', 'Profile', 'in use'),
    ('Date pills', None, None, 'No glyph: the formatted value on the pill is the cue, as iOS’s compact date picker (step 6, #26; the Solar calendar it used is gone).', 'none'),
    ('Card meta · location', 'map-point', 'icon-pin', 'Before the city on every race card (CSS mask, no markup change).', 'in use'),
    ('Format chip', None, None, 'No icon and no dot: the same neutral chip for every format (dot option dropped 2026-10-13).', 'none'),
    ('Proof line', 'link-round', 'icon-link', 'One link icon before "Self-reported · via …" (Hierarchy rule 6).', 'in use'),
    ('Search field', 'magnifer-linear', 'icon-search-field', 'Inside the field, Text 2. Linear (step 6, #23).', 'in use'),
    ('Button · primary', 'add-circle', None, 'Log result.', 'in use'),
    ('Button · external', 'arrow-right-up', None, 'Register on &lt;domain&gt;, Open official result: the arrow says it leaves Onrace (voice principle 2).', 'in use'),
    ('Button · secondary', 'tuning-2', 'icon-filters', 'Filters, before the label (CSS mask, no markup change).', 'in use'),
    ('Pop-up rows', 'alt-arrow-down-linear', 'icon-chevron', 'After the value of a row that opens a menu (Region, Sport type, Country, Language; G65). Linear (step 6, #23).', 'in use'),
    ('Filters sheet · checkbox', 'check', 'icon-check', 'The tick in a checked sport type, on Text 1 (neutral, never the accent).', 'in use'),
    ('Filter chip · remove', 'close-circle', 'icon-close', 'Drawn by CSS over the chip’s text "×" (step 7); the text stays in the markup, aria-hidden, until Lesson 7.', 'in use'),
    ('State · empty, Race browse', 'magnifer', 'icon-search', 'On top of the empty state (“No races match…”), 48px, Text 2: iOS’s own search-unavailable pattern (designer, 2026-10-19: ContentUnavailableView).', 'in use'),
    ('Race browse · Sort', 'sort-vertical', 'icon-sort', 'After the current order on the Sort button (“Soonest first”), which flips it (G21; markup pass, 2026-10-23).', 'in use'),
    ('State · empty, Results list', 'archive', 'icon-archive', 'On top of “No results logged yet”, 48px, Text 2: the results archive (designer, 2026-10-19).', 'in use'),
    ('State · error', 'danger-circle', 'icon-error', 'On top of an error state (“Couldn’t load races”), 48px, the screen’s only coral (since 2026-10-19; before, 18px before the heading). Still 18px before headings in inline errors and form alerts.', 'in use'),
    ('Saved confirmation', 'diskette', 'icon-saved', 'Results list after Save, in Text 2: neutral, not a success check (Color rule 2).', 'in use'),
    ('State · success', 'check-circle', None, 'This stand’s success specimen only; no product screen uses it.', 'specimen'),
    ('State · warning', 'danger-triangle', None, 'Warning messages, when one exists.', 'planned'),
    ('State · loading', None, None, 'No icon and no spinner: skeleton cards, pulsing subtly (C6), plus "Loading races…" for screen readers (voice.md → Loading). A busy button draws its own CSS spinner (G26).', 'none'),
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
<link rel="stylesheet" href="../tokens/tokens.css?v={CSS_V}">
<link rel="stylesheet" href="../components/index.css?v={CSS_V}">
<link rel="stylesheet" href="specimens.css?v={CSS_V}">
<link rel="stylesheet" href="stand.css?v={CSS_V}">
</head>
<body class="onrace">
<main class="stand">

  <header class="stand-head">
    <h1>Onrace concept · Podium</h1>
    <p>Direction A, chosen 2026-10-13 (<code>concept.md</code> → Directions). Every value on this page comes from <code>tokens/tokens.css</code> and every product component from <code>components/</code> (since Lesson 8); the specimens no screen uses (the <code>.btn</code> family, status messages) from <code>specimens.css</code>; the stand's own layout from <code>stand.css</code>. The page itself holds no style values. Each decision below is signed with its reason: an attribute (a–e), the designer's taste, or a hierarchy rule. The full comparison is in <a class="stand-link" href="directions.html">directions.html</a>.</p>
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
    <p>Two levels (Lesson 8): primitives hold the values, named by hue and lightness; roles say what a color is for, and the components read only roles.</p>
    {PRIM_TABLE}
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
        <p>Source: our own generated illustrations of each format (ChatGPT image generation, checked and retouched; <code>visuals/README.md</code>), not photos taken at the named race. Until Lesson 7 step 4 they were Unsplash photos, logged in <code>references.md</code> → Photos.</p>
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
        <p class="stand-label">Try it: hover shows a stronger outline; focus shows the 2px Text 1 ring. The outline is Boundary ({cr(tok('boundary'), tok('surface')):.2f}:1 on the field), the placeholder Text secondary ({cr(tok('text-secondary'), tok('surface')):.2f}:1).</p>
        {why("Hierarchy rule 3: not a button, so it sits on the surface, not raised", "jtbd.md → Hypothesis 7 [?]: search by race name or city")}
      </div>
    </div>
  </section>

  <section class="stand-section" id="race-browse-parts" aria-labelledby="rb-h">
    <h2 id="rb-h">Race browse parts, live</h2>
    <p>Everything Race browse needs besides the card, in the wireframes' own markup and copy, styled only from <code>tokens/tokens.css</code> and <code>components/index.css</code>, the files the screen links.</p>
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
        {why("voice.md → Loading: a skeleton plus “Loading races…” for screen readers; no spinner, no invented progress", "Race card anatomy (designer): the skeleton has the card's shape: photo band, date tile, title, chip, location", "C6: a subtle pulse, still under reduced motion; no shimmer")}
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
    <h3 class="stand-label">Step 3b (2026-10-19): content runs under the floating glass tab bar</h3>
    {wrap('First screen after step 3b', '<table class="spec"><thead><tr><th>Where</th><th>Page height</th><th>List starts at</th><th>Tab bar top</th><th>Clear of the bar</th><th>On screen, through the glass</th></tr></thead><tbody>'
      + ''.join(f'<tr><td>{w}</td><td class="num">{h}px</td><td class="num">{t}px</td><td class="num">{tb}px</td><td class="num">{c[0]} full + {c[1]}%{f", {c[2]}px to spare" if c[2] is not None else ""}</td><td class="num">{o[0]} full + {o[1]}%</td></tr>' for w, h, t, tb, c, o in FS_3B) + '</tbody></table>')}
    <p class="stand-why"><b>Step 3b:</b> the race card is 216px (the C3 meta line); the floating bar's top sits 8px higher than the old bar's, and the title is 4px shorter. Attribute b still holds inside the viewer, two full cards clear of the bar, but with 1.7px to spare (9.7px with C3 alone). Under the glass a third card shows through.</p>
    <p class="stand-why"><b>Why (attribute b, a calendar, not a poster):</b> two full races on the first screen with no filters, so the list reads as a run of dates rather than one poster per screen. With two filters on, the chips row costs one card's worth of the second race (1 full + 79%).</p>
  </section>
{rules_section()}
{decisions_section()}
  <section class="stand-section" aria-labelledby="contrast-h">
    <h2 id="contrast-h">Contrast · every text pair and the key non-text pairs</h2>
    <p>Generated by <code>scripts/concept/build_stand.py</code> from the hex values in <code>tokens/tokens.css</code> (WCAG 2 relative luminance); the build stops if a text pair fails. Body text needs 4.5:1; non-text UI (focus ring, outlines) needs 3:1.</p>
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
# Every token is signed: each one defined in tokens/tokens.css, ui/map-data.css or the docs layer appears on the stand with its reason
_defined = set(re.findall(r'(?:^|;)\s*--([a-z0-9-]+):', TOK, flags=re.M))
_unsigned = sorted(n for n in _defined if not re.search(r'--' + re.escape(n) + r'(?![a-z0-9-])', page))
assert not _unsigned, ('Unsigned tokens (add a row with its reason)', _unsigned)
print('Signed tokens:', len(_defined), 'of', len(_defined))
open(os.path.join(ROOT, 'concept/concept.html'), 'w').write(page)
print('pairs', len(PAIRS), 'min text ratio', min(cr(tok(f), tok(b)) for _, f, b, k in PAIRS if k == 'text'))
# Horizontal overflow (2026-10-24): every wireframe page and state at 390 and 320 wide, Race browse with 0-5 active
# filters (scripts/check_overflow.mjs, headless Chrome, over local HTTP with the real fonts; since 2026-10-25 it also
# fails on a wrapped one-line control or a font that didn't load). The build stops on any overflow; it is skipped, with a
# message, only when Node or Chrome is missing.
import subprocess, shutil
_node = shutil.which('node')
if not _node:
    print('check_overflow: SKIPPED, node not found')
else:
    _r = subprocess.run([_node, os.path.join(ROOT, 'scripts/check_overflow.mjs'), '--quiet'], capture_output=True, text=True)
    print(_r.stdout.strip() or _r.stderr.strip())
    if _r.returncode == 2: print('check_overflow: SKIPPED, Chrome not available')
    elif _r.returncode != 0: sys.exit('check_overflow failed (overflow, a wrapped one-line control, or a font not loaded): the build stops')
# mirror to public/ (GitHub Pages serves public/)
for _f in ['concept/concept.html', 'concept/stand.css', 'concept/specimens.css', 'concept/first-screen.html', 'concept/first-screen.css', 'ui/kit-doc.css', 'ui/kit.html', 'ui/shell.html', 'tokens/tokens.css', 'tokens/theme.js', 'components/index.css', 'ui/map-data.css'] + STAMPED[3:]:
    if os.path.exists(os.path.join(ROOT, _f)):
        os.makedirs(os.path.dirname(os.path.join(ROOT, 'public', _f)), exist_ok=True)
        shutil.copyfile(os.path.join(ROOT, _f), os.path.join(ROOT, 'public', _f))
shutil.copytree(os.path.join(ROOT, 'ui/review-3b'), os.path.join(ROOT, 'public/ui/review-3b'), dirs_exist_ok=True)   # step 3b before/after shots
shutil.copyfile(os.path.join(ROOT, 'ui/review-3b.html'), os.path.join(ROOT, 'public/ui/review-3b.html'))
shutil.copytree(os.path.join(ROOT, 'ui/review-step5'), os.path.join(ROOT, 'public/ui/review-step5'), dirs_exist_ok=True)   # step 5 before/after and group shots
shutil.copyfile(os.path.join(ROOT, 'ui/review-step5.html'), os.path.join(ROOT, 'public/ui/review-step5.html'))
shutil.copytree(os.path.join(ROOT, 'ui/review-markup'), os.path.join(ROOT, 'public/ui/review-markup'), dirs_exist_ok=True)   # markup pass before/after
shutil.copyfile(os.path.join(ROOT, 'ui/review-markup.html'), os.path.join(ROOT, 'public/ui/review-markup.html'))
shutil.copytree(os.path.join(ROOT, 'ui/review-markup-2'), os.path.join(ROOT, 'public/ui/review-markup-2'), dirs_exist_ok=True)   # markup pass round 2
shutil.copyfile(os.path.join(ROOT, 'ui/review-markup-2.html'), os.path.join(ROOT, 'public/ui/review-markup-2.html'))
shutil.copytree(os.path.join(ROOT, 'ui/review-overflow'), os.path.join(ROOT, 'public/ui/review-overflow'), dirs_exist_ok=True)   # overflow fix before/after
shutil.copyfile(os.path.join(ROOT, 'ui/review-overflow.html'), os.path.join(ROOT, 'public/ui/review-overflow.html'))
shutil.copytree(os.path.join(ROOT, 'ui/review-step6'), os.path.join(ROOT, 'public/ui/review-step6'), dirs_exist_ok=True)   # step 6 critique fixes before/after
shutil.copyfile(os.path.join(ROOT, 'ui/review-step6.html'), os.path.join(ROOT, 'public/ui/review-step6.html'))
shutil.copytree(os.path.join(ROOT, 'ui/review-step7'), os.path.join(ROOT, 'public/ui/review-step7'), dirs_exist_ok=True)   # step 7 final check before/after
shutil.copyfile(os.path.join(ROOT, 'ui/review-step7.html'), os.path.join(ROOT, 'public/ui/review-step7.html'))
shutil.copytree(os.path.join(ROOT, 'ui/review-lessons'), os.path.join(ROOT, 'public/ui/review-lessons'), dirs_exist_ok=True)   # lesson pages and kit showcase before/after (2026-10-26)
shutil.copyfile(os.path.join(ROOT, 'ui/review-lessons.html'), os.path.join(ROOT, 'public/ui/review-lessons.html'))
shutil.copytree(os.path.join(ROOT, 'ui/review-overviews'), os.path.join(ROOT, 'public/ui/review-overviews'), dirs_exist_ok=True)   # the overviews restructured (2026-10-26)
shutil.copyfile(os.path.join(ROOT, 'ui/review-overviews.html'), os.path.join(ROOT, 'public/ui/review-overviews.html'))
shutil.copytree(os.path.join(ROOT, 'ui/review-kit-sheet'), os.path.join(ROOT, 'public/ui/review-kit-sheet'), dirs_exist_ok=True)   # the kit as a component sheet (2026-10-26)
shutil.copyfile(os.path.join(ROOT, 'ui/review-kit-sheet.html'), os.path.join(ROOT, 'public/ui/review-kit-sheet.html'))
shutil.copytree(os.path.join(ROOT, 'ui/review-theme'), os.path.join(ROOT, 'public/ui/review-theme'), dirs_exist_ok=True)   # step 5: every state in both themes (Lesson 8)
shutil.copyfile(os.path.join(ROOT, 'ui/review-theme.html'), os.path.join(ROOT, 'public/ui/review-theme.html'))
for _f in ['visuals/review-round3.html']:   # the photos' round 3 review, linked from the Lesson 7 overview
    shutil.copyfile(os.path.join(ROOT, _f), os.path.join(ROOT, 'public', _f))
import glob
# the wireframes' published docs: the rulebooks and notes (wireframes/*.md: _conventions.md, _screens.md, _critique.md,
# README.md) and the viewer's index.html, so an edit needs no manual copy. The frozen _wireframe/ snapshot is never
# touched by the build (_conventions.md § 6).
_docs = sorted(glob.glob(os.path.join(ROOT, 'wireframes', '*.md'))) + [os.path.join(ROOT, 'wireframes', 'index.html')]
for _d in _docs:
    shutil.copyfile(_d, os.path.join(ROOT, 'public', 'wireframes', os.path.basename(_d)))
shutil.copyfile(os.path.join(ROOT, 'ia.html'), os.path.join(ROOT, 'public/ia.html'))   # the IA page: the published copy is always the source (2026-10-25)
print('mirrored wireframes docs:', ', '.join(os.path.basename(d) for d in _docs))
import glob   # our own photos (visuals/*.jpg), linked by the screens as ../visuals/<file>
os.makedirs(os.path.join(ROOT, 'public/visuals'), exist_ok=True)
for _v in [f for e in ('jpg', 'webp', 'avif') for f in glob.glob(os.path.join(ROOT, f'visuals/*.{e}'))]:   # the pre-cropped responsive sets too (step 7, #5)
    shutil.copyfile(_v, os.path.join(ROOT, 'public/visuals', os.path.basename(_v)))
print('mirrored to public/')
# every page links only files that exist (Lesson 8 step 4): a page still linking a deleted file stops the build
_l = subprocess.run([sys.executable, os.path.join(ROOT, 'scripts/check_links.py')], capture_output=True, text=True)
print(_l.stdout.strip())
if _l.returncode: sys.exit('check_links failed: a page links a file that does not exist; the build stops')
# the lesson overviews (06 and 07, scripts/lesson_page.py) carry the kit's counts: rebuilt with it
subprocess.run([sys.executable, os.path.join(ROOT, 'scripts/build_ui_overview.py')], check=True)
