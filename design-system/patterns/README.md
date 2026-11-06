# Patterns

Lesson 9 step 4 (2026-11-06). A pattern is a composition of existing components that already stands on three or more screens. Each is one page here, composed only of the components: it links `../index.css` and nothing else, and has no style block, no inline style and no class `components/index.css` doesn't define. Its words are product words, each in `microcopy.md`. `scripts/check_kit.py` stops the build on any of these.

| File | Pattern | Stands on | Composed of |
|---|---|---|---|
| `tab-screen.html` | Tab screen | Race browse, Results list, Profile | Large title header, Tab bar, the screen's content (drawn as Results list) |
| `empty-or-error-state.html` | Empty or error state | Race browse, Results list, Race picker, Race detail, Result detail, Profile | State message, Primary button (drawn as Results list, empty) |
| `grouped-form.html` | Grouped form | Log result, Sign in / Sign up, New password, Profile | Text field, Field hint, Field error; Grouped settings rows on Profile, Gate layout on the sign-in screens (drawn as New password, the passwords not matching) |
| `pushed-screen.html` | Pushed screen | Race detail, Result detail, Race picker, Reset password, New password | Top bar, the screen's content (drawn as Race picker) |

**Not patterns:** the detail screen with a bottom action bar (Race detail and Result detail: two screens, so it stays the Top bar and the Sticky action bar); the top bar over a page of grouped rows (three screens, but already one component, Gate layout).

**The evidence is checked, not claimed.** `ui/inventory.md` → Patterns map gives each pattern the classes a screen's page must carry (and must not, with `!`). `scripts/build_kit_showcase.py` finds the screens in `wireframes/` that carry them and stops the build unless they are exactly the screens listed, at least three for a pattern. It then writes `docs/patterns.html` and the Patterns section of `docs/specimens.html`, each pattern live from its file in a frame, and `scripts/check_docs_stages.mjs` checks that the two compute alike, dark and light, at 1280 and 390. `scripts/check_overflow.mjs` measures each file at 390, 320 and 200% text.

**Adding one:** draw it from a real screen with existing classes, add its row to the Patterns map with its classes, screens and components, and its words to `DESIGN.md` → Patterns. A composition on fewer than three screens isn't a pattern yet: list it under Not patterns with why.
