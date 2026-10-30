"""Regenerate DESIGN.md's frontmatter values and .impeccable/design.json (the impeccable sidecar) from tokens/tokens.css.

Usage, from the repo root:  python3 scripts/build_design_sidecar.py      (build_stand.py runs it on every build)
Lesson 8 step 4: hex values live in one file, tokens/tokens.css. This script first rewrites, in DESIGN.md:
  - the frontmatter's colors (every semantic role, resolved), typography (each style from its tokens), rounded and
    spacing; the components block is hand-written and only references these by name;
  - the hex in each Colors bullet (`#RRGGBB`, `--role`), from that role.
Then the sidecar. It follows impeccable's document reference, schemaVersion 2: the sidecar carries only
what DESIGN.md's frontmatter can't (color display names, roles, OKLCH and tonal
ramps; type purposes; shadows; motion; breakpoints; component snippets; the
narrative, quoted verbatim). Everything is read from DESIGN.md, except:
  - motion and shadow values, read from tokens/tokens.css (DESIGN.md names them in prose only);
  - component snippets: kept from the current sidecar, and replaced by COMPONENTS
    below where the kit has changed since (step 3b and its review, 2026-10-19).
Re-run it after every DESIGN.md change."""
import json, math, os, re, datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TOKENS = open(os.path.join(ROOT, 'tokens/tokens.css')).read()
DOCS = open(os.path.join(ROOT, 'concept/stand.css')).read()   # --radius-3, a docs-layer token DESIGN.md lists
_DEF = {}
for _src in (re.search(r':root\s*\{(.*?)\n\}', TOKENS, flags=re.S).group(1), re.search(r':root\s*\{(.*?)\n\}', DOCS, flags=re.S).group(1)):
    for _n, _v in re.findall(r'(?:^|;)\s*--([a-z0-9-]+):\s*([^;]+);', re.sub(r'/\*.*?\*/', '', _src, flags=re.S), flags=re.M):   # comments out first: they quote old values
        _DEF.setdefault(_n, _v.strip())
def raw(n): return _DEF[n]
def resolve(n):
    """A token's value with every var() replaced: '#RRGGBB', 'color-mix(in srgb, #0F1114 85%, transparent)', '34px'…"""
    v = re.sub(r'var\(--([a-z0-9-]+)\)', lambda m: resolve(m.group(1)), raw(n))
    v = re.sub(r'#([0-9A-Fa-f]{3})\b', lambda m: '#' + ''.join(c * 2 for c in m.group(1)), v)   # #000 → #000000
    c = re.fullmatch(r'calc\((.*)\)', v)
    if c:   # simple px arithmetic: the type sizes (n × 1rem/16 at the default size) and the capsule radii
        e = c.group(1).replace('calc', '').replace('1rem', '16').replace('px', '')
        if re.fullmatch(r'[\d\s.+\-*/()]+', e): v = f'{eval(e):g}px'
    return v

# ---------------------------------------------------------------- DESIGN.md's frontmatter values, from the tokens
MD_PATH = os.path.join(ROOT, 'DESIGN.md')
MD = open(MD_PATH).read()
_sem = re.search(r':root\s*\{(.*?)\n\}', TOKENS, flags=re.S).group(1).split('     2. SEMANTIC: color roles\n')[1]   # the main :root only, not the overrides
ROLES = [n for n in re.findall(r'^\s*--([a-z0-9-]+):', _sem, flags=re.M) if n != 'float-shadow']   # a shadow, not a color
TYPE = {   # style: font, size, weight, line height, tracking (DESIGN.md → Typography)
    'title': ('font-display', 'size-title', 'weight-display', 'leading-tight', 'tracking-display'),
    'finish-time': ('font-display', 'size-time', 'weight-display', 'leading-tight', 'tracking-display'),
    'date-day': ('font-display', 'size-day', 'weight-display', 'leading-tight', 'tracking-display'),
    'item': ('font-text', 'size-item', 'weight-strong', 'leading-item', None),
    'body': ('font-text', 'size-body', 'weight-regular', 'leading-body', None),
    'button': ('font-text', 'size-body', 'weight-strong', 'leading-tight', None),
    'meta': ('font-text', 'size-meta', 'weight-regular', 'leading-body', None),
    'proof': ('font-text', 'size-proof', 'weight-regular', 'leading-body', None),
    'label': ('font-text', 'size-label', 'weight-strong', 'leading-tight', 'tracking-label'),
    'tab-label': ('font-text', 'size-label', 'weight-strong', 'leading-body', None),
}
ROUNDED = ['radius-1', 'radius-2', 'radius-3', 'radius-sheet', 'radius-bar-control', 'radius-bar-inner', 'radius-circle', 'radius-filter-chip', 'radius-alert', 'radius-tabbar']
fm_lines = ['colors:'] + [f'  {n}: "{resolve(n)}"' for n in ROLES] + ['typography:']
for t, (f, z, w, l, tr) in TYPE.items():
    fm_lines += [f'  {t}:', f'    fontFamily: "{resolve(f).replace(chr(34), "")}"', f'    fontSize: "{resolve(z)}"', f'    fontWeight: {resolve(w)}', f'    lineHeight: {resolve(l)}']
    if tr: fm_lines.append(f'    letterSpacing: "{resolve(tr)}"')
fm_lines += ['rounded:'] + [f'  {n}: "{resolve(n)}"' for n in ROUNDED] + ['spacing:'] + [f'  space-{i}: "{resolve(f"space-{i}")}"' for i in range(1, 10)]
_gen = '\n'.join(fm_lines) + '\n'
_m = re.search(r'^colors:\n.*?(?=^components:\n)', MD, flags=re.S | re.M)
assert _m, 'DESIGN.md: frontmatter colors … spacing before components'
MD = MD[:_m.start()] + _gen + MD[_m.end():]
_refs = set(re.findall(r'\{colors\.([a-z0-9-]+)\}', MD))
assert _refs <= set(ROLES), ('DESIGN.md components reference colors tokens/tokens.css lacks', _refs - set(ROLES))
# the Colors bullets: **Name** (`#RRGGBB`, `--role` …) take the role's hex
def _bullet(m):
    v = resolve(m.group(2)); return f'(`{v}`, `--{m.group(2)}`' if re.fullmatch(r'#[0-9A-F]{6}', v, flags=re.I) else m.group(0)
MD = re.sub(r'\(`(#[0-9A-Fa-f]{6})`, `--([a-z0-9-]+)`', _bullet, MD)
open(MD_PATH, 'w').write(MD)
OUT = os.path.join(ROOT, '.impeccable/design.json')
OLD = json.load(open(OUT)) if os.path.exists(OUT) else {}

# ---------------------------------------------------------------- frontmatter (two levels deep is all DESIGN.md uses)
fm = re.match(r'^---\n(.*?)\n---\n', MD, flags=re.S).group(1)
FM, top, sub = {}, None, None
for line in fm.split('\n'):
    if not line.strip():
        continue
    ind = len(line) - len(line.lstrip())
    k, _, v = line.strip().partition(':')
    v = v.strip().strip('"')
    if ind == 0:
        top = k; FM[top] = v if v else {}
    elif ind == 2:
        sub = k; FM[top][sub] = v if v else {}
    else:
        FM[top][sub][k] = v
body = MD[MD.index('\n---\n', 4) + 5:]

def section(title):
    m = re.search(r'^## ' + re.escape(title) + r'\n(.*?)(?=^## |\Z)', body, flags=re.M | re.S)
    return m.group(1) if m else ''

# ---------------------------------------------------------------- color: names from the prose bullets, OKLCH, ramps
def lin(c): return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
def delin(c): return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055
def to_oklch(h):
    r, g, b = [lin(int(h[i:i + 2], 16) / 255) for i in (1, 3, 5)]
    l = (0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b) ** (1 / 3)
    m = (0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b) ** (1 / 3)
    s = (0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b) ** (1 / 3)
    L = 0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s
    A = 1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s
    B = 0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s
    return L, math.hypot(A, B), math.degrees(math.atan2(B, A)) % 360
def from_oklch(L, C, H):
    A, B = C * math.cos(math.radians(H)), C * math.sin(math.radians(H))
    l = (L + 0.3963377774 * A + 0.2158037573 * B) ** 3
    m = (L - 0.1055613458 * A - 0.0638541728 * B) ** 3
    s = (L - 0.0894841775 * A - 1.2914855480 * B) ** 3
    rgb = [4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
           -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
           -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s]
    if any(c < -1e-4 or c > 1 + 1e-4 for c in rgb):
        return None
    return '#' + ''.join(f'{round(min(1, max(0, delin(min(1, max(0, c))))) * 255):02X}' for c in rgb)
def ramp(h):
    _, C, H = to_oklch(h)
    out = []
    for L in [0.15 + i * (0.80 / 7) for i in range(8)]:   # dark to light, ~15% to ~95%
        c = C
        while from_oklch(L, c, H) is None: c -= 0.002
        out.append(from_oklch(L, c, H))
    return out

NAMES = {}
for m in re.finditer(r'^- \*\*([^*]+)\*\* \(`([^`]+)`, `--([a-z0-9-]+)`', section('Colors'), flags=re.M):
    NAMES[m.group(3)] = m.group(1)
for m in re.finditer(r'^- \*\*([^*]+)\*\* \(`--([a-z0-9-]+)`\)', section('Colors'), flags=re.M):
    NAMES[m.group(2)] = m.group(1)
def role(t):
    if t.startswith('accent') or t == 'on-accent-fill': return 'primary'
    if t.startswith('error') or t == 'scrim': return 'state'
    if t.startswith('glass'): return 'material'
    return 'neutral'
colorMeta = {}
for t, v in FM['colors'].items():
    e = {'role': role(t), 'displayName': NAMES.get(t, t.replace('-', ' ').title()), 'canonical': v}
    if re.fullmatch(r'#[0-9A-Fa-f]{6}', v):
        L, C, H = to_oklch(v)
        e['oklch'] = f'oklch({L * 100:.1f}% {C:.3f} {H:.1f})'
        e['tonalRamp'] = ramp(v)
    colorMeta[t] = e

# ---------------------------------------------------------------- type: purposes from Typography → Hierarchy
hier = {m.group(1).lower().replace(' ', '-'): m.group(2).strip() for m in
        re.finditer(r'^- \*\*([^*]+)\*\* \([^\n]*?\): ([^\n]+)$', section('Typography'), flags=re.M)}
typographyMeta = {t: {'displayName': t.replace('-', ' ').title(), 'purpose': hier.get(t, OLD.get('extensions', {}).get('typographyMeta', {}).get(t, {}).get('purpose', ''))}
                  for t in FM['typography']}

# ---------------------------------------------------------------- shadows, motion, breakpoints
def kit(name): return resolve(name)
shadows = [{'name': 'float-shadow', 'value': re.sub(r'color-mix\(in srgb, #000000 60%, transparent\)', 'rgba(0, 0, 0, 0.6)', kit('float-shadow')), 'purpose': 'What floats over content: the Filters sheet and the floating tab bar (The Float Rule). Cards are flat.'}]
motion = [
    {'name': 'ease-out', 'value': kit('ease-out'), 'purpose': 'Every transition.'},
    {'name': 'ease-in-out', 'value': kit('ease-in-out'), 'purpose': 'The skeleton pulse.'},
    {'name': 'dur-fast', 'value': kit('dur-fast'), 'purpose': 'Button background and press; 0ms under prefers-reduced-motion.'},
    {'name': 'dur-sheet', 'value': kit('dur-sheet'), 'purpose': 'Filters sheet slide and scrim fade; 0ms under prefers-reduced-motion.'},
    {'name': 'dur-pulse', 'value': kit('dur-pulse'), 'purpose': 'One breath of the skeleton pulse (C6); still under prefers-reduced-motion.'},
    {'name': 'dur-spin', 'value': kit('dur-spin'), 'purpose': 'One turn of the busy spinner (G26); keeps turning under reduced motion (HIG: a still indicator reads as stalled).'},
]
breakpoints = [{'name': 'screen', 'value': '390px', 'purpose': 'iPhone logical width; single layout, no breakpoints.'}]

# ---------------------------------------------------------------- components (snippets: see the docstring)
FONT = 'font-family:"Hanken Grotesk", sans-serif;'
COMPONENTS = {
    'List / Map Segmented Control': {
        'name': 'List / Map Segmented Control', 'kind': 'custom', 'refersTo': 'segmented-track',
        'description': 'In the controls bar: a capsule track with concentric segments of equal width (C7, G11); the pressed segment is bg-3 with a field-line outline.',
        'html': '<div class="ds-seg" role="group" aria-label="View"><button aria-pressed="true">List</button><button aria-pressed="false">Map</button></div>',
        'css': '.ds-seg { display:inline-grid; grid-auto-flow:column; grid-auto-columns:1fr; padding:4px; border-radius:var(--radius-bar-control, 22px); background:var(--bg-2, #272B30); } '
               '.ds-seg button { min-height:36px; padding:0 16px; border:0; border-radius:var(--radius-bar-inner, 18px); background:transparent; color:var(--text-2, #A3A9B0); ' + FONT + ' font-size:15px; font-weight:600; cursor:pointer; } '
               '.ds-seg button:hover { background:var(--bg-3, #2C3035); } .ds-seg button[aria-pressed="true"] { background:var(--bg-3, #2C3035); color:var(--text-1, #F4F5F6); box-shadow:inset 0 0 0 1px var(--field-line, #686E75); } '
               '.ds-seg button:focus-visible { outline:2px solid var(--focus, #F4F5F6); outline-offset:2px; }'},
    'Result Row': {
        'name': 'Result Row', 'kind': 'card', 'refersTo': 'result-row',
        'description': 'Signature: the finish time is the loudest thing on the row; proof stated, not stamped. The disclosure indicator ends the meta row (G22), so the time and the proof keep the full width.',
        'html': '<a class="ds-result" href="#"><span class="ds-result-top"><span class="ds-result-name">HYROX London</span><span class="ds-result-time">1:18:42</span></span><span class="ds-result-meta"><span class="ds-result-chip">HYROX</span> 6 Dec 2025<svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path fill="currentColor" d="M15.8351 11.6296L9.20467 5.1999C8.79094 4.79869 8 5.04189 8 5.5703L8 18.4297C8 18.9581 8.79094 19.2013 9.20467 18.8001L15.8351 12.3704C16.055 12.1573 16.0549 11.8427 15.8351 11.6296Z"/></svg></span><span class="ds-result-proof">Self-reported · via results.hyrox.com</span></a>',
        'css': '.ds-result { display:grid; gap:8px; padding:12px 16px 16px; border-radius:var(--radius-2, 6px); background:var(--bg-1, #1D2024); color:var(--text-1, #F4F5F6); text-decoration:none; ' + FONT + ' } '
               '.ds-result:hover { box-shadow:inset 0 0 0 1px var(--field-line, #686E75); } .ds-result:active { background:var(--bg-3, #2C3035); } .ds-result:focus-visible { outline:2px solid var(--focus, #F4F5F6); outline-offset:2px; } '
               '.ds-result-top { display:flex; justify-content:space-between; align-items:baseline; gap:12px; } .ds-result-name { font-size:17px; font-weight:600; line-height:1.2; } '
               '.ds-result-time { font-family:"Schibsted Grotesk", "Hanken Grotesk", sans-serif; font-size:32px; font-weight:800; line-height:1; letter-spacing:-0.03em; white-space:nowrap; } '
               '.ds-result-meta { display:flex; align-items:center; gap:12px; font-size:15px; color:var(--text-2, #A3A9B0); } .ds-result-meta svg { margin-left:auto; flex:none; } '
               '.ds-result-chip { display:inline-flex; align-items:center; min-height:24px; padding:0 8px; border-radius:var(--radius-1, 4px); background:var(--bg-2, #272B30); color:var(--chip-text, #BFC4CA); font-size:11px; font-weight:600; letter-spacing:0.07em; text-transform:uppercase; } '
               '.ds-result-proof { font-size:13px; color:var(--text-2, #A3A9B0); }'},
    'Tab Bar': {
        'name': 'Tab Bar', 'kind': 'nav', 'refersTo': 'tab-bar',
        'description': 'Three destinations; the current tab is the screen\'s amber. Floats above content as a glass capsule (C1, G1, G2).',
        'html': '<nav class="ds-tabs" aria-label="Global navigation"><a href="#" aria-current="page">Discover</a><a href="#">My Results</a><a href="#">Profile</a></nav>',
        'css': '.ds-tabs { display:grid; grid-template-columns:repeat(3, 1fr); height:64px; align-items:center; margin:0 16px; padding:4px 8px; border-radius:32px; '
               'background:color-mix(in srgb, var(--bg-bar, #0F1114) 85%, transparent); -webkit-backdrop-filter:blur(20px); backdrop-filter:blur(20px); '
               'box-shadow:inset 0 0 0 1px rgba(244, 245, 246, 0.08), 0 12px 32px -12px rgba(0, 0, 0, 0.6); } '
               '.ds-tabs a { display:grid; justify-items:center; min-height:44px; align-content:center; color:var(--text-2, #A3A9B0); ' + FONT + ' font-size:11px; font-weight:600; text-decoration:none; } '
               '.ds-tabs a[aria-current="page"] { color:var(--accent, #F5B649); } .ds-tabs a:focus-visible { outline:2px solid var(--focus, #F4F5F6); outline-offset:2px; }'},
    'Filters Sheet': {
        'name': 'Filters Sheet', 'kind': 'custom', 'refersTo': 'filters-sheet',
        'description': 'Signature: a native sheet on raised glass (C1, C4), 38px corners [?], the large detent only; Cancel outlined, Apply filters the one primary.',
        'html': '<div class="ds-sheet" role="dialog" aria-label="Filters"><div class="ds-sheet-grab"></div><p class="ds-sheet-h">Filters</p><label class="ds-sheet-check"><input type="checkbox" checked> HYROX</label><div class="ds-sheet-actions"><button type="button">Cancel</button><button type="submit">Apply filters</button></div></div>',
        'css': '.ds-sheet { display:grid; gap:12px; padding:8px 16px 12px; border-radius:38px 38px 0 0; background:color-mix(in srgb, var(--bg-2, #272B30) 90%, transparent); -webkit-backdrop-filter:blur(20px); backdrop-filter:blur(20px); '
               'box-shadow:inset 0 1px 0 rgba(244, 245, 246, 0.08), 0 12px 32px -12px rgba(0, 0, 0, 0.6); color:var(--text-1, #F4F5F6); ' + FONT + ' } '
               '.ds-sheet-grab { width:32px; height:4px; margin:0 auto; border-radius:4px; background:var(--field-line, #686E75); } .ds-sheet-h { margin:0; font-size:17px; font-weight:600; } '
               '.ds-sheet-check { display:flex; align-items:center; gap:12px; min-height:44px; font-size:15px; accent-color:var(--text-1, #F4F5F6); } '
               '.ds-sheet-actions { display:flex; gap:12px; } .ds-sheet-actions button { flex:1; min-height:44px; border:0; border-radius:var(--radius-2, 6px); ' + FONT + ' font-size:15px; font-weight:600; cursor:pointer; } '
               '.ds-sheet-actions button[type="button"] { background:transparent; color:var(--text-1, #F4F5F6); box-shadow:inset 0 0 0 1px var(--field-line, #686E75); } '
               '.ds-sheet-actions button[type="submit"] { background:var(--accent, #F5B649); color:var(--on-accent, #131518); } .ds-sheet-actions button[type="submit"]:hover { background:var(--accent-hover, #FFC46A); } '
               '.ds-sheet-actions button:focus-visible { outline:2px solid var(--focus, #F4F5F6); outline-offset:2px; }'},
}
components = [COMPONENTS.get(c['name'], c) for c in OLD.get('components', [])]
components += [c for n, c in COMPONENTS.items() if n not in {x['name'] for x in components}]
# the snippets' fallback values come from tokens/tokens.css too (Lesson 8 step 4): var(--name, value) takes today's role
# and its resolved value; the old kit names map to the roles; the rim and the scrim literals become their roles
_OLD = {'bg-bar': 'graphite-5', 'bg-0': 'page', 'bg-1': 'surface', 'bg-2': 'raised', 'bg-3': 'pressed', 'line': 'hairline',
        'field-line': 'boundary', 'text-1': 'text-primary', 'text-2': 'text-secondary', 'focus': 'text-primary',
        'control-tint': 'text-primary', 'on-accent': 'on-accent-fill', 'error-bg': 'error-surface', 'invalid': 'error', 'destructive': 'error'}
def _snippet(css):
    def v(m):
        n = _OLD.get(m.group(1), m.group(1))
        if n == 'accent': n = 'accent-ink' if re.search(r'aria-current|bar-action|save', css[max(0, m.start() - 120):m.start()]) else 'accent-fill'
        return f'var(--{n}, {resolve(n)})' if n in _DEF else m.group(0)
    css = re.sub(r'color-mix\(in srgb, var\(--(bg-bar|bg-0|bg-2), #[0-9A-F]{6}\)', lambda m: 'color-mix(in srgb, var(--' + {'bg-bar': 'graphite-5', 'bg-0': 'graphite-7', 'bg-2': 'graphite-17'}[m.group(1)] + ', ' + resolve({'bg-bar': 'graphite-5', 'bg-0': 'graphite-7', 'bg-2': 'graphite-17'}[m.group(1)]) + ')', css)   # glass builds on primitives
    css = css.replace('0 12px 32px -12px rgba(0, 0, 0, 0.6)', f'var(--float-shadow, {resolve("float-shadow")})')
    css = re.sub(r'var\(--([a-z0-9-]+), [^()]+?\)', v, css)
    css = css.replace('rgba(244, 245, 246, 0.08)', f'var(--glass-rim, {resolve("glass-rim")})').replace('rgba(0, 0, 0, 0.6)', f'var(--scrim, {resolve("scrim")})')
    return css
for c in components:
    if 'css' in c: c['css'] = _snippet(c['css'])
    if 'description' in c: c['description'] = re.sub(r'\b(bg-bar|bg-[0-3]|field-line|text-[12])\b', lambda m: _OLD[m.group(1)], c['description'])

# ---------------------------------------------------------------- narrative, verbatim
ov = section('Overview')
north = re.search(r'\*\*Creative North Star: "([^"]+)"\*\*', ov).group(1)
paras = [p.strip() for p in ov.split('**Key Characteristics:**')[0].split('\n\n') if p.strip() and not p.strip().startswith('**Creative')]
keys = re.findall(r'^- (.+)$', ov.split('**Key Characteristics:**')[1], flags=re.M)
rules = []
for title, sec in [('Colors', 'colors'), ('Typography', 'typography'), ('Elevation & Depth', 'elevation')]:
    for m in re.finditer(r'^\*\*(The [^*]+ Rule(?: \([^)]*\))?)\.\*\* (.+)$', section(title), flags=re.M):
        rules.append({'name': m.group(1), 'body': m.group(2).strip(), 'section': sec})
dd = section("Do's and Don'ts")
dos = re.findall(r'^- (\*\*Do\*\* .+)$', dd, flags=re.M)
donts = re.findall(r"^- (\*\*Don't\*\* .+)$", dd, flags=re.M)

out = {'schemaVersion': 2, 'generatedAt': datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat(),
       'title': 'Design System: ' + FM['name'],
       'extensions': {'colorMeta': colorMeta, 'typographyMeta': typographyMeta, 'shadows': shadows, 'motion': motion, 'breakpoints': breakpoints},
       'components': components,
       'narrative': {'northStar': north, 'overview': '\n\n'.join(paras), 'keyCharacteristics': keys, 'rules': rules, 'dos': dos, 'donts': donts}}
assert set(colorMeta) == set(FM['colors']) and set(typographyMeta) == set(FM['typography'])
json.dump(out, open(OUT, 'w'), ensure_ascii=False, indent=2)
open(OUT, 'a').write('\n')
print(f'design.json: {len(colorMeta)} colors, {len(typographyMeta)} type styles, {len(components)} components, {len(rules)} rules, {len(dos)} dos, {len(donts)} donts')
