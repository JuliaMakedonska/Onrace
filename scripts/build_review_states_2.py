"""ui/review-states-2.html: the before/after of the Step 3 follow-ups (Lesson 9, 2026-11-06), the same way as
ui/review-states.html (scripts/build_review_states.py, of which this is a copy with its own header and folder).

Reads ui/review-states/shots.json, written by scripts/review_states.mjs (every component state on specimens.html and the
changed screens, before the step and after, dark and light), and design-system/tokens/tokens.css (the state roles and
their contrast). Shows every changed state with its four shots; lists the unchanged ones; deletes the unchanged shots.
Run from anywhere: python3 scripts/build_review_states.py   (after node scripts/review_states.mjs; not part of the build).
"""
import os, re, json, html as H
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'ui/review-states-2')
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
    return f'<img src="review-states-2/{key}-{theme}-{side}.webp" alt="{H.escape(alt)}" loading="lazy">'
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
<title>States follow-ups</title>
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
    <h1>Lesson 9 · step 3 follow-ups · component states</h1>
    <p>2026-11-06. Five follow-ups, made through the tokens and components, each in both themes. This page shows every state that changed, before (commit <code>d811d69</code>, the end of step 3) and after, dark and light: {n_changed} component states and {len(screens) - len(scr_same)} screens. Each state is the real one, forced by Chrome DevTools on the control and its ancestors (<code>scripts/review_states.mjs</code>). A theme where the state didn't change shows the after shot, dimmed. A state counts as changed when any computed style of the part changed, so a radius that computes differently but draws the same pixels at this size still shows here.</p>
    <ul>
      <li><b>The date tile and the format chip</b> stay one level above their card and move up with it: <code>--raised-hover</code> and <code>--raised-pressed</code> while the card is hovered or pressed (Race card, Result row), so they never merge into the card's state.</li>
      <li><b>The pressed amber dims:</b> <code>--accent-pressed</code> and the dark <code>--accent-ink-pressed</code> are <code>--amber-69</code> <code>#DF9A46</code>, darker than rest, its hue 7° warmer, clear of HYROX yellow under rule 3b on its own (26.6°, ΔE 25.8); the build stops if it isn't. Hover stays one step lighter. The light ink pressed stays <code>--amber-26</code>, so the Top bar's pressed shot changes in dark only.</li>
      <li><b>Tab bar icons</b> are chosen by <code>data-tab</code>, not by where the tab links, so the specimens show the real compass, stopwatch and person instead of squares.</li>
      <li><b>One capsule rule:</b> the search field, Filters, the action bar's button, the active filter chips, the tab bar and its tabs take <code>--radius-capsule</code>; the three half-height radii are retired. At this text size the shapes draw the same; at 200% text they stay capsules.</li>
      <li><b>A field error replaces only its own field's helper:</b> on New password with the passwords not matching, "At least 8 characters." stays; on Profile, the group note "Changes save as you make them…" stays beside a save error.</li>
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
open(os.path.join(ROOT, 'ui/review-states-2.html'), 'w').write(page)
print(f'review-states-2: {n_changed} changed component states, {len(screens) - len(scr_same)} changed screens, {len(same)} unchanged; {len(keep)} shots kept')
