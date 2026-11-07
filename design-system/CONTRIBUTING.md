# Contributing to the system

**One rule: anything new appears first in `design-system/`, then on a screen. Never the other way round.**

A screen (`wireframes/*.html`) only assembles what the system already has. If a screen needs something the system doesn't have, stop, add it to the system with its docs, then use it on the screen. This file is the checklist. Read it at the start of any change, whoever you are: a developer, a designer, or Claude in a new session. The rules live here and in `DESIGN.md` → Contributing to the system and `CLAUDE.md` → Contributing to the system, not in a chat.

## Before you start

- **Read the sources of truth** (`CLAUDE.md` → Sources of truth): the look is `design-system/`, the words are `microcopy.md`, the structure is `wireframes/`, the decisions are `concept/concept.md`.
- **A decision is recorded before it's built:** a dated entry in `concept/concept.md` with what was decided, by whom and why. If a question is still open there, answer it there first.
- **Words first:** every product line goes into `microcopy.md` first, then `python3 scripts/build_voice_html.py`. No word reaches a screen, a specimen or a pattern without a row there (build checks 11 and 20).

## Which kind of change is it?

### A new value: `tokens/tokens.css`

- [ ] **A raw value** (a color, a size, a duration) is a **primitive**, named by what it is: a color by hue and L* (`--amber-69`), anything else by its scale or part (`--space-4`, `--target`).
- [ ] **What a value is for** is a **semantic role** (`--accent-pressed`, `--surface-hover`): a `var()` of a primitive, with a comment naming where it's used. Components read roles, never color primitives.
- [ ] **A role has a value in both themes:** in the dark `:root` block and, if light needs a different one, in the light block (`:root[data-theme="light"]`). A state role (hover, pressed, focus, disabled) must have both.
- [ ] **A count of a primitive** (three targets) is a named primitive defined as `calc(var(--x) * n)` with its reason on the same line.
- [ ] **Sign it:** every token has a row on the stand (`scripts/concept/build_stand.py`) with its reason.
- Checked by: 4 (contrast, both themes), 5 (signed tokens), 14 (no raw value in a component), 15 (both themes), 16 (counts are named), 19 (state roles in both themes, state ladders).

### A new component, variant or state: `components/` and its docs section

- [ ] **The CSS:** one file per component in `components/`, with an `order` block (`components/README.md`). Values only through tokens: no hex, px, font name or color primitive.
- [ ] **The inventory:** a row in `ui/inventory.md` (its screens, states, HIG link), a Showcase map row (its specimen and states), a Docs map row (what it's for, its parts, when to use it, when not to, with real screens), and its family in Docs families.
- [ ] **The specimen:** every variant on its own stage in `docs/specimens.html`, with the screens' own words. The family page is generated from it. **A variant differs in look or structure** (width, size, an icon, a busy state, a layout); an instance that differs only in its words is not a variant: list it in `ui/inventory.md` → Instances map (Used as), not as a stage.
- [ ] **States, if you act on it:** a States map row in `ui/inventory.md`: At rest, Hover, Pressed, Focus and Disabled (and Invalid if it has one) come from state roles, shown side by side in the docs' theme (Dark or Light, by the switch), each built and checked in both. Hover sits under `@media (hover: hover)`; a state changes only fill, color or border; disabled is `--opacity-disabled`.
- [ ] **Native iOS:** if it has a native counterpart, it follows Apple's HIG for anatomy, metrics and behavior; Podium supplies the look (`DESIGN.md` → Native iOS).
- [ ] **Then** use it on the screens, the same markup everywhere it stands.
- Checked by: 10 (every inventory component has a specimen and every state), 12 (a screen uses no class the components don't define), 17 (a docs section per component, its anatomy found on the stage), 18 (the docs stage computes as the specimen), 21 (every class a component defines is on a specimen or a pattern).

### A new composition: `patterns/`

- [ ] **Only when it already stands on three or more screens**, and you can name them. Two screens is not a pattern: it stays its components.
- [ ] **One page** in `patterns/`, composed only of existing components: it links `../index.css` only, no style block, no inline style, no new class. Draw it from a real screen's content.
- [ ] **Its row** in `ui/inventory.md` → Patterns map: the classes a screen must carry, the screens, the components, when to use the pattern and when the components. Its words in `DESIGN.md` → Patterns.
- Checked by: 20 (the screens carrying its classes are exactly the listed ones, at least three; no style of its own; its words in `microcopy.md`; its stage on `docs/patterns.html` as on `specimens.html`).

### A change to something that exists: the "keep it" rule

- **A value change** goes into the token of the right level in `tokens/tokens.css` (a primitive or a role), never into a component.
- **A component change** goes into its file in `components/` and its docs section (the specimen in `docs/specimens.html`, its rows in `ui/inventory.md`), then to every screen where it stands.
- **A new composition** goes into `patterns/` (above).
- **Sign the reason** in `DESIGN.md` either way, and record the decision in `concept/concept.md`.

### A screen change: `wireframes/`

- [ ] Only components and patterns that exist. No style block, no inline style.
- [ ] Every state the screen has is a page or a URL state (`wireframes/_conventions.md`), listed in `wireframes/_screens.md`, in the viewer's notes (`wireframes/index.html`) and, if it's a new cause, in `scripts/check_overflow.mjs`'s `CAUSES`.
- [ ] Flows in `flows.md`, entities and states in `sitemap.md`.
- Checked by: 6–9 (overflow, one line, fonts, scripts and styles), 12, 13 (links).

## Shipping

- [ ] **Everything ships through `scripts/ship.sh "message"`:** the build (`python3 scripts/concept/build_stand.py`, every check), then commit, push to `main`, and wait for the Pages deploy. Each step runs only if the one before it passed.
- [ ] **A failed build never commits.** The hooks (`scripts/hooks/`) refuse a commit or push whose tree isn't the one the build stamped. No `--no-verify`.
- [ ] **Before/after:** a visual change gets a review page in `ui/` with the changed states before and after, in both themes.

## What the build can't check

- **Order in time:** the build sees the result, not whether the system came first. The checks above make the wrong order fail (a screen can't use an undefined class; a component can't skip its specimen), but the rule is yours to follow.
- **Judgement:** whether a docs section's "when to use" is right, whether a pattern is worth naming, whether a state reads well. Look at it, in both themes, at 390 and at 200% text.
