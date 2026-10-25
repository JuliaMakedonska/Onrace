"""Build public/ui-overview.html, the Lesson 7 overview (UI assembly), on the lessons' template (scripts/lesson_page.py).

Run from anywhere:  python3 scripts/build_ui_overview.py
Re-run after editing CLAUDE.md (Sources of truth, UI assembly), DESIGN.md, concept/concept.md (→ Native iOS),
ui/inventory.md, visuals/README.md, ui/kit.css, ui/map.css or build_stand.py; the page is generated, never hand-edited.
Every line on the page is rendered from those files and every count is read from the files it describes. It shares the
Lesson 6 overview's helpers (scripts/build_concept_overview.py, imported, which also rebuilds that page).
"""
import os, re, glob, json
import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_concept_overview as CO
import lesson_page as LP
ROOT, GH = CO.ROOT, CO.GH
md, inline, sections, para, esc = CO.md, CO.inline, CO.sections, CO.para, CO.esc
read = lambda p: open(os.path.join(ROOT, p)).read()

DESIGN = read('DESIGN.md')
DS = sections(DESIGN.split('\n---\n', 1)[1] if DESIGN.startswith('---') else DESIGN)
NATIVE_HEAD = 'Native iOS (designer rule, 2026-10-18)'
NATIVE = sections(CO.CS[NATIVE_HEAD], '### ')
INV = read('ui/inventory.md')
IS = sections(INV)
VIS = read('visuals/README.md')
VS = sections(VIS)
CLAUDE = read('CLAUDE.md')
CL = sections(CLAUDE)
ASSEMBLY = CL['UI assembly']
S6 = NATIVE['Step 6: critique fixes (designer priorities, 2026-10-25)']
S7 = NATIVE['Step 7: the final check (designer priorities, 2026-10-25)']
ST = LP.repo_stats()
first = lambda t: re.split(r'(?<=[.!?])\s', re.sub(r'\s+', ' ', t.strip()), 1)[0]
bold_led = lambda lead, rest: f'<strong>{inline(lead)}</strong> {inline(rest)}'

# ---------------------------------------------------------------- dispositions (the step 6 and 7 tables in concept.md)
def dispositions(body):
    t = re.search(r'\*\*Dispositions\*\*[^\n]*\n\n((?:\|[^\n]*\n)+)', body).group(1)
    rows = [[c.strip() for c in l.strip().strip('|').split(' | ')] for l in t.strip().split('\n')[2:]]
    return [(r[0], int(r[1]), r[2] if len(r) > 2 else '') for r in rows]
D6, D7 = dispositions(S6), dispositions(S7)
N6, N7 = sum(n for _, n, _ in D6), sum(n for _, n, _ in D7)
def dispo_card(title, rows, total, link):
    lis = ''.join(f'<li><span class="dn">{n}</span> {esc(k)}{(" <span class=dr>" + inline(r) + "</span>") if r and n else ""}</li>' for k, n, r in rows)
    return f'<div class="dispo"><p class="dispo-t">{title}</p><p class="dispo-n">{total}</p><ul>{lis}</ul><p class="dispo-l"><a href="{link}">The record →</a></p></div>'
dispo_body = '<div class="dispos">' + dispo_card('Step 6 · the critique (four subagents)', D6, N6, CO.anchor('Step 6: critique fixes (designer priorities, 2026-10-25)')) + \
    dispo_card('Step 7 · the final check and its re-check', D7, N7, CO.anchor('Step 7: the final check (designer priorities, 2026-10-25)')) + '</div>'

# ---------------------------------------------------------------- where each change goes in (CLAUDE.md → Sources of truth)
SRC_ROWS = [[c.strip() for c in l.strip().strip('|').split(' | ')] for l in CL['Sources of truth'].strip().split('\n')[2:] if l.startswith('|')]
FLOW = [('A value', 'ui/kit.css', ':root, one token', 'Look'), ('A look', 'ui/kit.css', 'a kit class, shown in ui/kit.html', 'Look'),
        ('A word', 'microcopy.md', 'one row, then voice.html', 'Words'), ('Structure', 'wireframes/*.html', 'the page, and every screen that shares it', 'Structure')]
assert {r[0].split('**')[1] for r in SRC_ROWS} >= {'Look', 'Words', 'Structure', 'Decisions'}
flow_body = '<div class="flow">' + ''.join(
    f'<div class="flow-row"><span class="flow-from">{a}</span><span class="flow-arrow" aria-hidden="true">→</span><span class="flow-to"><code>{f}</code><span class="flow-how">{h}</span></span></div>'
    for a, f, h, _ in FLOW) + '</div>' + LP.fold('The sources of truth', md(CL['Sources of truth']), 'the table at the top of CLAUDE.md and README.md')
checks_body = f'''<h3>Where each change goes in</h3>
{flow_body}
{LP.fold(f"{len(ST['checks'])} checks that stop the build", '<ol class="checks">' + "".join(f"<li>{inline(c)}</li>" for c in ST["checks"]) + '</ol><p class="note">Listed in <code>CLAUDE.md</code> → UI assembly; run by <code>scripts/concept/build_stand.py</code>, which calls <code>scripts/check_overflow.mjs</code> and <code>scripts/check_kit.py</code>.</p>', 'color rules, contrast, signed tokens, overflow, one line, fonts, scripts, the showcase')}'''

# ---------------------------------------------------------------- the Wireframe / Design switch (the viewer's two folders)
PAGES = sorted(os.path.basename(p)[:-5] for p in glob.glob(os.path.join(ROOT, 'wireframes/*.html')) if not p.endswith('index.html'))
FROZEN = {os.path.basename(p)[:-5] for p in glob.glob(os.path.join(ROOT, 'wireframes/_wireframe/*.html'))}
assert set(PAGES) <= FROZEN
options = ''.join(f'<option value="{p}"{" selected" if p == "race-browse" else ""}>{p}</option>' for p in PAGES)
look_body = f'''<p>The same screen as the frozen Lesson 5 wireframe or as it is now. Pick a screen and switch.</p>
{LP.fold('About the toggle', md(para(CLAUDE.split("## Wireframes", 1)[1], "- **Wireframe / Design toggle (2026-10-18):**").lstrip("- ")), 'from CLAUDE.md → Wireframes')}
<div class="look">
  <div class="look-controls">
    <label for="look-page">Screen and state</label>
    <select id="look-page">{options}</select>
    <div class="look-switch" role="group" aria-label="Wireframe or Design">
      <button type="button" data-mode="wireframe" aria-pressed="false">Wireframe</button>
      <button type="button" data-mode="design" aria-pressed="true">Design</button>
    </div>
    <a class="btn" id="look-open" href="wireframes/index.html#race-browse">Open it in the viewer →</a>
  </div>
  {CO.phone('race-browse.html', 'Race browse', [('race-browse.html', 'Design'), ('_wireframe/race-browse.html', 'Wireframe')], 'The frozen Lesson 5 wireframe or the screen as it is now: the same file name in <code>wireframes/_wireframe/</code> or <code>wireframes/</code>.').replace('<figure class="phone-fig">', '<figure class="phone-fig" id="look-fig">')}
</div>'''
LOOK_JS = '''(function () {
  var sel = document.getElementById('look-page'), fig = document.getElementById('look-fig');
  var frame = fig.querySelector('iframe'), open = document.getElementById('look-open'), mode = 'design';
  var btns = Array.prototype.slice.call(document.querySelectorAll('.look-switch button'));
  function show() {
    frame.src = 'wireframes/' + (mode === 'wireframe' ? '_wireframe/' : '') + sel.value + '.html';
    frame.title = sel.value + ', ' + mode;
    open.href = 'wireframes/index.html#' + sel.value + (mode === 'wireframe' ? '?mode=wireframe' : '');
    btns.forEach(function (b) { b.setAttribute('aria-pressed', String(b.getAttribute('data-mode') === mode)); });
  }
  sel.addEventListener('change', show);
  btns.forEach(function (b) { b.addEventListener('click', function () { mode = b.getAttribute('data-mode'); show(); }); });
})();'''

# ---------------------------------------------------------------- the stage sections (as before, from the same files)
design_body = LP.fold('DESIGN.md → Overview', md(DS["Overview"]), 'the system in a page') + f'<p><a class="btn" href="{GH}DESIGN.md">Open DESIGN.md →</a></p>'
inv_intro = INV.split('\n## ', 1)[0].split('\n', 1)[1]
role_counts = {}
for l in IS['Showcase map (2026-10-26)'].split('\n'):
    if l.startswith('| ') and not l.startswith(('| Role', '|---')):
        role_counts[l.split(' | ')[0].strip('| ')] = role_counts.get(l.split(' | ')[0].strip('| '), 0) + 1
inventory_body = f'''{LP.fold('How the inventory reads', md(inv_intro))}
<div class="tbl-wrap"><table><thead><tr><th>Role</th><th>Components</th></tr></thead><tbody>{"".join(f"<tr><td>{r}</td><td>{n}</td></tr>" for r, n in role_counts.items())}</tbody></table></div>
<p class="note">Roles as <code>ui/inventory.md</code> → Showcase map groups them; the kit showcase's nav follows it.</p>
<p><a class="btn" href="{GH}ui/inventory.md">Open the inventory →</a> <a class="btn" href="ui/kit.html">The showcase →</a></p>'''
kit_body = f'''<p>The showcase, live: every component in its states, with its role nav working inside the panel. Beside it, the shell every top-level screen shares.</p>
<div class="embeds">
  {LP.embed('ui/kit.html', 'The kit · <code>ui/kit.html</code>')}
  {LP.embed('ui/shell.html', 'The shell · <code>ui/shell.html</code>', 'phone')}
</div>
{LP.fold('Where the kit lives', md(ASSEMBLY.split(chr(10) + chr(10), 1)[1].split('**Visuals', 1)[0]), 'ui/kit.css, ui/map.css, ui/shell.html, ui/kit.html, ui/inventory.md')}
{LP.fold('The rules', md('**The rules:**' + ASSEMBLY.split('**The rules:**', 1)[1].split('**Checks that stop the build', 1)[0].split(chr(10), 1)[1]), 'every screen links the kit, "keep it", native iOS')}'''
ios_body = LP.fold('The HIG rule, the component table and C1–C7', md(DS['Native iOS']), '7 decided conflicts')
PHOTOS = [m.group(1) for m in re.finditer(r'^\| ([a-z0-9-]+) \| [^|]+ \| \d+% \|', VS['Export (step 7, 2026-10-25)'], flags=re.M)]
thumbs = ''.join(f'<figure class="thumb"><picture><source type="image/avif" srcset="visuals/{p}-684.avif"><source type="image/webp" srcset="visuals/{p}-684.webp"><img src="visuals/{p}-684.jpg" alt="" width="684" height="228" loading="lazy"></picture><figcaption>{p}</figcaption></figure>' for p in PHOTOS)
visuals_body = f'''<div class="thumbs">{thumbs}</div>
{LP.fold('How they were made', md(VIS.split(chr(10) + '## ', 1)[0].split(chr(10), 1)[1]) + '<h3>Tool</h3>' + md(VS['Tool']) + '<h3>Workflow</h3>' + md(VS['Workflow']), 'the tool, the workflow, the check')}
{LP.fold('How they were exported', md(VS['Export (step 7, 2026-10-25)']), '3:1 crops, AVIF / WebP / JPEG, srcset')}
<p><a class="btn" href="{GH}visuals/README.md">Open visuals/README.md →</a> <a class="btn" href="visuals/review-round3.html">Round 3 retouching review →</a></p>'''
native = lambda t: LP.fold(inline(t), md(NATIVE[t]))
assembly_body = '\n'.join(native(t) for t in ['Step 3b: native iOS pass in the kit (2026-10-19)', 'Step 5, Discovery: Race detail on the kit (2026-10-22)',
                                               'Step 5, Archive and Infrastructure on the kit (2026-10-22)', 'Consolidation (2026-10-23)'])
markup_body = '\n'.join(native(t) for t in ['Markup pass (2026-10-23)', 'Markup pass, round 2 (2026-10-23)', 'Race picker pushed (designer, 2026-10-24)',
                                             'Overflow fix: the controls bar (designer report, 2026-10-24)', 'Overflow check, round 2 (designer, 2026-10-25)'])
critique_body = LP.fold(f'{N6 + N7} findings', dispo_body, f'step 6: {N6} · step 7: {N7} · by disposition') + native('Step 6: critique fixes (designer priorities, 2026-10-25)') + \
    LP.fold(inline('Step 7: the final check (designer priorities, 2026-10-25)'), md(S7.split('**Still deferred', 1)[0]))
REVIEWS = sorted(glob.glob(os.path.join(ROOT, 'ui/review-*.html'))) + [os.path.join(ROOT, 'visuals/review-round3.html')]
title_of = lambda p: re.search(r'<title>([^<]+)</title>', open(p).read()).group(1).strip()
reviews_body = '<div class="card-grid">' + ''.join(
    f'<a class="card-link" href="{os.path.relpath(p, ROOT)}"><span class="si-tag" style="color:var(--accent)">Before / after</span><span class="si-title">{esc(title_of(p))}</span><span class="si-desc">{os.path.relpath(p, ROOT)} →</span></a>'
    for p in REVIEWS) + '</div>'

# ---------------------------------------------------------------- the decision register (concept.md → Native iOS; DESIGN.md → C1–C7)
REG = CO.cards_from(NATIVE_HEAD, CO.CS[NATIVE_HEAD].split('\n### ', 1)[0], 'paras')
for head, mode in [('Native sheet anatomy (the Filters sheet, designer decision 2026-10-18)', 'items'), ('Kit feedback (designer, 2026-10-19)', 'items'),
                   ('Step 3b review (designer, 2026-10-19)', 'items'), ('Step 5 review (designer, 2026-10-23)', 'items')]:
    REG += CO.cards_from(head, NATIVE[head], mode)
for m in re.finditer(r'^- \*\*(C\d [^:*]+):\*\* (.*)$', DS['Native iOS'], flags=re.M):
    REG.append((inline(m.group(1)), inline(CO.first_sentences(m.group(2))), '2026-10-18', 'DESIGN.md → Native iOS', GH + 'DESIGN.md#native-ios'))
h = 'Race picker pushed (designer, 2026-10-24)'
REG.append(('Race picker: a sheet or a pushed screen?', inline(first(NATIVE[h])), '2026-10-24', h, CO.anchor(h)))
h = 'Overflow fix: the controls bar (designer report, 2026-10-24)'
m = re.search(r'^\*\*"Clear all filters": (.+?)\*\* (.*)$', NATIVE[h], flags=re.M)
REG.append(('"Clear all filters": its own line, or pinned?', f'<strong>{inline(m.group(1))}</strong>', '2026-10-24', h, CO.anchor(h)))
dec6 = S6.split('**Designer decisions (the conflict rows):**', 1)[1].split('\n\n', 1)[0]
for m in re.finditer(r'^- \*\*(#\d+)(?:, (.+?))?:?\*\*:? ?(.*)$', dec6, flags=re.M):
    lead = f'<strong>{inline(m.group(2))}</strong> ' if m.group(2) else ''
    REG.append((f'Critique {m.group(1)}', lead + inline(CO.first_sentences(m.group(3), 200)), '2026-10-25',
                'Step 6: critique fixes', CO.anchor('Step 6: critique fixes (designer priorities, 2026-10-25)')))
m = re.search(r"^\*\*Designer decision:\*\* (.*)$", S7, flags=re.M)
REG.append(('Profile: the menu values in Text 1 or Text 2?', inline(m.group(1)), '2026-10-25', 'Step 7: the final check', CO.anchor('Step 7: the final check (designer priorities, 2026-10-25)')))

# ---------------------------------------------------------------- what's open (concept.md → Step 7, each with its lesson)
OPEN_ROWS = []
for m in re.finditer(r'^- (.+?) → Lesson (\d\d) \(([^)]+)\)(.*)$', S7.split('**Still deferred', 1)[1], flags=re.M):
    OPEN_ROWS.append((m.group(1), m.group(2), 'Proposed in `concept.md` → Step 7; the designer confirms when that lesson starts'))
assert len(OPEN_ROWS) >= 5

# ---------------------------------------------------------------- what we saw, what we decided (sentences from the record)
OVF = NATIVE['Overflow fix: the controls bar (designer report, 2026-10-24)']
SAW = [bold_led('HIG gaps.', first(NATIVE['Gap triage (2026-10-18)']) if 'Gap triage (2026-10-18)' in NATIVE else ''),
       bold_led('Overflow at 390.', first(re.search(r'\*\*The defect:\*\* (.*)', OVF).group(1))),
       bold_led('The critique.', first(S6.split('\n\n', 1)[0])),
       bold_led('The final check.', first(S7.split('\n\n', 1)[0]))]
DECIDED = [bold_led('Native iOS.', first(re.search(r'\*\*The rule\.\*\* (.*)', CO.CS[NATIVE_HEAD]).group(1))),
           bold_led('"Keep it".', re.search(r'\*\*"Keep it" rule \(2026-10-25\):\*\* (.*)', ASSEMBLY).group(1)),
           bold_led('One kit.', re.search(r'- \*\*`ui/kit.css`:\*\* (.*?\.)', ASSEMBLY).group(1)),
           bold_led('Race picker.', first(NATIVE['Race picker pushed (designer, 2026-10-24)'])),
           bold_led('Result detail.', re.search(r'\*\*#11, (.+?)\*\*', S6).group(1) + '.'),
           bold_led('Icons.', re.search(r'\*\*#23, (.+?)\*\*', S6).group(1) + '.')]

# ---------------------------------------------------------------- the page
EXTRA_CSS = CO.DEVICE_CSS + '''
  .thumbs{display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,220px),1fr)); gap:12px; margin:8px 0 18px}
  .thumb{margin:0}
  .thumb img{display:block; width:100%; height:auto; border-radius:6px; filter:grayscale(1) contrast(1.12) brightness(.85)}
  .thumb figcaption{margin:6px 0 0; font-size:12.5px; color:var(--text-faint)}
  .look{display:grid; grid-template-columns:minmax(0,280px) minmax(0,1fr); gap:24px; align-items:start; margin:16px 0}
  .look-controls{display:grid; gap:10px; align-content:start}
  .look .device-slot{overflow:hidden}   /* the frame is scaled to fit; its unscaled box mustn't widen the page */
  .look-controls label{font-size:12px; font-weight:800; text-transform:uppercase; letter-spacing:.06em; color:var(--text-faint)}
  .look-controls select{min-height:44px; background:var(--bg-elev); color:var(--text); border:1px solid var(--border); border-radius:8px; padding:0 10px; font:inherit}
  .look-switch{display:grid; grid-template-columns:1fr 1fr; background:var(--bg-elev); border:1px solid var(--border); border-radius:999px; padding:3px}
  .look-switch button{min-height:40px; border:0; border-radius:999px; background:transparent; color:var(--text-dim); font:inherit; font-weight:700; cursor:pointer}
  .look-switch button[aria-pressed="true"]{background:var(--accent-dim); color:var(--accent)}
  .look-switch button:focus-visible, .look-controls select:focus-visible{outline:2px solid var(--text); outline-offset:2px}
  @media (max-width:760px){ .look{grid-template-columns:minmax(0,1fr)} }
  .flow{display:grid; gap:10px; margin:12px 0 18px}
  .flow-row{display:grid; grid-template-columns:minmax(0,160px) 32px minmax(0,1fr); align-items:center; gap:8px}
  .flow-from{background:var(--bg-elev); border:1px solid var(--border); border-radius:8px; padding:10px 12px; font-weight:700; color:var(--text)}
  .flow-arrow{text-align:center; color:var(--accent); font-weight:800; font-size:18px}
  .flow-to{background:var(--bg-elev-2); border:1px solid var(--border); border-left:3px solid var(--accent); border-radius:8px; padding:10px 12px; display:grid; gap:2px}
  .flow-how{font-size:12.5px; color:var(--text-faint)}
  @media (max-width:560px){ .flow-row{grid-template-columns:minmax(0,1fr)} .flow-arrow{text-align:left; transform:rotate(90deg); width:20px} }
  .checks{padding-left:22px}
  .checks li{margin-bottom:8px}
  .dispos{display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr)); gap:14px; margin:6px 0 18px}
  .dispo{background:var(--bg-elev); border:1px solid var(--border); border-radius:var(--radius); padding:16px 18px}
  .prose .dispo-t{margin:0; color:var(--text); font-weight:700}
  .prose .dispo-n{margin:4px 0 8px; font-size:36px; font-weight:800; color:var(--text); line-height:1.1}
  .dispo ul{list-style:none; padding:0; margin:0}
  .dispo li{font-size:13.5px}
  .dn{display:inline-block; min-width:28px; font-weight:800; color:var(--text)}
  .dr{display:block; color:var(--text-faint); font-size:12.5px; margin:2px 0 6px 28px}
  .prose .dispo-l{margin:8px 0 0; font-size:13px}
'''
# ---------------------------------------------------------------- the page: what was made, how to see it, how it works, what was decided
HIG = 'https://developer.apple.com/design/human-interface-guidelines'
c6 = lambda n: re.search(r'^- \*\*#' + n + r', (.+?)\*\*(.*)$', dec6, flags=re.M)
S6_HEAD = 'Step 6: critique fixes (designer priorities, 2026-10-25)'
KEY = [   # the decisions a reader needs first; the full register is folded under them
    ('Native iOS', inline(first(re.search(r'\*\*The rule\.\*\* (.*)', CO.CS[NATIVE_HEAD]).group(1))) + f' <a href="{HIG}">The Human Interface Guidelines ↗</a>',
     '2026-10-18', 'concept.md → Native iOS', CO.anchor(NATIVE_HEAD)),
    ('Liquid Glass (C1)', inline(CO.first_sentences(re.search(r'^- \*\*C1 Liquid Glass:\*\* (.*)$', DS['Native iOS'], flags=re.M).group(1), 220)),
     '2026-10-18', 'DESIGN.md → Native iOS', GH + 'DESIGN.md#native-ios'),
    ('Solar Linear for small glyphs', '<strong>' + inline(c6('23').group(1)) + '</strong>' + inline(CO.first_sentences(c6('23').group(2), 200)),
     '2026-10-25', 'concept.md → Step 6', CO.anchor(S6_HEAD)),
    ('Our own race photos', inline(first(VIS.split('\n## ', 1)[0].split('\n', 2)[2])), '2026-10-20', 'visuals/README.md', GH + 'visuals/README.md'),
    ('The frozen wireframe snapshot', inline(CO.first_sentences(para(CLAUDE.split('## Wireframes', 1)[1], '- **Wireframe / Design toggle (2026-10-18):**').split(':** ', 1)[1], 240)),
     '2026-10-18', 'CLAUDE.md → Wireframes', GH + 'CLAUDE.md#wireframes'),
    ('The finish time leads Result detail', '<strong>' + inline(c6('11').group(1)) + '</strong>' + inline(CO.first_sentences(c6('11').group(2), 200)),
     '2026-10-25', 'concept.md → Step 6', CO.anchor(S6_HEAD)),
    ('The "keep it" rule', inline(re.search(r'\*\*"Keep it" rule \(2026-10-25\):\*\* (.*)', ASSEMBLY).group(1)),
     '2026-10-25', 'CLAUDE.md → UI assembly', GH + 'CLAUDE.md#ui-assembly'),
]
PHOTO_ROWS = re.findall(r'^\| ([a-z0-9-]+) \| ([^|]+?) \| \d+% \|', VS['Export (step 7, 2026-10-25)'], flags=re.M)
photo_strip = '<div class="thumbs">' + ''.join(
    f'<figure class="thumb"><picture><source type="image/avif" srcset="visuals/{p}-684.avif"><source type="image/webp" srcset="visuals/{p}-684.webp">'
    f'<img src="visuals/{p}-684.jpg" alt="" width="684" height="228" loading="lazy"></picture><figcaption><strong>{esc(race)}</strong> · {p}</figcaption></figure>'
    for p, race in PHOTO_ROWS) + '</div>'
summary = ' '.join(re.split(r'(?<=[.!?])\s', re.sub(r'\s+', ' ', ASSEMBLY.strip().split('\n\n', 1)[0]))[:2])
RECORD = [(inline(t), CO.anchor(t), '') for t in ['Step 3b: native iOS pass in the kit (2026-10-19)', 'Step 5, Discovery: Race detail on the kit (2026-10-22)',
          'Step 5, Archive and Infrastructure on the kit (2026-10-22)', 'Consolidation (2026-10-23)', 'Markup pass (2026-10-23)', 'Markup pass, round 2 (2026-10-23)',
          'Race picker pushed (designer, 2026-10-24)', 'Overflow fix: the controls bar (designer report, 2026-10-24)', 'Overflow check, round 2 (designer, 2026-10-25)',
          S6_HEAD, 'Step 7: the final check (designer priorities, 2026-10-25)']]
inv_rows = ''.join(f'<tr><td>{r}</td><td>{n}</td></tr>' for r, n in role_counts.items())
inv_more = (f'<div class="tbl-wrap"><table><thead><tr><th>Role</th><th>Components</th></tr></thead><tbody>{inv_rows}</tbody></table></div>'
            f'<p><a class="btn" href="{GH}ui/inventory.md">Open ui/inventory.md →</a></p>')
MORE = (LP.fold(f'{N6 + N7} findings, by disposition', dispo_body, f'step 6: {N6} · step 7: {N7}')
        + LP.fold(f'The inventory: {ST["components"]} components', inv_more, 'by role, as the showcase groups them')
        + LP.fold('DESIGN.md, the HIG table and C1–C7', md(DS['Overview']) + md(DS['Native iOS']), 'the system, documented from the code')
        + LP.fold('The record, step by step', LP.strip(RECORD) + f'<p class="note">Every step is in <a href="{GH}concept/concept.md">concept/concept.md</a> → Native iOS.</p>', f'{len(RECORD)} entries in concept.md')
        + LP.fold(f'{len(REVIEWS)} review pages', reviews_body, 'before and after, step by step'))
flow_only = '<div class="flow">' + ''.join(
    f'<div class="flow-row"><span class="flow-from">{a}</span><span class="flow-arrow" aria-hidden="true">→</span><span class="flow-to"><code>{f}</code><span class="flow-how">{h}</span></span></div>'
    for a, f, h, _ in FLOW) + '</div>'
checks_list = ('<ol class="checks">' + ''.join(f'<li>{inline(c)}</li>' for c in ST['checks']) + '</ol>'
               '<p class="note">Listed in <code>CLAUDE.md</code> → UI assembly; run by <code>scripts/concept/build_stand.py</code>.</p>')
look_switch = look_body[look_body.index('<div class="look">'):]
SECTIONS = ''.join([
    LP.section('kit', 'Made', 'tag-m', 'The kit, live', '<p class="lede">Every component in its states, from <code>ui/kit.css</code> alone. Its role nav works inside the panel; the shell is in it too.</p>'
               + LP.embed('ui/kit.html', 'The kit · <code>ui/kit.html</code>')),
    LP.section('screens', 'See it', 'tag-p', 'The screens', '<p class="lede">Every screen and state, as the frozen Lesson 5 wireframe or as it is now. Pick one and switch.</p>' + look_switch),
    LP.section('system', 'How it works', 'tag-d', 'Where each change goes in', flow_only
               + LP.fold(f'{len(ST["checks"])} checks stop the build', checks_list, 'color rules, contrast, signed tokens, overflow at 390 / 320 / 200%, fonts, scripts, the showcase')),
    LP.section('decisions', 'Decided', 'tag-t', 'Key decisions', LP.register(KEY) + LP.fold(f'The full register: {len(REG)} decisions', LP.register(REG), 'each with its date and its entry')),
    LP.section('photos', 'Made', 'tag-o', 'The race photos', photo_strip
               + LP.fold('How they were made', md(VS['Tool']) + md(VS['Workflow']) + '<h3>Export</h3>' + md(VS['Export (step 7, 2026-10-25)']), 'generated, checked for text and logos, retouched, pre-cropped')),
    LP.section('open', 'Close', 'tag-f', "What's open", LP.open_table(OPEN_ROWS, inline)),
    LP.section('more', 'More', 'tag-m', 'The rest of the record', MORE)])
STAGES = [('kit', 'Made', 'The kit, live'), ('screens', 'See it', 'The screens'), ('system', 'How it works', 'Changes and checks'),
          ('decisions', 'Decided', 'Key decisions'), ('photos', 'Made', 'The photos'), ('open', 'Close', "What's open"), ('more', 'More', 'The record')]
STATS = [(ST['pages'], 'pages', f"{ST['screens']} screens and their states"), (ST['components'], 'inventory components', 'in ui/inventory.md'),
         (ST['variables'], 'kit tokens', 'in ui/kit.css and ui/map.css'), (len(ST['checks']), 'build checks', 'each stops the build')]
PAGE = LP.render(7, 'UI assembly', 'ui-overview.html', '18–26 Oct 2026', 'One kit, every screen, native iOS', inline(summary),
    STATS, STAGES, None, None, SECTIONS, None, None,
    ['scripts/build_ui_overview.py', 'scripts/lesson_page.py'], extra_css=EXTRA_CSS,
    scripts='<script>\n' + CO.DEVICE_JS + '\n' + LOOK_JS + '\n</script>')
open(os.path.join(ROOT, 'public/ui-overview.html'), 'w').write(PAGE)
print('ui overview: key', len(KEY), 'register', len(REG), 'open', len(OPEN_ROWS), 'photos', len(PHOTO_ROWS), 'bytes', len(PAGE))
