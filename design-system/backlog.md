# Backlog

What is known to be open in the design system, by the lesson that takes it. Each item names where it was found and how to see it. When an item is done, it leaves this file and its decision goes into `concept/concept.md`, dated.

## Lesson 10 (responsive)

Found on 2026-11-08 (`concept/concept.md` → Large text and keyboard focus). The build checks 320 at the default text size and 390 at 200% text (`scripts/check_overflow.mjs`, `scripts/check_focus.mjs`); 320 with 200% text isn't a build target yet, so these are recorded, not checked.

- **Results list cards reach the screen's right edge** at 320 with 200% text: the cards lose their side gutter.
- **New password's rows clip their labels** at 320 with 200% text: "New password" reads "ew password".
- **Top-bar titles overlap their buttons:** the New password and Results list top-bar titles run under their buttons at 320 with 200% text. On Results list the small title that replaces the large one on scroll ("Results") also runs under "Log result" at 390 with 200% text.
- **Map pin labels run past the map's frame** at 200% text, at 390 and at 320: Berlin, Chamonix and Dallas. The label is cut by the frame, and its focus halo with it. Fixing it means moving where the labels sit. `scripts/check_focus.mjs` reports these pins apart and doesn't fail on them; a pin whose label fits is checked like everything else.
