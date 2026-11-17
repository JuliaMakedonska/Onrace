"""ui/review-split.html: the before/after of the Split view pattern (Lesson 10 step 5, 2026-11-17).

Reads ui/review-split/shots.json, written by
  node scripts/review_split.mjs <before-tree>
(the backlog's defects at 320×568 with 200% text, single-column screens at 820 and 1440, the selected race card and
result row in both themes). Not part of the build.
"""
import os, json, html as H
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'ui/review-split')
shots = json.load(open(os.path.join(D, 'shots.json')))
NOTE = {
  'race-browse-820': 'Before: the list, alone in a centred column; the map behind the List / Map switch. After: the list in a phone-width pane and the map beside it; no switch.',
  'race-browse-820-chosen': 'After choosing the first card: its race takes the map’s place, “‹ Map” back; the card is Selected and ?race= is in the address.',
  'race-browse-1440': 'After: list, detail and map, beside the sidebar; with nothing chosen the detail pane says “No race selected”.',
  'race-browse-1440-chosen': 'A choice linked: ?race=utmb opens with UTMB in the detail pane, its card and its pin marked.',
  'results-list-820': 'After: the list and “No result selected” beside it (microcopy row 595).',
  'results-list-1440-chosen': 'After: the chosen result in the pane, its row Selected; its column stops at 672 in the wide pane.',
  'race-browse-loading-1440': 'The list pane shows its skeleton; the detail pane keeps “No race selected”.',
  'race-browse-empty-820': 'The list pane says nothing matches; the map beside it stays a map, without a second message.',
  'results-list-error-1440': 'The list pane carries the error; the detail pane keeps “No result selected”.',
  'detail-error-1440': 'A detail that fails to load (?fail=1, the reviewer switch): Result detail’s own error inside the pane; Try again retries there.',
  'race-browse-390': 'The phone: unchanged. A card still opens Race detail, its own screen.',
  'race-browse-320-200': 'A phone with ?race= in the address: unchanged; the choice only matters where there is a pane.',
}
def fig(src, cap):
    return f'<figure><img src="review-split/{src}.webp" alt="{H.escape(cap)}" loading="lazy"><figcaption>{cap}</figcaption></figure>'
rows, seen = [], []
for s in shots:
    if s.get('selected') or s['key'] in seen: continue
    seen.append(s['key'])
    where = f'{s["w"]}' + (', 200% text' if s['text'] == 32 else '')
    figs = fig(s['key'] + '-before', '<b>Before</b>') + fig(s['key'] + '-after', '<b>After</b>')
    rows.append(f'<section class="rv-pair rv-w{s["w"]}"><h2>{H.escape(s["cap"])} · {where}</h2><p>{H.escape(NOTE[s["key"]])}</p><div class="rv-shots">{figs}</div></section>')
sel = []
page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Split view</title>
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
    <h1>Split view</h1>
    <p>Lesson 10, step 5 (2026-11-17). Race browse and Results list as the Split view pattern: a list in a phone-width pane and, beside it, the map or the chosen detail; from the desktop breakpoint, Race browse is list, detail and map. Before is the commit before this step, after is this one; dark.</p>
    <ul>
      <li><b>The choice in the URL</b> (<code>?race=</code>, <code>?result=</code>): a choice can be linked, Back undoes it, the chosen card is Selected.</li>
      <li><b>States:</b> the list pane carries the screen’s state, the pane beside it keeps “nothing selected”; a detail that fails shows its error in its pane.</li>
      <li><b>The phone:</b> unchanged.</li>
    </ul>
  </header>
  {''.join(rows)}
  {''.join(sel)}
</main>
</body>
</html>
'''
open(os.path.join(ROOT, 'ui/review-split.html'), 'w').write(page)
print(f'review-split: {len(rows)} before/after rows')
