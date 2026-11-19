"""ui/review-gate.html: the sign-in screens on wide screens (2026-11-20): every state of Sign in / Sign up, Reset
password and New password at 390, 820 and 1440, side by side.
Usage: ONLY=sign-in,reset-password,new-password node scripts/review_layout.mjs ui/review-gate && python3 scripts/build_review_gate.py
"""
import os, json, html as H
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
shots = json.load(open(os.path.join(ROOT, 'ui/review-gate/shots.json')))
LIVE = 'https://onrace-five.vercel.app/wireframes/'
groups = {}
for s in shots: groups.setdefault(s['label'], []).append(s)
fig = lambda s: (f'<figure><img src="review-gate/{s["key"]}.webp" alt="{H.escape(s["label"])} at {s["w"]}" loading="lazy"><figcaption>{s["w"]}'
                 + ''.join(f' <span class="rv-bad">{H.escape(r)}: {H.escape(t)}</span>' for r, t in s['fails']) + '</figcaption></figure>')
rows = ''.join(f'<section class="rv-row"><h2>{H.escape(lab)} <a href="{LIVE}{H.escape(ss[0]["name"] + ".html" + ("?" + ss[0]["q"] if ss[0]["q"] else ""))}">live ↗</a></h2><div class="rv-shots">{"".join(fig(s) for s in ss)}</div></section>' for lab, ss in groups.items())
nfail = sum(1 for s in shots if s['fails'])
page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sign-in screens</title>
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
  .rv-shots figcaption {{ font-size: var(--size-proof); color: var(--text-secondary); }}
  .rv-bad {{ display: block; color: var(--error); }}
</style>
</head>
<body class="onrace">
<main class="rv">
  <header>
    <h1>Sign-in screens</h1>
    <p>2026-11-20. Sign in / Sign up, Reset password and New password on wide screens. References: Microsoft Copilot, Dribbble and Midday sign-in (desktop), Pandora (tablet). Dark; every state at 390, 820 and 1440 ({len(groups)} states, {len(shots)} shots; {nfail} with a layout failure in the self-check).</p>
    <ul>
      <li><b>Phone:</b> unchanged.</li>
      <li><b>Tablet:</b> the phone's page, the form centred at <code>--form-w</code>, a phone's width; no longer a form sheet.</li>
      <li><b>Desktop:</b> a split page: the form half on the left, every state in its place, centred both ways; the photo half on the right, a tall crop of hyrox-sled-hall-1 in the Podium treatment, the Onrace wordmark over it. Built once in <code>gate-layout.css</code>.</li>
    </ul>
  </header>
  {rows}
</main>
</body>
</html>
'''
open(os.path.join(ROOT, 'ui/review-gate.html'), 'w').write(page)
print(f'review-gate: {len(groups)} states, {len(shots)} shots, {nfail} failing')
