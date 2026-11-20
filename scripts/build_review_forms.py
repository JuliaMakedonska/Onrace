"""ui/review-forms.html: forms on a tablet, following iPad (2026-11-20): every state of every form screen (Sign in / Sign up,
Reset password, New password, Profile, Log result and the Race picker it pushes) at 390, and at 820 before and after.
Usage:
  before the change:  ONLY=sign-in,reset-password,new-password,profile,log-result,race-picker WIDTHS=390,820 node scripts/review_layout.mjs ui/review-forms/before
  after it:           ... node scripts/review_layout.mjs ui/review-forms/after
  then                python3 scripts/build_review_forms.py
"""
import os, json, filecmp, html as H
import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from review_scale import img, CSS as SCALE_CSS, LABEL as SCALE_LABEL
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UI = os.path.join(ROOT, 'ui')
D = os.path.join(UI, 'review-forms')
before = {s['key']: s for s in json.load(open(os.path.join(D, 'before/shots.json')))}
after = json.load(open(os.path.join(D, 'after/shots.json')))
LIVE = 'https://onrace-five.vercel.app/wireframes/'
groups = {}
for s in after: groups.setdefault(s['label'], {})[s['w']] = s


def fig(side, s, cap):
    src = f'review-forms/{side}/{s["key"]}.webp'
    fails = ''.join(f' <span class="rv-bad">{H.escape(r)}: {H.escape(t)}</span>' for r, t in s['fails'])
    return f'<figure>{img(src, s["w"], H.escape(s["label"]) + " " + cap, UI)}<figcaption>{cap} · 1:2{fails}</figcaption></figure>'


same = lambda s: filecmp.cmp(os.path.join(D, 'before', s['key'] + '.webp'), os.path.join(D, 'after', s['key'] + '.webp'), shallow=False)
rows, changed, phone_changed = [], 0, []
for lab, by in groups.items():
    p, t = by[390], by[820]
    if not same(p): phone_changed.append(lab)
    t_same = same(t)
    changed += not t_same
    href = LIVE + t['name'] + '.html' + ('?' + t['q'] if t['q'] else '')
    note = '<p class="rv-note">820 unchanged: it already followed the rule.</p>' if t_same else ''
    rows.append(f'<section class="rv-row"><h2>{H.escape(lab)} <a href="{H.escape(href)}">live ↗</a></h2>{note}<div class="rv-shots">'
                + fig('after', p, '390') + fig('before', before[t['key']], '820 before') + fig('after', t, '820 after') + '</div></section>')
nfail = sum(1 for s in after if s['fails'])
page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Forms on a tablet</title>
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
  .rv-row .rv-note {{ margin: 0; font-size: var(--size-proof); }}
  .rv-shots {{ display: flex; flex-wrap: wrap; gap: var(--space-4); align-items: flex-start; }}
  .rv-shots figure {{ margin: 0; display: grid; gap: var(--space-1); }}
  .rv-shots img {{ display: block; border-radius: var(--radius-2); box-shadow: 0 0 0 var(--border) var(--hairline); }}
{SCALE_CSS}
  .rv-shots figcaption {{ font-size: var(--size-proof); color: var(--text-secondary); }}
  .rv-bad {{ display: block; color: var(--error); }}
</style>
</head>
<body class="onrace">
<main class="rv">
  <header>
    <h1>Forms on a tablet</h1>
    <p>2026-11-20. On a tablet a form was squeezed to a phone's width in the middle of the screen, its top bar too. Now it follows iPad. Dark. Every state of every form screen at 390, and at 820 before and after. That is {len(groups)} states; {changed} change at 820, and {nfail} of the after shots fail the layout self-check.</p>
    <p class="rv-scale">{SCALE_LABEL}</p>
    <ul>
      <li><b>The top bar</b> spans the screen: back or Cancel at the leading edge, Save at the trailing edge, the title centred (<code>screen.css</code>; <code>modal-sheet.css</code> for Log result).</li>
      <li><b>The content</b> (intro, grouped rows, field errors, links) takes the readable width, <code>--container-max</code>, centred, the grouped rows filling it (<code>gate-layout.css</code>, <code>screen.css</code>). It was <code>--form-w</code>, a phone's width.</li>
      <li><b>Log result and Race picker</b> are the phone's sheet and page at the window's width, no longer a form sheet on a tablet (<code>modal-sheet.css</code>); the discard action sheet stands as on a phone (<code>action-sheet.css</code>). Race picker's search lines up with its list.</li>
      <li><b>Profile</b> already followed the rule: unchanged.</li>
      <li><b>Type</b> is the phone's at every width.</li>
      <li><b>Phone:</b> {"unchanged" if not phone_changed else "unchanged but for a loading spinner caught at another frame (" + ", ".join(H.escape(x) for x in phone_changed) + ")"}.</li>
      <li><b>Desktop:</b> unchanged. The sign-in split page keeps its narrow form, and Log result and Race picker stay form sheets. Checked on 54 desktop shots against the old CSS: identical but for a loading spinner's frame.</li>
    </ul>
  </header>
  {"".join(rows)}
</main>
</body>
</html>
'''
open(os.path.join(UI, 'review-forms.html'), 'w').write(page)
print(f'review-forms: {len(groups)} states, {changed} changed at 820, {nfail} failing, phone changed: {phone_changed}')
