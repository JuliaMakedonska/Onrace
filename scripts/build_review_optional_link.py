"""ui/review-optional-link.html: the before/after of the screens the optional official result link changed (Lesson 9
step 5, 2026-11-06), the proof of the contribution rule (design-system/CONTRIBUTING.md).

Reads ui/review-optional-link/shots.json, written by
  node scripts/review_states.mjs <before-tree> <{}> ui/review-optional-link <screens.json>
(screens only: each at 390 wide, its own height, dark and light, before = the commit before the step). Not part of the build.
"""
import os, json, html as H
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'ui/review-optional-link')
shots = [s for s in json.load(open(os.path.join(D, 'shots.json'))) if s['kind'] == 'screen']
NOTE = {
  'Results list, the whole archive': 'A fifth sample result, logged without a link: "Self-reported · no official result link yet" and Add official result link under the row. The count reads 5.',
  'Results list, Add official result link': 'Before: the add state didn’t exist, so the page is the plain list. After: the one-field sheet at its own height over the list, Save dimmed until there’s text.',
  'Results list, the sheet\'s error': 'An invalid link (&try=athlinks): the coral footnote replaces the helper.',
  'Results list, a link just added': 'After Save: "Saved: <race name>", and the row names its domain; the add action is gone.',
  'Result detail, no official result link yet': 'Before: the slug didn’t exist, so the page showed Berlin Marathon. After: the proof section says there’s no link and no evidence yet; the primary is Add official result link; no Copy link.',
  'Result detail, Add official result link': 'The same sheet over Result detail.',
  'Log result, the form': 'The intro reads "Every field but the official result link is needed to save a result."; the link’s helper opens "Optional: you can add it later."',
  'Log result -error, not a link': 'Before: an empty link was the error. After: only a link that isn’t one is ("That isn’t a link. Paste the full address, starting with https://").',
  'Log result -error, fields missing': 'Only the intro and the link’s helper change.',
  'Sign in': '"Sign in to see your results archive and the official result links you’ve added."',
  'Create account': '"Create an account to start your results archive. Add each result’s official result link now or later."',
}
def fig(k, t, side):
    return f'<figure><img src="review-optional-link/{k}-{t}-{side}.webp" alt="{H.escape(side)}, {t}" loading="lazy"><figcaption><b>{t.capitalize()}</b> · {side}</figcaption></figure>'
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
<title>Optional result link</title>
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
    <h1>Lesson 9 · step 5 · the official result link becomes optional</h1>
    <p>2026-11-06. The proof of the contribution rule (<a href="https://github.com/JuliaMakedonska/Onrace/blob/main/design-system/CONTRIBUTING.md">design-system/CONTRIBUTING.md</a>): anything new appears first in the design system, then on a screen. Every changed screen, before (the commit before the step) and after, dark and light, each at 390 wide and tall enough to show what changed. Decided in <code>concept/concept.md</code> → The official result link becomes optional.</p>
    <ol>
      <li><b>Words first:</b> <code>microcopy.md</code>, <code>voice.md</code>, <code>voice.html</code>.</li>
      <li><b>The system:</b> the result row with no link yet and its Add official result link, the sheet at its own height (<code>.sheet--fit</code>), and their specimens and docs states.</li>
      <li><b>The screens:</b> Results list, Result detail, Log result, Sign in / Sign up.</li>
      <li><b>The viewer and the docs:</b> the new states in <code>wireframes/index.html</code>, <code>flows.md</code>, <code>sitemap.md</code>, <code>research/jtbd.md</code>, <code>CLAUDE.md</code>.</li>
    </ol>
  </header>
  {rows}
</main>
</body>
</html>
'''
open(os.path.join(ROOT, 'ui/review-optional-link.html'), 'w').write(page)
print(f'review-optional-link: {len(shots)} screens, {len(keep)} shots')
