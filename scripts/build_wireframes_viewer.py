"""Fill the wireframes viewer's screen data (wireframes/index.html, Lesson 04) and mirror it to public/.

Run from anywhere:  python3 scripts/build_wireframes_viewer.py
Re-run after editing wireframes/_screens.md, research/jtbd.md, sitemap.md, or adding a state file.

Writes one JSON block between /* screens:start */ and /* screens:end */ in wireframes/index.html:
- the tree: flow folders (Discovery = _screens.md Pass 1, Infrastructure = its [INFRASTRUCTURE] screens,
  Archive = the rest) → screens → states (the files that exist: base, -empty, -error, -loading, -check-inbox)
- "main": the screen is ticked for Main Job 1 or Main Job 2 in sitemap.md's traceability matrix
- Job: the first sentence of _screens.md's "Job it closes" line, plus the job's own statement quoted from research/jtbd.md
- Persona: the persona research/jtbd.md names for that job; [?] where there's no job
- Flow: the first sentence of _screens.md's "Where it sits in the flow", with its flows.md reference
Everything else in the page (zone notes, phone frame) is hand-written and left alone.
"""
import os, re, json, html, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = open(ROOT + '/wireframes/_screens.md').read()
J = open(ROOT + '/research/jtbd.md').read()
M = open(ROOT + '/sitemap.md').read()

def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', t)
    return t

# ---- jtbd.md: each job's statement and persona
def job_block(title_re):
    m = re.search(title_re, J, flags=re.M | re.S)
    assert m, title_re
    return m.group(1)
def statement(block):
    line = re.search(r'^\s*(?:\d\. )?> (.*)$', block, flags=re.M).group(1)
    return re.sub(r'\s*\*\(.*?\)\*\s*$', '', line).strip()   # drop the italic aside after the statement
def persona(block):
    return re.search(r'\*\*Persona:\*\* (.*)$', block, flags=re.M).group(1).strip()
JOBS = {}
for key, title_re in [('Main Job 1', r'^## Main Job 1 — Discovery\n(.*?)\n---'),
                      ('Main Job 2', r'^## Main Job 2 — Results archiving\n(.*?)\n---'),
                      ('Related Job 1', r'^1\. (> .*?)(?=^2\. )'),
                      ('Related Job 2', r'^2\. (> .*?)(?=^### )'),
                      ('Related Job 3', r'^3\. (> .*?)(?=^4\. )'),
                      ('Related Job 4', r'^4\. (> .*?)(?=^---)')]:
    b = job_block(title_re)
    JOBS[key] = {'statement': statement(b), 'persona': persona(b)}

# ---- sitemap.md: screens ticked for the two main jobs
trace = re.search(r'^\| Job \(`jtbd\.md`\) \|(.*?)\|\n\|[-:| ]+\|\n(.*?)\n\n', M, flags=re.M | re.S)
cols = [c.strip() for c in trace.group(1).split('|')]
MAIN = set()
for row in trace.group(2).split('\n'):
    cells = [c.strip() for c in row.strip().strip('|').split('|')]
    if cells[0].startswith('Main Job'):
        MAIN |= {cols[i] for i, c in enumerate(cells[1:]) if c == '✓'}

# ---- _screens.md: one section per screen
SLUG = lambda name: re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')
STATE_ORDER = [('', 'Base'), ('-empty', 'Empty'), ('-error', 'Error'), ('-loading', 'Loading'), ('-check-inbox', 'Check inbox')]
# States that are a base page plus URL parameters, not files of their own (designer, 2026-10-18: "filtered, with results" is Race browse with its filter parameters)
URL_STATES = {'race-browse': [('race-browse?sport=hyrox&sport=marathon', 'Filtered')]}
pass1_end = S.index('## Pass 2')
flows = {'Discovery': [], 'Archive': [], 'Infrastructure': []}
for m in re.finditer(r'^## ([^\n]+)\n(.*?)(?=^## |\Z)', S, flags=re.M | re.S):
    head, body = m.group(1), m.group(2)
    if head.startswith(('Pass ', 'Summary')) or '**Job it closes:**' not in body:
        continue
    name = re.sub(r' \(.*$', '', re.sub(r' — `\[INFRASTRUCTURE\]`.*$', '', head)).strip()
    slug = SLUG(name)
    folder = 'Infrastructure' if '[INFRASTRUCTURE]' in head else 'Discovery' if m.start() < pass1_end else 'Archive'
    job_line = re.search(r'^\*\*Job it closes:\*\* (.*)$', body, flags=re.M).group(1).strip()
    jk = re.match(r'(Main Job \d|Related Job \d)', job_line)
    job = JOBS.get(jk.group(1)) if jk else None
    fm = re.search(r'^\*\*Where it sits in the flow(?::\*\*|\*\*(?: \((.*?)\))?:) (.*)$', body, flags=re.M)
    ref, text = fm.group(1), fm.group(2)
    sents = re.split(r'(?<=[.?!])(?:["”])?\s+(?=[A-Z`"])', text)
    first = sents[0] if len(sents[0]) >= 60 or len(sents) == 1 else sents[0] + ' ' + sents[1]
    first = first if first.rstrip().endswith(('.', '"', '”', '?')) else first + '.'
    states = [[slug + suf, label] for suf, label in STATE_ORDER if os.path.exists(f'{ROOT}/wireframes/{slug}{suf}.html')]
    assert states and states[0][1] == 'Base', slug
    states[1:1] = [list(x) for x in URL_STATES.get(slug, [])]
    flows[folder].append({
        'slug': slug, 'name': name, 'main': name in MAIN, 'states': states,
        'job': inline(job_line if job_line.startswith('none') else re.split(r'(?<=[.?!])(?:["”])?\s+(?=[A-Z`"])', job_line)[0]),   # 'none' keeps its reason
        'jobQuote': inline(job['statement']) if job else '',
        'persona': inline(job['persona']) if job else '<span class="unknown">[?]</span> No job, so <code>research/jtbd.md</code> names no persona.',
        'flow': (inline(ref) + ': ' if ref else '') + inline(first),
    })
DATA = [{'flow': f, 'screens': s} for f, s in flows.items()]
n_screens = sum(len(f['screens']) for f in DATA); n_states = sum(1 for f in DATA for s in f['screens'] for st in s['states'] if '?' not in st[0])
files = [os.path.basename(p) for p in glob.glob(ROOT + '/wireframes/*.html') if not p.endswith('/index.html')]
assert n_states == len(files), (n_states, len(files))

block = '/* screens:start (generated by scripts/build_wireframes_viewer.py; do not edit by hand) */\n  var SCREENS = ' + \
        json.dumps(DATA, ensure_ascii=False, indent=1).replace('\n', '\n  ') + ';\n  /* screens:end */'
for p in ['wireframes/index.html', 'public/wireframes/index.html']:
    path = os.path.join(ROOT, p)
    h = open(os.path.join(ROOT, 'wireframes/index.html')).read()
    assert '/* screens:start' in h
    h = re.sub(r'/\* screens:start.*?/\* screens:end \*/', lambda m: block, h, flags=re.S)
    open(path, 'w').write(h)
print('viewer:', n_screens, 'screens,', n_states, 'state pages,', 'main:', ', '.join(sorted(MAIN)))
