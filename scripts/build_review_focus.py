"""ui/review-focus.html: the before/after of 2026-11-07's three docs and system fixes: variants that differ in look or
structure only, States by the docs' theme, and the focus halo redesigned (iOS Full Keyboard Access).

Reads ui/review-focus/shots.json (node scripts/review_states.mjs <before-tree> <states-map.json> ui/review-focus <[]>:
every component state forced on specimens.html, dark and light) and ui/review-focus/docs/docs.json (each changed docs
section on its family page at 1280, before and after). Keeps the focus shots and the section shots. Not part of the build.
"""
import os, json, html as H
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'ui/review-focus')
shots = json.load(open(os.path.join(D, 'shots.json')))
docs = json.load(open(os.path.join(D, 'docs/docs.json')))
focus = [s for s in shots if s.get('state') == 'Focus']
other = sorted({s['component'] for s in shots if s.get('state') != 'Focus' and (s['changed']['dark'] or s['changed']['light'])})
keep = set()
def fig(src, cap, alt):
    return f'<figure><img src="{src}" alt="{H.escape(alt)}" loading="lazy"><figcaption>{cap}</figcaption></figure>'
def focus_row(s):
    cells = []
    for t in ('dark', 'light'):
        for side in ('before', 'after'):
            f = f"{s['key']}-{t}-{side}.webp"; keep.add(f)
            cells.append(fig('review-focus/' + f, f'<b>{t.capitalize()}</b> · {side}', f"{s['component']}, focus, {t}, {side}"))
    return f'<div class="rv-state"><h3>{H.escape(s["component"])}</h3><div class="rv-shots">{"".join(cells)}</div></div>'
names = []
for d in docs:
    if d['name'] not in names: names.append(d['name'])
def doc_row(n):
    cells = []
    for t in ('dark', 'light'):
        for side in ('before', 'after'):
            hit = [d for d in docs if d['name'] == n and d['theme'] == t and d['side'] == side]
            if hit: cells.append(fig('review-focus/docs/' + hit[0]['f'], f'<b>{t.capitalize()}</b> · {side}', f'{n} docs section, {t}, {side}'))
    return f'<div class="rv-state"><h3>{H.escape(n)}</h3><div class="rv-shots rv-docs">{"".join(cells)}</div></div>'
focus_html = ''.join(focus_row(s) for s in focus)
docs_html = ''.join(doc_row(n) for n in names)
for f in os.listdir(D):   # only the focus shots; the other states changed only in computed styles the group or the line already hid
    if f.endswith('.webp') and f not in keep: os.remove(os.path.join(D, f))
page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Focus and variants</title>
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
  .rv-pair {{ display: grid; gap: var(--space-4); padding-top: var(--space-6); border-top: var(--border) solid var(--hairline); }}
  .rv-pair h2 {{ margin: 0; font-family: var(--font-text); font-size: var(--size-item); font-weight: var(--weight-strong); line-height: var(--leading-item); }}
  .rv-state {{ display: grid; gap: var(--space-2); }}
  .rv-state h3 {{ margin: 0; font-size: var(--size-meta); font-weight: var(--weight-strong); color: var(--text-secondary); }}
  .rv-shots {{ display: flex; flex-wrap: wrap; gap: var(--space-4); align-items: flex-start; }}
  .rv-shots figure {{ margin: 0; display: grid; gap: var(--space-1); max-width: 100%; }}
  .rv-shots figcaption {{ font-size: var(--size-proof); color: var(--text-secondary); }}
  .rv-shots img {{ display: block; max-width: min(100%, var(--screen-w)); height: auto; zoom: 0.5; border-radius: var(--radius-2); }}
  .rv-docs img {{ max-width: 100%; zoom: 0.5; }}
</style>
</head>
<body class="onrace">
<main class="rv">
  <header class="rv-head">
    <h1>Focus halo, variants, states by theme</h1>
    <p>2026-11-07. Three fixes in the system and the docs. Before (<code>29a5a70</code>) and after.</p>
    <ol>
      <li><b>Focus halo</b> (iOS Full Keyboard Access): <code>--focus</code> is the accent, amber in dark and the light accent ink in light, 2px, 2px from the element (<code>--focus-gap</code>), following its shape; a grouped row's halo inside it, keeping the group's corners; a rounded halo round a text control's words (<code>--focus-text-pad</code>), never the 44pt box; only on <code>:focus-visible</code>. Every focus state below is the real one, <code>:focus-visible</code> forced by Chrome DevTools on the specimen, in both themes.</li>
      <li><b>Variants</b> differ in look or structure only; instances in other words are one line, "Used as" (<code>ui/inventory.md</code> → Instances map).</li>
      <li><b>States follow the docs' theme switch:</b> Dark shows the dark states, Light the light ones. The sections below are at 1280; three are shown in Light too.</li>
    </ol>
  </header>
  <section class="rv-pair" aria-labelledby="f-h">
    <h2 id="f-h">Focus · {len(focus)} components, both themes</h2>
    {focus_html}
    <p>Other states that changed in computed style only, with no visible change: {H.escape(", ".join(other))}. The first and last grouped rows now carry the group's corner radius (the group already clipped them), and a text link is as wide as its words.</p>
  </section>
  <section class="rv-pair" aria-labelledby="d-h">
    <h2 id="d-h">Docs sections · {len(names)} changed</h2>
    <p>Each section from its name to its States, before and after: words-only variants gone, "Used as" under the rules, one States row in the page's theme.</p>
    {docs_html}
  </section>
</main>
</body>
</html>
'''
open(os.path.join(ROOT, 'ui/review-focus.html'), 'w').write(page)
print(f'review-focus: {len(focus)} focus states, {len(names)} docs sections, {len(keep)} focus shots kept')
