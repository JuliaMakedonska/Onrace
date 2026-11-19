"""ui/review-webapp.html: the before/after of the new direction (2026-11-19): the tablet the phone's, the desktop a web
app (Strava Maps and Komoot as references), Race browse first.

Reads ui/review-webapp/shots.json, written by  node scripts/review_webapp.mjs <before-tree>. Not part of the build.
"""
import os, json, html as H
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'ui/review-webapp')
LIVE = 'https://onrace-five.vercel.app/wireframes/'
PAGES = [('rb', 'race-browse.html'), ('rb-map', 'race-browse.html'), ('rb-chosen', 'race-browse.html?race=utmb'), ('rb-filters', 'race-browse.html'), ('rb-loading', 'race-browse-loading.html'), ('rb-empty', 'race-browse-empty.html'), ('rb-error', 'race-browse-error.html'), ('rb-fail', 'race-browse.html?race=spartan-beast-killington&fail=1'), ('rl', 'results-list.html?result=hyrox-london-2025'), ('pr', 'profile.html')]
shots = json.load(open(os.path.join(D, 'shots.json')))
NOTE = {
  'rb': 'Phone: unchanged. Tablet: the phone’s list, its column capped at --container-max and centred, the tab bar at the bottom (was: list and map side by side, the tab bar at the top). Desktop: the top bar (the wordmark, the destinations, Log result) and the map full bleed under it, the list a floating card (was: the sidebar and two panes).',
  'rb-map': 'The Map view. Phone: unchanged. Tablet: the map fills the screen’s width edge to edge, framed to the races (was: the map was always beside the list).',
  'rb-chosen': 'A race chosen. Phone and tablet: the list (a card opens Race detail as its own screen). Desktop: the race card beside the list card, Close at its corner, Register its primary; the chosen card and its pin Selected.',
  'rb-filters': 'The filters. Phone and tablet: the sheet (a form sheet on a tablet), Cancel and Apply. Desktop: a card under the Filters button over the map, Reset and Done, the screen not dimmed.',
  'rb-loading': 'Loading. Desktop: the list card’s skeleton and the map’s pulse.',
  'rb-empty': 'No race matches. Desktop: the message inside the list card, the filters and chips over the map, the map without pins.',
  'rb-error': 'The races failed to load. Desktop: the error inside the list card; its Try again steps the top bar’s Log result down to plain text (one primary).',
  'rb-fail': 'A race that fails to load (&fail=1). Desktop: its error inside the race card, Try again there; the list and the map stay.',
  'rl': 'Results list: its layout waits. Tablet: its two panes above the bottom tab bar, the detail ending above it. Desktop: the top bar in place of the sidebar, its Log result the one primary (the large title’s own hides).',
  'pr': 'Profile: its layout waits; the new navigation only (the bottom tab bar on a tablet, the top bar on a desktop).',
}
def fig(src, cap):
    return f'<figure><img src="review-webapp/{src}.webp" alt="{H.escape(cap)}" loading="lazy"><figcaption>{cap}</figcaption></figure>'
rows, seen = [], []
for s in shots:
    if s['key'] in seen: continue
    seen.append(s['key'])
    base = s['key'].rsplit('-', 1)[0]
    page = next(p for k, p in PAGES if k == base)
    figs = fig(s['key'] + '-before', '<b>Before</b>') + fig(s['key'] + '-after', '<b>After</b>')
    rows.append(f'<section class="rv-pair rv-w{s["w"]}"><h2>{H.escape(s["cap"])} · {s["w"]} <a href="{LIVE}{H.escape(page)}">live ↗</a></h2><p>{H.escape(NOTE[base])}</p><div class="rv-shots">{figs}</div></section>')
sel = []
page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Web app desktop</title>
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
    <h1>Web app desktop</h1>
    <p>2026-11-19, a new direction, Race browse first (the other screens wait). References: Strava Maps and Komoot, a routes list and a route’s detail as floating cards over a full-bleed map. Before is the commit before, after is this one; dark; every Race browse state at 390, 820 and 1440, then Results list and Profile under the new navigation.</p>
    <ul>
      <li><b>Tablet</b> behaves like the phone, navigation included: the tab bar at the bottom, the List / Map switch, the column capped at <code>--container-max</code>, the Map view edge to edge. The tablet breakpoint now only caps the column, a deliberate deviation from the width audit.</li>
      <li><b>Desktop</b> is a web app, not macOS: a top bar (Onrace, Discover, Results, Profile, Log result), the map full bleed under it, the list and the chosen race as floating cards, the filters floating over the map.</li>
      <li><b>Through the system:</b> <code>tab-bar.css</code>, <code>split-view.css</code>, <code>static-map.css</code>, <code>modal-sheet.css</code>, <code>screen.css</code>, three new tokens; no media query in a screen.</li>
    </ul>
  </header>
  {''.join(rows)}
  {''.join(sel)}
</main>
</body>
</html>
'''
open(os.path.join(ROOT, 'ui/review-webapp.html'), 'w').write(page)
print(f'review-webapp: {len(rows)} before/after rows')
