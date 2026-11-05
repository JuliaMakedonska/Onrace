"""Write design-system/docs/why.html, "why the system looks like this" (Lesson 9, step 2, 2026-11-04).

Run from anywhere:  python3 scripts/build_docs_why.py      (build_stand.py runs it with the component pages)
Every section is rendered from concept/references.md and concept/concept.md, never rewritten by hand: the references
and techniques, the designer's taste, the attributes, the hierarchy rules, and the chosen direction with why. Each
section keeps its source heading and links back to it. Re-run after editing either file; the page is generated.
"""
import os, re, sys, html as H
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docs_md import md, sections, GH
from docs_clean import clean   # no course-process text on a docs page (2026-11-05)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C = open(os.path.join(ROOT, 'concept/concept.md')).read()
R = open(os.path.join(ROOT, 'concept/references.md')).read()
CS, RS = sections(C), sections(R)

def anchor(h):   # GitHub's heading anchor
    return re.sub(r'\s', '-', re.sub(r'[^\w\s-]', '', h.lower()))

# (source file, its sections, the heading, the page's section id), in the order a reader needs them:
# where the look comes from, what the designer likes, what it must say, how it ranks, and what was chosen
PARTS = [('concept/references.md', RS, '2. Visual language per product', 'references'),
         ('concept/references.md', RS, '4. Picked styles', 'techniques'),
         ('concept/concept.md', CS, "Designer's taste", 'taste'),
         ('concept/concept.md', CS, 'Attributes', 'attributes'),
         ('concept/concept.md', CS, 'Hierarchy rules (designer)', 'hierarchy'),
         ('concept/concept.md', CS, 'Directions (step 3, chosen 2026-10-13)', 'direction')]
import docs_shell as DS
body = []
for src, secs, head, id_ in PARTS:
    assert head in secs, f'{src}: no section "## {head}"'
    shown = clean(re.sub(r'^\d+\.\s*', '', head))   # the heading as the docs show it: no number, no process note
    body.append(f'''<section class="dc-why" id="{id_}" aria-labelledby="{id_}-h"><h2 id="{id_}-h">{H.escape(shown)}</h2>
<div class="dp-why">
{md(clean(secs[head]), src)}
</div>
<p class="dp-src">From <a href="{GH}{src}#{anchor(head)}">{src} → {H.escape(shown)}</a></p>
</section>''')
main = (f'<h1>Why the system looks like this</h1><p class="ds-lede">The visual language behind every component, from <a href="{GH}concept/references.md">concept/references.md</a> '
        f'(the references and techniques) and <a href="{GH}concept/concept.md">concept/concept.md</a> (the designer\'s taste, the attributes, the hierarchy rules, '
        f'the chosen direction and why), as those files say it.</p>\n' + '\n'.join(body))
page = DS.page('Why the system looks like this · Onrace design system', 'why', main, [(id_, clean(re.sub(r'^\d+\.\s*', '', head))) for _, _, head, id_ in PARTS])
open(os.path.join(ROOT, 'design-system/docs/why.html'), 'w').write(page)
print('why.html:', len(PARTS), 'sections from concept/references.md and concept/concept.md,', len(page), 'bytes')
