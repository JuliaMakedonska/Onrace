"""Bundle design-system/components/*.css into design-system/components/index.css, write design-system/index.css (tokens + components) and check the component rules (Lesson 8, step 3, 2026-10-27).

Run from anywhere:  python3 scripts/build_components.py      (build_stand.py runs it first; exit code 1 on a failure)

1. The bundle. Each component file holds its rules in blocks, and each block starts with a line `/* order NNNN */`.
   The number is the block's place in the cascade: the order ui/kit.css had before the split. One component's rules
   were spread over several places in that file, so a component can have several blocks. The bundle sorts every
   block of every file by its number and writes them into design-system/components/index.css, one file, so a page makes one request
   instead of an @import chain. index.css is generated: edit the component files, then run this.
2. The check. It fails when a component file:
   - reads a color primitive (--graphite-*, --amber-*, --coral-*, --black, --alpha-*; anything design-system/tokens/tokens.css defines
     as a raw color or an alpha) instead of a semantic role;
   - writes a hex color, a px value or a font name in a declaration (everything goes through var());
   - (step 5) writes a named or functional color (black, white, rgb(), hsl()) or a fixed color-scheme: a value the
     theme can't reach;
   - has text outside an order block (other than its header comment), or two blocks share a number.
(Until step 4 it also derived design-system/map-data.css from ui/map.css. Since step 4, design-system/map-data.css is the map's own file,
written by scripts/concept/build_map.py, and ui/map.css is gone.)
"""
import os, re, sys, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DS = os.path.join(ROOT, 'design-system')
C = os.path.join(DS, 'components')
TOK = open(os.path.join(DS, 'tokens/tokens.css')).read()
fails = []

# ---------------------------------------------------------------- the color primitives (read from tokens.css)
prims = re.split(r'^\s+2\. SEMANTIC: color roles\n\s+=+', TOK, maxsplit=1, flags=re.M)[0]   # the PRIMITIVES level, up to the SEMANTIC banner
COLOR_PRIM = {n for n, v in re.findall(r'^\s*--([a-z0-9-]+):\s*([^;]+);', prims, flags=re.M)
              if re.match(r'#[0-9A-Fa-f]{3,8}$', v.strip()) or n.startswith('alpha-')}
FONT_NAMES = set(re.findall(r'"([^"]+)"', ' '.join(v for n, v in re.findall(r'^\s*--(font-[a-z-]+):\s*([^;]+);', TOK, flags=re.M))))
assert COLOR_PRIM and FONT_NAMES, 'design-system/tokens/tokens.css: no color primitives or font names found'

# ---------------------------------------------------------------- read every component file into blocks
MARK = re.compile(r'^/\* order (\d{4}) \*/$', flags=re.M)
blocks = []
files = sorted(f for f in glob.glob(os.path.join(C, '*.css')) if os.path.basename(f) != 'index.css')
for f in files:
    name = os.path.basename(f)
    src = open(f).read()
    parts = MARK.split(src)
    if re.sub(r'/\*.*?\*/', '', parts[0], flags=re.S).strip():
        fails.append(f'{name}: text before its first order block')
    for key, text in zip(parts[1::2], parts[2::2]):
        blocks.append((int(key), name, text.strip('\n')))
    # the check, on declarations only (comments out; selectors such as #map-view are ids, not colors)
    code = re.sub(r'/\*.*?\*/', '', src, flags=re.S)
    for n in sorted(set(re.findall(r'var\(--([a-z0-9-]+)', code)) & COLOR_PRIM):
        fails.append(f'{name}: reads the color primitive --{n} (use a semantic role from design-system/tokens/tokens.css)')
    for decl in re.findall(r'[{;]\s*([a-z-]+\s*:[^;{}]+)', code):
        prop, val = decl.split(':', 1)
        if re.search(r'#[0-9A-Fa-f]{3,8}\b', val): fails.append(f'{name}: a hex color in "{decl.strip()[:80]}"')
        if re.search(r'(?<![\w-])-?\d*\.?\d+px\b', val): fails.append(f'{name}: a px value in "{decl.strip()[:80]}"')
        if any(fn in val for fn in FONT_NAMES) or (prop.strip() == 'font-family' and not re.fullmatch(r'\s*(var\(--[a-z0-9-]+\)|inherit)\s*', val)):
            fails.append(f'{name}: a font name in "{decl.strip()[:80]}"')
        # step 5: a component never fixes the appearance; color-scheme comes from :root (dark, or light under [data-theme])
        if prop.strip() == 'color-scheme' and val.strip() != 'inherit': fails.append(f'{name}: a fixed color-scheme in "{decl.strip()[:80]}" (inherit it)')
        if re.search(r'(?<![\w-])(black|white|rgba?\(|hsla?\()', val) and prop.strip() not in ('mask', '-webkit-mask'): fails.append(f'{name}: a named or functional color in "{decl.strip()[:80]}" (use a role)')
# ---------------------------------------------------------------- the state roles (Lesson 9 step 3, 2026-11-05)
# Every state role (the "states" part of the SEMANTIC level) has a value in the dark :root and in the light block: a state
# with a value in one theme only is a defect. Then the dark roles' copy for [data-theme-scope="dark"], so one part of a
# page can show dark inside a light page (the docs' States grids show both themes side by side), is written into
# tokens.css between its markers: generated from the dark :root, so it can't drift.
MAIN = re.search(r'^:root \{(.*?)\n\}', TOK, flags=re.S | re.M).group(1)
SEM = MAIN.split('     2. SEMANTIC: color roles\n')[1]
code_of = lambda t: re.sub(r'/\*.*?\*/', '', t, flags=re.S)
DARK_ROLES = re.findall(r'^\s*(--[a-z0-9-]+):\s*([^;]+);', code_of(SEM), flags=re.M)
STATES = [n for n, _ in re.findall(r'^\s*(--[a-z0-9-]+):\s*([^;]+);', code_of(SEM.split('---------- states')[1]), flags=re.M)] if '---------- states' in SEM else []
LIGHT_BLOCK = re.search(r':root\[data-theme="light"\][^{]*\{(.*?)\n\}', TOK, flags=re.S).group(1)
LIGHT_NAMES = set(re.findall(r'^\s*(--[a-z0-9-]+):', code_of(LIGHT_BLOCK), flags=re.M))
assert STATES, 'design-system/tokens/tokens.css: no "---------- states" part in the SEMANTIC level'
for n in STATES:
    if n not in LIGHT_NAMES: fails.append(f'tokens.css: the state role {n} has a dark value and no light one (a state in one theme only)')
for n in LIGHT_NAMES:
    if n not in dict(DARK_ROLES): fails.append(f'tokens.css: the light block sets {n}, which has no dark value')
RT = re.search(r'@media \(prefers-reduced-transparency: reduce\) \{\n  :root \{(.*?)\n  \}', TOK, flags=re.S).group(1)
RT_ROLES = [l.strip() for l in code_of(RT).split('\n') if l.strip().startswith('--glass-') and 'blur' not in l]
SCOPE = ('/* dark-scope:start (generated by scripts/build_components.py from the dark roles above; do not edit by hand) */\n'
         '[data-theme-scope="dark"] {\n  color-scheme: dark;\n' + ''.join(f'  {n}: {v.strip()};\n' for n, v in DARK_ROLES) + '}\n'
         '@media (prefers-reduced-transparency: reduce) {\n  [data-theme-scope="dark"] {\n' + ''.join(f'    {l}\n' for l in RT_ROLES) + '  }\n}\n'
         '/* dark-scope:end */')
NEW_TOK = re.sub(r'/\* dark-scope:start.*?dark-scope:end \*/', lambda m: SCOPE, TOK, flags=re.S)
if '/* dark-scope:start' not in TOK: fails.append('tokens.css: no dark-scope markers')
elif NEW_TOK != TOK:
    open(os.path.join(DS, 'tokens/tokens.css'), 'w').write(NEW_TOK); TOK = NEW_TOK

keys = [k for k, _, _ in blocks]
for k in sorted({k for k in keys if keys.count(k) > 1}):
    fails.append(f'order {k:04d} is used by more than one block: ' + ', '.join(n for kk, n, _ in blocks if kk == k))

if fails:
    print(f'build_components: FAIL ({len(fails)})\n  ' + '\n  '.join(fails))
    sys.exit(1)

# ---------------------------------------------------------------- the bundle
blocks.sort()
out = ['/* design-system/components/index.css: GENERATED by scripts/build_components.py from design-system/components/*.css. Do not edit.',
       '   Every block of every component file, in its "order" number: the cascade of ui/kit.css before the split (Lesson 8).',
       '   Pages don\'t link it: it is the components half of design-system/index.css (design-system/README.md). */']
for k, name, text in blocks:
    out.append(f'\n/* ---- design-system/components/{name} · order {k:04d} ---- */\n{text}')
COMP = '\n'.join(out) + '\n'
open(os.path.join(C, 'index.css'), 'w').write(COMP)

# ---------------------------------------------------------------- the entry point (Lesson 9, step 1)
# design-system/index.css, the one file the product links: design-system/tokens/tokens.css, then the components bundle, in that order,
# as the two files were linked until step 1. One bundle, so a page makes one request, not an @import chain.
open(os.path.join(DS, 'index.css'), 'w').write(
    '/* design-system/index.css: GENERATED by scripts/build_components.py. Do not edit. The one file the product links:\n'
    '   design-system/tokens/tokens.css, then design-system/components/index.css, in that order (design-system/README.md). */\n\n'
    + TOK.rstrip('\n') + '\n\n' + COMP)

print(f'build_components: {len(STATES)} state roles, each in both themes; the dark scope written ({len(DARK_ROLES)} roles)')
print(f'build_components: pass · {len(files)} component files, {len(blocks)} blocks bundled into design-system/components/index.css in order, design-system/index.css written; '
      f'no color primitive ({len(COLOR_PRIM)} checked), hex, px or font name in design-system/components/')
