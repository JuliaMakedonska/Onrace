"""Build public/concept-overview.html, the Lesson 6 overview, from concept/concept.md and concept/references.md.

Run from anywhere:  python3 scripts/build_concept_overview.py
Re-run after editing either .md, ui/kit.css, ui/map.css or build_stand.py; the page is generated, never hand-edited.
Styling is the artifact pages' own (ia.html's :root tokens, like voice.html); the product's Podium values stay in concept/.
Every line on the page is quoted or rendered from the two .md files; the counts are read from the files they describe.
"""
import re, html, os
import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lessons_nav import BAR_CSS, bar as lessons_bar
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C = open(ROOT + '/concept/concept.md').read()
R = open(ROOT + '/concept/references.md').read()
esc = lambda t: html.escape(t, quote=False)
GH = 'https://github.com/JuliaMakedonska/Onrace/blob/main/'

# Mobbin links need a login (they redirect), so the page keeps the screen id and points to references.md for the links
def unmobbin(t):
    return re.sub(r'\[([^\]]+)\]\(https://mobbin\.com/[^)]+\)', r'\1', t)

def inline(t):
    t = esc(unmobbin(t))
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', t)
    t = t.replace('](#color-rules-designer-2026-10-13)', '](#color-rules)')   # concept.md's GitHub anchor → this page's Color rules
    t = t.replace('](#native-ios-designer-rule-2026-10-18)', '](' + GH + 'concept/concept.md#native-ios-designer-rule-2026-10-18)')   # Lesson 7: not on this page, so link to concept.md
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', t)
    return t.replace('\\&lt;', '&lt;').replace('\\&gt;', '&gt;').replace('\\|', '|')

def table(lines):
    rows = [[c.strip() for c in re.split(r'(?<!\\)\|', l.strip().strip('|'))] for l in lines]
    h = '<div class="tbl-wrap"><table><thead><tr>' + ''.join(f'<th>{inline(c)}</th>' for c in rows[0]) + '</tr></thead><tbody>'
    for r in rows[2:]:
        h += '<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>'
    return h + '</tbody></table></div>'

def md(text):
    out, lines, i = [], text.split('\n'), 0
    while i < len(lines):
        l = lines[i]
        if not l.strip() or l.strip() == '---': i += 1; continue
        if l.startswith('### '): out.append(f'<h3>{inline(l[4:])}</h3>'); i += 1; continue
        if l.startswith('|'):
            blk = []
            while i < len(lines) and lines[i].startswith('|'): blk.append(lines[i]); i += 1
            out.append(table(blk)); continue
        if re.match(r'^\s*(- |\d+\. )', l):
            h, stack = [], []
            while i < len(lines) and re.match(r'^\s*(- |\d+\. )', lines[i]):
                m = re.match(r'^(\s*)(- |\d+\. )(.*)$', lines[i])
                ind, tag = len(m.group(1)), 'ol' if m.group(2)[0].isdigit() else 'ul'
                while stack and ind < stack[-1][0]: h.append(f'</{stack.pop()[1]}>')
                if not stack or ind > stack[-1][0]: h.append(f'<{tag}>'); stack.append((ind, tag))
                h.append(f'<li>{inline(m.group(3))}</li>'); i += 1
            while stack: h.append(f'</{stack.pop()[1]}>')
            s = ''.join(h)
            s = re.sub(r'</li><(ul|ol)>', r'<\1>', s)
            s = re.sub(r'</(ul|ol)>(?=<li>|</ul>|</ol>)', r'</\1></li>', s)
            out.append(s); continue
        blk = []
        while i < len(lines) and lines[i].strip() and not re.match(r'^(#|\||\s*- |\s*\d+\. |---)', lines[i]): blk.append(lines[i].strip()); i += 1
        out.append(f'<p>{inline(" ".join(blk))}</p>')
    return '\n'.join(out)

def sections(text, level='## '):
    parts = re.split(r'^' + re.escape(level), text, flags=re.M)
    return {p.split('\n', 1)[0].strip(): p.split('\n', 1)[1] if '\n' in p else '' for p in parts[1:]}

CS = sections(C)
RS = sections(R)
def sub(sec, title):  # a ### subsection of a ## section
    return sections(sec, '### ')[title]
def para(sec, start):  # the paragraph (and its list) that starts with `start`
    m = re.search(r'^' + re.escape(start) + r'.*?(?=\n\n(?!\s*- )|\Z)', sec, flags=re.M | re.S)
    assert m, start
    return m.group(0)

# ---------------------------------------------------------------- counts, read from the files they describe
import re as _re
_KIT = open(ROOT + '/ui/kit.css').read()
TOK = ''.join(_re.findall(r':root\s*\{(.*?)\n\}', _KIT, flags=_re.S)) + open(ROOT + '/ui/map.css').read()
N_TOKENS = len(set(re.findall(r'(?:^|;)\s*--([a-z0-9-]+):', TOK, flags=re.M)))
BS = open(ROOT + '/scripts/concept/build_stand.py').read()
PAIRS = re.findall(r"^\s+\('[^\n]*', '[a-z0-9-]+', '[a-z0-9-]+', '(text|large|ui|exempt|info)'\),$", BS[BS.index('PAIRS = ['):BS.index('rows, failures')], flags=re.M)
N_PAIRS = len(PAIRS)
N_CHECKED = sum(1 for k in PAIRS if k in ('text', 'large', 'ui'))
assert N_PAIRS > 0 and N_TOKENS > 0
N_STEP7 = len(re.findall(r'^\d+\. ', CS['Step 7 check (2026-10-14 to 2026-10-15)'], flags=re.M))
_m = re.search(r'(\w+) defects found, (\w+) fixed', CS['Step 7 check (2026-10-14 to 2026-10-15)'])
STEP7_FOUND, STEP7_FIXED = _m.group(1).lower(), _m.group(2)
_NUM = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}
STEP7_FOUND_N = _NUM.get(STEP7_FOUND, STEP7_FOUND)
DEFERRED_ROWS = len(re.findall(r'^\| (?!Item|---)', CS['Deferred to Lesson 7 (markup)'], flags=re.M))

# ---------------------------------------------------------------- 2. references: technique cards from the § 4 tables
def technique_rows(sec):
    rows = []
    for l in sec.split('\n'):
        if l.startswith('| **') and not l.startswith('| **What not'):
            c = [x.strip() for x in re.split(r'(?<!\\)\|', l.strip().strip('|'))]
            name = re.match(r'\*\*(.+?)\*\*', c[0]).group(1)
            scope = re.match(r'\*\*(.+?)\*\*', c[1]).group(1).rstrip('.')
            rows.append((name, scope, c[3]))
    return rows
def tech_cards(rows, who):
    return '<div class="tech-grid">' + ''.join(
        f'<div class="tech"><span class="tech-from">{who}</span><p class="tech-name">{inline(n)}</p><p class="tech-meta"><span class="scope">{inline(s)}</span> · {inline(where)}</p></div>'
        for n, s, where in rows) + '</div>'
PICKED = RS['4. Picked styles']
STRAVA = sub(PICKED, 'Base: Strava')
LINKEDIN = sub(PICKED, 'Donor: LinkedIn (licenses and certifications), source-line logic only')
HYBRID = sub(PICKED, '4b. Hybrid-racing products (Lesson 1 screenshots, not Mobbin)')
HYBRID_TAKEN = para(HYBRID, '**Technique taken:')
ANTI = para(HYBRID, '**Anti-reference: what we don\'t take.**')
LINKEDIN_TAKEN = para(LINKEDIN, "- **What's taken: the logic of the source line only, not its styling.**")

refs_body = f'''
<p class="rule">{inline(R.split(chr(10), 1)[0])}</p>
{md(para(R, '**What these references are for:**'))}
<h3>Which products were on Mobbin</h3>
{md(para(RS['1. Which research.md products are on Mobbin'], '**The consequence:**'))}
<h3>Base: Strava</h3>
{md(para(STRAVA, '- **What "base" means here:**'))}
{tech_cards(technique_rows(STRAVA), 'Strava · base')}
<h3>Donor: LinkedIn, source-line logic only</h3>
{md(LINKEDIN_TAKEN)}
{tech_cards(technique_rows(LINKEDIN), 'LinkedIn · donor')}
<h3>Hybrid-racing products (Lesson 1 screenshots)</h3>
{md(para(HYBRID, '**Tally:**'))}
{md(HYBRID_TAKEN)}
{md(ANTI)}
<h3>Documented, not picked</h3>
{md(para(sub(PICKED, 'Documented, not picked: Letterboxd (diary)'), '- **Why not picked:**'))}
{md(para(PICKED, 'Two styles: one base and one donor'))}
<p class="note">Mobbin screen IDs are shown as text: Mobbin pages need a login. The full links are in <a href="{GH}concept/references.md">references.md</a>.</p>
'''

# ---------------------------------------------------------------- 3. taste and attributes
TASTE = CS["Designer's taste"]
likes = re.search(r'\*\*Like:\*\*\n\n(.*?)\n\n\*\*Don', TASTE, re.S).group(1)
donts = re.search(r"\*\*Don't want:\*\*\n\n(.*?)\n\n\*\*Shape", TASTE, re.S).group(1)
ATTR = CS['Attributes']
attr_cards = ''
for title, body in sections(ATTR, '### ').items():
    lede = body.strip().split('\n\n', 1)[0]
    strength = re.search(r'^- \*\*Strength:\*\* (.*)$', body, re.M).group(1)
    attr_cards += f'<div class="attr"><p class="attr-title">{inline(title)}</p><p>{inline(lede)}</p><p class="attr-strength"><strong>Strength:</strong> {inline(strength)}</p></div>'
taste_body = f'''
<div class="two-col">
  <div><h3>Like</h3>{md(likes)}</div>
  <div><h3>Don't want</h3>{md(donts)}</div>
</div>
{md(para(TASTE, '**Shape: slightly rounded, small radius.**'))}
{md(para(TASTE, '**Theme: dark.**'))}
<h3>The five attributes</h3>
{md(ATTR.strip().split(chr(10) + chr(10) + '### ', 1)[0])}
<div class="attr-grid">{attr_cards}</div>
<h3>Hierarchy rules (designer)</h3>
{md(CS['Hierarchy rules (designer)'])}
'''

# ---------------------------------------------------------------- 4. directions
R1 = CS['Step 3, round 1 (rejected 2026-10-13)']
R2 = CS['Directions (step 3, chosen 2026-10-13)']
dir_body = f'''
<h3>Round 1 · rejected</h3>
{md(R1.split(chr(10) + chr(10), 1)[1].replace('(live: https://juliamakedonska.github.io/Onrace/concept/directions-round-1.html)', ''))}
<p><a class="btn" href="concept/directions-round-1.html">Open round 1 · directions-round-1.html →</a></p>
<h3>Round 2 · Podium chosen</h3>
{md(R2)}
<p><a class="btn" href="concept/directions.html">Open round 2 · directions.html →</a></p>
'''

# ---------------------------------------------------------------- 5. the stand
RULES = CS['Color rules (designer, 2026-10-13)']
stand_body = f'''
<div class="stat-row">
  <div class="stat"><span class="stat-n">{N_TOKENS}</span><span class="stat-l">tokens in <code>ui/kit.css</code> and <code>ui/map.css</code>, every one signed on the stand with its reason</span></div>
  <div class="stat"><span class="stat-n">{N_PAIRS}</span><span class="stat-l">contrast pairs in the build, {N_CHECKED} of them held to WCAG AA (the rest are disabled or decorative)</span></div>
  <div class="stat"><span class="stat-n">3</span><span class="stat-l">color rules checked on every build; 1, 2 and 3a stop it</span></div>
</div>
<p><a class="btn" href="concept/concept.html">Open the stand · concept.html →</a></p>
<p>The stand is generated by <code>scripts/concept/build_stand.py</code> from <code>ui/kit.css</code> and <code>ui/map.css</code>. The build stops if a text pair fails AA, if color rule 1, 2 or 3a breaks, or if a token has no signed row.</p>
<h3 id="color-rules">Color rules, checked by the build</h3>
{md(RULES)}
'''

# ---------------------------------------------------------------- 6. the two screens
ANAT = CS['Race card anatomy (decided by the designer, 2026-10-13)']
first_screen = para(ANAT, '**Photo band: 3:1 (decided 2026-10-14).**')
RB_STATES = [('race-browse.html', 'Base'), ('race-browse.html?sport=hyrox&amp;sport=marathon', 'Filtered'), ('race-browse-empty.html', 'Empty'), ('race-browse-loading.html', 'Loading'), ('race-browse-error.html', 'Error')]
RL_STATES = [('results-list.html', 'Base'), ('results-list.html?saved=1', 'Saved'), ('results-list-empty.html', 'Empty'), ('results-list-loading.html', 'Loading'), ('results-list-error.html', 'Error')]
# The phone frame is the wireframes viewer's own (wireframes/index.html): its device CSS, status-bar markup and
# corner construction are read from that file on every build, so the frames match the viewer's dimensions
# (390×844 screen: 47px status bar, 757px page, 40px home strip) that the first-screen figures were measured in.
VIEWER = open(ROOT + '/wireframes/index.html').read()
DEVICE_CSS = VIEWER[VIEWER.index('  .device-slot {'):VIEWER.index('  /* --- zone notes')].rstrip()
STATUS_BAR = re.search(r'<div class="status-bar" id="status-bar" aria-hidden="true">(.*?)</div>\s*<iframe', VIEWER, re.S).group(1).strip()
SQUIRCLE_JS = VIEWER[VIEWER.index('  function corner(r, s) {'):VIEWER.index(".join(' ');\n  }", VIEWER.index('  function squircle(')) + len(".join(' ');\n  }")]
_c0 = VIEWER.index('  function luminance(color) {')
CONTENT_JS = VIEWER[_c0:VIEWER.index("return luminance(bg) < 0.179 ? '#fff' : '#000';\n  }", _c0) + len("return luminance(bg) < 0.179 ? '#fff' : '#000';\n  }")]
CORNER = re.search(r'var SCREEN_R = (\d+), SMOOTH = ([\d.]+);', VIEWER)
SCREEN_R, SMOOTH = CORNER.group(1), CORNER.group(2)
assert 'status-icons' in STATUS_BAR and 'function squircle' in SQUIRCLE_JS and '--status-h: 47px' in DEVICE_CSS

def phone(src, title, states, caption):
    links = ' · '.join(f'<a href="wireframes/{u}">{n}</a>' for u, n in states)
    return f'''<figure class="phone-fig">
    <div class="device-slot"><div class="device">
      <svg class="device-body" aria-hidden="true"><path class="body-fill"/><path class="screen-edge"/></svg>
      <div class="device-screen">
        <div class="status-bar" aria-hidden="true">{STATUS_BAR}</div>
        <iframe src="wireframes/{src}" title="{title}, live" loading="lazy"></iframe>
        <div class="home-indicator" aria-hidden="true"></div>
      </div>
    </div></div>
    <figcaption><strong>{title}</strong><br>{caption}<br><span class="states">States: {links}</span></figcaption>
  </figure>'''
screens_body = f'''
<div class="phones">
  {phone('race-browse.html', 'Race browse', RB_STATES, 'Race cards with black-and-white photos, the date on a tile, neutral chips. Filters and the List / Map switch above; the Map is a static Natural Earth background.')}
  {phone('results-list.html', 'Results list', RL_STATES, 'The finish time is the loudest thing on each row; the proof line states the source. Log result is the one primary.')}
</div>
<p class="note">Live pages, scrollable inside the frames. They link <code>ui/kit.css</code> (since Lesson 7 step 3a; Lesson 6 built it as the concept's <code>tokens.css</code> and <code>components.css</code>) and keep the wireframes' text and structure. The other 8 screens stay grayscale until Lesson 7. All 35 pages: <a href="wireframes/">wireframes viewer</a>.</p>
<h3>First screen: how many race cards fit</h3>
{md(first_screen)}
<h3>Results list details</h3>
{md(CS['Results list details (designer, 2026-10-14)'])}
'''

# ---------------------------------------------------------------- 7. check, 8. open
check_body = md(CS['Step 7 check (2026-10-14 to 2026-10-15)'])
MAP = CS['Map (designer decision, 2026-10-14)']
open_body = f'''
<h3>Deferred to Lesson 7 (markup)</h3>
{md(CS['Deferred to Lesson 7 (markup)'])}
<h3>Structural techniques waiting for Lesson 7</h3>
{md(RS['4. Picked styles'].split('### 4c. Deferred to Lesson 7 (structural)', 1)[1])}
<h3>The Map upgrade</h3>
{md(MAP)}
'''

# ---------------------------------------------------------------- 1. overview (each line rendered from the sources)
SAW = [
    para(RS['1. Which research.md products are on Mobbin'], '**The consequence:**').replace('**The consequence:** ', ''),
    re.sub(r'^\*\*Tally:\*\* ', '', para(HYBRID, '**Tally:**')),
    re.search(r"For the record: (.*)$", para(RS["6. Still unknown"], "- **Light vs. dark: decided, dark.**"), re.M).group(1),
    'Round 1: ' + re.search(r"^- \*\*Direction 1's layout is the wireframes\.\*\* (.*)$", R1, re.M).group(1),
]
DECIDED = [
    re.search(r'^\*\*Chosen: Direction A, "Podium"\.\*\* (.*)$', R2, re.M).group(1),
    re.search(r'^- (Graphite ground.*)$', R2, re.M).group(1),
    'Theme: dark. ' + re.search(r'^\*\*Theme: dark\.\*\* (This is a designer decision\.)', TASTE, re.M).group(1),
    re.search(r'^1\. (\*\*Accent is scarce\.\*\*.*)$', CS['Hierarchy rules (designer)'], re.M).group(1),
    re.search(r'^(Added before step 5\.)? ?(.*)$', RULES.strip().split('\n')[0]).group(2),
    f'Race browse and Results list are in Podium; every markup change waits for Lesson 7 ({DEFERRED_ROWS} items listed under What\'s open).',
]
DECIDED[0] = 'Direction A, Podium, chosen. ' + DECIDED[0].replace('Why: it', 'It', 1)
cap = lambda x: x[:1].upper() + x[1:]
lis = lambda xs: ''.join(f'<li>{inline(cap(x))}</li>' for x in xs)
overview_body = f'''
<div class="two-col">
  <div class="panel"><h3>What we saw</h3><ul>{lis(SAW)}</ul></div>
  <div class="panel"><h3>What we decided</h3><ul>{lis(DECIDED)}</ul></div>
</div>
'''

DEVICE_JS = """(function () {
""" + SQUIRCLE_JS + """
""" + CONTENT_JS + """
  var SCREEN_R = """ + SCREEN_R + """, SMOOTH = """ + SMOOTH + """;
  // As in the viewer, the status bar and home strip take the colour of the screen's own top and bottom edge,
  // and the status bar's content and the home indicator turn light or dark with them.
  function edgeColor(doc, y) {
    var el = doc.elementFromPoint(doc.documentElement.clientWidth / 2, y);
    while (el) {
      var bg = doc.defaultView.getComputedStyle(el).backgroundColor;
      if (bg && bg !== 'transparent' && !/rgba\\(\\s*0,\\s*0,\\s*0,\\s*0\\s*\\)/.test(bg)) return bg;
      el = el.parentElement;
    }
    return '#fff';
  }
  var devices = Array.prototype.slice.call(document.querySelectorAll('.phone-fig .device'));
  devices.forEach(function (device) {
    var bezel = parseFloat(getComputedStyle(device).paddingLeft);
    var W = device.offsetWidth, H = device.offsetHeight, sw = W - 2 * bezel, sh = H - 2 * bezel;
    var body = device.querySelector('.device-body');
    body.setAttribute('viewBox', '0 0 ' + W + ' ' + H); body.setAttribute('width', W); body.setAttribute('height', H);
    body.querySelector('.body-fill').setAttribute('d', squircle(0.5, 0.5, W - 1, H - 1, SCREEN_R + bezel, SMOOTH));
    body.querySelector('.screen-edge').setAttribute('d', squircle(bezel - 0.5, bezel - 0.5, sw + 1, sh + 1, SCREEN_R + 0.5, SMOOTH));
    device.querySelector('.device-screen').style.clipPath = "path('" + squircle(0, 0, sw, sh, SCREEN_R, SMOOTH) + "')";
    var frame = device.querySelector('iframe'), bar = device.querySelector('.status-bar'), home = device.querySelector('.home-indicator');
    frame.addEventListener('load', function () {
      try { var doc = frame.contentDocument; bar.style.background = edgeColor(doc, 1); bar.style.color = statusContent(bar.style.background); home.style.background = edgeColor(doc, frame.contentWindow.innerHeight - 1); home.style.color = statusContent(home.style.background); }
      catch (e) { bar.style.background = home.style.background = '#fff'; bar.style.color = home.style.color = '#000'; }
    });
  });
  // Scale each device as one piece (never its internals) to fit its column, as the viewer does for the window.
  function fit() {
    devices.forEach(function (device) {
      var slot = device.parentElement, W = device.offsetWidth, H = device.offsetHeight;
      var scale = Math.min(1, slot.parentElement.clientWidth / W);
      device.style.transform = 'scale(' + scale + ')';
      slot.style.width = (W * scale) + 'px'; slot.style.height = (H * scale) + 'px';
    });
  }
  fit();
  window.addEventListener('resize', fit);
})();"""

import lesson_page as LP

# ---------------------------------------------------------------- the decision register (the designer's own decisions, from concept.md)
def date_of(h, default='2026-10-13 to 2026-10-15'):
    m = re.search(r'(\d{4}-\d\d-\d\d)', h); return m.group(1) if m else default
def first_sentences(t, limit=280):
    t = re.sub(r'\s+', ' ', t).strip()
    if len(t) <= limit: return t
    cut = t.rfind('. ', 0, limit)
    return t[:cut + 1] if cut > 80 else t[:limit].rsplit(' ', 1)[0] + ' …'
def anchor(h):
    return GH + 'concept/concept.md#' + re.sub(r'[^a-z0-9 -]', '', h.lower()).replace(' ', '-')
def cards_from(head, body, mode):
    out, d, src = [], date_of(head), head
    if mode == 'items':      # numbered or bulleted items that start with a bold lead
        for m in re.finditer(r'^(?:\d+\. |- )\*\*(.+?)\*\*[:.]? (.*)$', body, flags=re.M):
            out.append((inline(m.group(1).rstrip('.:')), inline(first_sentences(m.group(2))), d, src))
    elif mode == 'paras':    # paragraphs that start with a bold lead
        for m in re.finditer(r'^\*\*(.+?)\*\*[:.]? ?(.*)$', body, flags=re.M):
            if m.group(1).startswith(('Like', "Don't want", 'Decision')): continue
            if len(m.group(2).strip()) < 12: continue   # a heading-like lead with no answer after it
            out.append((inline(m.group(1).rstrip('.:')), inline(first_sentences(m.group(2))), date_of(m.group(1), d), src))
    elif mode == 'decisions':    # a question in bold, then its "**Decision: …**"
        for m in re.finditer(r'^\*\*([A-Z]\. .+?)\*\*.*?^\*\*Decision: (.+?)\*\*([^\n]*)$', body, flags=re.M | re.S):
            out.append((inline(m.group(1).rstrip('.')), '<strong>' + inline(m.group(2)) + '</strong> ' + inline(first_sentences(m.group(3), 200)), d, src))
    return [(q, a, dd, s, anchor(s)) for q, a, dd, s in out]
REG = []
for head, mode in [("Designer's taste", 'paras'), ('Hierarchy rules (designer)', 'items'), ('Color rules (designer, 2026-10-13)', 'items'),
                   ('Race card anatomy (decided by the designer, 2026-10-13)', 'paras'), ('Results list details (designer, 2026-10-14)', 'items'),
                   ('Map (designer decision, 2026-10-14)', 'paras'), ('Where data and taste pull apart (decided 2026-10-13)', 'decisions'),
                   ('Directions (step 3, chosen 2026-10-13)', 'paras')]:
    REG += cards_from(head, CS[head], mode)
assert len(REG) > 15

# ---------------------------------------------------------------- what's open: Lesson 6's deferrals, all taken by Lesson 7
OPEN_ROWS = []
for l in CS['Deferred to Lesson 7 (markup)'].split('\n'):
    if l.startswith('| ') and not l.startswith(('| Item', '|---')):
        item = re.split(r'(?<!\\)\|', l.strip().strip('|'))[0].strip()
        OPEN_ROWS.append((item, '07', 'Taken into Lesson 7: `concept.md` → Gap triage → Markup pass'))

# ---------------------------------------------------------------- the page, on the lessons' template
ST = LP.repo_stats()
bold_led = lambda x: re.sub(r'^(.+?[.:])( |$)', r'<strong>\1</strong>\2', x, count=1)
STAGES = [('references', 'Step 1', 'References'), ('taste', 'Step 2', 'Taste'), ('directions', 'Step 3', 'Directions'), ('stand', 'Step 4', 'The stand'),
          ('screens', 'Steps 5–6', 'Two screens'), ('check', 'Step 7', 'The check'), ('register', 'Register', f'{len(REG)} decisions'), ('open', 'Close', "What's open")]
SECTIONS = ''.join([LP.section('references', 'Step 1', 'tag-d', 'References', refs_body), LP.section('taste', 'Step 2', 'tag-f', 'Taste and attributes', taste_body),
                    LP.section('directions', 'Step 3', 'tag-m', 'Directions', dir_body), LP.section('stand', 'Step 4', 'tag-p', 'The stand', stand_body),
                    LP.section('screens', 'Steps 5–6', 'tag-t', 'The two screens', screens_body), LP.section('check', 'Step 7', 'tag-o', 'The check', check_body)])
STATS = [(ST['screens'], 'screens', f"{ST['pages']} pages with their states"), (ST['variables'], 'kit variables', f"{ST['classes']} classes in ui/kit.css"),
         (ST['components'], 'inventory components', 'ui/inventory.md'), (STEP7_FOUND_N, 'findings in the step 7 check', f'{STEP7_FIXED} fixed'),
         (N_PAIRS, 'contrast pairs', f'{N_CHECKED} held to AA'), (len(ST['checks']), 'build checks', 'each stops the build')]
PAGE = LP.render(6, 'Concept', 'concept-overview.html', '13–15 Oct 2026', 'Podium: how Onrace looks',
    'Rendered from <code>concept/concept.md</code> (taste, attributes, rules, decisions) and <code>concept/references.md</code> (what we borrowed, and from where). The numbers are read from the repo today, so the kit counts include what Lesson 7 added.',
    STATS, STAGES, [bold_led(inline(cap(x))) for x in SAW], [bold_led(inline(cap(x))) for x in DECIDED], SECTIONS, LP.register(REG),
    open_body + LP.open_table(OPEN_ROWS, inline), ['scripts/build_concept_overview.py', 'scripts/lesson_page.py'],
    extra_css=DEVICE_CSS, scripts='<script>\n' + DEVICE_JS + '\n</script>')
open(ROOT + '/public/concept-overview.html', 'w').write(PAGE)
print('concept overview: tokens', N_TOKENS, 'pairs', N_PAIRS, 'register', len(REG), 'open', len(OPEN_ROWS), 'bytes', len(PAGE))
