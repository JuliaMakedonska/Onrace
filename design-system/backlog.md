# Backlog

What is known to be open in the design system, by the lesson that takes it. Each item names where it was found and how to see it. When an item is done, it leaves this file and its decision goes into `concept/concept.md`, dated.

## Lesson 10 (responsive)

Found on 2026-11-08 (`concept/concept.md` → Large text and keyboard focus). The build checks 320 at the default text size and 390 at 200% text (`scripts/check_overflow.mjs`, `scripts/check_focus.mjs`); 320 with 200% text isn't a build target yet, so these are recorded, not checked.

- **Results list cards reach the screen's right edge** at 320 with 200% text: the cards lose their side gutter.
- **New password's rows clip their labels** at 320 with 200% text: "New password" reads "ew password".
- **Top-bar titles overlap their buttons:** the New password and Results list top-bar titles run under their buttons at 320 with 200% text. On Results list the small title that replaces the large one on scroll ("Results") also runs under "Log result" at 390 with 200% text.
- **Map pin labels run past the map's frame** at 200% text, at 390 and at 320: Berlin, Chamonix and Dallas. The label is cut by the frame, and its focus halo with it. Fixing it means moving where the labels sit. `scripts/check_focus.mjs` reports these pins apart and doesn't fail on them; a pin whose label fits is checked like everything else.

## Examples: Saved races (found 2026-11-10)

What the system lacked when Saved races (`design-system/examples/`) was built only from it, for `research/jtbd.md` → Related job 2 (choose races by where they are; the Multi-Region Season Planner). Nothing here was drawn on the screen: each is left out, and the screen says nothing it can't show.

- **A save control (component, states, words).** For: putting a race on the list. Needed on Race detail (and maybe the race card). Nothing in the system saves anything, so the screen has no way in except its own address, and the empty state's line "Races you save show up here" names an action the product doesn't offer yet. It needs a control with saved / not saved, its accessible name, and a word for it.
- **A way to remove a saved race (component or variant).** For: taking a race off the list. Needed on each card. A race card is one link and can't hold another (as the result row found, `DESIGN.md` → Result row), and the system has no swipe action or row action. Left out: the list can't be edited.
- **A heading over a group of cards (component).** For: grouping the list by region or country, the axis this job weighs by. Needed above each run of race cards. The only group heading is the grouped settings rows' (`.group-heading`), made for rows on Profile. Left out: the list is in date order, and each card's place line carries where.
- **The static map at a fixed height inside a scrolling screen (variant).** For: seeing the saved races by place at a glance, the job itself. The map only exists as Race browse's Map view, a panel that fills the screen (`.view-area`, `flex: 1`) behind the List / Map switch, whose behaviour is Race browse's script. Left out.
- **An empty-state icon for "nothing saved yet" (token: an icon mask).** For: the empty state. The state message has two icons: the search glass (nothing matches a search or filter) and the archive (Results list). The empty state shows the default, the search glass, which says "nothing matched" rather than "nothing saved yet". Not drawn by hand; the icon is a known mismatch.
- **"Saved" means two things (word).** `voice.md` → Dictionary is one concept, one word: "Saved: <race name>" already says a result was logged (Results list `?saved=`). A saved race is a second meaning. Needs a decision in `voice.md` before the screen is real ("Saved races", "Shortlist", "Watching"…).
- **Where the screen lives (structure).** For: getting there. It isn't a tab and isn't in `sitemap.md` or `flows.md`; the example's back link goes to Discover only because the pushed screen pattern needs a parent. Placing it (a Profile row, a Discover entry, a fourth tab) is an IA decision.
- **Data (not the system's, recorded so it isn't lost).** No `saved_races` table in the data model (`CLAUDE.md` → Data model); the three races are Race browse's sample data. Distance or travel from the athlete's home (the job's "worth traveling for") has no data and no component.
- **The results row in a pushed screen's loading state.** Used as Race browse's: a skeleton bar for the count, the Sort button left out (the example's order is an order label, as Results list's, which has no loading form of its own). Works; noted because the order label has no loading variant.
