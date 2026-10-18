"""Build public/concept-overview.html, the Lesson 6 overview, from concept/concept.md and concept/references.md.

Run from anywhere:  python3 scripts/build_concept_overview.py
Re-run after editing either .md, tokens.css, map.css or build_stand.py; the page is generated, never hand-edited.
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
TOK = open(ROOT + '/concept/tokens.css').read() + open(ROOT + '/concept/map.css').read()
N_TOKENS = len(set(re.findall(r'(?:^|;)\s*--([a-z0-9-]+):', TOK, flags=re.M)))
BS = open(ROOT + '/scripts/concept/build_stand.py').read()
PAIRS = re.findall(r"^\s+\('[^\n]*', '[a-z0-9-]+', '[a-z0-9-]+', '(text|large|ui|exempt|info)'\),$", BS[BS.index('PAIRS = ['):BS.index('rows, failures')], flags=re.M)
N_PAIRS = len(PAIRS)
N_CHECKED = sum(1 for k in PAIRS if k in ('text', 'large', 'ui'))
assert N_PAIRS > 0 and N_TOKENS > 0
N_STEP7 = len(re.findall(r'^\d+\. ', CS['Step 7 check (2026-10-14 to 2026-10-15)'], flags=re.M))
_m = re.search(r'(\w+) defects found, (\w+) fixed', CS['Step 7 check (2026-10-14 to 2026-10-15)'])
STEP7_FOUND, STEP7_FIXED = _m.group(1).lower(), _m.group(2)
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
  <div class="stat"><span class="stat-n">{N_TOKENS}</span><span class="stat-l">tokens in <code>tokens.css</code> and <code>map.css</code>, every one signed on the stand with its reason</span></div>
  <div class="stat"><span class="stat-n">{N_PAIRS}</span><span class="stat-l">contrast pairs in the build, {N_CHECKED} of them held to WCAG AA (the rest are disabled or decorative)</span></div>
  <div class="stat"><span class="stat-n">3</span><span class="stat-l">color rules checked on every build; 1, 2 and 3a stop it</span></div>
</div>
<p><a class="btn" href="concept/concept.html">Open the stand · concept.html →</a></p>
<p>The stand is generated by <code>scripts/concept/build_stand.py</code> from <code>tokens.css</code>, <code>map.css</code> and <code>components.css</code>. The build stops if a text pair fails AA, if color rule 1, 2 or 3a breaks, or if a token has no signed row.</p>
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
<p class="note">Live pages, scrollable inside the frames. They link the concept's <code>tokens.css</code> and <code>components.css</code> and keep the wireframes' text and structure. The other 8 screens stay grayscale until Lesson 7. All 35 pages: <a href="wireframes/">wireframes viewer</a>.</p>
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

NAV = [('overview', 'Overview'), ('references', 'References'), ('taste', 'Taste'), ('directions', 'Directions'), ('stand', 'Stand'), ('screens', 'Screens'), ('check', 'Check'), ('open', 'Open')]
CSSSRC = open(ROOT + '/public/ia.html').read()
root_css = CSSSRC[CSSSRC.index(':root{'):CSSSRC.index('/* Hero */')]

def section(id_, tag, tagcls, title, body):
    return f'<section class="block" id="{id_}"><span class="section-tag {tagcls}">{tag}</span><h2>{esc(title)}</h2><div class="prose">{body}</div></section>\n'

PAGE = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Onrace — Concept</title>
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<style>
  {root_css}{BAR_CSS}
  /* Hero (same as ia.html and voice.html) */
  header.hero{{ max-width:var(--maxw); margin:0 auto; padding:64px 24px 40px; }}
  .kicker{{ font-size:12px; font-weight:800; letter-spacing:.14em; text-transform:uppercase; color:var(--accent); margin:0 0 14px; }}
  header.hero h1{{ font-size:clamp(36px,6vw,60px); margin:0 0 14px; font-weight:800; letter-spacing:-.02em; }}
  .hero-desc{{color:var(--text-dim); font-size:18px; max-width:720px; margin:0 0 6px; line-height:1.5}}
  .meta-row{{display:flex; gap:10px; flex-wrap:wrap; margin:24px 0 0}}
  .pill{{ font-size:12px; font-weight:700; text-transform:uppercase; letter-spacing:.04em; padding:6px 12px; border-radius:999px; border:1px solid var(--border); color:var(--text-dim); }}
  .card-grid{{display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:14px; margin:28px 0 0}}
  a.card-link{{ display:block; background:var(--bg-elev); border:1px solid var(--border); border-radius:var(--radius); padding:16px 18px; text-decoration:none; transition:border-color .15s, transform .15s; }}
  a.card-link:hover{{border-color:var(--accent); transform:translateY(-1px)}}
  .si-tag{{font-size:11px; font-weight:800; text-transform:uppercase; letter-spacing:.06em; display:block; margin-bottom:6px}}
  .si-title{{color:var(--text); font-weight:700; font-size:15px; display:block; margin-bottom:4px}}
  .si-desc{{color:var(--text-dim); font-size:13px; display:block}}
  main{{max-width:var(--maxw); margin:0 auto; padding:0 24px 80px}}
  section.block{{padding:56px 0; border-top:1px solid var(--border); scroll-margin-top:72px}}
  .section-tag{{ display:inline-flex; font-size:12px; font-weight:800; letter-spacing:.08em; text-transform:uppercase; padding:5px 12px; border-radius:999px; margin-bottom:16px; }}
  .tag-p{{background:var(--accent-dim); color:var(--accent)}}
  .tag-d{{background:var(--patterns-dim); color:var(--patterns)}}
  .tag-f{{background:var(--unconfirmed-dim); color:var(--unconfirmed)}}
  .tag-m{{background:var(--benchmark-dim); color:var(--benchmark)}}
  .tag-t{{background:var(--job-loc-dim); color:var(--job-loc)}}
  .tag-o{{background:var(--ok-dim); color:var(--ok)}}
  h2{{font-size:28px; margin:0 0 8px; font-weight:800; letter-spacing:-.01em}}
  h3{{font-size:19px; margin:34px 0 10px; font-weight:700}}
  h3[id]{{scroll-margin-top:72px}}
  .prose p, .prose li{{color:var(--text-dim); font-size:15px; max-width:820px}}
  .prose strong{{color:var(--text)}}
  .prose ul, .prose ol{{padding-left:20px; margin:0 0 14px}}
  .prose li{{margin-bottom:6px}}
  .prose li ul{{margin-top:6px}}
  .prose p.rule{{font-size:16.5px; color:var(--text); background:var(--bg-elev); border:1px solid var(--border); border-left:3px solid var(--accent); border-radius:8px; padding:12px 16px}}
  .prose p.note{{font-size:13.5px; color:var(--text-faint)}}
  .tbl-wrap{{overflow-x:auto; margin:10px 0 20px; border:1px solid var(--border); border-radius:var(--radius)}}
  table{{border-collapse:collapse; width:100%; font-size:13.5px}}
  th{{text-align:left; background:var(--bg-elev-2); color:var(--text-faint); font-size:11px; text-transform:uppercase; letter-spacing:.05em; padding:10px 12px; border-bottom:1px solid var(--border); white-space:nowrap}}
  td{{padding:9px 12px; border-bottom:1px solid var(--border); vertical-align:top; color:var(--text-dim)}}
  tr:last-child td{{border-bottom:none}}
  td strong{{color:var(--text)}}
  .two-col{{display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr)); gap:18px}}
  .two-col h3{{margin-top:6px}}
  .panel{{background:var(--bg-elev); border:1px solid var(--border); border-radius:var(--radius); padding:6px 20px 8px}}
  .tech-grid, .attr-grid{{display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr)); gap:14px; margin:14px 0 8px}}
  .tech, .attr{{background:var(--bg-elev); border:1px solid var(--border); border-radius:var(--radius); padding:14px 18px}}
  .tech p, .attr p{{margin:0 0 8px}}
  .tech-from{{font-size:11px; font-weight:800; text-transform:uppercase; letter-spacing:.06em; color:var(--patterns)}}
  .prose .tech-name, .prose .attr-title{{color:var(--text); font-weight:700; font-size:15.5px; margin-top:6px}}
  .prose .tech-meta, .prose .attr-strength{{font-size:13px; color:var(--text-faint)}}
  .scope{{color:var(--benchmark); font-weight:700}}
  a.btn{{display:inline-block; background:var(--bg-elev); border:1px solid var(--border); border-radius:8px; padding:10px 14px; color:var(--text); font-weight:700; font-size:14px; text-decoration:none}}
  a.btn:hover{{border-color:var(--accent)}}
  .stat-row{{display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); gap:14px; margin:6px 0 18px}}
  .stat{{background:var(--bg-elev); border:1px solid var(--border); border-radius:var(--radius); padding:16px 18px}}
  .stat-n{{display:block; font-size:36px; font-weight:800; letter-spacing:-.02em; color:var(--text); line-height:1.1}}
  .stat-l{{display:block; font-size:13px; color:var(--text-dim); margin-top:6px}}
  .phones{{display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr)); gap:28px; margin:18px 0}}
  .phone-fig{{margin:0}}
  /* device frame: copied from wireframes/index.html at build time */
{DEVICE_CSS}
  .phone-fig .device-slot{{margin:0 auto}}
  figcaption{{max-width:412px; margin:12px auto 0; font-size:13.5px; color:var(--text-dim)}}
  figcaption strong{{color:var(--text)}}
  .states{{color:var(--text-faint)}}
  footer{{max-width:var(--maxw); margin:0 auto; padding:24px; color:var(--text-faint); font-size:12.5px; border-top:1px solid var(--border)}}
  @media (prefers-reduced-motion: reduce){{ html{{scroll-behavior:auto}} a.card-link{{transition:none}} a.card-link:hover{{transform:none}} }}
</style>
</head>
<body>
{lessons_bar('concept-overview.html')}
<nav>
  <div class="nav-inner">
    <a href="#top" class="brand" style="text-decoration:none">ON<span>RACE</span> · Concept</a>
    <div class="navlinks">
      {''.join(f'<a href="#{i}">{n}</a>' for i, n in NAV)}
    </div>
  </div>
</nav>
<a id="top"></a>
<header class="hero">
  <p class="kicker">Lesson 6 · Concept</p>
  <h1>Podium: how Onrace looks</h1>
  <p class="hero-desc">Rendered from <code>concept/concept.md</code> (taste, attributes, rules, decisions) and <code>concept/references.md</code> (what we borrowed, and from where). The product's own values live in <code>concept/</code>; this page only documents them.</p>
  <div class="meta-row">
    <span class="pill">Direction A chosen 2026-10-13</span>
    <span class="pill">{N_TOKENS} tokens, all signed</span>
    <span class="pill">{N_PAIRS} contrast pairs</span>
    <span class="pill">2 screens in Podium</span>
    <span class="pill">Step 7: {STEP7_FOUND} defects found, {STEP7_FIXED} fixed</span>
  </div>
  <div class="card-grid">
    <a class="card-link" href="concept/concept.html"><span class="si-tag" style="color:var(--accent)">Stand</span><span class="si-title">concept.html</span><span class="si-desc">Every token, component and contrast pair, signed with its reason →</span></a>
    <a class="card-link" href="concept/directions.html"><span class="si-tag" style="color:var(--patterns)">Directions</span><span class="si-title">Round 2: A, B, C</span><span class="si-desc">Podium chosen; Telemetry and Bib number not picked →</span></a>
    <a class="card-link" href="wireframes/race-browse.html"><span class="si-tag" style="color:var(--benchmark)">Screen</span><span class="si-title">Race browse</span><span class="si-desc">Live, in Podium →</span></a>
    <a class="card-link" href="wireframes/results-list.html"><span class="si-tag" style="color:var(--job-loc)">Screen</span><span class="si-title">Results list</span><span class="si-desc">Live, in Podium →</span></a>
  </div>
</header>
<main>
{section('overview', 'Overview', 'tag-p', 'What we saw, what we decided', overview_body)}
{section('references', 'Step 1', 'tag-d', 'References', refs_body)}
{section('taste', 'Step 2', 'tag-f', 'Taste and attributes', taste_body)}
{section('directions', 'Step 3', 'tag-m', 'Directions', dir_body)}
{section('stand', 'Step 4', 'tag-p', 'The stand', stand_body)}
{section('screens', 'Steps 5–6', 'tag-t', 'The two screens', screens_body)}
{section('check', 'Step 7', 'tag-o', 'The check', check_body)}
{section('open', 'Open', 'tag-f', "What's open", open_body)}
</main>
<footer>Generated by <code>scripts/build_concept_overview.py</code> from <a href="{GH}concept/concept.md">concept/concept.md</a> and <a href="{GH}concept/references.md">concept/references.md</a>. Counts are read from <code>tokens.css</code>, <code>map.css</code> and <code>build_stand.py</code>.</footer>
<script>
{DEVICE_JS}
</script>
<script>
(function(){{
  var links = Array.prototype.slice.call(document.querySelectorAll('.navlinks a'));
  var byId = {{}};
  links.forEach(function(l){{ byId[l.getAttribute('href').slice(1)] = l; }});
  var sections = Array.prototype.slice.call(document.querySelectorAll('section.block[id]'));
  if(!('IntersectionObserver' in window) || !sections.length) return;
  var io = new IntersectionObserver(function(entries){{
    entries.forEach(function(e){{
      if(e.isIntersecting){{ links.forEach(function(l){{ l.classList.remove('active'); }}); var l = byId[e.target.id]; if(l) l.classList.add('active'); }}
    }});
  }}, {{rootMargin:'-45% 0px -50% 0px'}});
  sections.forEach(function(s){{ io.observe(s); }});
}})();
</script>
</body>
</html>
'''
open(ROOT + '/public/concept-overview.html', 'w').write(PAGE)
print('tokens', N_TOKENS, 'pairs', N_PAIRS, 'checked', N_CHECKED, 'step7', N_STEP7, 'deferred', DEFERRED_ROWS, 'bytes', len(PAGE))
