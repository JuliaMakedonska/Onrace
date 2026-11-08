"""Course-process text out of the design-system docs (2026-11-05).

The docs say what a component is and how to use it, not how the course got there: no steps, lessons, rounds, markup
passes, gap codes (G23) or finding numbers (#9). Those facts live in concept/concept.md. The sources the docs quote
(DESIGN.md, concept/concept.md, concept/references.md, the specimen sheet's labels and notes) keep them; clean() takes
them out of what a docs page shows:
- in a parenthetical, the parts (split at ";") that name a process step go; if nothing is left, the parenthetical goes;
- a leading process label ("Markup pass (2026-10-23):", "**Round 2 (2026-10-23):**") goes;
- a phrase like "since step 7" or "(step 6, #9)" goes; a "Gaps: G22 K, G23 K." sentence goes.
PROCESS is what scripts/check_kit.py looks for in the visible text of every docs page: a hit stops the build.
"""
import re

PROCESS = re.compile(r"\b(?:steps?|lessons?|rounds?)[\s-]+\d+\w*|\bmarkup pass(?:es)?\b|\bG\d{1,2}\b|(?<![\w&~])#\d{1,2}\b|\bkit fix\b|\boverflow fix\b"
                     r"|\bgap triage\b|\bdeferred to lesson\b", re.I)

# a part that only says who decided and when, "designer, 2026-10-18" or "2026-11-08" (2026-11-08: the dates go as the steps do)
DATED = re.compile(r'^(?:(?:designer|decided|updated|added|found|since|until|from)\b[\s,]*)*\d{4}-\d{2}-\d{2}(?:[\s,]*(?:designer|decided))*$', re.I)

def _paren(m):   # m: the space before it, then its text; a kept one keeps its own spacing
    keep = [seg for seg in re.split(r';\s*', m.group(2)) if not PROCESS.search(seg) and not DATED.match(seg.strip())]
    keep = [k for k in (x.strip() for x in keep) if k]
    return f'{m.group(1)}\u27e8{"; ".join(keep)}\u27e9' if keep else ''   # parked, so the parenthesis round it is judged next

def _sentences(line):   # the last pass: a sentence that still names the process goes; a line left empty goes too
    m = re.match(r'^(\s*(?:[-*] |\d+\. |#{1,4} |> )?)(.*)$', line)
    lead, body = m.group(1), m.group(2)
    if not PROCESS.search(body): return line
    kept = [x for x in re.split(r'(?<=[.!?])\s+(?=[A-Z*`"(])', body) if not PROCESS.search(x)]
    return lead + ' '.join(kept) if kept else None

def clean(t):
    for _ in range(4):   # inner parentheses first, then the ones round them
        t = re.sub(r'(\s*)(?<!\])\(([^()]*)\)', _paren, t)   # not a link's target: [text](url)
    t = t.replace('\u27e8', '(').replace('\u27e9', ')')
    # a leading process label: "Markup pass (2026-10-23):", "**Round 2 (2026-10-23):**", "Kit fix 2026-10-22 (designer):"
    t = re.sub(r'(?:\*\*)?\b(?:Markup pass|Round \d+|Kit fix|Overflow fix|Step \d+\w*|Lesson \d+)\b[^:.\n]{0,60}:(?:\*\*)?\s*', '', t)
    t = re.sub(r'\bG\d{1,2} done:\s*', '', t)
    t = re.sub(r'\bGaps?:[^.]*\.\s*', '', t)
    # a phrase: "since step 7", "until Lesson 8 step 4", "in step 5", with a finding number after it
    t = re.sub(r',?\s*\b(?:since|until|in|from|after|before|for|as of|by)\s+(?:the\s+)?(?:step|lesson|round|markup pass)\b[^,;.)]*', '', t, flags=re.I)
    t = '\n'.join(l for l in (_sentences(l) for l in t.split('\n')) if l is not None and l.strip() not in ('-', '*', '#', '##', '###', '####', '>'))
    t = re.sub(r'[ \t]+([,.;:])', r'\1', t)
    t = re.sub(r'([.!?][ \t]+)([a-z])', lambda m: m.group(1) + m.group(2).upper(), t)   # a sentence whose label went starts upper-case
    return re.sub(r'[ \t]{2,}', ' ', t).strip()
