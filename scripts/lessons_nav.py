"""The lesson list shared by the whole project (one list, one look).

LESSONS holds all twelve lessons; a lesson without a page yet (href None) is a future one.
- The workspace shell (public/workspace.html, scripts/build_workspace.py) shows all twelve in its rail.
- Each lesson page carries a bar of the done lessons. Generated pages (voice.html, concept-overview.html)
  import BAR_CSS and bar() from their build scripts; hand-written pages are updated in place:
  python3 scripts/lessons_nav.py
- The bar sits just above each page's sticky <nav> and scrolls away. Inside the shell the page gets the
  class "in-shell" on <html> and the bar is hidden, because the shell's rail does the job.
- start.html (the 01–02 overview, the shell's start page) lists the done lessons in its "Lessons" sidebar group.
"""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LESSONS = [('research.html', '01', 'Research'), ('personas.html', '02', 'Personas &amp; JTBD'), ('ia.html', '03', 'IA'),
           ('wireframes/index.html', '04', 'Wireframes'), ('voice.html', '05', 'Voice'), ('concept-overview.html', '06', 'Concept'),
           ('ui-overview.html', '07', 'UI assembly'), (None, '08', 'Design tokens'), (None, '09', 'Design system'), (None, '10', 'Responsive'),
           (None, '11', 'Animation &amp; micro-interactions'), (None, '12', 'Handoff')]
DONE = [l for l in LESSONS if l[0]]

# Marks a page shown inside the workspace shell, before anything paints
IN_SHELL_JS = '<script>if (window.top !== window.self) document.documentElement.classList.add("in-shell");</script>'

BAR_CSS = '''
  /* Lessons bar (scripts/lessons_nav.py): the same six links on every artifact page */
  .lessonbar{border-bottom:1px solid var(--border)}
  .lessonbar-inner{max-width:var(--maxw); margin:0 auto; padding:0 24px; display:flex; gap:2px; overflow-x:auto; scrollbar-width:none}
  .lessonbar-inner::-webkit-scrollbar{display:none}
  .lessonbar a{flex:none; color:var(--text-faint); text-decoration:none; font-size:12px; font-weight:700; letter-spacing:.04em; padding:8px 10px; border-bottom:2px solid transparent; white-space:nowrap}
  .lessonbar a:hover{color:var(--text)}
  .lessonbar a[aria-current="page"]{color:var(--text); border-bottom-color:var(--accent)}
  .in-shell .lessonbar{display:none}
'''

def bar(current=None):
    cur = ' aria-current="page"'
    links = ''.join(f'<a href="{href}"{cur if href == current else ""}>{n} · {name}</a>' for href, n, name in DONE)
    return f'<!-- lessons:start -->{IN_SHELL_JS}<div class="lessonbar"><div class="lessonbar-inner" role="navigation" aria-label="Lessons">{links}</div></div><!-- lessons:end -->'

def sidebar_links():
    return ''.join(f'\n        <a href="{href}">{n} · {name}</a>' for href, n, name in DONE)

def apply(path, current):
    """Put the bar just above a hand-written page's <nav> (idempotent)."""
    h = open(path).read()
    h = re.sub(r'\n\s*<a href="concept-overview\.html">06 · Concept</a>', '', h)   # the single link from the first pass
    h = re.sub(r'<!-- lessons:start -->.*?<!-- lessons:end -->\n?', '', h, flags=re.S)
    h = re.sub(r'\n  /\* Lessons bar \(scripts/lessons_nav\.py\).*?\.lessonbar a\[aria-current="page"\]\{[^}]*\}\n(  \.in-shell \.lessonbar\{display:none\}\n)?', '\n', h, flags=re.S)
    assert h.count('<nav>\n') == 1, path
    h = h.replace('</style>', BAR_CSS + '</style>', 1)
    h = h.replace('<nav>\n', bar(current) + '\n<nav>\n', 1)
    open(path, 'w').write(h)

if __name__ == '__main__':
    for p, cur in [('public/research.html', 'research.html'), ('public/personas.html', 'personas.html'),
                   ('public/ia.html', 'ia.html'), ('ia.html', 'ia.html')]:
        apply(os.path.join(ROOT, p), cur)
    # start.html: the sidebar's Lessons group (01 and 02 are merged into this page)
    p = os.path.join(ROOT, 'public/start.html')
    h = open(p).read()
    h, n = re.subn(r'(<h4>Lessons</h4>)(?:\n        <a href="[^"]+">[^<]+</a>)+', lambda m: m.group(1) + sidebar_links(), h)
    assert n == 1
    # inside the shell, start.html hides its own sidebar: the shell's rail lists the same sections
    h = re.sub(r'<!-- shell:start -->.*?<!-- shell:end -->\n', '', h, flags=re.S)
    h = h.replace('<body>\n', '<body>\n<!-- shell:start -->' + IN_SHELL_JS + '<style>.in-shell .sidebar{display:none}</style><!-- shell:end -->\n', 1)
    open(p, 'w').write(h)
    print('lessons bar applied')
