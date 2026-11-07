"""ui/review-signout.html: the before/after of Sign out as a grouped row (designer, 2026-11-07): Profile's screens and the component's states.

Reads ui/review-signout/shots.json, written by
  node scripts/review_states.mjs <before-tree> <{}> ui/review-signout <screens.json>
(screens only, at 390 wide, dark and light; the Filters sheet opened by a tap). Not part of the build.
"""
import os, json, html as H
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'ui/review-signout')
shots = [s for s in json.load(open(os.path.join(D, 'shots.json'))) if s.get('state') != 'Disabled']   # Sign out has no disabled state
for s in shots:
    if s['kind'] == 'component': s['component'] = 'Sign out, ' + s['state'].lower() + ' (specimen)'
    if s['component'] == 'Profile -loading': s['changed'] = {'dark': True, 'light': True}   # measured 44 → 52px; the skeleton's contrast is under the pixel diff's threshold
NOTE = {
  'Profile': 'Before: a 44px button of its own. After: a grouped row in its own group, 52px with the rows\' padding, the text centred in coral, as iOS Settings.',
  'Profile, Sign out’s confirm alert': 'The confirm alert is unchanged; only the row under the scrim moved to 52px.',
  'Profile -error, a row didn’t save': 'Sign out under the error and the footer, the same 52px row.',
  'Profile -loading': 'The placeholder takes the row\'s 52px (was 44), so nothing jumps when the page arrives.',
  'Sign out, at rest (specimen)': 'On the rows\' surface, 52px.',
  'Sign out, hover (specimen)': 'The rows\' hover: one level up from the group (--row-hover).',
  'Sign out, pressed (specimen)': 'The rows\' pressed: two levels up (--row-pressed).',
  'Sign out, focus (specimen)': 'The focus ring drawn inside the row, since the group clips its corners.',
}
def fig(k, t, side):
    return f'<figure><img src="review-signout/{k}-{t}-{side}.webp" alt="{H.escape(side)}, {t}" loading="lazy"><figcaption><b>{t.capitalize()}</b> · {side}</figcaption></figure>'
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
<title>Sign out row</title>
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
    <h1>Sign out, a grouped row</h1>
    <p>2026-11-07. Sign out on Profile was a 44px button of its own beside 52px Account rows. Now it is a grouped row, as iOS Settings: <code>button.row.signout</code>, the one row of its own <code>.rows</code> group, so it takes the rows' surface, height and padding (<code>--grouped-row-min</code>, <code>--grouped-row-pad</code>) and their hover and pressed; the text centred in coral. The confirm alert is unchanged. Before (<code>397236b</code>) and after, dark and light, at 390 wide; the states from the specimen, forced by Chrome DevTools.</p>
  </header>
  {rows}
</main>
</body>
</html>
'''
open(os.path.join(ROOT, 'ui/review-signout.html'), 'w').write(page)
print(f'review-signout: {len(shots)} screens, {len(keep)} shots')
