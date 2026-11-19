# Width audit

Lesson 10, step 1 (2026-11-15). Decisions first, no styles: what a wider screen should do on each of the 10 screens, before any breakpoint is set. Nothing in `design-system/`, `wireframes/` or the build changed for this file.

## Decisions (designer, 2026-11-15)

Taken on this audit; they settle its "Open, for the designer" list and override the audit's text below where they differ. Also recorded in `concept/concept.md` → Lesson 10, step 1.

1. **Tablet: two panes.** Race browse shows the list and the map; choosing a race replaces the map with Race detail, with a way back to the map. **Desktop: three panes** (list, detail, map). As recommended.
2. **Results list, tablet and desktop:** the list with a "nothing selected" detail pane by default, "No result selected" (`microcopy.md` row 595). Not the newest result selected.
3. **Desktop gets the three-pane Race browse**, so the second breakpoint is a real behavior change, not a layout one.
4. **Navigation differs by width.** Tablet behaves like iPad: the tab bar at the top, icons beside labels (HIG Tab bars, iPadOS: "The system displays a tab bar near the top of the screen"; HIG Sidebars: "Consider using a tab bar first", three areas fit). **Desktop behaves like macOS, with a sidebar** (HIG Layout: "Consider taking advantage of larger spaces to switch from a tab bar to a sidebar"; HIG Sidebars: a sidebar "appears on the leading side of a view and lets people navigate between areas of your app"). This replaces the audit's reading of desktop as "an iPad app in a bigger window" (below, and Open question 4): the web on a desktop has no iPad idiom to keep, so HIG Layout's "its idiom … remains the same" is departed from on purpose. The sidebar's width counts in the desktop breakpoint.
5. **No screen gets "wider layout".** Width goes to panes, not to more card columns: a **deliberate deviation from the lesson's card grid**. Reason: HIG Split views, "selecting an item in the view's primary pane displays the item's contents in the secondary pane"; beside a phone-width list the room is worth more as the map or the detail. The grid tokens still exist and count panes: `--col-count-tablet: 2`, `--col-count-desktop: 3`.
6. **A "selected" state for the race card and the result card**, for the panes (HIG Split views: "persistently highlight the current selection"): a new component state, through `design-system/` first, in both themes. Logged in `design-system/backlog.md` → Lesson 10; not built in step 2.

**Step 2 (2026-11-15):** the two points are `--bp-tablet` (48.8125rem, 781px: two `--pane-w` and a divider) and `--bp-desktop` (83.9375rem, 1343px since the revision below; was 88.3125rem, 1413px: a 15rem sidebar [?], three panes, three dividers), in `design-system/tokens/tokens.css`; why: `DESIGN.md` → Width.

**Read for it:** `flows.md` (Flows 1–6), `research/jtbd.md`, every `wireframes/*.html` with its states (`wireframes/_screens.md` for the state list), `design-system/backlog.md` → Lesson 10.

**The question, the way iPad asks it:** Onrace is mobile-first and follows iOS (`DESIGN.md` → Native iOS). The phone layout is the product; a wider screen may only add what iPad would add. Each screen gets one verdict:

- **same:** a wider screen adds nothing but air. The phone layout, centred or in a sheet at a readable width.
- **wider layout:** the same content in more columns.
- **new behavior:** width opens something the phone doesn't have, named concretely.

"Tablet" below means an iPad full-screen window, portrait or landscape (HIG's regular width). "Desktop" means a browser window wider than an iPad in landscape. Since the product follows iOS, desktop is read as an iPad app in a bigger window, not as a Mac app (see HIG → Layout, "its idiom … remains the same" below).

---

## What HIG says (each link checked: HTTP 200 on 2026-11-15)

| Page | Status | What it says that decides something here |
|---|---|---|
| [Layout](https://developer.apple.com/design/human-interface-guidelines/layout) | 200 | "Determine layout based on size classes, not device type or orientation." · "Keep functionality the same as size classes change … Don't change your app's functionality based on the space it occupies. However, you can change the amount of functionality that's visible onscreen as the amount of space changes. Consider taking advantage of larger spaces to switch from a tab bar to a sidebar or expose functionality that might otherwise be grouped into an overflow menu." · "while an app's size classes might change when someone resizes it, its idiom — the device type it's made for — remains the same: keep the layout recognizable and familiar to the platform even when resizing." · On Dynamic Type: "horizontally adjacent views may need to stack vertically to provide more space for text." |
| [Split views](https://developer.apple.com/design/human-interface-guidelines/split-views) | 200 | "Typically, you use a split view to show multiple levels of your app's hierarchy at once … selecting an item in the view's primary pane displays the item's contents in the secondary pane." · "persistently highlight the current selection in each pane that leads to the detail view." · iOS: "Prefer using a split view in a regular — not a compact — environment." · iPadOS: "a split view can include either two vertical panes, like Mail, or three vertical panes, like Keynote." "Account for narrow, compact, and intermediate window widths … ensure that it's possible to navigate between the various panes in a logical way." · "Consider letting people hide a pane when it makes sense." |
| [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars) | 200 | "A sidebar requires a large amount of vertical and horizontal space. When space is limited or you want to devote more of the screen to other information or functionality, a more compact control such as a tab bar may provide a better navigation experience." · iOS, iPadOS: "Consider using a tab bar first. A tab bar provides more space to feature content … If you need to expose more areas than fit in a tab bar, the tab bar's convertible sidebar-style appearance can provide access to content that people use less frequently." |
| [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) | 200 | iPadOS: "The system displays a tab bar near the top of the screen. You can choose to have the tab bar appear as a fixed element, or with a button that converts it to a sidebar." "Prefer a tab bar for navigation … If your app is more complex, you can provide the option to convert the tab bar to a sidebar." · "Tab bar icons appear above tab labels in compact views, whereas in regular views, the icons and labels appear side by side." · "Make sure the tab bar is visible when people navigate to different sections … The exception is when a modal view covers the tab bar." · "aim for a default list of five or fewer to preserve continuity between compact and regular view sizes." |
| [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets) (added: Log result, the Filters sheet and the Sign in gate are sheets) | 200 | iOS, iPadOS: "Prefer using the page or form sheet presentation styles in an iPadOS app. Each style uses a default size for the sheet, centering its content on top of a dimmed background view." |

---

## One decision for every top-level screen: the tab bar

**Superseded for desktop by Decision 4:** the tab bar at the top stands for tablet; desktop gets a macOS sidebar. The audit's original reasoning, kept:

**Tablet and desktop: the 3-tab bar moves to the top, icons beside labels; no sidebar.** (Discover, Results, Profile: Race browse, Results list, Profile.)

- HIG → Tab bars, iPadOS: the tab bar sits "near the top of the screen", and in regular views "icons and labels appear side by side".
- No sidebar, and no convertible one: Onrace has three destinations and no hierarchy under them. HIG → Sidebars: "Consider using a tab bar first"; a sidebar "requires a large amount of vertical and horizontal space", and that space is what Race browse needs for its panes (below). The tab-to-sidebar switch HIG → Layout offers is for apps with more areas than fit in a tab bar; three fit.
- The floating glass capsule at the bottom stays the phone's (compact) form only. That is a change of place, not of function: same three tabs, same order, same gate behind Results and Profile (HIG → Layout: "keep functionality the same").
- `[?]` A top tab bar on a phone-width *pane* inside a wider window: it belongs to the window, not to the leading pane, so it spans the top. To be drawn in step 2.

---

## The table

| Screen | What the user does there (flow, job) | Tablet (iPad) | Desktop | Verdict |
|---|---|---|---|---|
| **Race browse** (Discover tab; base, `-empty`, `-error`, `-loading`, Filters sheet, Map view) | Main Job 1 (Discovery), Related Jobs 1–2. Scans upcoming races, narrows by search, filters and sort, switches List / Map to weigh where races are, taps a card or pin to open Race detail, comes back to compare another (`flows.md` Flow 1: "back / compares another race"). | **List and map side by side; the List / Map switch goes.** The race list keeps its phone width in a leading pane; the map fills the trailing pane. Selecting a card or a pin opens **Race detail in the trailing pane** in place of the map, with the card highlighted in the list; tapping another card swaps the detail (the "compares another race" loop without a Back). Race detail's back control returns the pane to the map. Search, Filters, Sort and the chips stay on the list pane; Filters opens as a form sheet centred over the window. | **Three panes: list, detail, map.** The map no longer gives way: a selected race shows its detail between the list and the map, its pin highlighted. With nothing selected, two panes (list, map), the tablet layout. | **new behavior.** Tablet: list + map in two panes (replaces the switch) and the detail opening in the trailing pane. Desktop: a third pane, so list, detail and map all show while comparing. |
| **Race detail** (base, `-error`, `-loading`) | Main Job 1: reads one race (photo band, date, place, format, about, official site) and decides "Worth entering?"; Register opens `registration_url` in a new tab. | **Becomes Race browse's trailing pane** when reached from the list or a pin: the same content top to bottom, the photo band at the pane's width (3:1), Register in the action bar at the pane's bottom edge. Opened on its own (its own address), it is the phone layout at a readable width. | The middle pane of Race browse (see above). On its own, as tablet. | **same** (content); its new behavior is Race browse's: it is a pane there, not a pushed screen. |
| **Results list** (Results tab; base with the no-link row, `-empty`, `-error`, `-loading`, the Add official result link sheet) | Related Job 4 (retrieve proof, Archivist), entry to Related Job 3 via **Log result**. Finds a result, opens it; adds a missing official result link from its row. | **List and Result detail side by side** (HIG's two-pane split view, like Mail): the result cards in a leading pane at phone width, the selected result's detail in the trailing pane, its card highlighted. Log result stays in the list pane's bar. Add official result link opens as a form sheet over the window. | The same two panes; the detail pane wider. No third pane: the archive has no third level. | **new behavior.** List and detail side by side; opening a proof no longer leaves the list. |
| **Result detail** (base, no-link state, `-error`, `-loading`, the add sheet) | Related Job 4: sees the finish time and the proof line ("Self-reported · via <domain>"), opens the official result, copies the link, or adds a missing one. | **Becomes Results list's trailing pane:** same content, Open official result in the action bar at the pane's bottom edge. On its own, the phone layout at a readable width. | As tablet. | **same** (content); it is a pane in Results list's new behavior. |
| **Log result** (base, `-error` ×3 causes, `-loading`, discard action sheet) | Related Job 3: types or links a race, finish time, optional official result link; Save. A modal sheet over Results (Cancel / Save). | A **form sheet** centred over the dimmed window (HIG → Sheets), at its phone width. Grouped rows, nothing to put side by side. | As tablet. | **same** |
| **Race picker** (base, `-empty`, `-error`, `-loading`) | Related Job 3, shortcut: searches past catalog races, picks one to fill and lock name, date and format. Pushed inside Log result's sheet ("‹ Log result"). | Pushed inside the same form sheet, at its width. | As tablet. | **same** |
| **Sign in / Sign up** (base in both modes, `-error` ×3, `-loading`, `-check-inbox`) | `[INFRASTRUCTURE]`, Flow 4 and the gate of Flows 2, 3, 5: email and password, Sign in or Create account, Forgot password?. A full-screen modal on the phone. | A **form sheet** over the window (HIG → Sheets). Two fields. | As tablet. | **same** |
| **Reset password** (base, `-error` ×2, `-loading`, `-check-inbox`) | `[INFRASTRUCTURE]`, Flow 6: one email field, Send. Pushed inside the gate. | Pushed inside the gate's form sheet. | As tablet. | **same** |
| **New password** (base, `-error` ×5 causes, `-loading`) | `[INFRASTRUCTURE]`, Flow 6: two password fields, Save; opened from the emailed link. | Inside the gate's form sheet (it opens from a link, so the sheet opens over Race browse, as on the phone the gate does). | As tablet. | **same** |
| **Profile** (Profile tab; base, `-error` ×2, `-loading`, sign-out alert) | `[INFRASTRUCTURE]`, Flow 5: sees whose account it is, edits name, country, language, signs out. | One grouped list at a readable width, centred. Not a split view: iPad Settings splits because it has sections to pick from; Profile has one group and Sign out, no level below. The sign-out alert is an alert at any width. | As tablet. | **same** |

### What the verdicts add up to

- **New behavior on two screens, both list-to-detail:** Race browse (list + map, then list + detail + map) and Results list (list + detail). They take Race detail and Result detail with them as panes.
- **Wider layout on none.** The candidate was the race list in two or three columns of cards. It loses to the panes: at tablet width the room beside a phone-width list is better spent on the map or the detail than on more cards, which is what HIG's split view is for ("show multiple levels of your app's hierarchy at once"). A multi-column card grid would come back only if the panes were refused.
- **Same on six:** the three gate screens, Log result, Race picker, Profile. Each is one short task in a sheet or one group of rows; width adds air.
- **The tab bar** changes place on every top-level screen (top, icons beside labels), the same three tabs.

### What changes in the flows (none of it new functionality)

HIG → Layout: "Don't change your app's functionality based on the space it occupies … you can change the amount of functionality that's visible." Every change below is that: more of what's already there, visible at once.

- **Flow 1:** `Detail → "back / compares another race" → Browse` becomes one tap on another card; the list keeps its scroll, search and filters. Tap depth to a race stays 1. `DetailError` and `DetailLoading` live in the detail pane only, so the list stays usable while a race fails to load (on the phone the error screen replaces everything).
- **Flow 3:** `ResultsList → taps a logged entry → ResultDetail` keeps the list on screen; `DetailError2` / `DetailLoading2` stay in the trailing pane.
- **Flows 2, 4, 5, 6:** unchanged; sheets and pushes, only presented as form sheets.

### New states the panes create (to name in step 2, words to `microcopy.md` first)

- **Nothing selected yet.** Race browse at tablet width shows the map, so it has no empty detail pane. Results list does: either the newest result is selected on arrival `[?]`, or the pane says nothing is selected (a new line). Race browse at desktop width, before a selection: two panes, so no empty state.
- **Each pane's own loading and error.** The list's fetch (`Loading2`, `FetchError2`) covers the list pane only; a failed list load means nothing to select, so the detail pane shows nothing. Race browse's list and map share one fetch, so its error and loading cover both panes as one state.
- **Empty with panes:** Race browse `-empty`: the list's message, the map with no pins (as Map view's empty form today). Results list `-empty`: nothing to select, so one pane, the empty state centred, Log your first result as today.
- **The selected card.** HIG → Split views: "persistently highlight the current selection". The race card and the result card have no selected state in the system yet: a new component state, through `design-system/` first (CONTRIBUTING).

---

## The Lesson 10 backlog, by screen

From `design-system/backlog.md` → Lesson 10 (found 2026-11-08). None of these is a tablet item: all are compact width with large text. They are on this list because 320 at 200% text becomes a build target in this lesson.

| Backlog item | Screen(s) and states | Width | Does a wider screen help? |
|---|---|---|---|
| **320 with 200% text isn't a build target** (`check_overflow.mjs`, `check_focus.mjs` run 320 at default text and 390 at 200%) | Every screen, every state (the 236 states of `scripts/screen_states.mjs`) | 320 + 200% | No. It is a compact case, and the panes reintroduce it: the list panes run at phone width beside the map or the detail, so their large-text behaviour has to hold there too. |
| **Results list cards reach the screen's right edge** (lose their gutter) | Results list: base, `-loading` (skeleton cards), and the cards in the list pane on tablet | 320 + 200% | No: the list pane stays phone-width. |
| **New password's rows clip their labels** ("New password" reads "ew password") | New password: base, `-error` (short, mismatch, same, submit; not `expired`, which has no form), `-loading` | 320 + 200% | Inside the gate's form sheet on tablet, the sheet is wider than 320, so it shows less there; the phone case stays. |
| **Top-bar titles overlap their buttons** | New password (‹ Sign in · title · Save) at 320 + 200%. Results list: the small title that replaces the large one on scroll ("Results") runs under **Log result** at 390 + 200%. The same three-part bar is on Reset password (‹ Sign in · Reset password · Send), Sign in / Sign up (Cancel · Account · Sign in), Log result (Cancel · title · Save) and the Add official result link sheet (Cancel · title · Save); Race picker's bar has two parts (‹ Log result · Find a race) but the same centred title. Not reported, worth measuring when 320 + 200% is checked. | 320 + 200%; 390 + 200% for Results list | Results list's collapsed bar sits on the phone-width list pane on tablet too, so it can collide there as on a phone. The sheet bars get the form sheet's width. |
| **Map pin labels run past the map's frame** (Berlin, Chamonix, Dallas; the label and its focus halo are cut) | Race browse: Map view (base map, the filtered map, the map's empty form), and on tablet and desktop the map pane | 390 and 320, at 200% | Not by itself. The map keeps its ratio (`--map-ratio`), so a wider pane scales the map, not the room at its edges; the fix the backlog names (moving where labels sit) has to hold in the pane too. The map pane is also the first place a pin is on screen at the same time as its card, so the selected pin state belongs with that fix. |

---

## Where behavior actually changes (input for step 2's two breakpoints, not set here)

From the table, behavior changes at two widths, and only on two screens plus the tab bar:

1. **Where a second pane fits beside a phone-width list.** This is the change HIG ties to the regular width class (Split views → iOS: "Prefer using a split view in a regular — not a compact — environment"). What changes there, all at once:
   - the tab bar moves to the top, icons beside labels (every top-level screen);
   - Race browse: list + map side by side, the List / Map switch goes, a selected race opens in the trailing pane;
   - Results list: list + Result detail side by side;
   - sheets (Log result and Race picker, Filters, the add sheet, the gate with Reset and New password) present as centred form sheets instead of from the bottom edge.
   The test for this width: a phone-width list (the 390 the screens are drawn at) plus a trailing pane that is no narrower than it, so the map and Race detail are each at least a phone wide.
2. **Where a third pane fits.** Only Race browse changes: list, detail and map side by side, so the map stays on screen while comparing races. The test: a phone-width list, a detail at least a phone wide, and a map wide enough for its pins and labels.

Everything else (six screens) does not change at either width; it only needs a readable maximum width and centring, which is layout, not a breakpoint.

**To weigh in step 2:** the second breakpoint rests on one screen. If the three-pane Race browse is dropped (the detail stays in place of the map, as at tablet width), there is one behavior breakpoint, and the second becomes a layout-only one (where the panes stop growing and the window gains margins). HIG → Split views supports either: "two vertical panes, like Mail, or three vertical panes, like Keynote", and "Consider letting people hide a pane".

---

**Revised 2026-11-18 (designer, the layout pass):** Race browse on a desktop is two panes, the list and a wide map, until a race is chosen; choosing one opens the detail pane between the list and the map (three panes). Until then the detail pane stood between them from the start, empty, "No race selected", which left the widest window's middle column with nothing in it and the map with what was left. Results list keeps its two panes and "No result selected": it has no map to give the room to. A list with nothing to choose (Results list empty or failed) is one centred column. The whole wide layout (margins, dividers, the sidebar on the panes' grid, the one top line, the map's frame) is `DESIGN.md` → Width → The wide layout.

**Revised 2026-11-19 (designer, a new direction; Strava Maps and Komoot as references), Race browse first:** the tablet behaves like the phone, navigation included: the tab bar stays at the bottom, the List / Map switch stays, the list's column stops at `--container-max` and centres, the Map view fills the screen; no split view on a tablet. The tablet breakpoint now only caps the column, a deliberate deviation from Decisions 1, 3 and 4 above (list and map side by side; the iPad tab bar at the top). The desktop is a web app, not macOS, a deliberate break from Decision 4's macOS sidebar: a top horizontal bar (the logo, Discover, Results, Profile, Log result as the one primary action); Race browse's map fills the screen under it, edge to edge, framed to the races; the list floats over it as a card on the left, a chosen race opens a second card beside it (Close, its pin and card Selected), the filters float as chips over the map and open in a card under them (Clear all, Done). The other screens wait: Results list keeps its two panes, under the new navigation. `DESIGN.md` → Width → A new direction.

**Revised 2026-11-20 (designer; Microsoft Copilot, Dribbble and Midday sign-in, Pandora on a tablet):** Sign in / Sign up, Reset password and New password are full pages at every width, not a form sheet over the app (the form sheet of 2026-11-18 is gone from them). Tablet: the phone's page, the form centred at `--form-w`. Desktop: a split page, the form half on the left (every state and step in its place) and a race photo full height on the right with the Onrace wordmark. `DESIGN.md` → Width → The sign-in screens by width.

## Open, for the designer (all four settled by the Decisions above, 2026-11-15)

1. Race browse at tablet width: should a selected race replace the map in the trailing pane (recommended above), or open as a third pane that squeezes both?
2. Results list on arrival at tablet width: select the newest result `[?]`, or a "nothing selected" pane (a new line in `microcopy.md`)?
3. Three panes on desktop for Race browse, or two panes everywhere and one behavior breakpoint?
4. Desktop is read as "an iPad app in a bigger window" (HIG → Layout, idiom stays the same). If it should follow macOS instead (sidebar, no tab bar), most of the table changes; nothing in `DESIGN.md` → Native iOS says so today.
5. Not a product screen, so not in the table: Saved races (`design-system/examples/`) would be a list-and-detail screen too, if it becomes real. Since Lesson 10 step 6 (2026-11-18) the example is one: a split view, list and Race detail, "No race selected" until one is chosen.

**Revised 2026-11-15 (designer), before step 3:** 1413px left many 13–14-inch laptops on the tablet form. The list and the detail stay `--pane-w`; the map is flexible, never narrower than `--map-min` (20rem [?], 320px, the narrowest screen the map is checked at). `--bp-desktop` = `--sidebar-w` (15rem [?]) + 2 × `--pane-w` + `--map-min` + three dividers = **83.9375rem, 1343px**. A 1440 window and a 1366 one reach it; a 1280 one doesn't. An iPad Pro 13-inch in landscape (1376) now does, so it gets the sidebar (`DESIGN.md` → Width).

**Step 4, 2026-11-17:** decision 6 is built: the race card and the result row have a Selected state (`aria-current="page"`, `--selected` with a `--text-secondary` edge), in both themes, with its docs States cell; the panes still to come will set it. The backlog's 320-with-200%-text defects are fixed and that size is now checked. Components adapt to their own width (`--stack-w`), never the window's; every single-column screen centres its column at `--container-max` (`concept/concept.md` → Step 4: adaptive components).

**Step 5, 2026-11-17:** decisions 1, 2 and 3 are built as the Split view pattern (`design-system/patterns/split-view.html`): Race browse list + map on a tablet (a chosen race's detail in the map's place, "‹ Map" back), list + detail + map on a desktop with "No race selected"; Results list list + detail with "No result selected". The choice rides in the URL and its card is Selected (decision 6).

