"""The token reference on the Lesson 8 overview (2026-11-01): every token in tokens/tokens.css, rendered from the file.

Imported by scripts/build_tokens_overview.py; nothing here is typed by hand but the sample words, which are the screens'
own (each named where it's used). Four groups, each a run of closed folds with "Expand all / Collapse all":
- color primitives as hue ladders, lightest first: swatch, hex, the comment's L* and name, and the roles that read each
  one in dark and in light (a role the light block doesn't redefine keeps its dark primitive);
- the other primitives, one table per group of tokens.css, with a sample: spacing and sizes as bars, radii as corners,
  type sizes as real text, durations as a moving marker (still under reduced motion), easings as their curve, icons as
  their masks; z-index, alpha and glass values listed;
- semantic roles: the dark value, the light value, and the source comment (what it's for, the usages it grew from);
- contrast pairs from the generated comment at the end of tokens.css (written by build_stand.py), text and non-text apart.
"""
import os, re, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOK = open(os.path.join(ROOT, 'tokens/tokens.css')).read()
esc = lambda s: html.escape(s, quote=True)
code = lambda s: re.sub(r'/\*.*?\*/', '', s, flags=re.S)

MAIN = re.search(r':root\s*\{(.*?)\n\}', TOK, flags=re.S).group(1)
PRIM_SRC, SEM_SRC = MAIN.split('     2. SEMANTIC: color roles\n')
LIGHT_SRC = re.search(r':root\[data-theme="light"\]\s*\{(.*?)\n\}', TOK, flags=re.S).group(1)
MOTION_SRC = re.search(r'@media \(prefers-reduced-motion: reduce\)\s*\{(.*?)\n\}', TOK, flags=re.S).group(1)
DECL = re.compile(r'^\s*--([a-z0-9-]+):\s*(.+?);\s*(?:/\*\s*(.*?)\s*(?:\*/)?)?\s*$')

def groups(src):
    """[(group title, [(name, value, comment)])] in file order, split on the '---------- title ----------' headers."""
    out = []
    for line in src.split('\n'):
        h = re.match(r'\s*/\* -{6,} (.+?) -{6,} \*/', line)
        if h: out.append((h.group(1), [])); continue
        m = DECL.match(line)
        if m and out: out[-1][1].append((m.group(1), m.group(2).strip(), (m.group(3) or '').strip()))
    return out

PRIM_GROUPS, SEM_GROUPS = groups(PRIM_SRC), groups(SEM_SRC)
DARK = {n: v for _, ds in PRIM_GROUPS + SEM_GROUPS for n, v, _ in ds}
LIGHT = {n: v for n, v, _ in (DECL.match(l).groups() for l in code(LIGHT_SRC).split('\n') if DECL.match(l)) for v in [v.strip()]}
REDUCED = dict(re.findall(r'--([a-z0-9-]+):\s*([^;]+);', MOTION_SRC))
ROLES = [n for _, ds in SEM_GROUPS for n, _, _ in ds]
HEX = re.compile(r'#[0-9A-Fa-f]{3,8}$')
COLOR_PRIMS = [n for _, ds in PRIM_GROUPS for n, v, _ in ds if HEX.match(v)]

def raw(name, theme='dark'):
    return LIGHT[name] if theme == 'light' and name in LIGHT else DARK[name]

def subst(value, theme='dark', keep=()):
    """Every var() replaced by its value, recursively (roles through the light block when asked)."""
    def rep(m):
        n = m.group(1)
        if n in keep or n not in DARK: return m.group(0)
        return subst(raw(n, theme), theme, keep)
    return re.sub(r'var\(--([a-z0-9-]+)\)', rep, value)

def px(value):
    """A length in px at the default text size, or None (%, vw, env(), a ratio, a word)."""
    v = subst(value).replace('calc(1rem / 16)', '1px')
    v = re.sub(r'calc\(1rem / ([0-9]+)\)', '1px', v)
    if not re.search(r'px', v) or re.search(r'[a-oq-z%]', v.replace('px', '').replace('calc', '')): return None
    expr = re.sub(r'(-?[0-9.]+)px', r'(\1)', v.replace('calc', ''))
    if not re.fullmatch(r'[0-9.()+\-*/ ]+', expr): return None
    try: return round(eval(expr), 3)
    except Exception: return None

def reads(role, theme):
    """The color primitives a role's value names in a theme."""
    return [p for p in re.findall(r'var\(--([a-z0-9-]+)\)', raw(role, theme)) if p in COLOR_PRIMS]

READERS = {t: {p: [r for r in ROLES if p in reads(r, t)] for p in COLOR_PRIMS} for t in ('dark', 'light')}

def css_color(value, theme='dark'):
    """A role's value as plain CSS (hex and percentages), drawable in an inline style."""
    return subst(value, theme)

# ---------------------------------------------------------------- small renderers
def chip(role): return f'<code class="rc">--{role}</code>'
def sw(color, cls='sw'): return f'<span class="{cls}" style="background:{esc(color)}"></span>'
def fold(summary, body, sub='', open_=False):
    return f'<details class="fold ref-fold"{" open" if open_ else ""}><summary>{summary}{f" <span class=fold-sub>{sub}</span>" if sub else ""}</summary><div class="fold-body">{body}</div></details>'
def table(head, rows, cls='ref'):
    return (f'<div class="tbl-wrap"><table class="{cls}"><thead><tr>' + ''.join(f'<th>{h}</th>' for h in head) + '</tr></thead><tbody>'
            + ''.join('<tr>' + ''.join(f'<td data-h="{esc(re.sub("<[^>]+>", "", h))}">{c}</td>' for h, c in zip(head, r)) + '</tr>' for r in rows) + '</tbody></table></div>')

# ---------------------------------------------------------------- 1. color primitives: hue ladders
def lstar(name, comment):
    m = re.search(r'L\* ([0-9.]+)', comment)
    return float(m.group(1)) if m else (100.0 if name == 'white' else 0.0 if name == 'black' else float(name.rsplit('-', 1)[1]))
def hue(name): return 'graphite' if name in ('white', 'black') else name.rsplit('-', 1)[0]
COMMENT = {n: c for _, ds in PRIM_GROUPS + SEM_GROUPS for n, _, c in ds}
HUE_NOTE = {'graphite': 'the one neutral ramp, with white and black', 'amber': 'the accent', 'coral': 'the error'}

def ladder(h):
    names = sorted((n for n in COLOR_PRIMS if hue(n) == h), key=lambda n: -lstar(n, COMMENT[n]))
    rows = []
    for n in names:
        d, l = READERS['dark'][n], READERS['light'][n]
        tag = 'light only' if l and not d else 'dark only' if d and not l else 'both' if d else 'in a mix or a mask' if n == 'black' else 'unread'
        if n == 'black': tag = 'in mixes and masks'
        note = re.sub(r'^L\* [0-9.]+ · ?', '', COMMENT[n])
        cells = (f'<span class="lad-sw" style="background:{DARK[n]}"></span>'
                 f'<span class="lad-id"><code>--{n}</code><span class="lad-hex">{DARK[n]}</span><span class="lad-note">{esc(note)}</span></span>'
                 f'<span class="lad-roles"><span class="lad-tag">{tag}</span>'
                 + (f'<span class="lad-t">dark</span>{"".join(chip(r) for r in d)}' if d else '')
                 + (f'<span class="lad-t">light</span>{"".join(chip(r) for r in l)}' if l else '') + '</span>')
        rows.append(f'<li class="lad-row">{cells}</li>')
    return f'<ol class="ladder">{"".join(rows)}</ol>'

HUES = sorted({hue(n) for n in COLOR_PRIMS}, key=lambda h: ['graphite', 'amber', 'coral'].index(h) if h in ('graphite', 'amber', 'coral') else 9)
def colors_html():
    return ''.join(fold(f'{h.capitalize()}: {sum(1 for n in COLOR_PRIMS if hue(n) == h)} primitives', ladder(h), HUE_NOTE.get(h, '')) for h in HUES)

# ---------------------------------------------------------------- 2. geometry and the other primitives
# The sample words are the screens' own: wireframes/race-browse.html (Discover, the date day 27, Berlin, Germany),
# result-detail.html (1:18:42), log-result.html (Berlin Marathon, HYROX), race-detail.html (Register on hyrox.com),
# results-list.html (Self-reported · via athlinks.com), profile.html (the initials MR).
TYPE_SAMPLE = {'size-title': ('Discover', 'display'), 'size-time': ('1:18:42', 'display'), 'size-time-hero': ('1:18:42', 'display'),
               'size-day': ('27', 'display'), 'size-initials': ('MR', 'display'), 'size-item': ('Berlin Marathon', 'text-strong'),
               'size-body': ('Register on hyrox.com', 'text'), 'size-meta': ('Berlin, Germany', 'text'),
               'size-proof': ('Self-reported · via athlinks.com', 'text'), 'size-label': ('HYROX', 'text-strong')}
FAM = {'display': (DARK['font-display'], DARK['weight-display']), 'text': (DARK['font-text'], DARK['weight-regular']), 'text-strong': (DARK['font-text'], DARK['weight-strong'])}

def bezier_svg(v):
    m = re.match(r'cubic-bezier\(([^)]+)\)', v)
    x1, y1, x2, y2 = (float(x) for x in m.group(1).split(','))
    W, H = 64, 40
    P = lambda x, y: f'{x * W:.1f},{H - y * H:.1f}'
    return (f'<svg class="curve" viewBox="-2 -8 {W + 4} {H + 16}" width="{W + 4}" height="{H + 16}" aria-hidden="true"><path d="M{P(0, 0)} C{P(x1, y1)} {P(x2, y2)} {P(1, 1)}"/></svg>')

def sample(name, value):
    if name in TYPE_SAMPLE:
        text, kind = TYPE_SAMPLE[name]; fam, w = FAM[kind]
        return f'<span class="ts" style="font-family:{esc(fam)};font-weight:{w};font-size:{px(value):g}px">{esc(text)}</span>'
    if name.startswith('font-'):
        w = DARK['weight-display'] if name == 'font-display' else DARK['weight-regular']   # each family at a weight the screens load
        return f'<span class="ts" style="font-family:{esc(value)};font-weight:{w};font-size:17px">Berlin Marathon</span>'
    if name.startswith('weight-'):
        fam = DARK['font-display'] if name == 'weight-display' else DARK['font-text']
        return f'<span class="ts" style="font-family:{esc(fam)};font-weight:{value};font-size:17px">Berlin Marathon</span>'
    if name.startswith('tracking-'):
        t, fam, w, s = ('Discover', DARK['font-display'], DARK['weight-display'], 22) if 'display' in name else ('HYROX', DARK['font-text'], DARK['weight-strong'], 11)
        return f'<span class="ts" style="font-family:{esc(fam)};font-weight:{w};font-size:{s}px;letter-spacing:{value}">{t}</span>'
    if name.startswith('leading-'):
        lh = subst(value)
        return f'<span class="ts lead" style="font-family:{esc(DARK["font-text"])};font-size:13px;line-height:{lh}">Self-reported ·<br>via athlinks.com</span>'
    if name.startswith('dur-'):
        reduced = f' <span class="ref-note">reduced motion: {REDUCED[name].strip()}</span>' if name in REDUCED else ''
        return f'<span class="track"><span class="runner" style="animation-duration:{value}"></span></span>{reduced}'
    if name.startswith('ease-'): return bezier_svg(value)
    if name.startswith('icon-') and value.startswith('url('):
        return f'<span class="glyph" style="-webkit-mask-image:{esc(value)};mask-image:{esc(value)}"></span>'
    if name.startswith('alpha-'):
        return f'<span class="alpha"><span style="width:{value}"></span></span>'
    if name.startswith('z-'): return f'<span class="z">{"▮" * (int(value) + 1)}</span>'
    if name == 'photo-filter':
        return f'<img class="ph-f" src="visuals/hyrox-sled-hall-1-684.jpg" alt="" width="114" height="38" loading="lazy" style="filter:{esc(value)}">'   # one of the race photos, as Race detail shows it
    if name.endswith('-w') and value.endswith('%'):
        return f'<span class="bar" style="width:{value}"></span>'
    p = px(value)
    if p is None: return '<span class="ref-note">—</span>'
    if 'radius' in name and p < 200:
        return f'<span class="corner" style="border-top-left-radius:{p:g}px"></span>'
    if name.startswith('icon-'):
        return f'<span class="box" style="width:{p:g}px;height:{p:g}px"></span>'
    if p < 0: return f'<span class="bar neg" style="width:{-p:g}px"></span>'
    return f'<span class="bar" style="width:{p:g}px"></span>' if p >= 1 else f'<span class="bar" style="width:1px"></span>'

def value_cell(name, value):
    if value.startswith('url('): return '<code>url(data:image/svg+xml…)</code>'
    p = px(value)
    shown = f'<code>{esc(value)}</code>'
    if p is not None and not re.fullmatch(r'-?[0-9.]+px', value): shown += f' <span class="ref-note">= {p:g}px</span>'
    return shown

def other_html():
    out = []
    for title, ds in PRIM_GROUPS:
        if title.startswith('color'): continue
        rows = [(f'<code>--{n}</code>', value_cell(n, v), sample(n, v)) for n, v, _ in ds]
        sub = ('type sizes at the default text size (one type unit = 1px); they double at 200%' if title == 'type'
               else 'still under reduced motion' if title == 'motion' else '')
        short = re.sub(r'\s*\(.*\)$', '', title)   # the header without its parenthesis
        out.append(fold(f'{short[0].upper() + short[1:]}: {len(ds)}', table(['Primitive', 'Value', 'Looks like'], rows), sub))
    return ''.join(out)

N_OTHER = sum(len(ds) for t, ds in PRIM_GROUPS if not t.startswith('color'))

# ---------------------------------------------------------------- 3. semantic roles
def role_cell(role, theme):
    v = raw(role, theme)
    kept = theme == 'light' and role not in LIGHT
    m = re.fullmatch(r'var\(--([a-z0-9-]+)\)', v)
    if m:
        p = m.group(1)
        return f'{sw(DARK[p])}<code>--{p}</code> <span class="lad-hex">{DARK[p]}</span>' + (' <span class="ref-note">kept</span>' if kept else '')
    plain = css_color(v, theme)
    named = re.sub(r'var\(--([a-z0-9-]+)\)', r'--\1', v)
    if plain.startswith('0 '):   # a shadow
        return f'<span class="shadow" style="box-shadow:{esc(plain)}"></span><code>{esc(named)}</code>' + (' <span class="ref-note">kept</span>' if kept else '')
    return f'{sw(plain, "sw sw-mix")}<code>{esc(named)}</code>' + (' <span class="ref-note">kept</span>' if kept else '')

def roles_html():
    out = []
    for title, ds in SEM_GROUPS:
        rows = [(f'<code>--{n}</code>', role_cell(n, 'dark'), role_cell(n, 'light'), esc(c)) for n, _, c in ds]
        out.append(fold(f'{title[0].upper() + title[1:]}: {len(ds)}', table(['Role', 'Dark', 'Light', 'What it is for, and the usages it grew from'], rows, 'ref roles')))
    return ''.join(out)

# ---------------------------------------------------------------- 4. contrast
LINE = re.compile(r'^\s+--([a-z0-9-]+) on --([a-z0-9-]+)( over the worst case)?\s+dark\s+([0-9.]+)\s+light\s+([0-9.]+)\s+needs ([0-9.]+)\s+(text|large text|non-text)$')
PAIRS = [LINE.match(l).groups() for l in re.search(r'contrast:start.*?\n(.*?)\n   contrast:end', TOK, flags=re.S).group(1).split('\n') if LINE.match(l)]

def solid(role, theme):
    """A background role as a drawable color: a glass mix is drawn at its own tint (the ratio is over its worst case)."""
    v = css_color(raw(role, theme), theme)
    m = re.match(r'color-mix\(in srgb, (#[0-9A-Fa-f]+) ', v)
    return m.group(1) if m else v

def contrast_cell(fg, bg, theme, ratio, need, nontext):
    s = (f'<span class="aa-s" style="background:{esc(solid(bg, theme))}"><span class="dot" style="background:{esc(solid(fg, theme))}"></span></span>' if nontext
         else f'<span class="aa-s" style="background:{esc(solid(bg, theme))};color:{esc(solid(fg, theme))}">Aa</span>')
    ok = float(ratio) >= float(need)
    return f'{s}<span class="ratio">{float(ratio):.2f}</span><span class="{"pass" if ok else "fail"}">{"AA" if ok else "fail"}</span>'

def contrast_html():
    def rows(sel):
        return [(f'{chip(fg)} on {chip(bg)}{" <span class=ref-note>over its worst case</span>" if glass else ""}',
                 contrast_cell(fg, bg, 'dark', d, need, kind == 'non-text'), contrast_cell(fg, bg, 'light', l, need, kind == 'non-text'),
                 f'{float(need):g}:1' + (' <span class=ref-note>large text</span>' if kind == 'large text' else ''))
                for fg, bg, glass, d, l, need, kind in PAIRS if sel(kind)]
    text, non = rows(lambda k: k != 'non-text'), rows(lambda k: k == 'non-text')
    return (fold(f'Text: {len(text)} pairs', table(['Pair', 'Dark', 'Light', 'Needs'], text, 'ref contrast'), 'an “Aa” on its background')
            + fold(f'Non-text: {len(non)} pairs', table(['Pair', 'Dark', 'Light', 'Needs'], non, 'ref contrast'), 'an edge, a dot or an icon at 3:1')
            + '<p class="note">From the generated comment at the end of <code>tokens/tokens.css</code>, written by <code>scripts/concept/build_stand.py</code> on every build. A glass background is drawn at its own tint; its ratio is measured over the worst case behind it.</p>')

# ---------------------------------------------------------------- the whole reference
def reference():
    def group(id_, title, lede, body):
        return f'<div class="ref-group" id="{id_}"><div class="ref-head"><h3>{title}</h3><span class="ref-ctl"><button type="button" data-ref="open">Expand all</button><button type="button" data-ref="close">Collapse all</button></span></div><p class="ref-lede">{lede}</p>{body}</div>'
    return (f'<p class="lede">Every token in <code>tokens/tokens.css</code>, rendered from the file on each build: {len(COLOR_PRIMS)} color primitives, {N_OTHER} other primitives, {len(ROLES)} semantic roles and {len(PAIRS)} contrast pairs.</p>'
            + group('ref-color', f'Color primitives · {len(COLOR_PRIMS)}', 'Hue ladders, lightest first. Each row: the swatch, the hex, the L* and name from the source comment, and the roles that read it in each theme. A role the light block doesn’t redefine reads its dark primitive in light too.', colors_html())
            + group('ref-geometry', f'Geometry and the other primitives · {N_OTHER}', 'One table per group of <code>tokens.css</code>, in file order. Type sizes are written in type units: one unit is 1px at the default size, so they double at 200% text.', other_html())
            + group('ref-roles', f'Semantic roles · {len(ROLES)}', 'Color only. Each role names a primitive, or mixes primitives for glass, the scrim and the shadow. The last column is the role’s comment in the source.', roles_html())
            + group('ref-contrast', f'Contrast pairs · {len(PAIRS)}', 'Every role pair the build checks, with its ratio in both themes (WCAG 2). Text needs 4.5:1, large text and non-text 3:1.', contrast_html()))

CSS = '''
  .ref-group{margin:22px 0 8px}
  .ref-head{display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:8px 16px}
  .ref-head h3{margin:0}
  .ref-ctl{display:flex; gap:6px}
  .ref-ctl button{min-height:44px; padding:0 14px; border-radius:999px; border:1px solid var(--border); background:var(--bg-elev); color:var(--text-dim); font:inherit; font-size:13px; font-weight:700; cursor:pointer}
  .ref-ctl button:hover{color:var(--text)}
  .ref-ctl button:focus-visible{outline:2px solid var(--text); outline-offset:2px}
  .ref-lede{color:var(--text-dim); font-size:14px; margin:6px 0 4px; max-width:760px}
  .ref-note{color:var(--text-faint); font-size:12px}
  .rc{display:inline-block; font-size:11.5px; padding:1px 6px; margin:2px 4px 2px 0; border-radius:4px; background:var(--bg-elev-2); border:1px solid var(--border); white-space:nowrap}
  table.ref td{vertical-align:middle; overflow-wrap:anywhere}
  table.ref td:first-child code{white-space:nowrap}
  table.ref td:nth-child(3){min-width:120px}
  table.roles td:last-child{font-size:12.5px; color:var(--text-dim); min-width:220px}
  table.roles td:nth-child(2), table.roles td:nth-child(3){min-width:150px}
  .ladder{list-style:none; margin:8px 0; padding:0; display:grid; gap:2px}
  .lad-row{display:grid; grid-template-columns:44px minmax(0,1fr) minmax(0,1.3fr); gap:12px; align-items:center; padding:6px 0; border-bottom:1px solid var(--border)}
  .lad-sw{width:44px; height:44px; border-radius:6px; box-shadow:inset 0 0 0 1px rgba(255,255,255,.18)}
  .lad-id{display:grid; gap:1px; min-width:0}
  .lad-id code{justify-self:start}
  .lad-hex{font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-size:12px; color:var(--text-dim)}
  .lad-note{font-size:12px; color:var(--text-faint); overflow-wrap:anywhere}   /* iOS names like secondarySystemGroupedBackground are one long word */
  .lad-roles{min-width:0}
  .lad-tag{display:inline-block; font-size:10.5px; font-weight:800; text-transform:uppercase; letter-spacing:.06em; color:var(--text-faint); margin-right:6px}
  .lad-t{font-size:11px; color:var(--text-faint); margin:0 4px 0 2px}
  @media (max-width:560px){ .lad-row{grid-template-columns:44px minmax(0,1fr)} .lad-roles{grid-column:1 / -1} }
  .sw-mix, .sw{vertical-align:middle; margin-right:6px}
  .ts{display:inline-block; color:var(--text); line-height:1.15; overflow-wrap:anywhere}
  .ts.lead{line-height:normal}
  .bar{display:inline-block; height:10px; max-width:100%; background:var(--accent); border-radius:2px; vertical-align:middle}
  .bar.neg{background:repeating-linear-gradient(90deg,var(--accent) 0 3px,transparent 3px 6px)}
  .corner{display:inline-block; width:56px; height:40px; border-top:3px solid var(--accent); border-left:3px solid var(--accent)}
  .box{display:inline-block; border:1px solid var(--accent); vertical-align:middle}
  .glyph{display:inline-block; width:24px; height:24px; background:var(--text); -webkit-mask-size:contain; mask-size:contain; -webkit-mask-repeat:no-repeat; mask-repeat:no-repeat; -webkit-mask-position:center; mask-position:center}
  .alpha{display:inline-block; width:120px; max-width:100%; height:10px; border-radius:2px; background:var(--bg-elev-2); overflow:hidden; vertical-align:middle}
  .alpha > span{display:block; height:100%; background:var(--text)}
  .z{letter-spacing:2px; color:var(--accent); font-size:12px}
  .ph-f{display:block; width:114px; height:38px; object-fit:cover; border-radius:4px}
  .curve path{fill:none; stroke:var(--accent); stroke-width:2.5}
  .track{display:inline-block; position:relative; width:120px; max-width:100%; height:12px; border-radius:6px; background:var(--bg-elev-2); vertical-align:middle}
  .runner{position:absolute; top:1px; left:1px; width:10px; height:10px; border-radius:50%; background:var(--accent); animation:ref-run 1s ease-in-out infinite alternate}
  @keyframes ref-run{to{left:calc(100% - 11px)}}
  @media (prefers-reduced-motion: reduce){ .runner{animation:none} }
  .shadow{display:inline-block; width:28px; height:20px; margin:4px 10px 10px 2px; border-radius:4px; background:var(--bg-elev-2); vertical-align:middle}
  .aa-s{display:inline-grid; place-items:center; width:40px; height:30px; border-radius:5px; font-weight:800; font-size:15px; box-shadow:inset 0 0 0 1px rgba(255,255,255,.12); vertical-align:middle; margin-right:8px}
  .aa-s .dot{width:12px; height:12px; border-radius:50%}
  .ratio{font-variant-numeric:tabular-nums; font-weight:700; margin-right:6px}
  table.contrast td{white-space:nowrap}
  table.contrast td:first-child{white-space:normal}
  /* a phone: each row becomes a small card, the column name above each cell (data-h), so nothing scrolls sideways */
  @media (max-width:560px){
    .tbl-wrap:has(table.ref){border:0; overflow:visible}
    table.ref, table.ref tbody{display:block}
    table.ref thead{display:none}
    table.ref tr{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:6px 12px; padding:10px 12px; border:1px solid var(--border); border-radius:8px; margin:0 0 8px}
    table.ref td{display:block; padding:0; border:0; min-width:0 !important; white-space:normal !important}
    table.ref td::before{content:attr(data-h); display:block; font-size:10.5px; font-weight:800; text-transform:uppercase; letter-spacing:.05em; color:var(--text-faint); margin-bottom:2px}
    table.ref td:first-child{grid-column:1 / -1}
    table.ref td:first-child::before{display:none}
    table.roles td:last-child, table.ref td:nth-child(3):last-child{grid-column:1 / -1}
    table.contrast td:last-child{grid-column:1 / -1}
  }
  .pass{font-size:11px; font-weight:800; color:var(--text-faint)}
  .fail{font-size:11px; font-weight:800; color:var(--text)}
'''

JS = '''(function () {
  document.querySelectorAll('.ref-group').forEach(function (g) {
    g.querySelectorAll('[data-ref]').forEach(function (b) {
      b.addEventListener('click', function () {
        var open = b.getAttribute('data-ref') === 'open';
        g.querySelectorAll('details').forEach(function (d) { d.open = open; });
      });
    });
  });
})();'''
