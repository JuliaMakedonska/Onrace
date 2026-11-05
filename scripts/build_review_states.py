"""ui/review-states.html: the before/after of Lesson 9 step 3, the component states (2026-11-05).

Reads ui/review-states/shots.json, written by scripts/review_states.mjs (every component state on specimens.html and the
changed screens, before the step and after, dark and light), and design-system/tokens/tokens.css (the state roles and
their contrast). Shows every changed state with its four shots; lists the unchanged ones; deletes the unchanged shots.
Run from anywhere: python3 scripts/build_review_states.py   (after node scripts/review_states.mjs; not part of the build).
"""
import os, re, json, html as H
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'ui/review-states')
shots = json.load(open(os.path.join(D, 'shots.json')))
TOK = open(os.path.join(ROOT, 'design-system/tokens/tokens.css')).read()
main = re.search(r'^:root \{(.*?)\n\}', TOK, re.S | re.M).group(1)
states_part = main.split('---------- states')[1]
light = re.search(r':root\[data-theme="light"\][^{]*\{(.*?)\n\}', TOK, re.S).group(1)
code = lambda t: re.sub(r'/\*.*?\*/', '', t, flags=re.S)
ROLES = re.findall(r'^\s*--([a-z0-9-]+):\s*var\(--([a-z0-9-]+)\);', code(states_part), re.M)
LIGHT = dict(re.findall(r'^\s*--([a-z0-9-]+):\s*var\(--([a-z0-9-]+)\);', code(light), re.M))
PRIM = dict(re.findall(r'^\s*--([a-z0-9-]+):\s*(#[0-9A-Fa-f]{6}|\d+%);', main, re.M))
CONTRAST = [l.strip() for l in re.search(r'contrast:start.*?\n(.*?)contrast:end', TOK, re.S).group(1).split('\n')
            if l.strip().startswith('--') and re.search(r'--(focus|[a-z]+-hover|[a-z]+-pressed|text-hover|text-pressed)\b', l)]

def img(key, theme, side, alt):
    return f'<img src="review-states/{key}-{theme}-{side}.webp" alt="{H.escape(alt)}" loading="lazy">'
by_comp, same, screens = {}, [], []
for s in shots:
    ch = s['changed']
    if s['kind'] == 'screen':
        screens.append(s); continue
    if not (ch['dark'] or ch['light']): same.append(s); continue
    by_comp.setdefault(s['component'], []).append(s)
keep = set()
def row(s):
    cells = []
    for t in ('dark', 'light'):
        if s['changed'][t]:
            for side in ('before', 'after'):
                keep.add(f"{s['key']}-{t}-{side}.webp")
                cells.append(f'<figure>{img(s["key"], t, side, s["component"] + " · " + s["state"] + ", " + t + ", " + side)}<figcaption><b>{t.capitalize()}</b> · {side}</figcaption></figure>')
        else:
            keep.add(f"{s['key']}-{t}-after.webp")
            cells.append(f'<figure class="rv-same">{img(s["key"], t, "after", s["component"] + " · " + s["state"] + ", " + t)}<figcaption><b>{t.capitalize()}</b> · unchanged</figcaption></figure>')
    return f'<div class="rv-state"><h3>{H.escape(s["state"])}</h3><div class="rv-shots">{"".join(cells)}</div></div>'
comp_html = ''.join(f'<section class="rv-pair" aria-labelledby="c-{i}"><h2 id="c-{i}">{H.escape(c)} · {len(v)} changed</h2>{"".join(row(s) for s in v)}</section>'
                    for i, (c, v) in enumerate(by_comp.items()))
scr_html = ''.join(row({**s, 'state': s['component']}) for s in screens if s['changed']['dark'] or s['changed']['light'])
scr_same = [s['component'] for s in screens if not (s['changed']['dark'] or s['changed']['light'])]
for f in os.listdir(D):   # only the shots the page shows
    if f.endswith('.webp') and f not in keep: os.remove(os.path.join(D, f))
same_by = {}
for s in same: same_by.setdefault(s['component'], []).append(s['state'])
roles = ''.join(f'<tr><td><code>--{n}</code></td><td><code>--{d}</code> {PRIM.get(d, "")}</td><td><code>--{LIGHT.get(n, "")}</code> {PRIM.get(LIGHT.get(n, ""), "")}</td></tr>' for n, d in ROLES)
contrast = ''.join(f'<tr><td><code>{H.escape(l[:74].strip())}</code></td><td>{H.escape(l[74:].strip())}</td></tr>' for l in CONTRAST)
n_changed = sum(len(v) for v in by_comp.values())
page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Component states</title>
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
  .rv-state {{ display: grid; gap: var(--space-2); }}
  .rv-state h3 {{ margin: 0; font-size: var(--size-meta); font-weight: var(--weight-strong); color: var(--text-secondary); }}
  .rv-shots {{ display: flex; flex-wrap: wrap; gap: var(--space-4); align-items: flex-start; }}
  .rv-shots figure {{ margin: 0; display: grid; gap: var(--space-1); max-width: 100%; }}
  .rv-shots figcaption {{ font-size: var(--size-proof); color: var(--text-secondary); }}
  .rv-shots img {{ display: block; max-width: min(100%, var(--screen-w)); height: auto; zoom: 0.5; border-radius: var(--radius-2); }}
  .rv-same img {{ opacity: var(--opacity-disabled); }}
  .rv table {{ width: 100%; border-collapse: collapse; font-size: var(--size-proof); }}
  .rv th, .rv td {{ text-align: left; padding: var(--space-2) var(--space-3); border-bottom: var(--border) solid var(--hairline); vertical-align: top; }}
  .rv th {{ color: var(--text-secondary); font-weight: var(--weight-strong); }}
  .rv-wrap {{ overflow-x: auto; }}
</style>
</head>
<body class="onrace">
<main class="rv">
  <header class="rv-head">
    <h1>Lesson 9 · step 3 · component states</h1>
    <p>2026-11-05. Every component you act on got Hover, Pressed, Focus and Disabled from new semantic roles in <code>design-system/tokens/tokens.css</code>, each with a value in dark and in light. This page shows every state that changed, before (the commit before this step) and after, in both themes: {n_changed} component states and {len(screens) - len(scr_same)} screens. Each state is the real one: <code>:hover</code>, <code>:active</code> and <code>:focus-visible</code> forced by Chrome DevTools on the control and its ancestors, as a pointer or a key does, and Disabled by its real attribute (<code>scripts/review_states.mjs</code>). A theme where the state didn't change shows the after shot, dimmed, marked unchanged. The live states, side by side: each component's States on its <a href="../design-system/docs/index.html">family page</a>.</p>
    <ul>
      <li><b>One rule for fills:</b> hover one level up, pressed two, for every component, cards included. It ends the Lesson 8 hover drift (a row went up one level, a card two).</li>
      <li><b>Hover only under <code>@media (hover: hover)</code>;</b> pressed is the state on touch.</li>
      <li><b>No state moves an element or changes its size:</b> the primary buttons' 1px press and the cards' hover ring are gone.</li>
      <li><b>Disabled</b> is the whole control at <code>--opacity-disabled</code> (40% dark, 38% light), no pointer events; <code>--text-disabled</code> is retired.</li>
      <li><b>Focus</b> is the role <code>--focus</code>: white in dark, dark in light, at least 3:1 on every background it sits on. Its values equal the old ring's, so no focus shot changed.</li>
      <li><b>The field error</b> (Log result, New password, Profile): no ring and no line on the field; a coral footnote with the small error icon under the field or its group, in place of the hint.</li>
      <li><b>The segmented control</b> is a capsule everywhere, also at 200% text (C7). Sign out in the alert is styled by a class, not its id.</li>
    </ul>
  </header>
  <section class="rv-pair" aria-labelledby="t-h">
    <h2 id="t-h">The state roles · {len(ROLES)}, each in both themes</h2>
    <div class="rv-wrap"><table><thead><tr><th>Role</th><th>Dark</th><th>Light</th></tr></thead><tbody>{roles}</tbody></table></div>
    <p>Contrast of the state pairs the build checks (generated at the end of <code>tokens.css</code>; the build stops if one fails in either theme):</p>
    <div class="rv-wrap"><table><thead><tr><th>Pair</th><th>Dark · light · needs</th></tr></thead><tbody>{contrast}</tbody></table></div>
  </section>
  <section class="rv-pair" aria-labelledby="s-h">
    <h2 id="s-h">Screens</h2>
    {scr_html}
    <p>Unchanged screens: {H.escape(", ".join(scr_same)) or "none"}.</p>
  </section>
  {comp_html}
  <section class="rv-pair" aria-labelledby="u-h">
    <h2 id="u-h">Unchanged in both themes · {len(same)}</h2>
    <div class="rv-wrap"><table><thead><tr><th>Component</th><th>States</th></tr></thead><tbody>{"".join(f"<tr><td>{H.escape(c)}</td><td>{H.escape(', '.join(v))}</td></tr>" for c, v in same_by.items())}</tbody></table></div>
  </section>
</main>
</body>
</html>
'''
open(os.path.join(ROOT, 'ui/review-states.html'), 'w').write(page)
print(f'review-states: {n_changed} changed component states, {len(screens) - len(scr_same)} changed screens, {len(same)} unchanged; {len(keep)} shots kept')
