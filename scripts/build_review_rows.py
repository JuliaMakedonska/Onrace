"""ui/review-rows.html: the before/after of one grouped row height everywhere (designer, 2026-11-07).

Reads ui/review-rows/shots.json, written by
  node scripts/review_states.mjs <before-tree> <{}> ui/review-rows <screens.json>
(screens only, at 390 wide, dark and light; the Filters sheet opened by a tap). Not part of the build.
"""
import os, json, html as H
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'ui/review-rows')
shots = [s for s in json.load(open(os.path.join(D, 'shots.json'))) if s['kind'] == 'screen']
NOTE = {
  'Sign in': 'Before: Email and Password rows 44px. After: 52px, the sheets\' height; the field fills its row.',
  'Create account': 'The same rows in Create account mode; the hint under the group.',
  'Sign in -error': 'The error is about the whole form, so it stays the inline error above the fields; the rows 52px.',
  'Sign in -loading': 'Locked while signing in: the same 52px rows, dimmed.',
  'Reset password': 'One row, 44px before, 52px after.',
  'Reset password -error': 'The inline error above the field (about the request, not the field); the row 52px.',
  'New password': 'Rows 44px before, 52px after; the hint under the group.',
  'New password -error, too short': 'The field error under the group, outside its surface; the rows 52px.',
  'New password -error, no match': 'The error under the group; New password\'s hint stays below it.',
  'Profile': 'Before: 44px rows, Email 45.8px. After: every row 52px; values stay right-aligned, as iOS Settings.',
  'Profile -error, a row didn’t save': 'The field error under the group with Try again; rows 52px.',
  'Profile -loading': 'The placeholder rows take the same 52px, so nothing jumps when the values arrive.',
  'Log result (a sheet, for comparison)': 'Unchanged: already 52px since 2026-11-06.',
  'Filters sheet (for comparison)': 'Unchanged: already 52px.',
  'Race browse, first screen': 'Unchanged: every visible element measured, the same box before and after.',
  'Results list, first screen': 'Unchanged: every visible element measured, the same box before and after.',
}
def fig(k, t, side):
    return f'<figure><img src="review-rows/{k}-{t}-{side}.webp" alt="{H.escape(side)}, {t}" loading="lazy"><figcaption><b>{t.capitalize()}</b> · {side}</figcaption></figure>'
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
<title>Grouped rows</title>
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
    <h1>Grouped rows, one height</h1>
    <p>2026-11-07. The sheets' rows became 52px on 2026-11-06; the grouped forms outside a sheet kept 44px. Now every grouped row is 52px, from one token, <code>--grouped-row-min</code> (was <code>--sheet-row-min</code>), read by <code>grouped-settings-rows.css</code>, with <code>--grouped-row-pad</code> (was <code>--sheet-row-pad</code>) for a stacked field. Before (<code>4d5145e</code>) and after, dark and light, at 390 wide.</p>
    <ol>
      <li><b>One height:</b> Sign in / Sign up, Reset password, New password and Profile, 44 to 52px; a field or menu fills its row.</li>
      <li><b>The same anatomy and errors as in sheets:</b> one line per field; a field error under the group, outside its surface. Sign in and Reset password errors are about the whole form, so they stay above the fields.</li>
      <li><b>Nothing else moved:</b> Log result, the Filters sheet and the first screens of Race browse and Results list are pixel-identical; every visible element on those first screens has the same box.</li>
    </ol>
  </header>
  {rows}
</main>
</body>
</html>
'''
open(os.path.join(ROOT, 'ui/review-rows.html'), 'w').write(page)
print(f'review-rows: {len(shots)} screens, {len(keep)} shots')
