# Backlog

What is known to be open in the design system, by the lesson that takes it. Each item names where it was found and how to see it. When an item is done, it leaves this file and its decision goes into `concept/concept.md`, dated.

## Lesson 10 (responsive)

Nothing open. The five items found on 2026-11-08 and 2026-11-15 (Results list cards at the edge, New password's clipped labels, top-bar titles over their buttons, the selected state for the race card and the result row, map pin labels past the frame) were fixed in Lesson 10 step 4 (2026-11-17, `concept/concept.md` → Step 4: adaptive components), and 320 with 200% text is now a pass of `scripts/check_overflow.mjs` and `scripts/check_focus.mjs`, so they stay fixed.

## Lesson 10 step 5: the Split view (found 2026-11-17)

Nothing open. The three items found with it (the search glass on "No race selected" and "No result selected", "Add official result link" leaving the pane, two `h1`s on a split screen) were closed on 2026-11-18 (`concept/concept.md` → Step 5 follow-ups): the placeholder is the quiet line alone, the add sheet opens over the split view as a form sheet, and the detail's title comes into its pane as an `h2`.

## Lesson 10 step 6: the rollout (found 2026-11-18)

Found by the group agents while rolling out; not fixed in step 6. The critique's findings are separate (`concept/concept.md` → Step 6).

- **Race browse's card photos load a larger file than they show.** `sizes` says `calc(100vw - 32px)`; at 820 a card's photo is 342px wide and loads the 1026 file. A pane-width `sizes` would fix it (Race detail's photos were fixed in step 6). The pane's Race detail photo carries the detail screen's `sizes`, too large there, never blurry.
- **Focus after the Filters sheet closes** returns to whatever had focus when it opened; after a click that didn't focus Filters (Safari), that is the page, so focus is lost. Fall back to the Filters button.
- **The discard action sheet on a tablet** sits at the bottom of Log result's form sheet; HIG draws an iPad action sheet as a popover from its button (Cancel). A popover is a new presentation: the designer's call.
- **Race picker's ground differs from Log result's** inside the same form sheet: Log result is the sheet glass, Race picker its page's ground (`body.form-sheet` keeps the page's own ground). Already so on a phone, more visible in a fixed sheet.
- **The confirm alert doesn't widen at 200% text:** "Sign out" wraps to two lines in its button (on a phone too); iOS widens alerts at the accessibility sizes.
- **Cancel on the sign-in gate goes to Race browse** even when it was opened from Results; over a split view on iPad, returning to the screen under the sheet may read better (flows.md DeadEnd2/4 as drawn).
- **The selected Spartan row's "Add official result link" strip** keeps its own darker band inside the Selected edge on Results list at 820 and 1440.

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
