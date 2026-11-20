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
open_rows = [r for i, r in enumerate(rows) if i not in CLOSED]
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
    <div class="rv-table"><table>{head}{''.join(tr(r) for r in NEW)}{''.join(tr(r) for r in open_rows)}</table></div>
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
print(f'review-layout: {len(groups)} states, {len(shots)} shots, {nfail} failing; {len(open_rows) + len(NEW)} open, {len(CLOSED)} closed')
