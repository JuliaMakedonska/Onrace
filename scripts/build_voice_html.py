"""Build voice.html (and its public/ copy) from voice.md and microcopy.md.

Run from anywhere:  python3 scripts/build_voice_html.py
Re-run after editing voice.md or microcopy.md; the page is generated, never hand-edited.
Styling is taken from ia.html's :root tokens so the pages stay consistent.
"""
import re, json, html
import os
import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lessons_nav import BAR_CSS, bar as lessons_bar
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root
V=open(ROOT+'/voice.md').read()
M=open(ROOT+'/microcopy.md').read()
esc=lambda t: html.escape(t, quote=False)

def inline(t):
    t=esc(t)
    t=re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t=re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t=re.sub(r'~~(.+?)~~', r'<s>\1</s>', t)
    t=re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', t)
    t=re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', t)
    t=t.replace('\\&lt;','&lt;').replace('\\&gt;','&gt;').replace('\\|','|')
    return t

def table(lines):
    rows=[]
    for l in lines:
        cells=re.split(r'(?<!\\)\|', l.strip().strip('|'))
        rows.append([c.strip() for c in cells])
    head, body = rows[0], [r for r in rows[2:]]
    h='<div class="tbl-wrap"><table class="md"><thead><tr>'+''.join(f'<th>{inline(c)}</th>' for c in head)+'</tr></thead><tbody>'
    for r in body: h+='<tr>'+''.join(f'<td>{inline(c)}</td>' for c in r)+'</tr>'
    return h+'</tbody></table></div>'

def md(text):
    out=[]; lines=text.split('\n'); i=0; pending=None
    while i<len(lines):
        l=lines[i]
        if not l.strip(): i+=1; continue
        if l.startswith('### '):
            out.append(f'<h3 id="{slug(l[4:])}">{inline(l[4:])}</h3>'); i+=1; continue
        if l.startswith('#### '):
            out.append(f'<h4>{inline(l[5:])}</h4>'); i+=1; continue
        if l.strip()=='---': out.append('<hr>'); i+=1; continue
        if l.startswith('|'):
            blk=[]
            while i<len(lines) and lines[i].startswith('|'): blk.append(lines[i]); i+=1
            out.append(table(blk)); continue
        if l.startswith('>'):
            blk=[]
            while i<len(lines) and lines[i].startswith('>'): blk.append(lines[i][1:].strip()); i+=1
            cls=' class="ex-ok"' if pending=='ok' else (' class="ex-bad"' if pending=='bad' else '')
            paras=[p for p in '\n'.join(blk).split('\n\n')]
            inner=''.join(f'<p>{inline(" ".join(x.strip() for x in p.split(chr(10)) if x.strip()))}</p>' for p in paras if p.strip())
            out.append(f'<blockquote{cls}>{inner}</blockquote>'); pending=None; continue
        if re.match(r'^\s*(- |\d+\. )',l):
            # nested list by indent
            html_=[]; stack=[]
            while i<len(lines) and (re.match(r'^\s*(- |\d+\. )',lines[i]) or (lines[i].startswith('   ') and lines[i].strip() and stack)):
                ln=lines[i]
                m=re.match(r'^(\s*)(- |\d+\. )(.*)$',ln)
                if not m:
                    html_[-1]=html_[-1][:-5]+' '+inline(ln.strip())+'</li>'; i+=1; continue
                ind=len(m.group(1)); tag='ol' if m.group(2)[0].isdigit() else 'ul'
                while stack and ind<stack[-1][0]: html_.append(f'</{stack.pop()[1]}>')
                if not stack or ind>stack[-1][0]:
                    html_.append(f'<{tag}>'); stack.append((ind,tag))
                html_.append(f'<li>{inline(m.group(3))}</li>'); i+=1
            while stack: html_.append(f'</{stack.pop()[1]}>')
            # merge nested lists into previous li
            s=''.join(html_); s=re.sub(r'</li><(ul|ol)>', r'<\1>', s); s=re.sub(r'</(ul|ol)>(?=<li>|</ul>|</ol>)', r'</\1></li>', s)
            out.append(s); continue
        # paragraph
        blk=[]
        while i<len(lines) and lines[i].strip() and not re.match(r'^(#|\||>|\s*- |\s*\d+\. |---)',lines[i]): blk.append(lines[i].strip()); i+=1
        p=' '.join(blk)
        if re.match(r'^\*\*Example:\*\*',p): pending='ok'
        elif re.match(r'^\*\*Counter-example:\*\*',p): pending='bad'
        cls=''
        if re.match(r'^\*\*Rule:\*\*',p): cls=' class="rule"'
        out.append(f'<p{cls}>{inline(p)}</p>')
    return '\n'.join(out)

def slug(t): return re.sub(r'[^a-z0-9]+','-',re.sub(r'<[^>]+>|`','',t.lower())).strip('-')

# split voice.md into ## sections
parts=re.split(r'^## ', V, flags=re.M)
intro=parts[0]; secs={}
for p in parts[1:]:
    title,body=p.split('\n',1); secs[title.strip()]=body
intro_body=intro.split('\n',1)[1]
# microcopy: intro sections and rows
mparts=re.split(r'^## ', M, flags=re.M)
msecs={}
for p in mparts[1:]:
    t,b=p.split('\n',1); msecs[t.strip()]=b
rows=[]
for l in M.split('\n'):
    m=re.match(r'^\| (\d+) \|([^|]+)\|((?:[^|\\]|\\\|)*)\|(.*?)\|(.*?)\|(.*?)\|([^|]+)\|([^|]*)\|([^|]+)\|([^|]*)\|$',l)
    if m:
        n,scr,zone,b,a,why,typ,st,src,fl=[x.strip().replace('\\|','|') for x in m.groups()]
        rows.append(dict(n=int(n),screen=scr,zone=zone,before=b,after=a,why=why,type=typ,states=st,source=src,flags=fl))
screens=list(dict.fromkeys(r['screen'] for r in rows))
changed=sum(1 for r in rows if r['after'] not in ('unchanged','') )
nprin=len(re.findall(r'^### \d+\.',secs['Principles'],re.M))

CSS=open(ROOT+'/ia.html').read()
root_css=CSS[CSS.index(':root{'):CSS.index('/* Hero */')]
PAGE=f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Onrace — Voice</title>
<style>
  {root_css}{BAR_CSS}
  /* Hero (same as ia.html) */
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
  h2{{font-size:28px; margin:0 0 8px; font-weight:800; letter-spacing:-.01em}}
  h3{{font-size:19px; margin:34px 0 8px; font-weight:700; scroll-margin-top:72px}}
  h4{{font-size:13px; margin:24px 0 8px; text-transform:uppercase; letter-spacing:.05em; color:var(--text-faint)}}
  .prose p, .prose li{{color:var(--text-dim); font-size:15px; max-width:820px}}
  .prose strong{{color:var(--text)}}
  .prose ul, .prose ol{{padding-left:20px; margin:0 0 14px}}
  .prose li{{margin-bottom:6px}}
  .prose li ul{{margin-top:6px}}
  .prose p.rule{{font-size:16.5px; color:var(--text); background:var(--bg-elev); border:1px solid var(--border); border-left:3px solid var(--accent); border-radius:8px; padding:12px 16px}}
  .prose hr{{border:none; border-top:1px solid var(--border); margin:28px 0}}
  s{{color:var(--text-faint)}}
  blockquote{{ margin:8px 0 16px; padding:12px 16px; border-left:3px solid var(--text-faint); background:var(--bg-elev); border-radius:0 8px 8px 0; }}
  blockquote p{{margin:4px 0; color:var(--text) !important; font-size:15px}}
  blockquote.ex-ok{{border-left-color:var(--ok); background:var(--ok-dim)}}
  blockquote.ex-bad{{border-left-color:var(--accent); background:var(--accent-dim)}}
  blockquote.ex-bad p{{text-decoration:line-through; text-decoration-color:var(--accent); text-decoration-thickness:1px}}
  .principle{{background:var(--bg-elev); border:1px solid var(--border); border-radius:var(--radius); padding:6px 22px 14px; margin:18px 0}}
  .principle h3{{margin-top:18px}}
  .tbl-wrap{{overflow-x:auto; margin:10px 0 20px; border:1px solid var(--border); border-radius:var(--radius)}}
  table{{border-collapse:collapse; width:100%; font-size:13.5px}}
  th{{text-align:left; background:var(--bg-elev-2); color:var(--text-faint); font-size:11px; text-transform:uppercase; letter-spacing:.05em; padding:10px 12px; border-bottom:1px solid var(--border); white-space:nowrap}}
  td{{padding:9px 12px; border-bottom:1px solid var(--border); vertical-align:top; color:var(--text-dim)}}
  tr:last-child td{{border-bottom:none}}
  td strong{{color:var(--text)}}
  /* microcopy browser */
  .mc-controls{{display:flex; flex-wrap:wrap; gap:10px; align-items:center; margin:0 0 18px; position:sticky; top:64px; z-index:10; background:var(--bg); padding:10px 0; border-bottom:1px solid var(--border)}}
  .mc-controls input[type=search], .mc-controls select{{background:var(--bg-elev); color:var(--text); border:1px solid var(--border); border-radius:8px; padding:9px 12px; font:inherit; font-size:14px}}
  .mc-controls input[type=search]{{flex:1 1 260px; min-width:0}}
  .mc-controls label{{font-size:13px; color:var(--text-dim); display:flex; gap:6px; align-items:center}}
  .mc-count{{font-size:12.5px; color:var(--text-faint); margin-left:auto}}
  .mc-btn{{background:var(--bg-elev); color:var(--text-dim); border:1px solid var(--border); border-radius:8px; padding:8px 12px; font:inherit; font-size:13px; cursor:pointer}}
  .mc-btn:hover{{color:var(--text); border-color:var(--text-faint)}}
  details.screen{{background:var(--bg-elev); border:1px solid var(--border); border-radius:var(--radius); margin:0 0 12px}}
  details.screen > summary{{cursor:pointer; list-style:none; padding:14px 18px; display:flex; gap:12px; align-items:baseline}}
  details.screen > summary::-webkit-details-marker{{display:none}}
  details.screen > summary::before{{content:"▸"; color:var(--text-faint); width:12px}}
  details.screen[open] > summary::before{{content:"▾"}}
  .s-name{{font-weight:800; font-size:16px}}
  .s-meta{{font-size:12.5px; color:var(--text-faint)}}
  details.screen .tbl-wrap{{margin:0 14px 14px}}
  td.c-after.changed{{color:var(--text)}}
  td.c-after.changed strong{{color:var(--ok)}}
  td.c-after.same{{color:var(--text-faint); font-style:italic}}
  td.c-after.removed{{color:var(--accent); font-style:italic}}
  td.c-zone, td.c-type{{white-space:nowrap; color:var(--text-faint); font-size:12.5px}}
  td.c-why{{font-size:12.5px}}
  .src{{display:inline-block; font-size:10.5px; font-weight:800; text-transform:uppercase; letter-spacing:.03em; padding:2px 7px; border-radius:999px; margin-top:4px}}
  .src.ours{{background:var(--accent-dim); color:var(--accent)}}
  .src.theirs{{background:var(--bg-elev-2); color:var(--text-faint); border:1px solid var(--border)}}
  .flag{{display:inline-block; font-size:10.5px; font-weight:800; padding:1px 6px; border-radius:4px; background:var(--unconfirmed-dim); color:var(--unconfirmed); margin:2px 2px 0 0}}
  mark{{background:#ff4d2e55; color:var(--text); border-radius:2px}}
  .empty-note{{color:var(--text-faint); font-size:14px; padding:20px 0}}
  footer{{max-width:var(--maxw); margin:0 auto; padding:24px; color:var(--text-faint); font-size:12.5px; border-top:1px solid var(--border)}}
  @media (max-width:640px){{ .mc-controls{{top:0; position:static}} .mc-count{{margin-left:0}} }}
</style>
</head>
<body>
{lessons_bar('voice.html')}
<nav>
  <div class="nav-inner">
    <a href="#top" class="brand" style="text-decoration:none">ON<span>RACE</span> · Voice</a>
    <div class="navlinks">
      <a href="#principles">Principles</a>
      <a href="#dictionary">Dictionary</a>
      <a href="#forbidden">Forbidden</a>
      <a href="#microcopy-rules">Microcopy rules</a>
      <a href="#microcopy-table">All lines</a>
    </div>
  </div>
</nav>
<a id="top"></a>
<header class="hero">
  <p class="kicker">Voice</p>
  <h1>How Onrace speaks</h1>
  <p class="hero-desc">Rendered from <code>voice.md</code> (the rules) and <code>microcopy.md</code> (every interface line, before and after the rewrite). For athletes deciding whether a race is worth entering, and keeping results they may later submit as proof, credibility comes before cleverness.</p>
  <div class="meta-row">
    <span class="pill">{nprin} principles</span>
    <span class="pill">Forbidden &gt; Dictionary &gt; Microcopy &gt; Principles</span>
    <span class="pill">{len(rows)} lines · {len(screens)} screens</span>
    <span class="pill">{changed} rewritten or removed</span>
  </div>
  <div class="card-grid">
    <a class="card-link" href="#principles"><span class="si-tag" style="color:var(--accent)">Principles</span><span class="si-title">5 rules, each sourced</span><span class="si-desc">Rule, example, counter-example, and the research line it follows from →</span></a>
    <a class="card-link" href="#dictionary"><span class="si-tag" style="color:var(--patterns)">Dictionary</span><span class="si-title">One concept, one word</span><span class="si-desc">Every flagged naming split resolved →</span></a>
    <a class="card-link" href="#forbidden"><span class="si-tag" style="color:var(--unconfirmed)">Forbidden</span><span class="si-title">What we never write</span><span class="si-desc">With a before and after for each →</span></a>
    <a class="card-link" href="#microcopy-table"><span class="si-tag" style="color:var(--job-loc)">All lines</span><span class="si-title">{len(rows)} lines, searchable</span><span class="si-desc">By screen: before, after, and why →</span></a>
  </div>
</header>
<main>
'''
def section(id_,tag,tagcls,title,body,lede=''):
    return f'<section class="block" id="{id_}"><span class="section-tag {tagcls}">{tag}</span><h2>{esc(title)}</h2>{lede}<div class="prose">{body}</div></section>\n'
# intro (context) as first block
PAGE+=section('context','Context','tag-p','What the rules are for', md(intro_body.strip()))
# principles: wrap each ### in a card
pb=md(secs['Principles'])
pb=re.sub(r'(<h3 id="\d[^"]*">)', r'</div><div class="principle">\1', pb, count=0)
pb=pb.replace('</div><div class="principle">','<div class="principle">',1)+'</div>'
PAGE+=section('principles','Principles','tag-p','Principles',pb)
PAGE+=section('not-adopted','Principles','tag-p','Considered and not adopted',md(secs['Considered and not adopted']))
PAGE+=section('dictionary','Dictionary','tag-d','Dictionary',md(secs['Dictionary']))
PAGE+=section('forbidden','Forbidden','tag-f','Forbidden',md(secs['Forbidden']))
PAGE+=section('microcopy-rules','Microcopy','tag-m','Microcopy rules by element type',md(secs['Microcopy']))
PAGE+=section('conflicts','Microcopy','tag-m','Where the copy conflicted (at the time of the principles)',md(secs['Where current copy already conflicts']))
# microcopy table
mc_intro=md(msecs.get('Text the user writes (don\'t rewrite)',''))
mc_flags=md(msecs.get('Flags',''))
PAGE+=f'''<section class="block" id="microcopy-table"><span class="section-tag tag-t">microcopy.md</span><h2>Every interface line</h2>
<p class="lede" style="color:var(--text-dim);max-width:780px">All {len(rows)} lines on the {len(screens)} wireframe screens, grouped by screen. <strong style="color:var(--text)">Before</strong> is the line as first transcribed. <strong style="color:var(--text)">After</strong> is what the page says now, following <code>voice.md</code>. Lines marked <span class="src theirs">not ours</span> are catalog data, reference data, the user's own text, or wireframe scaffolding, and are never rewritten.</p>
<div class="mc-controls">
  <input type="search" id="mc-q" placeholder="Search lines, zones, reasons…" aria-label="Search the microcopy table">
  <select id="mc-screen" aria-label="Screen"><option value="">All screens</option>{''.join(f'<option>{esc(s)}</option>' for s in screens)}</select>
  <select id="mc-src" aria-label="Source"><option value="ours">Our copy</option><option value="">All sources</option><option value="theirs">Not ours</option></select>
  <label><input type="checkbox" id="mc-changed"> Changed only</label>
  <button type="button" class="mc-btn" id="mc-expand">Expand all</button>
  <span class="mc-count" id="mc-count"></span>
</div>
<div id="mc-list"></div>
<details class="screen" style="margin-top:28px"><summary><span class="s-name">Flags</span><span class="s-meta">the naming and tone splits found in the first transcription, all resolved in the Dictionary</span></summary><div class="prose" style="padding:0 18px 14px">{mc_flags}</div></details>
<details class="screen"><summary><span class="s-name">Text the user writes</span><span class="s-meta">never rewritten</span></summary><div class="prose" style="padding:0 18px 14px">{mc_intro}</div></details>
</section>
</main>
<footer>Generated from <code>voice.md</code> and <code>microcopy.md</code>. If this page and the files ever disagree, the files win.</footer>
<script>
var ROWS = {json.dumps(rows, ensure_ascii=False)};
var SCREENS = {json.dumps(screens, ensure_ascii=False)};
(function () {{
  var q = document.getElementById('mc-q'), sel = document.getElementById('mc-screen'),
      src = document.getElementById('mc-src'), ch = document.getElementById('mc-changed'),
      list = document.getElementById('mc-list'), count = document.getElementById('mc-count'),
      expandBtn = document.getElementById('mc-expand');
  var openState = {{}}; var allOpen = false;
  function ours(r) {{ return r.source.indexOf('UI copy') === 0; }}
  function isChanged(r) {{ return r.after && r.after !== 'unchanged'; }}
  function e(t) {{ return String(t).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }}
  function mdi(t) {{ return e(t).replace(/\\*\\*(.+?)\\*\\*/g,'<strong>$1</strong>').replace(/`([^`]+)`/g,'<code>$1</code>').replace(/\\*\\((.+?)\\)\\*/g,'($1)'); }}
  function hl(html, term) {{
    if (!term) return html;
    var re = new RegExp('(' + term.replace(/[.*+?^${{}}()|[\\]\\\\]/g,'\\\\$&') + ')', 'gi');
    return html.split(/(<[^>]+>)/).map(function (part) {{ return part.charAt(0) === '<' ? part : part.replace(re,'<mark>$1</mark>'); }}).join('');
  }}
  function render() {{
    var term = q.value.trim(), t = term.toLowerCase(), s = sel.value, so = src.value, onlyCh = ch.checked, shown = 0;
    var html = '';
    SCREENS.forEach(function (scr) {{
      if (s && s !== scr) return;
      var rs = ROWS.filter(function (r) {{
        if (r.screen !== scr) return false;
        if (so === 'ours' && !ours(r)) return false;
        if (so === 'theirs' && ours(r)) return false;
        if (onlyCh && !isChanged(r)) return false;
        if (t && (r.before + ' ' + r.after + ' ' + r.why + ' ' + r.zone + ' ' + r.type).toLowerCase().indexOf(t) === -1) return false;
        return true;
      }});
      if (!rs.length) return;
      shown += rs.length;
      var total = ROWS.filter(function (r) {{ return r.screen === scr; }});
      var nCh = total.filter(isChanged).length;
      var open = (t || s || allOpen || openState[scr]) ? ' open' : '';
      html += '<details class="screen" data-screen="' + e(scr) + '"' + open + '><summary><span class="s-name">' + e(scr) + '</span><span class="s-meta">' + rs.length + ' shown · ' + nCh + ' of ' + total.length + ' lines changed</span></summary>';
      html += '<div class="tbl-wrap"><table><thead><tr><th>Zone</th><th>Before</th><th>After</th><th>Why</th><th>Type</th></tr></thead><tbody>';
      rs.forEach(function (r) {{
        var a = r.after || '', cls = 'same', at;
        if (a.indexOf('*(removed') === 0) {{ cls = 'removed'; at = mdi(a); }}
        else if (isChanged(r)) {{ cls = 'changed'; at = mdi(a); }}
        else {{ at = 'unchanged'; }}
        var srcTag = ours(r) ? '' : '<br><span class="src theirs">' + e(r.source) + '</span>';
        var flags = r.flags ? '<br>' + r.flags.split(/\\s+/).filter(Boolean).map(function (f) {{ return '<span class="flag">' + e(f) + '</span>'; }}).join('') : '';
        html += '<tr><td class="c-zone">' + hl(e(r.zone), term) + '</td><td>' + hl(mdi(r.before), term) + srcTag + flags + '</td><td class="c-after ' + cls + '">' + hl(at, term) + '</td><td class="c-why">' + hl(mdi(r.why), term) + '</td><td class="c-type">' + e(r.type) + '<br>' + e(r.states) + '</td></tr>';
      }});
      html += '</tbody></table></div></details>';
    }});
    list.innerHTML = html || '<p class="empty-note">No lines match. Try a shorter search or another screen.</p>';
    count.textContent = shown + ' of ' + ROWS.length + ' lines';
    list.querySelectorAll('details.screen').forEach(function (d) {{
      d.addEventListener('toggle', function () {{ openState[d.getAttribute('data-screen')] = d.open; }});
    }});
  }}
  [q, sel, src, ch].forEach(function (el) {{ el.addEventListener(el === q ? 'input' : 'change', render); }});
  expandBtn.addEventListener('click', function () {{
    allOpen = !allOpen; expandBtn.textContent = allOpen ? 'Collapse all' : 'Expand all';
    if (!allOpen) openState = {{}};
    render();
  }});
  render();
}})();
</script>
</body>
</html>
'''
open(ROOT+'/voice.html','w').write(PAGE)
open(ROOT+'/public/voice.html','w').write(PAGE)
print('rows',len(rows),'screens',len(screens),'changed',changed,'bytes',len(PAGE))
