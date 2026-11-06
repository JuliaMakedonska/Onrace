"""ui/review-sheets.html: the before/after of the sheets' spacing (designer, 2026-11-06): every sheet and its states.

Reads ui/review-sheets/shots.json, written by
  node scripts/review_states.mjs <before-tree> <{}> ui/review-sheets <screens.json>
(screens only, at 390 wide, dark and light; the Filters sheet opened by a tap). Not part of the build.
"""
import os, json, html as H
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'ui/review-sheets')
shots = [s for s in json.load(open(os.path.join(D, 'shots.json'))) if s['kind'] == 'screen']
NOTE = {
  'Filters sheet': 'Before: the form 8px under the bar, rows 44–52px. After: 24px under the bar, every row 52px (a menu fills its row), 32px between groups.',
  'Log result': 'Before: the intro touched the bar (0px), text-field rows 60px beside 44–52px ones. After: 24px under the bar, every row 52px, the stacked link row 8px above and below.',
  'Log result -error, fields missing': 'The same spacing with the field errors under their rows.',
  'Log result -loading': 'The locked form, the same spacing.',
  'Add official result link, on Results list': 'Before: "Official result link" as title and as the field\'s label, the field 8px under the bar. After: the title alone names it; the field shows "https://…" (its label stays as its accessible name); 24px under the bar, sized to its content.',
  'Add official result link, an invalid link': 'The coral footnote in the helper\'s place, the same spacing.',
  'Add official result link, on Result detail': 'The same sheet over Result detail.',
}
def fig(k, t, side):
    return f'<figure><img src="review-sheets/{k}-{t}-{side}.webp" alt="{H.escape(side)}, {t}" loading="lazy"><figcaption><b>{t.capitalize()}</b> · {side}</figcaption></figure>'
rows = ''.join(f'<section class="rv-pair" aria-labelledby="s{i}"><h2 id="s{i}">{H.escape(s["component"])}</h2><p>{H.escape(NOTE.get(s["component"], ""))}</p>'
               f'<div class="rv-shots">{"".join(fig(s["key"], t, side) for t in ("dark", "light") for side in ("before", "after"))}</div></section>' for i, s in enumerate(shots))
keep = {f'{s["key"]}-{t}-{side}.webp' for s in shots for t in ('dark', 'light') for side in ('before', 'after')}
for f in os.listdir(D):
    if f.endswith('.webp') and f not in keep: os.remove(os.path.join(D, f))
page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sheet spacing</title>
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
    <h1>Sheets · spacing, every sheet</h1>
    <p>2026-11-06. Sheets had too little vertical space: content stuck to the top bar and rows felt cramped. Fixed once in the system, for every sheet and every state of it, with tokens in <code>design-system/tokens/tokens.css</code> read by <code>modal-sheet.css</code>. Before (the commit before this change) and after, dark and light, at 390 wide.</p>
    <ol>
      <li><b>Under the bar:</b> <code>--sheet-content-top</code>, 24px before the first group or line.</li>
      <li><b>Between groups:</b> <code>--sheet-group-gap</code>, 32px, as iOS sections.</li>
      <li><b>Rows:</b> <code>--sheet-row-min</code>, 52px for every row (the 44pt target plus 8); a field or menu fills its row; a stacked field keeps <code>--sheet-row-pad</code>, 8px, above and below.</li>
      <li><b>Below:</b> <code>--sheet-content-bottom</code>, 32px, then the bottom safe area. The last group drops its gap, and a one-field sheet sizes to its content.</li>
      <li><b>Add official result link:</b> the title alone says "Official result link"; the field shows "https://…", its label kept as its accessible name.</li>
    </ol>
  </header>
  {rows}
</main>
</body>
</html>
'''
open(os.path.join(ROOT, 'ui/review-sheets.html'), 'w').write(page)
print(f'review-sheets: {len(shots)} screens, {len(keep)} shots')
