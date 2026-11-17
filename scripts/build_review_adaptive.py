"""ui/review-adaptive.html: the before/after of adaptive components (Lesson 10 step 4, 2026-11-17).

Reads ui/review-adaptive/shots.json, written by
  node scripts/review_adaptive.mjs <before-tree>
(the backlog's defects at 320×568 with 200% text, single-column screens at 820 and 1440, the selected race card and
result row in both themes). Not part of the build.
"""
import os, json, html as H
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'ui/review-adaptive')
shots = json.load(open(os.path.join(D, 'shots.json')))
NOTE = {
  'new-password-320': 'Before: the title ran under “‹ Sign in” and Save, and the rows cut their labels (“ew password”). After: the title truncates between the buttons; each row’s label goes above its field.',
  'results-list-320': 'Before: the small title “Results” ran under Log result, and a card reached the screen’s edge (its meta line couldn’t wrap). After: the title moves off centre; the meta line wraps.',
  'race-picker-320': 'Before: the title ran under “‹ Log result”; the date tile squeezed the race name to a word a line. After: the title truncates; the tile goes above the name.',
  'race-browse-320': 'Before: “7 upcoming races” broke mid-word beside Sort. After: Sort goes under the count.',
  'race-browse-map-320': 'Before: Dallas and Chamonix ran past the map’s sides, Berlin past its top. After: each label slides inside the sides, and the map keeps room above for Berlin; the screen scrolls.',
  'result-detail-320': 'Before: “21 September 2025” ran past the screen. After: the label goes above its value.',
  'profile-320': 'Before: the email was cut. After: it wraps.',
  'race-detail-820': 'Before: the phone screen, 390 wide, alone in the window. After: the screen fills the window and its column stops at 672 and centres, the back link and the action bar’s button at the column’s edges.',
  'new-password-1440': 'The same for the sign-in screens.',
  'result-detail-1440': 'And for a detail opened on its own.',
}
def fig(src, cap):
    return f'<figure><img src="review-adaptive/{src}.webp" alt="{H.escape(cap)}" loading="lazy"><figcaption>{cap}</figcaption></figure>'
rows, seen = [], []
for s in shots:
    if s.get('selected') or s['key'] in seen: continue
    seen.append(s['key'])
    where = f'{s["w"]}' + (', 200% text' if s['text'] == 32 else '')
    figs = fig(s['key'] + '-before', '<b>Before</b>') + fig(s['key'] + '-after', '<b>After</b>')
    rows.append(f'<section class="rv-pair rv-w{s["w"]}"><h2>{H.escape(s["cap"])} · {where}</h2><p>{H.escape(NOTE[s["key"]])}</p><div class="rv-shots">{figs}</div></section>')
sel = []
for key, cap in (('selected-race-card', 'Race card'), ('selected-result-row', 'Result row')):
    figs = fig(key + '-dark', '<b>Dark</b>') + fig(key + '-light', '<b>Light</b>')
    sel.append(f'<section class="rv-pair rv-w390"><h2>Selected · {cap}</h2><p>The second one selected (<code>aria-current="page"</code>): <code>--selected</code> and a hairline <code>--text-secondary</code> edge, its tile and chip a step above. Set by the review script; the screens set it when the panes come.</p><div class="rv-shots">{figs}</div></section>')
page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Adaptive components</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@800&family=Hanken+Grotesk:wght@400;600&display=swap">
<link rel="stylesheet" href="../design-system/index.css">
<link rel="stylesheet" href="../concept/stand.css">
<style>
  /* review page only: tokens from design-system/tokens/tokens.css and the docs layer (concept/stand.css), no values of its own */
  .rv {{ max-width: var(--stand-max); margin: 0 auto; padding: var(--space-8) var(--space-4) var(--space-9); display: grid; gap: var(--space-8); }}
  .rv-head {{ display: grid; gap: var(--space-3); }}
  .rv-head p, .rv-head li, .rv-pair > p {{ margin: 0; max-width: var(--measure); color: var(--text-secondary); }}
  .rv-head ul {{ margin: 0; padding-left: var(--space-5); display: grid; gap: var(--space-2); }}
  .rv-pair {{ display: grid; gap: var(--space-4); padding-top: var(--space-6); border-top: var(--border) solid var(--hairline); }}
  .rv-pair h2 {{ margin: 0; font-family: var(--font-text); font-size: var(--size-item); font-weight: var(--weight-strong); line-height: var(--leading-item); }}
  .rv-shots {{ display: flex; flex-wrap: wrap; gap: var(--space-4); align-items: flex-start; }}
  .rv-shots figure {{ margin: 0; display: grid; gap: var(--space-1); max-width: 100%; }}
  .rv-shots figcaption {{ font-size: var(--size-proof); color: var(--text-secondary); }}
  .rv-shots img {{ display: block; max-width: 100%; height: auto; border-radius: var(--radius-2); box-shadow: 0 0 0 var(--border) var(--hairline); }}
  .rv-w820 .rv-shots figure {{ flex: 1 1 calc(var(--screen-w) / 2); }}
  .rv-w1440 .rv-shots figure {{ flex: 1 1 var(--screen-w); }}
</style>
</head>
<body class="onrace">
<main class="rv">
  <header class="rv-head">
    <h1>Adaptive components</h1>
    <p>Lesson 10, step 4 (2026-11-17). Components adapt to the pane they are given, never to the window: below <code>--stack-w</code> (18rem: 288px at the default text size, 576px at 200%) a component stacks its parts, by a container query on its own width. Before is the commit before this step, after is this one; dark.</p>
    <ul>
      <li><b>The Lesson 10 backlog at 320 with 200% text</b>, now a pass of the overflow and focus checks: titles under their buttons, cut labels, a card at the edge, map pins past the frame, and what the new pass found besides.</li>
      <li><b>Single-column screens</b> at 820 and 1440: the column stops at <code>--container-max</code> (672) and centres, drill-downs and sign-in screens too.</li>
      <li><b>Selected</b>, the race card and the result row, in both themes.</li>
    </ul>
  </header>
  {''.join(rows)}
  {''.join(sel)}
</main>
</body>
</html>
'''
open(os.path.join(ROOT, 'ui/review-adaptive.html'), 'w').write(page)
print(f'review-adaptive: {len(rows)} before/after rows, {len(sel)} selected rows')
