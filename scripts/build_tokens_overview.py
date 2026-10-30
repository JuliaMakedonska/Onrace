"""Build public/tokens-overview.html, the Lesson 8 overview (Design tokens), on the lessons' template (scripts/lesson_page.py).

Run from anywhere:  python3 scripts/build_tokens_overview.py      (build_stand.py runs it after the 06 and 07 pages)
Re-run after editing CLAUDE.md (→ Tokens), tokens/tokens.css, tokens/tokens-audit.md, components/, concept/concept.md,
concept/key-decisions.md or build_stand.py; the page is generated, never hand-edited. Every line on it is rendered from
those files and every count is read from the files it describes, as on the 06 and 07 pages, whose helpers it shares.

Visible: the hero (a short summary, five numbers), primitive → role → component with the amber as the real example,
the light-theme stress test on a live screen with the two holes it found, the key decisions, "After the lesson".
Folded under "More": the audit, the old → new mapping, the build checks, the step 6 table, the review pages.
"""
import os, re, glob
import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_concept_overview as CO
import lesson_page as LP
ROOT, GH = CO.ROOT, CO.GH
md, inline, sections, esc = CO.md, CO.inline, CO.sections, CO.esc
read = lambda p: open(os.path.join(ROOT, p)).read()

CLAUDE = read('CLAUDE.md')
TOKENS_SEC = sections(CLAUDE)['Tokens']
TOK = read('tokens/tokens.css')
AUDIT = read('tokens/tokens-audit.md')
AS = sections(AUDIT)
COMP = read('components/index.css')
COMP_README = read('components/README.md')
ST = LP.repo_stats()

# ---------------------------------------------------------------- the numbers, read from the files
MAIN = re.search(r':root\s*\{(.*?)\n\}', TOK, flags=re.S).group(1)
PRIM, SEM = MAIN.split('     2. SEMANTIC: color roles\n')
code = lambda s: re.sub(r'/\*.*?\*/', '', s, flags=re.S)
N_PRIM = len(re.findall(r'^\s*--[a-z0-9-]+:', code(PRIM), flags=re.M))
N_COLOR_PRIM = len([1 for n, v in re.findall(r'^\s*--([a-z0-9-]+):\s*([^;]+);', code(PRIM), flags=re.M) if re.match(r'#[0-9A-Fa-f]{3,8}$', v.strip())])
ROLES = re.findall(r'^\s*--([a-z0-9-]+):', code(SEM), flags=re.M)
N_FILES = len([f for f in glob.glob(os.path.join(ROOT, 'components/*.css')) if not f.endswith('index.css')])
CONTRAST = re.search(r'/\* contrast:start.*?\n(.*?)\n   contrast:end \*/', TOK, flags=re.S).group(1)
ROLE_PAIRS = [l for l in CONTRAST.split('\n') if l.strip().startswith('--')]
BS = read('scripts/concept/build_stand.py')
N_USE_PAIRS = len(re.findall(r"^\s+\('[^\n]*', '[a-z0-9-]+', '[a-z0-9-]+', '(?:text|large|ui|exempt|info)'\),$", BS[BS.index('PAIRS = ['):BS.index('# ---------------------------------------------------------------- glass')], flags=re.M))
N_GLASS = len(re.findall(r"^\s+\('[^\n]*', '[a-z0-9-]+', '(?:bar|ground|sheet)', '(?:text|ui)'\),$", BS, flags=re.M))
assert N_PRIM and ROLES and N_FILES and ROLE_PAIRS and N_USE_PAIRS and N_GLASS

def val(name, theme='dark'):
    """A token's hex in a theme, following var() through the light block when asked."""
    light = dict(re.findall(r'^\s*--([a-z0-9-]+):\s*([^;]+);', code(re.search(r':root\[data-theme="light"\]\s*\{(.*?)\n\}', TOK, flags=re.S).group(1)), flags=re.M))
    v = (light.get(name) if theme == 'light' and name in light else re.search(r'--' + re.escape(name) + r':\s*([^;]+);', code(MAIN)).group(1)).strip()
    m = re.match(r'var\(--([a-z0-9-]+)\)$', v)
    return val(m.group(1), theme) if m else v
def prim_of(name, theme='dark'):
    light = dict(re.findall(r'^\s*--([a-z0-9-]+):\s*var\(--([a-z0-9-]+)\);', code(re.search(r':root\[data-theme="light"\]\s*\{(.*?)\n\}', TOK, flags=re.S).group(1)), flags=re.M))
    if theme == 'light' and name in light: return light[name]
    return re.search(r'--' + re.escape(name) + r':\s*var\(--([a-z0-9-]+)\)', code(SEM)).group(1)
def users(role):
    sels = []
    for sel, body in re.findall(r'([^{}]+)\{([^{}]*)\}', code(COMP)):
        if f'var(--{role})' in body: sels += [x.strip() for x in sel.split(',')]
    return sels

# ---------------------------------------------------------------- primitive → role → component, the amber as the example
FILL_USERS, INK_USERS = users('accent-fill'), users('accent-ink')
assert any('register-btn' in s for s in FILL_USERS) and any('bar-action' in s for s in INK_USERS)
sw = lambda hexv: f'<span class="sw" style="background:{hexv}"></span>'
def node(kind, name, hexv, note):
    return f'<div class="dg-node dg-{kind}"><span class="dg-k">{kind}</span><code>--{name}</code><span class="dg-v">{sw(hexv)}{hexv}</span><span class="dg-n">{note}</span></div>'
def comp(sel, what):
    return f'<div class="dg-node dg-component"><span class="dg-k">component</span><code>{esc(sel)}</code><span class="dg-n">{what}</span></div>'
amber = prim_of('accent-fill')
diagram = f'''<div class="dg">
  <div class="dg-row">
    {node('primitive', amber, val(amber), 'a raw value, named by hue and L*')}
    <span class="dg-arrow" aria-hidden="true">→</span>
    {node('role', 'accent-fill', val('accent-fill'), 'the primary action’s fill')}
    <span class="dg-arrow" aria-hidden="true">→</span>
    {comp('.register-btn', 'Register on hyrox.com, Race detail · also ' + str(len(FILL_USERS) - 1) + ' more selectors')}
  </div>
  <div class="dg-row">
    {node('primitive', amber, val(amber), 'the same primitive, in dark')}
    <span class="dg-arrow" aria-hidden="true">→</span>
    {node('role', 'accent-ink', val('accent-ink'), 'amber as text on a bar')}
    <span class="dg-arrow" aria-hidden="true">→</span>
    {comp('.top-bar .bar-action', 'Log result on Results list, and the current tab · ' + str(len(INK_USERS)) + ' selectors')}
  </div>
  <div class="dg-row dg-light">
    {node('primitive', prim_of('accent-ink', 'light'), val('accent-ink', 'light'), 'light theme only')}
    <span class="dg-arrow" aria-hidden="true">→</span>
    {node('role', 'accent-ink', val('accent-ink', 'light'), 'the same role, in light')}
    <span class="dg-arrow" aria-hidden="true">→</span>
    {comp('.top-bar .bar-action', 'the same component, untouched')}
  </div>
</div>
<p class="note">Read from <code>tokens/tokens.css</code> and <code>components/index.css</code>. In dark the fill and the ink are one amber; in light the ink takes a darker, warmer one so amber text holds AA on a light bar. The component never changes: only the role's value does.</p>'''

# ---------------------------------------------------------------- the stress test: a live screen, Light / Dark
PAGES = sorted(os.path.basename(p)[:-5] for p in glob.glob(os.path.join(ROOT, 'wireframes/*.html')) if not p.endswith('index.html'))
options = ''.join(f'<option value="{p}"{" selected" if p == "results-list" else ""}>{p}</option>' for p in PAGES)
holes = COMP_README.split('## The theme test', 1)[1].split('\n', 1)[1]
proof_body = f'''<p class="lede">The proof that every color goes through a role: a second appearance needs new role values and nothing else. Pick a screen and switch it.</p>
<div class="look">
  <div class="look-controls">
    <label for="theme-page">Screen and state</label>
    <select id="theme-page">{options}</select>
    <div class="look-switch" role="group" aria-label="Theme">
      <button type="button" data-theme="dark" aria-pressed="true">Dark</button>
      <button type="button" data-theme="light" aria-pressed="false">Light</button>
    </div>
    <a class="btn" id="theme-open" href="wireframes/index.html#results-list">Open it in the viewer →</a>
    <div class="holes"><h3>The two holes it found</h3>{md(holes)}</div>
  </div>
  {CO.phone('results-list.html?theme=dark', 'Results list', [('results-list.html?theme=dark', 'Dark'), ('results-list.html?theme=light', 'Light')], 'The same page in both themes: <code>?theme=light</code> sets <code>data-theme</code>, and <code>tokens/tokens.css</code> swaps the role values.').replace('<figure class="phone-fig">', '<figure class="phone-fig" id="theme-fig">')}
</div>
<p>The product stays dark-only. <a href="ui/review-theme.html">Every state in both themes →</a></p>'''
THEME_JS = '''(function () {
  var sel = document.getElementById('theme-page'), fig = document.getElementById('theme-fig');
  var frame = fig.querySelector('iframe'), open = document.getElementById('theme-open'), theme = 'dark';
  var btns = Array.prototype.slice.call(document.querySelectorAll('[data-theme]'));
  function show() {
    frame.src = 'wireframes/' + sel.value + '.html?theme=' + theme;
    frame.title = sel.value + ', ' + theme + ' theme';
    open.href = 'wireframes/index.html#' + sel.value + (theme === 'light' ? '?theme=light' : '');
    btns.forEach(function (b) { b.setAttribute('aria-pressed', String(b.getAttribute('data-theme') === theme)); });
  }
  sel.addEventListener('change', show);
  btns.forEach(function (b) { b.addEventListener('click', function () { theme = b.getAttribute('data-theme'); show(); }); });
})();'''

# ---------------------------------------------------------------- after the lesson, and the folded record
after = re.search(r'^### After the lesson[^\n]*\n(.*?)(?=^### |^## |\Z)', AUDIT, flags=re.M | re.S).group(1)
after_items = re.findall(r'^- \*\*(.+?)\*\*', after, flags=re.M)
step6 = AS['Step 6 record (2026-10-30): the final check']
step6_table = step6.split('### The check', 1)[1].split('### Mapping addition', 1)[0]
mapping = AS['Mapping: old variable → new token (Lesson 8, step 2, 2026-10-27; for steps 3–4)']
findings = AS['Findings']
checks_list = ('<ol class="checks">' + ''.join(f'<li>{inline(c)}</li>' for c in ST['checks']) + '</ol>'
               '<p class="note">Listed in <code>CLAUDE.md</code> → UI assembly; run by <code>scripts/concept/build_stand.py</code>. The token rules they enforce: <code>CLAUDE.md</code> → Tokens.</p>')
REVIEWS = [('ui/review-theme.html', 'Step 5 · every state in both themes'), ('concept/concept.html', 'The stand · every token signed, contrast in both themes'),
           ('ui/kit.html', 'The showcase · on tokens and components')]
reviews_body = '<div class="card-grid">' + ''.join(
    f'<a class="card-link" href="{h}"><span class="si-tag" style="color:var(--accent)">Review</span><span class="si-title">{esc(t)}</span><span class="si-desc">{h} →</span></a>' for h, t in REVIEWS) + '</div>'
RECORD = [(t, GH + 'tokens/tokens-audit.md#' + re.sub(r'[^a-z0-9 -]', '', t.lower()).replace(' ', '-'), '') for t in AS if re.match(r'Step \d record', t)]
MORE = (LP.fold('The audit (step 1): findings', md(findings), f'{len(re.findall(r"^### ", findings, flags=re.M))} kinds of finding, from tokens/tokens-audit.md')
        + LP.fold('The old → new mapping', md(mapping), 'every kit variable and the token that replaced it')
        + LP.fold(f'{len(ST["checks"])} checks stop the build', checks_list, 'color rules in both themes, contrast, signed tokens, components, links, overflow')
        + LP.fold('The final check (step 6): the defect table', md(step6_table), '4 defects, each fixed without a pixel changed')
        + LP.fold(f'{len(REVIEWS)} review pages', reviews_body, 'the themes, the stand, the showcase')
        + LP.fold('The record, step by step', LP.strip(RECORD), f'{len(RECORD)} records in tokens/tokens-audit.md'))

# ---------------------------------------------------------------- the page
EXTRA_CSS = CO.DEVICE_CSS + '''
  .dg{display:grid; gap:12px; margin:12px 0 10px}
  .dg-row{display:grid; grid-template-columns:minmax(0,1fr) 28px minmax(0,1fr) 28px minmax(0,1fr); align-items:stretch; gap:6px}
  .dg-node{background:var(--bg-elev); border:1px solid var(--border); border-radius:8px; padding:10px 12px; display:grid; gap:3px; align-content:start}
  .dg-role{border-left:3px solid var(--accent)}
  .dg-light .dg-node{background:var(--bg-elev-2)}
  .dg-k{font-size:11px; font-weight:800; text-transform:uppercase; letter-spacing:.06em; color:var(--text-faint)}
  .dg-v{display:flex; align-items:center; gap:6px; font-size:12.5px; color:var(--text-dim)}
  .dg-n{font-size:12.5px; color:var(--text-faint)}
  .dg-arrow{align-self:center; text-align:center; color:var(--accent); font-weight:800; font-size:18px}
  .sw{display:inline-block; width:14px; height:14px; border-radius:3px; box-shadow:inset 0 0 0 1px rgba(255,255,255,.2)}
  @media (max-width:760px){ .dg-row{grid-template-columns:minmax(0,1fr)} .dg-arrow{transform:rotate(90deg); width:20px} }
  .look{display:grid; grid-template-columns:minmax(0,320px) minmax(0,1fr); gap:24px; align-items:start; margin:16px 0}
  .look-controls{display:grid; gap:10px; align-content:start}
  .look .device-slot{overflow:hidden}
  .look-controls label{font-size:12px; font-weight:800; text-transform:uppercase; letter-spacing:.06em; color:var(--text-faint)}
  .look-controls select{min-height:44px; background:var(--bg-elev); color:var(--text); border:1px solid var(--border); border-radius:8px; padding:0 10px; font:inherit}
  .look-switch{display:grid; grid-template-columns:1fr 1fr; background:var(--bg-elev); border:1px solid var(--border); border-radius:999px; padding:3px}
  .look-switch button{min-height:40px; border:0; border-radius:999px; background:transparent; color:var(--text-dim); font:inherit; font-weight:700; cursor:pointer}
  .look-switch button[aria-pressed="true"]{background:var(--accent-dim); color:var(--accent)}
  .look-switch button:focus-visible, .look-controls select:focus-visible{outline:2px solid var(--text); outline-offset:2px}
  .holes{font-size:13.5px}
  .holes h3{margin:8px 0 4px}
  @media (max-width:760px){ .look{grid-template-columns:minmax(0,1fr)} }
  .checks{padding-left:22px}
  .checks li{margin-bottom:8px}
  .after li{margin-bottom:10px}
'''
summary = ' '.join(re.split(r'(?<=[.!?])\s', re.sub(r'\s+', ' ', TOKENS_SEC.strip().split('\n\n', 1)[0]))[:1])
STATS = [(N_PRIM, 'primitives', f'{N_COLOR_PRIM} of them colors, named by hue and L*'), (len(ROLES), 'semantic roles', 'color only; components read nothing else'),
         (N_FILES, 'component files', 'bundled into components/index.css'), (len(ROLE_PAIRS), 'role pairs, both themes', f'{N_USE_PAIRS} use pairs and {N_GLASS} glass pairs checked by the build'),
         (len(ST['checks']), 'build checks', 'each stops the build')]
after_body = ('<p class="lede">Decided, and done after Lesson 8 as "keep it" changes or one product pass. Nothing changed for them in this lesson.</p>'
              + md(after) + f'<p class="note">From <a href="{GH}tokens/tokens-audit.md">tokens/tokens-audit.md</a> → After the lesson; the optional link’s full checklist is in <a href="{GH}concept/concept.md">concept/concept.md</a>.</p>')
SECTIONS = ''.join([
    LP.section('how', 'How it works', 'tag-d', 'Primitive → role → component', diagram + LP.fold('The two levels, the rules, where they live', md(TOKENS_SEC.split('\n\n', 1)[1]), 'CLAUDE.md → Tokens')),
    LP.section('proof', 'The proof', 'tag-p', 'The theme stress test', proof_body),
    LP.section('decisions', 'Decided', 'tag-t', 'Key decisions', LP.key_decisions(8, inline)[0]),
    LP.section('after', 'Next', 'tag-f', 'After the lesson', f'<div class="after">{after_body}</div>'),
    LP.section('more', 'More', 'tag-m', 'The rest of the record', MORE)])
STAGES = [('how', 'How it works', 'Primitive → role → component'), ('proof', 'The proof', 'The theme stress test'), ('decisions', 'Decided', 'Key decisions'),
          ('after', 'Next', 'After the lesson'), ('more', 'More', 'The record')]
PAGE = LP.render(8, 'Design tokens', 'tokens-overview.html', '27–30 Oct 2026', 'Two levels of tokens, every page on them', inline(summary),
    STATS, STAGES, None, None, SECTIONS, None, None,
    ['scripts/build_tokens_overview.py', 'scripts/lesson_page.py'], extra_css=EXTRA_CSS,
    scripts='<script>\n' + CO.DEVICE_JS + '\n' + THEME_JS + '\n</script>')
open(os.path.join(ROOT, 'public/tokens-overview.html'), 'w').write(PAGE)
print('tokens overview: primitives', N_PRIM, 'roles', len(ROLES), 'files', N_FILES, 'role pairs', len(ROLE_PAIRS), 'after', len(after_items), 'bytes', len(PAGE))
