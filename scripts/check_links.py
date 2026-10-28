"""Every page links only files that exist (Lesson 8, step 4, 2026-10-28).

Run from anywhere:  python3 scripts/check_links.py      exit code 1 on any failure.
build_stand.py runs it on every build. It reads every .html page of the published site, public/ (what GitHub Pages
serves), and of the source folders mirrored into it as they are (wireframes/, ui/, concept/, visuals/), but not the
frozen wireframes/_wireframe/ snapshots, which link files that are gone on purpose. The repo-root pages (ia.html,
voice.html, index.html) are checked as their published copies in public/. It fails when a local
stylesheet, script, image, frame, link or srcset entry points to a file that doesn't exist: href, src and srcset
attributes, including inside a srcdoc frame, where the quotes are &quot;. External URLs, in-page anchors, data:,
mailto: and javascript: are skipped; ?query and #hash are dropped before the file is looked up.
It is how the build stops a page that still links a deleted file (ui/kit.css and ui/map.css, removed in step 4).
"""
import os, re, sys, html
from urllib.parse import unquote
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIRS = ['public', 'wireframes', 'ui', 'concept', 'visuals']
SKIP_DIRS = {'_wireframe'}
ATTR = re.compile(r'''\b(href|src|srcset)\s*=\s*("|'|&quot;)(.*?)\2''', flags=re.S | re.I)
EXTERNAL = re.compile(r'^(?:[a-z][a-z0-9+.-]*:|//|#|\$\{|\{)', flags=re.I)   # scheme, protocol-relative, anchor, template

def targets(attr, value):
    if attr.lower() == 'srcset':
        return [c.strip().split()[0] for c in value.split(',') if c.strip()]
    return [value.strip()]

pages, fails, checked = [], [], 0
for top in DIRS:
    for d, dirs, files in os.walk(os.path.join(ROOT, top)):
        dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
        pages += [os.path.join(d, f) for f in files if f.endswith('.html')]
for page in sorted(pages):
    text = open(page, encoding='utf-8').read()
    text = re.sub(r'<script\b[^>]*>.*?</script>', lambda m: m.group(0) if 'src=' in m.group(0)[:m.group(0).find('>')] else '', text, flags=re.S | re.I)   # URLs built by page scripts aren't links
    text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
    for attr, _, raw in ATTR.findall(text):
        for t in targets(attr, html.unescape(raw)):
            if not t or EXTERNAL.match(t) or '<' in t:   # '<scene>-1026.jpg': markup quoted as text in a <code>, not a link
                continue
            path = unquote(re.split(r'[?#]', t, 1)[0])
            if not path:
                continue
            base = os.path.join(ROOT, 'public') if path.startswith('/') else os.path.dirname(page)   # / is the site root
            full = os.path.normpath(os.path.join(base, path.lstrip('/')))
            checked += 1
            if not os.path.exists(full):
                fails.append(f'{os.path.relpath(page, ROOT)}: {attr}="{t}" (no {os.path.relpath(full, ROOT)})')
if fails:
    print(f'check_links: FAIL, {len(fails)} links to missing files\n  ' + '\n  '.join(sorted(set(fails))))
    sys.exit(1)
print(f'check_links: pass ({checked} local links in {len(pages)} pages, every file exists)')
