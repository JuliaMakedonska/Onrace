"""ui/review-sheet-bar.html: the before/after of the sheet's bar (designer, 2026-11-07): every sheet, both themes.

Reads ui/review-sheet-bar/shots.json, written by
  node scripts/review_states.mjs <before-tree> <{}> ui/review-sheet-bar <screens.json>
(screens only, at 390 wide, dark and light; the Filters sheet opened by a tap). Not part of the build.
"""
import os, json, html as H
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'ui/review-sheet-bar')
shots = [s for s in json.load(open(os.path.join(D, 'shots.json'))) if s['kind'] == 'screen']
NOTE = {
  'Filters sheet': 'Before: Cancel and Apply filters as bare text against the top edge, inside the corner curve. After: two capsules, 44pt, inset 12px from the top and 16px from the sides; Apply filters keeps its amber ink.',
  'Log result': 'Cancel and Save as capsules, the title centred between them.',
  'Log result -loading, saving': 'Busy as before: the spinner alone on the Save capsule, Cancel locked with the form.',
  'Log result -error': 'The same bar over the field errors.',
  'Add official result link, on Results list (Save waits)': 'Save waits for the link: the capsule at the disabled opacity, as before.',
  'Add official result link, an invalid link': 'The same bar over the invalid link.',
  'Add official result link, on Result detail': 'The same sheet over Result detail.',
}
def fig(k, t, side):
    return f'<figure><img src="review-sheet-bar/{k}-{t}-{side}.webp" alt="{H.escape(side)}, {t}" loading="lazy"><figcaption><b>{t.capitalize()}</b> · {side}</figcaption></figure>'
shots.sort(key=lambda s: not (s['changed']['dark'] or s['changed']['light']))
rows = ''.join(f'<section class="rv-pair" aria-labelledby="s{i}"><h2 id="s{i}">{H.escape(s["component"])}</h2><p>{H.escape(NOTE.get(s["component"], ""))}</p>'
               f'<div class="rv-shots">{"".join(fig(s["key"], t, side) for t in ("dark", "light") for side in ("before", "after")) if (s["changed"]["dark"] or s["changed"]["light"]) else "".join(fig(s["key"], t, "after").replace("· after<", "· unchanged<") for t in ("dark", "light"))}</div></section>' for i, s in enumerate(shots))
keep = {f'{s["key"]}-{t}-{side}.webp' for s in shots for t in ('dark', 'light') for side in (('before', 'after') if (s['changed']['dark'] or s['changed']['light']) else ('after',))}
for f in os.listdir(D):
    if f.endswith('.webp') and f not in keep: os.remove(os.path.join(D, f))
page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sheet bar</title>
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
  .rv-head ol {{ margin: 0; padding-left: var(--space-5); display: grid; gap: var(--space-2); }}
  .rv a {{ color: var(--text-primary); text-underline-offset: var(--space-1); }}
  .rv-pair {{ display: grid; gap: var(--space-4); padding-top: var(--space-6); border-top: var(--border) solid var(--hairline); }}
  .rv-pair h2 {{ margin: 0; font-family: var(--font-text); font-size: var(--size-item); font-weight: var(--weight-strong); line-height: var(--leading-item); }}
  .rv-shots {{ display: flex; flex-wrap: wrap; gap: var(--space-4); align-items: flex-start; }}
  .rv-shots figure {{ margin: 0; display: grid; gap: var(--space-1); max-width: 100%; }}
  .rv-shots figcaption {{ font-size: var(--size-proof); color: var(--text-secondary); }}
  .rv-shots img {{ display: block; max-width: min(100%, var(--screen-w)); height: auto; zoom: 0.5; border-radius: var(--radius-2); }}
</style>
</head>
<body class="onrace">
<main class="rv">
  <header class="rv-head">
    <h1>The sheet's bar</h1>
    <p>2026-11-07. Every sheet (Filters, Log result, Add official result link) had Cancel and its action as bare text against the sheet's top edge, inside the 38px corner curve, with a tap area only the text's height. Now, following HIG Sheets: Cancel on the leading edge, the confirming action on the trailing edge, each a capsule (C7) 44pt tall on <code>--sheet-button</code>; the bar inset from the top (<code>--sheet-bar-top</code>, 12px) and the sides (<code>--sheet-bar-side</code>, 16px) so nothing enters the curve; the title centred between them, truncated. Apple gives no numbers, so the three values are provisional [?]. Before (<code>2aaae4c</code>) and after, dark and light, at 390 wide.</p>
  </header>
  {rows}
</main>
</body>
</html>
'''
open(os.path.join(ROOT, 'ui/review-sheet-bar.html'), 'w').write(page)
print(f'review-sheet-bar: {len(shots)} screens, {len(keep)} shots')
