"""Build public/system-overview.html, the Lesson 9 overview (Design system), on the lessons' template (scripts/lesson_page.py).

Run from anywhere:  python3 scripts/build_system_overview.py      (build_stand.py runs it with the 08 page)
Re-run after editing CLAUDE.md (→ Design system), concept/concept.md, concept/key-decisions.md, design-system/backlog.md,
ui/inventory.md or the docs; the page is generated, never hand-edited, and every count is read from the files.

Visible: the hero (a short summary, a few numbers), the docs live in a frame, the key decisions (Lesson 09 cards from
concept/key-decisions.md), the backlog (design-system/backlog.md). Folded under "More": the step 7 defect table (from
concept/concept.md), the build checks, the review pages of the lesson, the record step by step.
"""
import os, re, glob
import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_concept_overview as CO
import lesson_page as LP
import docs_shell as DS
ROOT, GH = CO.ROOT, CO.GH
md, inline, sections, esc = CO.md, CO.inline, CO.sections, CO.esc
read = lambda p: open(os.path.join(ROOT, p)).read()

CLAUDE = read('CLAUDE.md')
DS_SEC = sections(CLAUDE)['Design system']
CONCEPT = read('concept/concept.md')
BACKLOG = read('design-system/backlog.md')
ST = LP.repo_stats()

# ---------------------------------------------------------------- the numbers, read from the files
N_COMP = len(DS.COMPONENTS)
N_SHOWN = len(DS.MERGED)
N_PATTERNS = len(glob.glob(os.path.join(ROOT, 'design-system/patterns/*.html')))
N_FOUND = len(DS.FOUNDATIONS)
DOC_PAGES = [p for p in glob.glob(os.path.join(ROOT, 'design-system/docs/*.html')) + glob.glob(os.path.join(ROOT, 'design-system/docs/components/*.html')) if 'http-equiv="refresh"' not in open(p).read()]
SIGNED = re.search(r'Signed tokens: (\d+) of (\d+)', open(os.path.join(ROOT, '.build.log')).read()) if os.path.exists(os.path.join(ROOT, '.build.log')) else None

def entry(head):   # a concept.md entry by the start of its heading
    m = re.search(r'^### ' + re.escape(head) + r'[^\n]*\n(.*?)(?=^#{2,3} |\Z)', CONCEPT, flags=re.M | re.S)
    assert m, f'concept/concept.md: no entry "{head}"'
    return m.group(0).split('\n', 1)[0].lstrip('# '), m.group(1)
s7_title, s7 = entry('Step 7: the system and the product checked together')
s7_table = '\n'.join(l for l in s7.split('\n') if l.startswith('|'))
N_DEFECTS = len([l for l in s7_table.split('\n')[2:] if l.startswith('| ')])

# ---------------------------------------------------------------- the sections
summary = ' '.join(re.split(r'(?<=[.!?])\s', re.sub(r'\s+', ' ', DS_SEC.strip().split('\n\n', 1)[0]))[:1])
docs_body = (LP.embed('design-system/docs/index.html', 'The design system docs', 'tall',
             '<p class="note">The same pages as <a href="design-system/docs/">design-system/docs/</a>: Getting started, Foundations, '
             f'{N_COMP} component pages under HIG\'s categories, {N_PATTERNS} patterns and every specimen, each linking the file the screens link. '
             'The example screen built only from the system: <a href="design-system/examples/saved-races.html">Saved races</a>.</p>'))
backlog_body = md(re.sub(r'^## ', '### ', BACKLOG.split('\n', 1)[1], flags=re.M)) + f'<p class="note">From <a href="{GH}design-system/backlog.md">design-system/backlog.md</a>, also <a href="design-system/docs/backlog.html">in the docs</a>.</p>'
checks_list = ('<ol class="checks">' + ''.join(f'<li>{inline(c)}</li>' for c in ST['checks']) + '</ol>'
               '<p class="note">Listed in <code>CLAUDE.md</code> → UI assembly; run by <code>scripts/concept/build_stand.py</code>.</p>')
REVIEWS = [('ui/review-states.html', 'Step 3 · component states'), ('ui/review-states-2.html', 'Step 3 follow-ups'),
           ('ui/review-optional-link.html', 'Step 5 · the optional official result link'), ('ui/review-sheets.html', 'Sheet spacing'),
           ('ui/review-rows.html', 'Grouped rows, one height'), ('ui/review-signout.html', 'Sign out, a grouped row'),
           ('ui/review-focus.html', 'The focus ring, variants, states by theme'), ('ui/review-sheet-bar.html', 'The sheet\'s bar'),
           ('ui/review-docs.html', 'The docs restructured'), ('ui/review-docs-2.html', 'The docs, quiet'), ('ui/review-docs-3.html', 'The docs, dark'),
           ('ui/review-docs-nav.html', 'Docs by navigation, the focus check'), ('ui/review-docs-fixes.html', 'Docs fixes, the ring, the sheet bar')]
REVIEWS = [r for r in REVIEWS if os.path.exists(os.path.join(ROOT, 'public', r[0]))]
reviews_body = '<div class="card-grid">' + ''.join(
    f'<a class="card-link" href="{h}"><span class="si-tag" style="color:var(--accent)">Review</span><span class="si-title">{esc(t)}</span><span class="si-desc">{h} →</span></a>' for h, t in REVIEWS) + '</div>'
heads = re.findall(r'^### (.+)$', CONCEPT.split('## Lesson 9: the design system', 1)[1].split('\n## ', 1)[0], flags=re.M)
anchor = lambda h: re.sub(r'\s', '-', re.sub(r'[^\w\s-]', '', h.lower()))
RECORD = [(h, GH + 'concept/concept.md#' + anchor(h), '') for h in heads]
MORE = (LP.fold(f'The final check (step 7): 22 defects in {N_DEFECTS} rows', md(s7_table) + f'<p class="note">From <a href="{GH}concept/concept.md#{anchor(s7_title)}">concept/concept.md → {esc(s7_title)}</a>.</p>', 'every defect and how it was fixed')
        + LP.fold(f'{len(ST["checks"])} checks stop the build', checks_list, 'color, contrast, tokens, overflow, focus, docs, names')
        + LP.fold(f'{len(REVIEWS)} review pages', reviews_body, 'before and after, step by step')
        + LP.fold('The record, step by step', LP.strip(RECORD), f'{len(RECORD)} entries in concept/concept.md → Lesson 9'))
decisions, n_dec = LP.key_decisions(9, inline)
SECTIONS = ''.join([
    LP.section('docs', 'Live', 'tag-d', 'The docs', docs_body),
    LP.section('decisions', 'Decided', 'tag-t', 'Key decisions', decisions),
    LP.section('backlog', 'Next', 'tag-f', 'The backlog', f'<div class="after">{backlog_body}</div>'),
    LP.section('more', 'More', 'tag-m', 'The rest of the record', MORE)])
STAGES = [('docs', 'Live', 'The docs'), ('decisions', 'Decided', 'Key decisions'), ('backlog', 'Next', 'The backlog'), ('more', 'More', 'The record')]
STATS = [(N_COMP, 'component pages', f'and {N_SHOWN} entries shown on another'), (N_FOUND, 'foundations', 'from DESIGN.md and the tokens'),
         (N_PATTERNS, 'patterns', 'each on three or more screens'), (len(DOC_PAGES), 'docs pages', 'each linking design-system/index.css'),
         (len(ST['checks']), 'build checks', 'each stops the build')]
EXTRA_CSS = '''
  .checks{padding-left:22px}
  .checks li{margin-bottom:8px}
  .after li{margin-bottom:10px}
  .after h2{font-size:17px; margin:18px 0 6px}
'''
PAGE = LP.render(9, 'Design system', 'system-overview.html', '3–10 Nov 2026', 'One design system, documented and checked', inline(summary),
    STATS, STAGES, None, None, SECTIONS, None, None, ['scripts/build_system_overview.py', 'scripts/lesson_page.py'], extra_css=EXTRA_CSS)
open(os.path.join(ROOT, 'public/system-overview.html'), 'w').write(PAGE)
print('system overview: components', N_COMP, 'decisions', n_dec, 'defects', N_DEFECTS, 'reviews', len(REVIEWS), 'bytes', len(PAGE))
