"""Rebase the relative URLs of a page that moves (Lesson 9, step 2, 2026-11-04).

rebase(html, old_dir, new_dir) rewrites every relative href, src and srcset in the markup, including those inside a
srcdoc frame (quoted &quot;), so each still points at the same repo file from the page's new folder. External URLs,
in-page anchors, data:, mailto: and javascript: stay as they are. Used to move the showcase out of ui/ and by
scripts/build_kit_showcase.py, which writes the component pages from the specimens of design-system/docs/index.html.
"""
import os, re
ATTR = re.compile(r'''\b(href|src|srcset)=("|&quot;)(.*?)\2''', flags=re.S)
SKIP = re.compile(r'^(?:[a-z][a-z0-9+.-]*:|//|#|\$\{|\{)', flags=re.I)

def _one(url, old_dir, new_dir):
    if not url or SKIP.match(url): return url
    m = re.match(r'([^?#]*)(.*)', url, flags=re.S)
    path, rest = m.group(1), m.group(2)
    if not path: return url
    target = os.path.normpath(os.path.join(old_dir, path))
    return os.path.relpath(target, new_dir) + ('/' if path.endswith('/') else '') + rest

def rebase(html, old_dir, new_dir):
    if os.path.normpath(old_dir) == os.path.normpath(new_dir): return html
    def sub(m):
        attr, q, val = m.groups()
        if attr == 'srcset':
            val = ', '.join(' '.join([_one(c.strip().split()[0], old_dir, new_dir)] + c.strip().split()[1:]) for c in val.split(',') if c.strip())
        else:
            val = _one(val, old_dir, new_dir)
        return f'{attr}={q}{val}{q}'
    return ATTR.sub(sub, html)
