"""Build public/responsive-overview.html, the Lesson 10 overview (Responsive), on the lessons' template (scripts/lesson_page.py).

Run from anywhere:  python3 scripts/build_responsive_overview.py      (build_stand.py runs it with the 08 and 09 pages)
Re-run after editing CLAUDE.md (→ Responsive), concept/concept.md, concept/key-decisions.md, design-system/tokens/tokens.css
or ui/review-final/; the page is generated, never hand-edited, and every number is read from the files.

Visible: the hero (a short summary, a few numbers), the breakpoint and why (from tokens.css and CLAUDE.md), the viewer
with its width switch, live, the key decisions with their references (Lesson 10 cards from concept/key-decisions.md),
before and after (ui/review-final/, the step 7 fixes), the deliberate deviations. Folded under "More": the step 7 defect
table (from concept/concept.md), the review pages of the lesson, the record step by step.
"""
import os, re
import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_concept_overview as CO
import lesson_page as LP
ROOT, GH = CO.ROOT, CO.GH
md, inline, sections, esc = CO.md, CO.inline, CO.sections, CO.esc
read = lambda p: open(os.path.join(ROOT, p)).read()

CLAUDE = read('CLAUDE.md')
RESP = sections(CLAUDE)['Responsive']
CONCEPT = read('concept/concept.md')
TOK = read('design-system/tokens/tokens.css')
ST = LP.repo_stats()

# ---------------------------------------------------------------- the numbers, read from the files
BPS = re.findall(r'^\s*--(bp-[a-z]+):\s*([\d.]+)rem;', TOK, flags=re.M)
assert len(BPS) == 1, ('one breakpoint', BPS)
BP_REM = float(BPS[0][1]); BP_PX = round(BP_REM * 16)
tokpx = lambda n: float(re.search(r'^\s*--' + n + r':\s*([\d.]+)(rem|px);', TOK, flags=re.M).group(1)) * (16 if re.search(r'^\s*--' + n + r':\s*[\d.]+rem;', TOK, flags=re.M) else 1)
PANE, MAPMIN, GAP = tokpx('pane-w'), tokpx('map-min'), 16
assert round(GAP + PANE + GAP + PANE + GAP + MAPMIN) == BP_PX, ('the breakpoint is the two cards and the map', BP_PX)
N_MEDIA = len(re.findall(r'@media \(min-width', ''.join(read('design-system/components/' + f) for f in os.listdir(os.path.join(ROOT, 'design-system/components')) if f.endswith('.css') and f != 'index.css')))

def entry(head):   # a concept.md entry by the start of its heading
    m = re.search(r'^### ' + re.escape(head) + r'[^\n]*\n(.*?)(?=^#{2,3} |\Z)', CONCEPT, flags=re.M | re.S)
    assert m, f'concept/concept.md: no entry "{head}"'
    return m.group(0).split('\n', 1)[0].lstrip('# '), m.group(1)
s7_title, s7 = entry('Step 7: the final check, and one breakpoint')
s7_table = '\n'.join(l for l in s7.split('\n') if l.startswith('|'))
N_DEFECTS = len([l for l in s7_table.split('\n')[2:] if re.match(r'\| \d+ ', l)])
anchor = lambda h: re.sub(r'\s', '-', re.sub(r'[^\w\s-]', '', h.lower()))

# ---------------------------------------------------------------- the sections
bullets = {re.match(r'- \*\*([^*]+)\*\*', b).group(1): b for b in re.split(r'\n(?=- \*\*)', RESP.split('\n\n', 1)[1].strip()) if b.startswith('- **')}   # each top bullet with its sub-list
pick = lambda k: md(next(v for n, v in bullets.items() if n.startswith(k)))
summary = (f'One breakpoint, {BP_PX}px, set by the web app\'s own behavior: below it every width is the phone\'s, a tablet included; '
           'from it a web app, with a top bar on every page. Checked at 320, 390, 820, 1148 and 1440, and at 200% text.')
bp_body = (f'<div class="bp"><div class="bp-row">'
           f'<span class="bp-seg">{GAP:g}</span><span class="bp-seg bp-card">list card {PANE:g}</span><span class="bp-seg">{GAP:g}</span>'
           f'<span class="bp-seg bp-card">race card {PANE:g}</span><span class="bp-seg">{GAP:g}</span><span class="bp-seg bp-map">map ≥ {MAPMIN:g}</span></div>'
           f'<p class="bp-sum"><code>--bp-desktop</code> = {BP_REM:g}rem = <strong>{BP_PX}px</strong> at the default text size, {BP_PX * 2}px at 200%</p></div>'
           + pick('One breakpoint') + pick('Why one, not two') + pick('Where responsive behavior lives') + pick('The checks'))
viewer_body = LP.embed('wireframes/index.html#race-browse?width=desktop', 'The viewer, Desktop 1440',
    'tall', '<p class="note">The viewer\'s device toolbar switches the width: Phone 390, Tablet 820, Desktop 1440 '
    '(<code>#race-browse?width=tablet</code>). The frame is the page\'s viewport, so the page\'s own media queries pick the form; '
    'the screen\'s states sit beside it.</p>')
PAIRS = [('race-browse-1280', 'before-race-browse-1280.jpg', 'Race browse at 1280, a laptop window', 'Before: the phone\'s column and a bottom tab bar (the breakpoint was 1343). After: the desktop, from 1148.'),
         ('filters-820', None, 'Filters on a tablet, 820', 'Before: a 620px form sheet cut OCR, the seventh sport type. After: the phone\'s sheet, every sport type in it.'),
         ('log-result-820', None, 'Log result on a tablet, 820', 'Before: footers at 116 characters a line. After: running text at --measure, 65ch.'),
         ('log-result-1440', None, 'Log result on a desktop', 'Before: a form sheet on a black void. After: over Results list, dimmed.'),
         ('race-detail-1440', None, 'race-detail.html?race=utmb on a desktop', 'Before: a lone column without the top bar. After: Race browse with that race\'s card.'),
         ('results-chosen-1440', None, 'Results list, a result chosen', 'Before: "Add official result link" twice, the row\'s hanging under it. After: said once, the list wider.')]
def pair(key, before, title, note):
    b = 'ui/review-final/' + (before or f'before-{key}.webp'); a = f'ui/review-final/after-{key}.webp'
    return (f'<figure class="ba"><figcaption><strong>{esc(title)}</strong> · {esc(note)}</figcaption><div class="ba-row">'
            f'<a href="{b}"><img src="{b}" alt="Before: {esc(title)}" loading="lazy"><span>Before</span></a>'
            f'<a href="{a}"><img src="{a}" alt="After: {esc(title)}" loading="lazy"><span>After</span></a></div></figure>')
ba_body = ''.join(pair(*p) for p in PAIRS) + f'<p class="note">Every screen and state at 390, 820 and 1440, after the fixes: <a href="ui/review-layout.html">ui/review-layout.html</a>.</p>'
dev_body = '<ul class="devs">' + ''.join(f'<li>{inline(x.strip())}</li>' for x in re.sub(r'^- \*\*Deliberate deviations:\*\*\s*', '', bullets['Deliberate deviations:']).split(';')) + '</ul>' \
    + f'<p class="note">Recorded, not defects: <code>DESIGN.md</code> → Width, <code>responsive/width-audit.md</code>, <code>concept/concept.md</code> → Lesson 10.</p>'
REVIEWS = [('ui/review-shell.html', 'Step 3 · the adaptive shell'), ('ui/review-adaptive.html', 'Step 4 · adaptive components'),
           ('ui/review-split.html', 'Step 5 · the Split view'), ('ui/review-webapp.html', 'The tablet the phone\'s, the desktop a web app'),
           ('ui/review-gate.html', 'The sign-in screens on wide screens'), ('ui/review-results.html', 'Results list on a desktop'),
           ('ui/review-forms.html', 'Forms on a tablet'), ('ui/review-layout.html', 'Step 7 · every screen and state, the final check')]
REVIEWS = [r for r in REVIEWS if os.path.exists(os.path.join(ROOT, r[0]))]
reviews_body = '<div class="card-grid">' + ''.join(
    f'<a class="card-link" href="{h}"><span class="si-tag" style="color:var(--accent)">Review</span><span class="si-title">{esc(t)}</span><span class="si-desc">{h} →</span></a>' for h, t in REVIEWS) + '</div>'
heads = re.findall(r'^### (.+)$', CONCEPT.split('## Lesson 10: responsive', 1)[1].split('\n## ', 1)[0], flags=re.M)
RECORD = [(h, GH + 'concept/concept.md#' + anchor(h), '') for h in heads]
MORE = (LP.fold(f'The final check (step 7): {N_DEFECTS} defects and the audit', md(s7_table) + f'<p class="note">From <a href="{GH}concept/concept.md#{anchor(s7_title)}">concept/concept.md → {esc(s7_title)}</a>.</p>', 'every defect and how it was fixed')
        + LP.fold(f'{len(REVIEWS)} review pages', reviews_body, 'before and after, step by step')
        + LP.fold('The record, step by step', LP.strip(RECORD), f'{len(RECORD)} entries in concept/concept.md → Lesson 10'))
decisions, n_dec = LP.key_decisions(10, inline)
SECTIONS = ''.join([
    LP.section('breakpoint', 'Rule', 'tag-d', 'One breakpoint, and why', bp_body),
    LP.section('viewer', 'Live', 'tag-p', 'The viewer\'s width switch', viewer_body),
    LP.section('decisions', 'Decided', 'tag-t', 'Key decisions, with their references', decisions),
    LP.section('beforeafter', 'Fixed', 'tag-f', 'Before and after', ba_body),
    LP.section('deviations', 'Deviations', 'tag-m', 'Deliberate deviations, not defects', dev_body),
    LP.section('more', 'More', 'tag-m', 'The rest of the record', MORE)])
STAGES = [('breakpoint', 'Rule', 'The breakpoint'), ('viewer', 'Live', 'The viewer'), ('decisions', 'Decided', 'Key decisions'),
          ('beforeafter', 'Fixed', 'Before and after'), ('deviations', 'Deviations', 'Deviations'), ('more', 'More', 'The record')]
STATS = [(1, 'breakpoint', f'--bp-desktop, {BP_PX}px'), (3, 'widths in the viewer', '390, 820, 1440'),
         (N_MEDIA, 'width queries', 'all in components, at the one number'), (N_DEFECTS, 'defects fixed', 'in the final check'),
         (len(ST['checks']), 'build checks', 'each stops the build')]
EXTRA_CSS = '''
  .bp{margin:6px 0 18px}
  .bp-row{display:flex; gap:2px; font-size:12.5px; font-weight:700; overflow-x:auto}
  .bp-seg{flex:0 0 auto; padding:10px 8px; border:1px solid var(--border); border-radius:6px; color:var(--text-faint); white-space:nowrap}
  .bp-card{flex:3 0 auto; color:var(--text)}
  .bp-map{flex:2.5 0 auto; color:var(--text); border-style:dashed}
  .bp-sum{margin-top:10px}
  .ba{margin:0 0 26px}
  .ba figcaption{margin:0 0 8px; max-width:none; text-align:left; color:var(--text-dim)}
  .ba-row{display:grid; grid-template-columns:1fr 1fr; gap:12px}
  .ba-row a{display:grid; gap:6px; color:var(--text-faint); font-size:12.5px; font-weight:700; text-decoration:none}
  .ba-row img{display:block; width:100%; height:auto; border:1px solid var(--border); border-radius:6px; background:#131518}
  .devs li{margin-bottom:8px}
  @media (max-width:640px){ .ba-row{grid-template-columns:1fr} }
'''
PAGE = LP.render(10, 'Responsive', 'responsive-overview.html', '15–20 Nov 2026', 'Every screen at every width, from one breakpoint', inline(summary),
    STATS, STAGES, None, None, SECTIONS, None, None, ['scripts/build_responsive_overview.py', 'scripts/lesson_page.py'], extra_css=EXTRA_CSS)
open(os.path.join(ROOT, 'public/responsive-overview.html'), 'w').write(PAGE)
print('responsive overview: breakpoint', BP_PX, 'decisions', n_dec, 'defects', N_DEFECTS, 'reviews', len(REVIEWS), 'bytes', len(PAGE))
