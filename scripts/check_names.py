"""Names that exist (designer, 2026-11-10; Lesson 9 step 7): DESIGN.md, ui/inventory.md and every page of
design-system/docs/ may only name tokens, files and classes that exist, so a renamed or deleted one can't stay in the
words (the step 7 check found `--pressed`, `--sheet-button`, `--radius-avatar` and `ui/map.css` still named).

What is checked, wherever it is written in `code` (Markdown) or <code> (a docs page), and in DESIGN.md's prose too:
- a token `--name`: defined in design-system/tokens/tokens.css, design-system/map-data.css or the docs layer
  (design-system/docs/doc.css, concept/stand.css, concept/specimens.css, concept/first-screen.css);
- a class `.name`: defined in design-system/index.css or the docs layer;
- a file path (with a folder and an extension, or a folder ending in /): exists from the repo root, design-system/ or
  design-system/docs/.
History is allowed: a sentence that says a name was renamed, removed, retired, merged or split, or what it was until a
date ("It was `--pressed` until …", "renamed from `--radius-avatar`"), may name what is gone. The record sections of
ui/inventory.md (Closed, Consolidated, the markup passes, Race picker pushed, Step 6, Step 7) are history whole. Not
names: `--no-verify` (git) and `--x`, the placeholder in the rule for counts.
Run by scripts/concept/build_stand.py after check_kit.py; exit 1 lists every name that doesn't exist, with where.
"""
import os, re, glob, sys, html as H
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rd = lambda p: open(os.path.join(ROOT, p)).read()
CSS_FILES = ['design-system/tokens/tokens.css', 'design-system/map-data.css', 'design-system/docs/doc.css', 'concept/stand.css', 'concept/specimens.css', 'concept/first-screen.css']
TOKENS = {n for f in CSS_FILES for n in re.findall(r'--([a-z0-9-]+)\s*:', re.sub(r'/\*.*?\*/', '', rd(f), flags=re.S))}
_css = ''.join(re.sub(r'/\*.*?\*/|url\([^)]*\)', '', rd(f), flags=re.S) for f in ['design-system/index.css'] + CSS_FILES[1:])
MARKUP = {c for f in glob.glob(os.path.join(ROOT, 'wireframes/*.html')) for a in re.findall(r'class="([^"]+)"', open(f).read()) for c in a.split()}   # a class the screens carry with no rule (a script's hook) exists too
CLASSES = set(re.findall(r'\.(-?[a-zA-Z_][\w-]*)', ''.join(re.findall(r'([^{}]+)\{', _css))))
NOT_NAMES = {'no-verify', 'x'}
NOT_CLASSES = {'prominent'}   # Apple's style name, in DESIGN.md's HIG table ("the `.prominent` style"), not a class of ours
HISTORY = re.compile(r"\b(Kit fix|Markup pass|On the kit|was|were|until|renamed|retired|removed|merged|split from|replaced|deleted|gone|formerly|no longer|superseded|moved from|left|redirects?|before that|the day before|old)\b", re.I)
EXT = r'(?:css|html|md|py|mjs|js|json|sh|svg|txt)'
FILE = re.compile(r'^(?:\.\./)*[\w.-]+(?:/[\w.*<>-]+)*/(?:[\w.-]+\.' + EXT + r')?$|^[\w-]+\.' + EXT + r'$')

def sentences(text):
    return re.split(r'(?<=[.!?])\s+(?=[A-Z`*"(])|\n', text)

def names_in(snippet):
    """The names one code span holds: tokens, classes and a path."""
    out = []
    for t in re.findall(r'(?<![\w-])--([a-z0-9][a-z0-9-]*)', snippet):
        if t not in NOT_NAMES: out.append(('token', t))
    s = snippet.strip()
    if FILE.match(s) and '*' not in s and '<' not in s and not s.startswith('http'):
        out.append(('file', s))
    elif not re.match(r'^[\w./-]+\.' + EXT + r'$', s):   # a selector, not a file name
        for c in re.findall(r'(?<![\w/-])\.([a-zA-Z][\w-]*)(?![\w/])', re.sub(r'\[[^\]]*\]|"[^"]*"|\([^)]*\.(?:' + EXT + r')[^)]*\)', '', snippet)):
            if c not in {'css', 'html', 'md', 'py', 'js', 'mjs', 'json', 'sh', 'svg', 'com', 'org', 'io'} and not re.fullmatch(r'\d+\w*', c):
                out.append(('class', c))
    return out

def exists(kind, name):
    if kind == 'token': return name in TOKENS
    if kind == 'class': return name in CLASSES or name in NOT_CLASSES or name in MARKUP
    p = name.rstrip('/')
    if name.endswith('/'):   # a folder
        return any(os.path.isdir(os.path.normpath(os.path.join(ROOT, base, p))) for base in ('', 'design-system', 'design-system/docs'))
    if '/' not in p:   # a bare file name ("jtbd.md"): any file of that name in the repo
        return bool(BASENAMES & {p})
    return any(os.path.exists(os.path.normpath(os.path.join(ROOT, base, p))) for base in ('', 'design-system', 'design-system/docs', 'scripts', 'wireframes'))

BASENAMES = {f for d, _, fs in os.walk(ROOT) if '/.git' not in d and '/node_modules' not in d for f in fs}
RECORD_LINE = re.compile(r'^\s*(?:[-|]\s*)?\*\*(?:On the kit|Kit fix|Step \d|Markup pass|Round \d|Updated|Retired|Removed)[^*]*\*\*')   # a dated record bullet: history whole
fails = []
def check_text(where, text, code_re):
    text = '\n'.join(l for l in text.split('\n') if not RECORD_LINE.match(l))
    for sent in sentences(text):
        if HISTORY.search(sent): continue
        spans = code_re.findall(sent)
        if where.startswith('DESIGN.md'):   # DESIGN.md's prose names tokens outside code too
            spans += re.findall(r'(?<![`\w-])(--[a-z0-9][a-z0-9-]*)', sent)
        for sp in spans:
            for kind, name in names_in(H.unescape(sp)):
                if not exists(kind, name): fails.append(f'{where}: the {kind} {"--" if kind == "token" else "." if kind == "class" else ""}{name} doesn\'t exist ("{sent.strip()[:90]}")')

# DESIGN.md, without its generated frontmatter
d = rd('DESIGN.md'); d = d.split('\n---\n', 1)[1] if d.startswith('---') else d
for i, block in enumerate(re.split(r'\n(?=#{2,3} )', d)):
    check_text('DESIGN.md → ' + block.split('\n', 1)[0].lstrip('# ')[:40], block, re.compile(r'`([^`]+)`'))
# ui/inventory.md, its live sections
RECORDS = ('Closed', 'Consolidated', 'Markup pass', 'Race picker pushed', 'Step 6', 'Step 7')
for block in re.split(r'\n(?=## )', rd('ui/inventory.md')):
    head = block.split('\n', 1)[0].lstrip('# ')
    if head.startswith(RECORDS): continue
    check_text('ui/inventory.md → ' + head[:40], block, re.compile(r'`([^`]+)`'))
# every docs page that isn't a redirect: the words a reader sees, <code> as names
for f in sorted(glob.glob(os.path.join(ROOT, 'design-system/docs/*.html')) + glob.glob(os.path.join(ROOT, 'design-system/docs/components/*.html'))):
    h = rd(os.path.relpath(f, ROOT))
    if 'http-equiv="refresh"' in h: continue
    body = re.sub(r'<script\b.*?</script>|<style\b.*?</style>|<div class="kit-frame.*?</div>', ' ', h.split('<body', 1)[1], flags=re.S)
    body = re.sub(r'<code>(.*?)</code>', lambda m: '`' + re.sub(r'<[^>]+>', '', m.group(1)) + '`', body, flags=re.S)
    text = re.sub(r'<(p|li|h[1-6]|dd|dt|td|th|blockquote|figcaption|footer)\b[^>]*>', '\n', body)
    text = re.sub(r'<[^>]+>', ' ', text)
    check_text(os.path.relpath(f, ROOT), text, re.compile(r'`([^`]+)`'))

fails = list(dict.fromkeys(fails))
if fails:
    print(f'check_names: FAIL ({len(fails)})\n  ' + '\n  '.join(fails[:60]))
    sys.exit(1)
print(f'check_names: pass (DESIGN.md, ui/inventory.md and every docs page name only tokens, classes and files that exist; {len(TOKENS)} tokens, {len(CLASSES)} classes known)')
