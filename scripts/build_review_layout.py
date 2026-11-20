"""ui/review-layout.html: the wide layout pass (Lesson 10, 2026-11-18). Every screen and every state at 390, 820 and
1440 side by side, each shot measured against DESIGN.md → Width → The wide layout (scripts/review_layout.mjs writes
ui/review-layout/shots.json and the shots), what still looks off, compared with HIG Split views and Sidebars, and the
step 6 critique (ui/review-layout/critique-step6.md, as returned, unchanged) merged into one list of what's open.
Not part of the build.  Usage: node scripts/review_layout.mjs && python3 scripts/build_review_layout.py
"""
import os, re, json, html as H
import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from review_scale import img, CSS as SCALE_CSS, LABEL as SCALE_LABEL
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'ui/review-layout')
shots = json.load(open(os.path.join(D, 'shots.json')))
crit = open(os.path.join(D, 'critique-step6.md')).read()
LIVE = 'https://onrace-five.vercel.app/'
esc = lambda t: H.escape(t)
def md(t):   # the table cells' own markdown: code and bold
    t = esc(t)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    return re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', t)
rows = [[c.strip() for c in l.strip().strip('|').split('|')] for l in crit.splitlines() if l.startswith('| ') and not l.startswith('| Group') ]
# the critique's rows this pass closed (index in the table, what closed it)
CLOSED = {
  1: 'the map pane shows the map without pins beside an empty or failed list',
  4: 'desktop is two panes, list and a wide map, until a race is chosen',
  5: 'a wide pane frames the pins with a margin at its own shape; the phone keeps the crop it always had (by design)',
  10: '--radius-sidebar is gone: the sidebar is edge to edge',
  11: 'a list with nothing to choose is one column; while it loads the pane waits without words',
  19: 'the large title starts --pane-top below its pane',
  25: 'the large title starts --pane-top below its pane, level with the sidebar\'s first row',
  35: '--radius-sidebar is gone',
  36: 'the bar\'s title sits over the list pane',
  37: 'the bar\'s title sits over the list pane',
}
# found in this pass, by eye and against HIG (not measurable by the self-check)
NEW = [
  ('Layout pass', 'Race browse (map pane)', '820; 1440 with a race chosen', 'A tall, narrow map pane (about 429×1120 at 820, 418×900 at 1440 with a race chosen) fits the pins\' width, so they sit in a band about 70–140px tall with the Arctic above and South America below. Maps lets you pan and zoom; this static map can\'t.', 'race-browse 820, race-browse · split view ?race=utmb 1440', 'Designer\'s call: frame tighter on a tall pane (the continents\' outer edges cut), or keep the whole Atlantic; or the interactive map (deferred).'),
  ('Layout pass', 'Every tab screen', '820', 'The tab bar has its own row and nothing scrolls under it; iPadOS 26 floats it over the content. Chosen so every pane starts on one line (DESIGN.md → Width → The wide layout).', 'any tab screen at 820', 'Keep, or float the bar over the panes with the top line under it (tab-bar.css, split-view.css).'),
  ('Layout pass', 'Every tab screen', '1440', 'The sidebar is edge to edge with a divider; macOS 26 and iPadOS 26 float it as a glass panel. Chosen for one grid with the panes\' thin divider (HIG Split views).', 'any tab screen at 1440', 'Keep, or float the sidebar and the panes together with one gap (tab-bar.css, split-view.css, a gap token).'),
  ('Layout pass', 'Race detail, Result detail on their own; Saved races', '820, 1440', 'A pushed screen at a wide width shows no tab bar or sidebar (the critique\'s rows on Race detail, Result detail and Saved races, unchanged by this pass).', 'race-detail ?race=utmb 1440', 'See the critique rows below.'),
]
# Lesson 10 step 7 (2026-11-20): rows the current layout superseded, re-checked at 390, 820 and 1440 on fresh shots.
# 7301bda: the tablet is the phone's (no split view, the tab bar at the bottom), the desktop a web app (the top bar
# replaced the sidebar; Race browse a full-bleed map with floating cards); c62f7d0: Results list on a tablet the
# phone's, a chosen race scrolled into view; d419cf6: the sign-in screens full pages at every width; 4493f00: forms
# on a tablet the phone's sheet and page, the desktop Results list a centred container with a detail card.
SUPERSEDED = {   # critique row: (commit, what supersedes it)
  2: ('7301bda', 'the chosen race\'s pin is Selected on the desktop\'s map (outlined label); the tablet has no split view'),
  3: ('c62f7d0', 'a race chosen by its address scrolls its card into view in the list card; the tablet has no split view (7301bda)'),
  20: ('4493f00', 'the action bar\'s buttons are sized to their text on a desktop, in the result card and on the screen alone'),
  28: ('d419cf6', 'Sign in / Sign up, Reset password and New password are full pages at every width, no longer form sheets'),
}
NARROWED = {     # critique row: (the width still open, why the other width closed)
  0: ('820', '1440 closed by 7301bda: the desktop\'s filters are a popover card sized to its content, OCR in view'),
  6: ('1440', '820 closed by 7301bda: no split view on a tablet'),
  7: ('1440', '820 closed by 7301bda: a tablet is the phone\'s, a pushed screen has no tab bar there. Now: no top bar on a desktop'),
  9: ('1440', '820 closed by 7301bda: no split view on a tablet'),
  12: ('1440', '820 closed by 4493f00: on a tablet Log result is the phone\'s sheet at the window\'s width. Now: the top bar and the list vanish too'),
  14: ('1440', '820 closed by c62f7d0: Results list on a tablet is the phone\'s'),
  15: ('1440', '820 closed by c62f7d0: Results list on a tablet is the phone\'s'),
  17: ('1440', '820 closed by c62f7d0: no panes on a tablet'),
  18: ('1440', '820 closed by c62f7d0: on a tablet the pushed screen is the phone\'s. Now: no top bar on a desktop'),
  21: ('1440', '820 closed by c62f7d0: no split view on a tablet'),
  38: ('1440', '820 closed by 7301bda: on a tablet a pushed screen is the phone\'s. Now: no top bar on a desktop'),
  39: ('1440', '820 closed by c62f7d0: the list-with-detail panes are a desktop\'s'),
  40: ('1440', '820 closed by c62f7d0: the list-with-detail panes are a desktop\'s'),
  41: ('1440', '820 closed by c62f7d0: the list-with-detail panes are a desktop\'s'),
}
NEW_SUPERSEDED = {   # this pass's own rows (index in NEW): (commit, what supersedes it)
  0: ('7301bda', 'no tall map pane: the tablet\'s Map view spans the window, the desktop\'s map is full bleed under the cards, framed to the races in the room they leave'),
  1: ('7301bda', 'the tablet\'s tab bar is the phone\'s, floating at the bottom, a phone\'s width'),
  2: ('7301bda', 'the desktop\'s top bar replaced the sidebar'),
}
NEW_NARROWED = {3: ('1440', '820 closed by 7301bda: a tablet is the phone\'s. Now: a pushed screen on a desktop shows no top bar')}
FIXED = {   # Lesson 10 step 7's defect table (#), fixed the same day: critique row → the fix
  0: '#3: Filters is the phone\'s sheet on a tablet, at the window\'s width, every sport type in it',
  6: '#11: the pane says what it shows in a polite status', 7: '#5: on a desktop race-detail?race= opens Race browse with that race\'s card; the top bar is on every desktop page',
  9: '#13: the race card\'s title at --size-title-1, one step under the large title', 12: '#6: Log result and Race picker sit over Results list, dimmed',
  13: '#9: the strip is inside the row, the article its surface', 14: '#9: on the chosen row the pane\'s primary says it once',
  15: '#10: a result just saved is the one chosen', 17: '#12: a failed detail centred in its pane, as "No result selected"',
  18: '#5: on a desktop result-detail?result= opens Results list with that result', 21: '#11: the pane\'s headings sit a level under its title (aria-level)',
  38: '#5: the top bar on every desktop page, Saved races included', 39: '#11: the pane\'s headings sit a level under its title',
  40: '#11: the pane says what it shows', 41: '#12: one vertical placement, centred', 42: '#8: sizes from the tokens and the slot (scripts/build_sizes.py)',
  43: '#15: card titles text-wrap: pretty, no short last line (balance broke at "Ultra-")',
}
NEW_FIXED = {3: '#5: the top bar on every desktop page'}
fig = lambda s: (f'<figure class="rv-w{s["w"]}">' + img(f'review-layout/{s["key"]}.webp', s['w'], esc(s['label']) + ' at ' + str(s['w']), os.path.join(ROOT, 'ui'))
                 + f'<figcaption>{s["w"]} · 1:2' + (''.join(f' <span class="rv-bad">{esc(r)}: {esc(t)}</span>' for r, t in s['fails']) or ' <span class="rv-ok">passes the spec</span>') + '</figcaption></figure>')
groups = {}
for s in shots: groups.setdefault(s['label'], []).append(s)
grid = []
for lab, ss in groups.items():
    page = ss[0]['name'] + '.html' + ('?' + ss[0]['q'] if ss[0]['q'] else '')
    href = LIVE + ('design-system/' + page[len('../design-system/'):] if page.startswith('../') else 'wireframes/' + page)
    grid.append(f'<section class="rv-row"><h3>{esc(lab)} <a href="{esc(href)}">live ↗</a></h3><div class="rv-shots">{"".join(fig(s) for s in ss)}</div></section>')
nfail = sum(1 for s in shots if s['fails'])
def narrow(r, n):   # the width still open, the closed width's reason after it
    return r[:2] + [f'{n[0]} ({n[1]})'] + r[3:]
open_rows = [narrow(r, NARROWED[i]) if i in NARROWED else r for i, r in enumerate(rows) if i not in CLOSED and i not in SUPERSEDED and i not in FIXED]
open_new = [narrow(list(r), NEW_NARROWED[i]) if i in NEW_NARROWED else list(r) for i, r in enumerate(NEW) if i not in NEW_SUPERSEDED and i not in NEW_FIXED]
fixed = ''.join(f'<li><b>{md(NEW[i][1])}</b> (this pass): {esc(w)}.</li>' for i, w in NEW_FIXED.items()) + ''.join(f'<li><b>{md(rows[i][1])}</b> ({md(rows[i][0])}): {esc(w)}.</li>' for i, w in FIXED.items())
superseded = (''.join(f'<li><b>{md(NEW[i][1])}, {md(NEW[i][2])}</b> (this pass): {esc(why)}. <code>{c}</code></li>' for i, (c, why) in NEW_SUPERSEDED.items())
              + ''.join(f'<li><b>{md(rows[i][1])}, {md(rows[i][2])}</b> ({md(rows[i][0])}): {esc(why)}. <code>{c}</code></li>' for i, (c, why) in SUPERSEDED.items())
              + ''.join(f'<li><b>{md(rows[i][1])}, 820</b> ({md(rows[i][0])}): {esc(n[1])}; 1440 stays open above.</li>' for i, n in NARROWED.items() if n[0] == '1440'))
tr = lambda r: '<tr>' + ''.join(f'<td>{md(c)}</td>' for c in r) + '</tr>'
head = '<tr><th>Group</th><th>Screen</th><th>Width</th><th>What\'s wrong</th><th>Evidence</th><th>Suggested fix</th></tr>'
closed = ''.join(f'<li><b>{md(rows[i][1])}, {md(rows[i][2])}</b> ({md(rows[i][0])}): {esc(why)}.</li>' for i, why in CLOSED.items())
page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Wide layout</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@800&family=Hanken+Grotesk:wght@400;600&display=swap">
<link rel="stylesheet" href="../design-system/index.css">
<link rel="stylesheet" href="../concept/stand.css">
<style>
  /* review page only: tokens from design-system/tokens/tokens.css and the docs layer (concept/stand.css), no values of its own */
  .rv {{ max-width: var(--stand-max); margin: 0 auto; padding: var(--space-8) var(--space-4) var(--space-9); display: grid; gap: var(--space-7); }}
  .rv p, .rv li {{ max-width: var(--measure); color: var(--text-secondary); }}
  .rv h2 {{ margin: 0; font-family: var(--font-text); font-size: var(--size-item); font-weight: var(--weight-strong); }}
  .rv h3 {{ margin: 0; font-family: var(--font-text); font-size: var(--size-body); font-weight: var(--weight-strong); }}
  .rv h3 a {{ font-weight: var(--weight-regular); color: var(--text-secondary); }}
  .rv section {{ display: grid; gap: var(--space-3); }}
  .rv-row {{ padding-top: var(--space-5); border-top: var(--border) solid var(--hairline); }}
  .rv-shots {{ display: flex; flex-wrap: wrap; gap: var(--space-4); align-items: flex-start; }}
  .rv-shots figure {{ margin: 0; display: grid; gap: var(--space-1); max-width: 100%; }}
  .rv-shots img {{ display: block; max-width: 100%; height: auto; border-radius: var(--radius-2); box-shadow: 0 0 0 var(--border) var(--hairline); }}
{SCALE_CSS}
  .rv-shots figcaption {{ font-size: var(--size-proof); color: var(--text-secondary); max-width: var(--measure); }}
  .rv-ok {{ color: var(--text-secondary); }}
  .rv-bad {{ display: block; color: var(--error); }}
  .rv-table {{ overflow-x: auto; }}
  .rv table {{ border-collapse: collapse; font-size: var(--size-proof); }}
  .rv th, .rv td {{ text-align: left; vertical-align: top; padding: var(--space-2); border-top: var(--border) solid var(--hairline); }}
  .rv td {{ color: var(--text-secondary); }}
</style>
</head>
<body class="onrace">
<main class="rv">
  <header>
    <h1>Wide layout</h1>
    <p>Lesson 10, the layout pass (2026-11-18). One spec for every wide screen, written first in <code>DESIGN.md</code> → Width → The wide layout and applied once, in the split view, the tab bar and sidebar and the screen layout; no screen has a media query. Every screen and state below at 390, 820 and 1440, dark, each measured against the spec.</p>
  </header>
  <section>
    <h2>The spec, in short</h2>
    <ul>
      <li><b>Panes meet edge to edge at the thin divider</b> (HIG Split views: “Prefer the thin divider style”), no outer margin, no gutter between them, as Mail and Maps.</li>
      <li><b>The sidebar is on the same grid</b> (HIG Sidebars: it “appears on the leading side of a view”): full height, edge to edge, the same divider.</li>
      <li><b>One top line:</b> every pane starts under the tablet's tab bar row or at the window's top; its first content starts <code>--pane-top</code> (16px) below, the sidebar's first row too.</li>
      <li><b>Gutters</b> are the phone's (<code>--space-4</code>) inside each pane; nothing stretches past <code>--container-max</code>.</li>
      <li><b>The map</b> fills its pane edge to edge, frames the pins with a margin at the pane's own shape, and pulses while it loads.</li>
      <li><b>No empty pane without a reason:</b> Race browse on a desktop is the list and a wide map until a race is chosen; Results list keeps “No result selected”; a list with nothing to choose is one column.</li>
      <li><b>Viewer:</b> the tablet icon is wider than the phone's.</li>
    </ul>
  </section>
  <section>
    <h2>Self-check</h2>
    <p>{len(shots)} shots ({len(groups)} states × 3 widths), measured in headless Chrome by <code>scripts/review_layout.mjs</code>: aligned top edges (panes, the large title, the sidebar's first row), the sidebar on the grid, no frame inside a pane, the map edge to edge, no blank or empty pane without a reason, no sideways scroll or pin cut by its map, nothing past <code>--container-max</code>, the list pane's gutter, form sheets centred. <b>{nfail} with a failure.</b></p>
    <p class="rv-scale">{SCALE_LABEL}</p>
  </section>
  <section>
    <h2>Still open: this pass and the step 6 critique, merged</h2>
    <p>What the self-check can't measure, found by eye and against HIG, then the step 6 critique's rows this pass didn't close (as returned).</p>
    <div class="rv-table"><table>{head}{''.join(tr(r) for r in open_new)}{''.join(tr(r) for r in open_rows)}</table></div>
    <h3>Superseded by the current layout (Lesson 10 step 7, 2026-11-20)</h3>
    <p>Re-checked on fresh shots at 390, 820 and 1440 against the layout since <code>7301bda</code> (the tablet the phone's, the desktop a web app), <code>c62f7d0</code>, <code>d419cf6</code> and <code>4493f00</code>. A row closed at one width only stays in the table above with the width still open.</p>
    <ul>{superseded}</ul>
    <h3>Fixed in step 7 ({len(FIXED) + len(NEW_FIXED)} rows)</h3>
    <p>The step 7 defect table, decided by the designer and fixed on 2026-11-20 (<code>concept/concept.md</code> → Lesson 10 → Step 7). The shots below are the fixed state.</p>
    <ul>{fixed}</ul>
    <h3>Closed by this pass ({len(CLOSED)} of the critique's {len(rows)} rows)</h3>
    <ul>{closed}</ul>
  </section>
  <section>
    <h2>The step 6 critique, as returned</h2>
    <div class="rv-table"><table>{head}{''.join(tr(r) for r in rows)}</table></div>
  </section>
  <section>
    <h2>Every screen and state</h2>
  </section>
  {''.join(grid)}
</main>
</body>
</html>
'''
open(os.path.join(ROOT, 'ui/review-layout.html'), 'w').write(page)
print(f'review-layout: {len(groups)} states, {len(shots)} shots, {nfail} failing; {len(open_rows) + len(open_new)} open, {len(FIXED) + len(NEW_FIXED)} fixed, {len(CLOSED)} closed')
