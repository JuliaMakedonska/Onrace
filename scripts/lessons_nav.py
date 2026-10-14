"""The numbered lessons bar shared by the artifact pages (one list, one look).

Generated pages (voice.html, concept-overview.html) import BAR_CSS and bar() from their build scripts.
Hand-written pages are updated in place:  python3 scripts/lessons_nav.py
The bar sits just above each page's sticky <nav> and scrolls away, so the sticky part keeps its height; workspace.html lists the same links in its "Lessons" sidebar group.
"""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LESSONS = [('research.html', '01', 'Research'), ('personas.html', '02', 'Personas &amp; JTBD'), ('ia.html', '03', 'IA'),
           ('wireframes/index.html', '04', 'Wireframes'), ('voice.html', '05', 'Voice'), ('concept-overview.html', '06', 'Concept')]

BAR_CSS = '''
  /* Lessons bar (scripts/lessons_nav.py): the same six links on every artifact page */
  .lessonbar{border-bottom:1px solid var(--border)}
  .lessonbar-inner{max-width:var(--maxw); margin:0 auto; padding:0 24px; display:flex; gap:2px; overflow-x:auto; scrollbar-width:none}
  .lessonbar-inner::-webkit-scrollbar{display:none}
  .lessonbar a{flex:none; color:var(--text-faint); text-decoration:none; font-size:12px; font-weight:700; letter-spacing:.04em; padding:8px 10px; border-bottom:2px solid transparent; white-space:nowrap}
  .lessonbar a:hover{color:var(--text)}
  .lessonbar a[aria-current="page"]{color:var(--text); border-bottom-color:var(--accent)}
'''

def bar(current=None):
    cur = ' aria-current="page"'
    links = ''.join(f'<a href="{href}"{cur if href == current else ""}>{n} · {name}</a>' for href, n, name in LESSONS)
    return f'<!-- lessons:start --><div class="lessonbar"><div class="lessonbar-inner" role="navigation" aria-label="Lessons">{links}</div></div><!-- lessons:end -->'

def sidebar_links():
    return ''.join(f'\n        <a href="{href}">{n} · {name}</a>' for href, n, name in LESSONS)

def apply(path, current):
    """Put the bar just above a hand-written page's <nav> (idempotent)."""
    h = open(path).read()
    h = re.sub(r'\n\s*<a href="concept-overview\.html">06 · Concept</a>', '', h)   # the single link from the first pass
    h = re.sub(r'<!-- lessons:start -->.*?<!-- lessons:end -->\n?', '', h, flags=re.S)
    h = re.sub(r'\n  /\* Lessons bar \(scripts/lessons_nav\.py\).*?\.lessonbar a\[aria-current="page"\]\{[^}]*\}\n', '\n', h, flags=re.S)
    assert h.count('<nav>\n') == 1, path
    h = h.replace('</style>', BAR_CSS + '</style>', 1)
    h = h.replace('<nav>\n', bar(current) + '\n<nav>\n', 1)
    open(path, 'w').write(h)

if __name__ == '__main__':
    for p, cur in [('public/research.html', 'research.html'), ('public/personas.html', 'personas.html'),
                   ('public/ia.html', 'ia.html'), ('ia.html', 'ia.html')]:
        apply(os.path.join(ROOT, p), cur)
    # workspace.html: the sidebar's Lessons group (01 and 02 are merged into this page)
    p = os.path.join(ROOT, 'public/workspace.html')
    h = open(p).read()
    h, n = re.subn(r'(<h4>Lessons</h4>)(?:\n        <a href="[^"]+">[^<]+</a>)+', lambda m: m.group(1) + sidebar_links(), h)
    assert n == 1
    open(p, 'w').write(h)
    print('lessons bar applied')
