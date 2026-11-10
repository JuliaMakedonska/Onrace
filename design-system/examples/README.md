# Examples

Screens the product doesn't have, built only from `design-system/` to test it (Lesson 9 step 6, 2026-11-10). Each is a demonstration, not a product feature: not in the tab bar, the viewer's product screens, `sitemap.md` or `flows.md`. Linked from the docs' Overview.

- **Saved races** (`saved-races.html`, `-empty`, `-loading`, `-error`): for `research/jtbd.md` → Related job 2, the Multi-Region Season Planner choosing races by where they are. The Pushed screen pattern, the results row with its order label, race cards; the Empty or error state pattern; the skeletons.

The rules are a pattern's: each page links `../index.css` only, has no style block, no inline style and no class the components don't define, and every word is in `microcopy.md` (`scripts/check_kit.py`); each state is measured by the overflow and focus checks like a screen (`scripts/screen_states.mjs`). What the system lacked is left out, not drawn, and listed in `../backlog.md` → Examples.
