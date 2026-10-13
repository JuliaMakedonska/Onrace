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
TOK = open(os.path.join(ROOT, 'concept/tokens.css')).read()

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
    ('Selected List/Map segment', 'text-1', 'line', 'text'),
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
]
rows, failures = [], []
for label, fg, bg, kind in PAIRS:
    f, b = tok(fg), tok(bg)
    r = cr(f, b)
    need = {'text': 4.5, 'large': 3.0, 'ui': 3.0, 'exempt': 0}[kind]
    ok = r >= need
    if kind != 'exempt' and not ok:
        failures.append((label, r))
    verdict = ('<span class="exempt">exempt (disabled, WCAG 1.4.3)</span>' if kind == 'exempt'
               else f'<span class="pass">pass</span> · needs {need:g}:1' if ok else f'<b>fail</b> · needs {need:g}:1')
    rows.append(f'<tr><td>{label}</td><td class="sample">{sw(fg)}<code>--{fg}</code> {f}</td>'
                f'<td class="sample">{sw(bg)}<code>--{bg}</code> {b}</td><td class="num">{r:.2f}:1</td><td>{verdict}</td></tr>')
assert not failures, failures
CONTRAST = ('<div class="spec-wrap" tabindex="0" role="region" aria-label="Contrast table"><table class="spec"><thead><tr><th>Where</th><th>Text</th><th>Background</th><th>Ratio</th><th>WCAG AA</th></tr></thead><tbody>'
            + ''.join(rows) + '</tbody></table></div>')

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
    ('bg-2', 'Raised', 'Secondary button, format chip, the date tile, segmented track, skeletons, disabled buttons.', 'Never for the primary action.', 'Hierarchy rule 3: secondary is tonal'),
    ('line', 'Line', 'Hairline dividers, the selected List/Map segment.', 'Not as a boundary someone must see (fields use Field line), not as a frame around every card.', 'Attribute a: the frame stays quiet'),
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
    ('success', 'Success', 'The saved confirmation: "Saved: HYROX London".', 'Not for "verified" or any claim about a result.', 'Voice principle 1: claim only what Onrace can know'),
    ('success-bg', 'Success tint', 'Behind the saved confirmation.', 'Not behind results or proof lines.', 'Voice principle 1: no verified look'),
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
           ('photo-ratio', 'Photo band ratio in the card', 'A band, not a poster', 'Attribute b: a calendar, not a poster'),
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
           ('photo-focus-low', 'Crop focus for photos whose subject sits low', 'Keeps the athletes in the 16:7 band', 'Attribute b: the band shows the race, not the sky'),
           ('photo-focus-mid', 'Crop focus for photos with a centered subject', 'Keeps the athletes in the 16:7 band', 'Attribute b'),
           ('ease-out', 'Easing for hover and press', 'Fast start, soft stop', 'Attribute e: intense, not jittery'),
           ('stand-max', 'Stand page width (stand only)', 'Never used in the product', 'Stand layout'),
           ('phone-width', 'Phone frame on the stand (stand only)', '390px screen + border', 'Stand layout'),
           ('dur-fast', 'Hover and press transitions', 'Quick, ease-out', 'Attribute e: intense, not jittery')]
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
<div class="spec-wrap" tabindex="0" role="region" aria-label="Component metrics"><table class="spec"><thead><tr><th>Component metric</th><th>Used for</th><th>Sizing</th><th>Why</th></tr></thead><tbody>{METRIC_TRS}</tbody></table></div>'''

# ---------------------------------------------------------------- icons
ICON_PLAN = [
    ('Tab bar', 'compass', 'Discover', 'in use'), ('Tab bar', 'stopwatch', 'My Results', 'in use'), ('Tab bar', 'user', 'Profile', 'in use'),
    ('Card meta · date', 'calendar', 'Where a date is inline (Race detail, the Log result date field). In the race card the date column itself is the cue, so no icon there.', 'planned'),
    ('Card meta · location', 'map-point', 'Before the city on every race card (CSS mask, no markup change).', 'in use'),
    ('Format chip', None, 'No icon and no dot: the same neutral chip for every format (dot option dropped 2026-10-13).', 'none'),
    ('Proof line', 'link-round', 'One link icon before "Self-reported · via …" (Hierarchy rule 6).', 'in use'),
    ('Search field', 'magnifer', 'Inside the field, Text 2.', 'in use'),
    ('Button · primary', 'add-circle', 'Log result.', 'in use'),
    ('Button · external', 'arrow-right-up', 'Register on &lt;domain&gt;, Open official result: the arrow says it leaves Onrace (voice principle 2).', 'in use'),
    ('Button · secondary', 'tuning-2', 'Filters.', 'in use'),
    ('Filter chip · remove', 'close-circle', 'Planned replacement for the × glyph in filter chips; the wireframe uses a text ×.', 'planned'),
    ('State · empty', 'inbox', 'Results list empty state, above "Log your first result".', 'planned'),
    ('State · error', 'danger-circle', 'Error messages ("Couldn’t load races").', 'in use'),
    ('State · success', 'check-circle', 'Saved confirmation.', 'in use'),
    ('State · warning', 'danger-triangle', 'Warning messages, when one exists.', 'planned'),
    ('State · loading', None, 'No icon and no spinner: skeleton cards plus "Loading races…" for screen readers (voice.md → Loading).', 'none'),
]
icon_trs = ''.join(f'<tr><td>{p}</td><td>{("<span class=icon-cell>" + svg(n) + f"<code>{n}</code></span>") if n else "None"}</td><td>{u}</td><td>{s}</td></tr>' for p, n, u, s in ICON_PLAN)

STATUS = f'''<div class="stand-stack">
            <div class="status status--error">{svg("danger-circle")}<p><strong>Couldn’t load races</strong><br>The connection may have dropped. Check it, then try again. Your filters stay as they are.</p></div>
            <div class="status status--success">{svg("check-circle")}<p><strong>Saved:</strong> HYROX London</p></div>
            <div class="status status--warning">{svg("danger-triangle")}<p><strong>Warning style</strong> (no warning copy exists in the wireframes yet)</p></div>
          </div>'''

page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Onrace concept stand</title>
<link rel="stylesheet" href="tokens.css">
<link rel="stylesheet" href="components.css">
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
        <p>Every photo is black and white: <code>--photo-filter</code> ({tok("photo-filter")}), set inside the card at 16:7 with a 4px radius. Color stays reserved for the accent and the states.</p>
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
    {wrap('Icon coverage plan', f'<table class="spec"><thead><tr><th>Where</th><th>Icon</th><th>Use</th><th>Status</th></tr></thead><tbody>{icon_trs}</tbody></table>')}
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

  <section class="stand-section" aria-labelledby="contrast-h">
    <h2 id="contrast-h">Contrast · every text pair and the key non-text pairs</h2>
    <p>Generated by <code>scripts/concept/build_stand.py</code> from the hex values in <code>tokens.css</code> (WCAG 2 relative luminance); the build stops if a text pair fails. Body text needs 4.5:1; non-text UI (focus ring, outlines) needs 3:1.</p>
    {CONTRAST}
  </section>

</main>
</body>
</html>
'''
open(os.path.join(ROOT, 'concept/concept.html'), 'w').write(page)
print('pairs', len(PAIRS), 'min text ratio', min(cr(tok(f), tok(b)) for _, f, b, k in PAIRS if k == 'text'))
