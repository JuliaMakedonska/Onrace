"""ui/review-shell.html: the before/after of the adaptive shell (Lesson 10 step 3, 2026-11-15).

Reads ui/review-shell/shots.json, written by
  node scripts/review_shell.mjs <before-tree> ui/review-shell
(the three tab screens at 390×844, 820×1180 and 1440×900, dark and light; the tab bar's states in each form). Not part
of the build.
"""
import os, json, html as H
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'ui/review-shell')
shots = json.load(open(os.path.join(D, 'shots.json')))
WIDTH = {'phone': 'Phone, 390', 'tablet': 'Tablet, 820', 'desktop': 'Desktop, 1440'}
NOTE = {
  'phone': 'Unchanged: the tab bar floats at the bottom.',
  'tablet': 'Before: the phone screen, 390 wide, alone in the middle of the window, its tab bar at its bottom. After: iPad’s tab bar, a glass capsule at the top, icon beside label; the screen fills the window and its column stops at 672 and centres.',
  'desktop': 'Before: the same phone column. After: a glass sidebar on the left (macOS), one row per destination; the large title header and the column sit beside it, never under it.',
}
def fig(src, cap):
    return f'<figure><img src="review-shell/{src}.webp" alt="{H.escape(cap)}" loading="lazy"><figcaption>{cap}</figcaption></figure>'
rows = []
for scr in ('Race browse', 'Results list', 'Profile'):
    for w in ('tablet', 'desktop', 'phone'):
        ss = [s for s in shots if s['kind'] == 'screen' and s['screen'] == scr and s['width'] == w]
        figs = ''.join(
            (fig(s['key'] + '-before', f'<b>{s["theme"].capitalize()}</b> · before') if w != 'phone' else '')
            + fig(s['key'] + '-after', f'<b>{s["theme"].capitalize()}</b> · {"after" if w != "phone" else "unchanged"}')
            for s in ss)
        rows.append(f'<section class="rv-pair rv-{w}"><h2>{H.escape(scr)} · {WIDTH[w]}</h2><p>{H.escape(NOTE[w])}</p><div class="rv-shots">{figs}</div></section>')
st_rows = []
for w in ('phone', 'tablet', 'desktop'):
    for t in ('dark', 'light'):
        figs = ''.join(fig(f'states-{w}-{t}-{st}', f'<b>{lab}</b>') for st, lab in (('rest', 'At rest, Results current'), ('hover', 'Hover, Discover'), ('pressed', 'Pressed, Discover'), ('focus', 'Keyboard focus, Results')))
        st_rows.append(f'<section class="rv-pair rv-states"><h2>States · {WIDTH[w]} · {t.capitalize()}</h2><div class="rv-shots">{figs}</div></section>')
page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Adaptive shell</title>
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
  .rv a {{ color: var(--text-primary); text-underline-offset: var(--space-1); }}
  .rv-pair {{ display: grid; gap: var(--space-4); padding-top: var(--space-6); border-top: var(--border) solid var(--hairline); }}
  .rv-pair h2 {{ margin: 0; font-family: var(--font-text); font-size: var(--size-item); font-weight: var(--weight-strong); line-height: var(--leading-item); }}
  .rv-shots {{ display: flex; flex-wrap: wrap; gap: var(--space-4); align-items: flex-start; }}
  .rv-shots figure {{ margin: 0; display: grid; gap: var(--space-1); max-width: 100%; }}
  .rv-shots figcaption {{ font-size: var(--size-proof); color: var(--text-secondary); }}
  .rv-shots img {{ display: block; max-width: 100%; height: auto; border-radius: var(--radius-2); box-shadow: 0 0 0 var(--border) var(--hairline); }}
  .rv-phone .rv-shots img {{ max-width: min(100%, var(--screen-w)); }}
  .rv-tablet .rv-shots figure {{ flex: 1 1 calc(var(--screen-w) / 2); }}
  .rv-desktop .rv-shots figure {{ flex: 1 1 var(--screen-w); }}
</style>
</head>
<body class="onrace">
<main class="rv">
  <header class="rv-head">
    <h1>The adaptive shell</h1>
    <p>Lesson 10, step 3 (2026-11-15). The tab bar component and the Tab screen pattern adapt by width; no screen’s markup changed. Each tab screen before (the commit before this step) and after, at the viewer’s three widths, dark and light; then the tab bar’s states in each form.</p>
    <ul>
      <li><b>Phone</b> (under <code>--bp-tablet</code>, 781): the tab bar at the bottom, as before.</li>
      <li><b>Tablet</b> (from 781): iPad’s tab bar at the top, icon beside label (HIG Tab bars).</li>
      <li><b>Desktop</b> (from <code>--bp-desktop</code>, 1343): a glass sidebar on the left (HIG Sidebars); the large title header narrows to its pane.</li>
      <li>The same three destinations and the same states from the same roles on the same glass in every form. Drill-downs and sheets keep the phone screen until the panes come.</li>
    </ul>
  </header>
  {''.join(rows)}
  {''.join(st_rows)}
</main>
</body>
</html>
'''
open(os.path.join(ROOT, 'ui/review-shell.html'), 'w').write(page)
print(f'review-shell: {len(rows)} screen rows, {len(st_rows)} state rows')
