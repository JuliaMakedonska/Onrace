"""Markdown to HTML for the design-system docs (Lesson 9, step 2, 2026-11-04).

The same small renderer the lesson overviews use (scripts/build_concept_overview.py): paragraphs, ### headings, lists,
tables, `code`, **bold**, *italic* and links. A relative link is read from the folder of the file it came from (`base`)
and goes to that file on GitHub, so a quote keeps its links wherever the page is. Mobbin links need a login, so they
keep their text and lose the link (as on the Lesson 6 overview).
"""
import os, re, html

GH = 'https://github.com/JuliaMakedonska/Onrace/blob/main/'

def sections(text, level='## '):
    parts = re.split(r'^' + re.escape(level), text, flags=re.M)
    return {p.split('\n', 1)[0].strip(): p.split('\n', 1)[1] if '\n' in p else '' for p in parts[1:]}

def inline(t, base=''):
    t = re.sub(r'\[([^\]]+)\]\(https://mobbin\.com/[^)]+\)', r'\1', t)
    t = html.escape(t, quote=False)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', t)
    def link(m):
        href = m.group(2)
        if href.startswith('#'):
            href = GH + base.rstrip('/') + href if base.endswith('.md') else href
        elif not re.match(r'^[a-z]+:', href):
            path, _, frag = href.partition('#')
            href = GH + os.path.normpath(os.path.join(os.path.dirname(base) if base.endswith('.md') else base, path)) + ('#' + frag if frag else '')
        return f'<a href="{href}">{m.group(1)}</a>'
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, t)
    return t.replace('\\&lt;', '&lt;').replace('\\&gt;', '&gt;').replace('\\|', '|')

def table(lines, base=''):
    rows = [[c.strip() for c in re.split(r'(?<!\\)\|', l.strip().strip('|'))] for l in lines]
    h = '<div class="tbl-wrap"><table><thead><tr>' + ''.join(f'<th>{inline(c, base)}</th>' for c in rows[0]) + '</tr></thead><tbody>'
    for r in rows[2:]:
        h += '<tr>' + ''.join(f'<td>{inline(c, base)}</td>' for c in r) + '</tr>'
    return h + '</tbody></table></div>'

def md(text, base=''):
    out, lines, i = [], text.split('\n'), 0
    while i < len(lines):
        l = lines[i]
        if not l.strip() or l.strip() == '---': i += 1; continue
        if l.startswith('#### '): out.append(f'<h4>{inline(l[5:], base)}</h4>'); i += 1; continue
        if l.startswith('### '): out.append(f'<h3>{inline(l[4:], base)}</h3>'); i += 1; continue
        if l.startswith('> '):
            blk = []
            while i < len(lines) and lines[i].startswith('>'): blk.append(lines[i].lstrip('> ').strip()); i += 1
            out.append(f'<blockquote><p>{inline(" ".join(blk), base)}</p></blockquote>'); continue
        if l.startswith('|'):
            blk = []
            while i < len(lines) and lines[i].startswith('|'): blk.append(lines[i]); i += 1
            out.append(table(blk, base)); continue
        if re.match(r'^\s*(- |\d+\. )', l):
            h, stack = [], []
            while i < len(lines) and re.match(r'^\s*(- |\d+\. )', lines[i]):
                m = re.match(r'^(\s*)(- |\d+\. )(.*)$', lines[i])
                ind, tag = len(m.group(1)), 'ol' if m.group(2)[0].isdigit() else 'ul'
                while stack and ind < stack[-1][0]: h.append(f'</{stack.pop()[1]}>')
                if not stack or ind > stack[-1][0]: h.append(f'<{tag}>'); stack.append((ind, tag))
                h.append(f'<li>{inline(m.group(3), base)}</li>'); i += 1
            while stack: h.append(f'</{stack.pop()[1]}>')
            s = ''.join(h)
            s = re.sub(r'</li><(ul|ol)>', r'<\1>', s)
            s = re.sub(r'</(ul|ol)>(?=<li>|</ul>|</ol>)', r'</\1></li>', s)
            out.append(s); continue
        blk = []
        while i < len(lines) and lines[i].strip() and not re.match(r'^(#|\||>|\s*- |\s*\d+\. |---)', lines[i]): blk.append(lines[i].strip()); i += 1
        if blk: out.append(f'<p>{inline(" ".join(blk), base)}</p>')
        else: i += 1
    return '\n'.join(out)
