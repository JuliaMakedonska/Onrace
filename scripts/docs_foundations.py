"""Getting started and Foundations for design-system/docs/ (designer, 2026-11-08: the navigation restructure).

pages() returns [(path, html)], written by scripts/build_kit_showcase.py with the rest of the docs:
- contributing.html, design-system/CONTRIBUTING.md rendered; backlog.html, design-system/backlog.md rendered;
- a page per foundation (ui/inventory.md → Docs navigation → Foundations): the DESIGN.md text it names, then the tokens
  of its groups in design-system/tokens/tokens.css, moved from the Lesson 08 token reference (scripts/tokens_reference.py,
  whose renderers it uses: hue ladders with the roles that read each primitive, a table per group with a sample, the
  semantic roles in both themes, the contrast pairs). Nothing is written by hand: every word is from DESIGN.md,
  tokens.css (its comments), the two Markdown files, or the reference's own column names.
No course-process text: DESIGN.md and the token comments go through docs_clean.clean(), as on every docs page. The
backlog is the exception: it is ordered by the lessons that take each item, so its page keeps them
(scripts/check_kit.py doesn't look for process text there).
"""
import os, re, html as H
import docs_shell as DS
import tokens_reference as REF
from docs_md import md, inline, GH
from docs_clean import clean
ROOT = DS.ROOT
DESIGN = open(os.path.join(ROOT, 'DESIGN.md')).read()
slug_c = DS.slug_c

def _design(ptr):
    """A DESIGN.md pointer: `Heading` is that section, rendered whole; `Heading › words` is the first bullet under it
    that starts with or holds those words."""
    head, _, words = ptr.partition(' › ')
    m = re.search(r'^(#{2,3}) ' + re.escape(head) + r'[^\n]*\n', DESIGN, flags=re.M)
    assert m, f'DESIGN.md has no heading "{head}" (ui/inventory.md → Docs navigation → Foundations)'
    lvl = len(m.group(1))
    end = re.search(r'^#{1,' + str(lvl) + r'} ', DESIGN[m.end():], flags=re.M)
    body = DESIGN[m.end():m.end() + end.start()] if end else DESIGN[m.end():]
    title = clean(m.group(0).lstrip('#').strip())
    if not words: return title, md(clean(body), 'DESIGN.md')
    first = re.search(r'^#{1,3} ', body, flags=re.M)   # the bullets directly under the heading
    bullets = re.findall(r'^- (.*)$', body[:first.start()] if first else body, flags=re.M)
    hit = next((b for b in bullets if b.startswith('**' + words) or b.startswith(words)), None) or next((b for b in bullets if words.lower() in b.lower()), None)
    assert hit, f'DESIGN.md → {head}: no bullet with "{words}"'
    return title, f'<p>{inline(clean(hit), "DESIGN.md")}</p>'

def _src(head):
    a = re.sub(r'\s', '-', re.sub(r'[^\w\s-]', '', head.lower()))
    return f'<p class="dp-src">From <a href="{GH}DESIGN.md#{a}">DESIGN.md → {H.escape(head)}</a></p>'

# ---------------------------------------------------------------- the tokens, as the token reference draws them
for _n in list(REF.COMMENT): REF.COMMENT[_n] = clean(REF.COMMENT[_n])   # the hue ladders read their notes from here
def _group(name):
    g = [(t, ds) for t, ds in REF.PRIM_GROUPS if t.split(':')[0].split(' (')[0] == name or t.startswith(name + ':') or t.startswith(name + ' (')]
    assert g, f'tokens.css has no group "{name}" (ui/inventory.md → Docs navigation → Foundations)'
    return g
def _table(ds):
    rows = [(f'<code>--{n}</code>', REF.value_cell(n, v), REF.sample(n, v), H.escape(clean(c)) or '—') for n, v, c in ds]
    return REF.table(['Token', 'Value', 'Looks like', 'What it is for'], rows, 'ref roles')
def _tokens(name):
    """[(id, title, html, count)] for one token group of a foundation."""
    if name == 'color':
        return [('primitives', 'Color primitives', ''.join(REF.fold(f'{h.capitalize()}: {sum(1 for n in REF.COLOR_PRIMS if REF.hue(n) == h)} primitives', REF.ladder(h),
                 REF.HUE_NOTE.get(h) or 'lightest first, with the roles that read each', open_=True) for h in REF.HUES), len(REF.COLOR_PRIMS))]
    if name == 'the semantic roles':
        out = ''.join(REF.fold(f'{clean(t)[0].upper() + clean(t)[1:]}: {len(ds)}',
                      REF.table(['Role', 'Dark', 'Light', 'What it is for'], [(f'<code>--{n}</code>', REF.role_cell(n, 'dark'), REF.role_cell(n, 'light'), H.escape(clean(c))) for n, _, c in ds], 'ref roles'),
                      'dark and light, and what each is for', open_=True) for t, ds in REF.SEM_GROUPS)
        return [('roles', 'Semantic roles', out, len(REF.ROLES))]
    if name == 'the contrast pairs':
        return [('contrast', 'Contrast pairs', REF.contrast_html(), 0)]
    return [(slug_c(clean(t).split(':')[0]), (clean(t).split(':')[0])[0].upper() + clean(t).split(':')[0][1:], _table(ds), len(ds)) for t, ds in _group(name)]

def count(f):   # how many tokens a foundation shows
    return sum(c for g in f['groups'] for *_, c in _tokens(g))

CSS = ('<style>/* the token reference\'s drawing (scripts/tokens_reference.py), on the docs layer\'s colors */\n'
       '.ds-ref { --border: var(--d-border); --bg-elev: var(--d-elev); --bg-elev-2: var(--d-elev-2); --text: var(--d-text); --text-dim: var(--d-dim); --text-faint: var(--d-faint); --accent: var(--d-text); display: grid; grid-template-columns: minmax(0, 1fr); gap: 12px; }\n'
       '.ds-ref > *, .ds-ref .fold-body { min-width: 0; }\n'
       + re.sub(r'(^|\n)(\s*)([^{}@\n][^{}\n]*)\{', lambda m: m.group(1) + m.group(2) + ', '.join('.ds-ref ' + x.strip() for x in m.group(3).split(',')) + '{', REF.CSS).replace('.bar', '.ref-bar')
       + '\n.ds-ref table { border-collapse: collapse; font-size: 13.5px; } .ds-ref th, .ds-ref td { text-align: left; padding: 8px 16px 8px 0; border-bottom: 1px solid var(--d-border); color: var(--d-dim); }'
       '\n.ds-ref .rc { white-space: normal; overflow-wrap: anywhere; }'
       '\n.ds-ref th { font-weight: 500; color: var(--d-faint); } .ds-ref .note { color: var(--d-faint); font-size: 13.5px; }'
       '\n</style>')

def _section(id_, title, body, sub=False):
    return f'<section class="dc dc--part" id="{id_}" aria-labelledby="{id_}-h"><h2 id="{id_}-h">{H.escape(title)}</h2>\n{body}\n</section>'

def foundation(f):
    secs = []
    for ptr in f['design']:
        title, body = _design(ptr)
        secs.append((slug_c(title), title, f'<div class="dp-why">{body}</div>' + _src(title)))
    for g in f['groups']:
        for id_, title, html_, n in _tokens(g):
            body = f'<div class="ds-ref">{html_}</div>'.replace('class="bar', 'class="ref-bar').replace('src="visuals/', 'src="../../visuals/')
            secs.append((id_, title, body + '<p class="dp-src">From <a href="' + GH + 'design-system/tokens/tokens.css">design-system/tokens/tokens.css</a></p>'))
    seen = set()
    for i, (id_, *_rest) in enumerate(secs):   # a heading may repeat (two "Named Rules"): its id takes a number
        k = id_; j = 2
        while k in seen: k = f'{id_}-{j}'; j += 1
        seen.add(k); secs[i] = (k, *_rest)
    main = (f'<p class="ds-crumb">Foundations</p><h1>{H.escape(f["title"])}</h1>\n' + '\n'.join(_section(*s) for s in secs))
    return DS.page(f'{f["title"]} · Onrace design system', f['page'], main, [(i, t) for i, t, _ in secs], CSS)

def markdown_page(page, title, path, keep_process=False):
    text = open(os.path.join(ROOT, path)).read()
    text = re.sub(r'^# [^\n]*\n', '', text, count=1)   # the file's own title is the page's h1
    if not keep_process: text = clean(text)
    parts = re.split(r'^## ', text, flags=re.M)
    lead, secs = parts[0], [(p.split('\n', 1)[0].strip(), p.split('\n', 1)[1] if '\n' in p else '') for p in parts[1:]]
    main = (f'<h1>{H.escape(title)}</h1><div class="dp-why ds-lead">{md(lead, path)}</div>\n'
            + '\n'.join(f'<section class="dc-why" id="{slug_c(h)}" aria-labelledby="{slug_c(h)}-h"><h2 id="{slug_c(h)}-h">{inline(h, path)}</h2><div class="dp-why">{md(b, path)}</div></section>' for h, b in secs)
            + f'<p class="dp-src">From <a href="{GH}{path}">{path}</a></p>')
    return DS.page(f'{title} · Onrace design system', page, main, [(slug_c(h), re.sub(r'`', '', h)) for h, _ in secs])

def pages():
    out = [('contributing.html', markdown_page('contributing', 'Contributing', 'design-system/CONTRIBUTING.md')),
           ('backlog.html', markdown_page('backlog', 'Backlog', 'design-system/backlog.md', keep_process=True))]
    return out + [(f['page'] + '.html', foundation(f)) for f in DS.FOUNDATIONS]
