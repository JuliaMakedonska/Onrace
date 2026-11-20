"""ui/review-results.html: Results list on a desktop, redone (2026-11-20): every Results list state at 390, 820 and 1440.
Usage: ONLY=results-list node scripts/review_layout.mjs ui/review-results && python3 scripts/build_review_results.py
"""
import os, json, html as H
import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from review_scale import img, CSS as SCALE_CSS, LABEL as SCALE_LABEL
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
shots = json.load(open(os.path.join(ROOT, 'ui/review-results/shots.json')))
LIVE = 'https://onrace-five.vercel.app/wireframes/'
groups = {}
for s in shots: groups.setdefault(s['label'], []).append(s)
fig = lambda s: ('<figure>' + img('review-results/' + s['key'] + '.webp', s['w'], H.escape(s['label']) + ' at ' + str(s['w']), os.path.join(ROOT, 'ui')) + '<figcaption>' + str(s['w']) + ' · 1:2'
                 + ''.join(f' <span class="rv-bad">{H.escape(r)}: {H.escape(t)}</span>' for r, t in s['fails']) + '</figcaption></figure>')
rows = ''.join(f'<section class="rv-row"><h2>{H.escape(lab)} <a href="{LIVE}{H.escape(ss[0]["name"] + ".html" + ("?" + ss[0]["q"] if ss[0]["q"] else ""))}">live ↗</a></h2><div class="rv-shots">{"".join(fig(s) for s in ss)}</div></section>' for lab, ss in groups.items())
nfail = sum(1 for s in shots if s['fails'])
page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Results on a desktop</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@800&family=Hanken+Grotesk:wght@400;600&display=swap">
<link rel="stylesheet" href="../design-system/index.css">
<link rel="stylesheet" href="../concept/stand.css">
<style>
  /* review page only: tokens from design-system/tokens/tokens.css and the docs layer (concept/stand.css), no values of its own */
  .rv {{ max-width: var(--stand-max); margin: 0 auto; padding: var(--space-8) var(--space-4) var(--space-9); display: grid; gap: var(--space-6); }}
  .rv p, .rv li {{ max-width: var(--measure); color: var(--text-secondary); }}
  .rv h2 {{ margin: 0; font-family: var(--font-text); font-size: var(--size-body); font-weight: var(--weight-strong); }}
  .rv h2 a {{ font-weight: var(--weight-regular); color: var(--text-secondary); }}
  .rv-row {{ display: grid; gap: var(--space-3); padding-top: var(--space-5); border-top: var(--border) solid var(--hairline); }}
  .rv-shots {{ display: flex; flex-wrap: wrap; gap: var(--space-4); align-items: flex-start; }}
  .rv-shots figure {{ margin: 0; display: grid; gap: var(--space-1); max-width: 100%; }}
  .rv-shots img {{ display: block; max-width: 100%; height: auto; border-radius: var(--radius-2); box-shadow: 0 0 0 var(--border) var(--hairline); }}
{SCALE_CSS}
  .rv-shots figcaption {{ font-size: var(--size-proof); color: var(--text-secondary); }}
  .rv-bad {{ display: block; color: var(--error); }}
</style>
</head>
<body class="onrace">
<main class="rv">
  <header>
    <h1>Results on a desktop</h1>
    <p>2026-11-20. Results list on a desktop, redone. References: Strava's activity feed (a card with the title, a row of stats, a big photo) and Komoot (a list with thumbnails, the detail as a card with its photo on top and its actions at the bottom). Dark; every state at 390, 820 and 1440 ({len(groups)} states, {len(shots)} shots; {nfail} with a layout failure in the self-check).</p>
    <p class="rv-scale">{SCALE_LABEL}</p>
    <ul>
      <li><b>Phone and tablet:</b> unchanged, one column.</li>
      <li><b>Desktop:</b> a centred container at <code>--container-max-wide</code> under the top bar; the list with photo thumbnails; the result as a card: the photo band, the name, the stats row (the finish time biggest, the date, the sport type), the official result link and the proof, the actions at its foot sized to their text. “No result selected” is its empty state.</li>
      <li><b>Photos:</b> a catalog race's own; a result entered by hand takes its format's (Valencia: the marathon photo).</li>
      <li><b>Selected:</b> the quiet fill alone; amber is keyboard focus only. Buttons on a desktop are sized to their text; Log result in the top bar is a normal button.</li>
    </ul>
  </header>
  {rows}
</main>
</body>
</html>
'''
open(os.path.join(ROOT, 'ui/review-results.html'), 'w').write(page)
print(f'review-results: {len(groups)} states, {len(shots)} shots, {nfail} failing')
