# UI inventory

Lesson 7, step 2, 2026-10-18. Every component in the product, read from all 35 wireframe pages (`wireframes/*.html`: 10 screens, each with its state pages) and `sitemap.md`. It covers the two Podium screens and the eight that are still grayscale.

**How to read it**
- **Screens:** the screen, then its files. A component counts as repeating when it appears on two or more of the 10 screens; state pages of one screen count once. Single-screen components are under [One-off](#one-off).
- **Groups:** `sitemap.md`'s clusters. **Discovery:** Race browse, Race detail. **Archive:** Results list, Log result, Race picker, Result detail. **Infrastructure:** Sign in / Sign up, Reset password, New password, Profile. **Shared:** components that repeat across two or more groups.
- **States:** what the pages actually show. "Base" is the default page.
- **Photo:** whether the wireframe or the Podium screen puts a photo in it. The Race browse card does, and since step 5 Race detail (the same band, at full content width).
- **Native iOS:** the HIG page from `concept/concept.md` → Native iOS, or "none" when iOS has no counterpart.
- **Gaps:** from `concept/concept.md` → Native iOS → Gap triage. **K** = kit (CSS, steps 3 and 5), **M** = markup pass (between steps 5 and 6), **O** = out of scope. The gaps were measured on the two Podium screens, so a gap is listed for a grayscale screen only where the same markup is there.
- Class names are the wireframes' own, quoted so the kit can find them.
- **Step 3b (2026-10-19)** closed every **K** gap listed here in `ui/kit.css` (`concept/concept.md` → Step 3b). The codes stay for the record; **M** and **O** are unchanged.

File-name shorthand: `race-browse` = `race-browse.html`; `-empty`, `-error`, `-loading`, `-check-inbox` are that screen's state pages.

---

## Shared

| Component | Screens (files) | States | Photo | Native iOS | Gaps |
|---|---|---|---|---|---|
| **Tab bar** (`nav.bottom-nav`: Discover, My Results, Profile) | Race browse (`race-browse`, `-empty`, `-error`, `-loading`); Results list (`results-list`, `-empty`, `-error`, `-loading`); Profile (`profile`, `-error`, `-loading`) | Current tab (`aria-current="page"`); unchanged in every loading and error state (the tabs keep working) | no | [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) | G1 K, G2 K, G3 M |
| **Large title header** (`h1` in the page header) | Race browse (all 4 files); Results list (all 4, with `a.header-action` Log result); Profile (all 3) | Base; the same in empty, error, loading | no | [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars) (large title), [Typography](https://developer.apple.com/design/human-interface-guidelines/typography) | G4 M, G5 M (Results list), G29 K |
| **Top bar** (`.top-bar`) | Race detail (`race-detail`, `-error`, `-loading`): back "‹ Discover"; Log result (`log-result`, `-error`, `-loading`): back "‹ My Results", title, Save; Race picker (all 4): Cancel, title "Find a race"; Result detail (all 3): back "‹ My Results"; Sign in / Sign up (all 4): Cancel, title; Reset password (all 4): back "‹ Sign in", title; New password (all 3): back "‹ Sign in", title | Back only; back + centered title (`.bar-title`); Cancel + title; Save → "Saving…" (`log-result-loading`); title switches Sign in / Create account / Check your inbox | no | [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars) | G6 K (C1 glass applies to every bar); G34 M (Race detail: no inline title on scroll) |
| **Search field** (`input type="search"`, "Race name or city") | Race browse (`.race-search`, all 4 files); Race picker (`form.search`, all 4) | Empty with placeholder; filled (`?q=`); submits on the keyboard's Search key | no | [Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields) | G8 M (Race browse), G9 O, G10 K |
| **Segmented control** (`.view-toggle` / `.view-btn`) | Race browse (all 4): List / Map; Sign in / Sign up (`sign-in-sign-up`, `-error`, `-loading`): Sign in / Create account | Selected (`aria-pressed="true"`); disabled while signing in (`sign-in-sign-up-loading`) | no | [Segmented controls](https://developer.apple.com/design/human-interface-guidelines/segmented-controls) | G11 K |
| **Race card** (`article.race-card`: name, format chip, date, location) | Race browse (`race-browse`); Race picker (`race-picker`) | Base; hover ring (Race browse, Podium); filtered subsets (`?sport=` on Race browse, `?q=` on Race picker) | **yes** on Race browse (B/W, 3:1); no on Race picker | [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables) (photo-led: a collection) | G23 K, G28 K (date tile), G33 M (Race browse `h3`) |
| **Format chip** (`.sport-tag`) | Race browse (`race-browse`); Race picker (`race-picker`); Results list (`results-list`) | One look for every format (uppercase by CSS) | no | none | none |
| **Results row** (`.results-row`: count, then sort or order) | Race browse (all 4): count + Sort; Results list (all 4): count + "Newest first" | Count ("7 upcoming races", "4 races match your filters", "4 results"); empty count on `-empty` and `-error`; a skeleton bar on `-loading`; sort hidden in Map view | no | none (the sort inside it: [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons)) | G21 M (sort), G29 K (meta size) |
| **Primary button** (`.header-action`, `.state-action`, `.submit-btn`, `.register-btn`, `.open-btn`, sheet `button[type=submit]`, `.save-btn`) | Race browse (Apply filters; Change filters on `-empty`; Try again on `-error`); Race detail (Register on \<domain\>; Try again on `-error`); Results list (Log result; Log your first result on `-empty`; Try again on `-error`); Log result (Save, in the top bar); Race picker (Type it in instead on `-empty`; Try again on `-error`); Result detail (Open official result on \<domain\>; Try again on `-error`); Sign in / Sign up (Sign in / Create account; Send a new link on `-error?cause=confirm`); Reset password (Send reset link); New password (Save new password; Reset password again on `-error?cause=expired`); Profile (Try again on `-error`) | Base; hover and 1px press (Podium); busy: "Saving…" (`log-result-loading`, `new-password-loading`), "Signing in…" / "Creating account…" (`sign-in-sign-up-loading`), "Sending…" (`reset-password-loading`); disabled inside a locked form; stepped down to secondary when a state block brings its own primary (Results list `-empty`, `-error`) | no | [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons) | G5 M (Log result), G12 M (Apply filters), G26 K |
| **Secondary button** (`.filters-trigger`, `.state-action.secondary`, `.secondary-btn`, sheet Cancel) | Race browse (Filters; Clear all filters on `-empty`; Cancel in the sheet); Race picker (Type it in instead on `-error`); Sign in / Sign up (Send a new link on `-check-inbox`); Reset password (Send a new link on `-check-inbox`) | Base; hover; Filters open (`aria-expanded="true"`) and "Filters · N"; "Sending…" then "Sent" (`sign-in-sign-up-check-inbox`) | no | [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons) | G12 M (sheet Cancel) |
| **Text link** (`.clear-all`, `.text-link`, `.forgot`, `.alert-link`, row "Try again") | Race browse (Clear all filters, in the chips row); Sign in / Sign up (Forgot password?; Use a different email on `-check-inbox`); Reset password (Use a different email on `-check-inbox`); New password (Reset password again on `-error?cause=submit`); Profile (Try again on a row, `-error?cause=save`) | Base; disabled while signing in (`aria-disabled`, `sign-in-sign-up-loading`) | no | [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons) | G27 K (Clear all filters beside the chips) |
| **Modal sheet** (`.sheet`) | Race browse (the Filters sheet, all 4 files: `.sheet-handle`, `.sheet-backdrop`, `.sheet-actions`); Race picker (the whole screen is a sheet over Log result, all 4 files, with a top bar instead of a handle) | Filters: closed / open, with a scrim; Race picker: list, empty, error, loading | no | [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets) | G12 M, G13 K, G14 M, G15 O, G16 K, G20 M, G32 M |
| **Pop-up select** (`select`) | Race browse (Sort; Region in the Filters sheet); Log result (Sport type); Profile (Country, Language) | Base; selected value; Sort disabled on `race-browse-loading` and hidden in Map view; Log result `-error`: "Choose a sport type." | no | [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons) (a pop-up button) | G17 M (Region), G21 M (Sort) |
| **Date field** (`input type="date"`) | Race browse (Race date from / to, in the sheet); Log result (Race date) | Base; pre-filled range; Log result `-error`: "Add the date you raced." | no | [Pickers](https://developer.apple.com/design/human-interface-guidelines/pickers) | G18 M |
| **Text field** (`.field`: label, input, hint) | Log result (Race name, Finish time, Official result link); Sign in / Sign up (Email, Password); Reset password (Email); New password (New password, Confirm new password) | Empty with placeholder; filled; locked (`fieldset disabled`) on every `-loading`; error text under the field on `-error` | no | [Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields) | G28 K |
| **Field hint** (`.hint`, `.field-hint`) | Log result (finish time, official result link); Sign in / Sign up ("At least 8 characters.", Create account mode); New password ("At least 8 characters.") | Shown; per mode on Sign in | no | none | none |
| **Field error** (`.field-error`; Profile's `.row-note.is-error`) | Log result (`-error?cause=fields`, `?cause=link`); New password (`-error?cause=short`, `same`, `mismatch`); Profile (`-error?cause=save`, on the row, with "Try again") | One per field, shown by cause | no | none | none |
| **Form alert** (`.form-alert`, top of the form) | Log result (`-error?cause=submit`); New password (`-error?cause=submit`, with "Reset password again") | Hidden; shown by cause | no | none | none |
| **Inline error** (`.inline-error`: heading, line, optional actions) | Race detail (`-error?cause=registration`, in the action bar, Dismiss); Result detail (`-error?cause=link`, in the action bar, Try again + Dismiss); Sign in / Sign up (`-error`: sign-in failed, couldn't create account, link expired); Reset password (`-error`: couldn't send, too many requests) | Shown by cause; dismissible on the two detail screens | no | none (HIG [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) prefers in-context messages to alerts) | none |
| **State message** (`.state-message`: heading, line, `.state-actions`) | Race browse (`-empty`, `-error`, in List and in Map); Race detail (`-error`); Results list (`-empty`, `-error`); Race picker (`-empty`, `-error`); Result detail (`-error`); Profile (`-error`) | Empty (`role="status"`), error (`role="alert"`, the error icon in Podium); one or two actions. **On the page, never framed** (kit fix 2026-10-22: no outline, frame or surface; the Map view's frame gives way) | no | none (in context, as HIG [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) advises) | G37 M (Race detail `-error`: the page has no `h1`); short button names are in Deferred to Lesson 7 |
| **Skeleton** (`.bar`, `.skeleton-card`) | Race browse (`-loading`: race-card shape with a photo band, count bar, map); Race detail (`-loading`, with action-bar bars); Results list (`-loading`: result-row shape, count bar); Race picker (`-loading`: race-card shape, no photo); Result detail (`-loading`); Profile (`-loading`: initials, rows, Sign out) | Loading only; `aria-hidden`, with a hidden status line | **yes**: a photo-band bar on Race browse and Race detail (step 5) | [Progress indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators) | G25 K |
| **Sticky action bar** (`.action-bar`: one primary link + `.action-caption`) | Race detail (all 3: "Register on \<domain\>", "Opens in a new tab — registration and payment happen there."); Result detail (all 3: "Open official result on \<domain\>", "Opens in a new tab.") | Base; holds the inline error on `-error`; skeleton bars on `-loading` | no | [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars) (bottom) | C1 glass; G38 K (its button a capsule, C7); G35 M (content stops at the bar instead of running under it) |
| **Detail header and facts** (`h1` + `dl.facts`: label / value pairs) | Race detail (Sport type, Race date, Location); Result detail (Race date, Sport type; with `dl.finish` above) | Base; skeleton on `-loading` | **yes** on Race detail (`.race > .photo`, step 5) | none | G29 K |
| **Detail section** (`section` with an `h2`: "About this race", "Official race website", "Official result link") | Race detail (`.about`, `.official`); Result detail (`.proof`) | Base; skeleton on `-loading` | no | none | none |
| **Status line** (one-line confirmation, `role="status"` or `aria-live`) | Results list (`.saved-status`, "Saved: \<race\>", `?saved=`); Sign in / Sign up (`.reset-done`, "Password changed…", `?reset=done`; `.sent-note`, "Sent. Check your inbox again.", `-check-inbox`); Profile (`.row-note`, "Saving…" / "Saved") | Hidden until its URL switch or event | no | none | none |

## Discovery

None. Every component that repeats on Race browse and Race detail also appears in Archive or Infrastructure, so it's under Shared. Discovery's single-screen blocks are in One-off.

## Archive

| Component | Screens (files) | States | Photo | Native iOS | Gaps |
|---|---|---|---|---|---|
| **Finish time** (`.finish-time`; `dl.finish` "Finish time") | Results list (`results-list`); Result detail (`result-detail`, `-error?cause=link`) | Base; skeleton bar on both `-loading` pages | no | none | none |
| **Proof line** (`.proof-label`, "Self-reported · via \<domain\>") | Results list (`results-list`); Result detail (`result-detail`, `-error?cause=link`) | Base; skeleton bar on `results-list-loading` | no | none | none |

## Infrastructure

| Component | Screens (files) | States | Photo | Native iOS | Gaps |
|---|---|---|---|---|---|
| **Gate intro** (`p.context`) | Sign in / Sign up (`sign-in-sign-up`, `-error`, `-loading`: by mode and by where the person was heading); Reset password (`reset-password`, `-error`, `-loading`); New password (`new-password`, `-error`, `-loading`) | One line per mode or cause | no | none | none |
| **Check-inbox block** (`.inbox-heading`, `.inbox-line` with `.addr`, resend button, "Use a different email", `.expiry-note`) | Sign in / Sign up (`sign-in-sign-up-check-inbox`: new account or unconfirmed); Reset password (`reset-password-check-inbox`) | Base; resend "Sending…" then "Sent" (Sign in) | no | none | none |

---

## One-off

Single-screen blocks, by screen.

**Race browse**
- **Controls bar** (`.controls`, sticky: Filters + List/Map, then the chips row). Gaps: G7 K.
- **Active filter chips row** (`.chips-bar`, `.chips-row`, `button.chip` with "×", "Clear all filters"). Seen on `race-browse` with `?sport=` and on `-empty`. Gaps: G27 K. **Kit fix 2026-10-22 (designer):** the chips are iOS capsules in a tonal `--bg-2` fill, no outline, sentence case, the × inside (C7: they sit in a bar).
- **Filters trigger with count** ("Filters · N").
- **Sort control** (`.sort-control`, "Sort: Soonest first"; two options; hidden in Map view; disabled on `-loading`). Native: [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons). Gaps: G21 M.
- **Sport-type checkboxes** (seven, in the Filters sheet). Native: [Toggles](https://developer.apple.com/design/human-interface-guidelines/toggles), [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables). Gaps: G19 M.
- **Static map** (`.map-placeholder.has-pins`, `a.map-pin` ×7, `.map-caption`). States: pins filtered with the list; empty, error and loading messages inside the map.
- **Race photo** (`img.photo` with `.photo--low/mid/lower/center/high` crops). Photo: yes.

**Race detail**
- **Official race website link** (an external text link in its section). Gaps: G36 K (44pt target, step 5).
- **Race photo, detail** (`.race > .photo`, step 5): the race card’s file and focus class, 3:1 at full content width (358 × 119 at 390), outer 6px radius. Shows exactly the round-3 band (`visuals/README.md`). Photo: yes. Skeleton: `.race .bar.photo`.

**Results list**
- **Result row** (`article.result-card`: name, finish time, format chip, date, proof line). Native: [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables). Gaps: G22 K, G23 K.
- **Order label** (`.results-order`, "Newest first").

**Log result**
- **Form intro** (`.form-intro`, "Every field is needed to save a result.").
- **Catalog row** (`a.catalog-row`: "Find in race catalog" + hint; disabled on `-loading`).
- **Linked race card** (`section.linked-race`: "From the race catalog", name, date, sport type, place, `.unlink-btn` "Unlink race"; shown with `?catalog=`).
- **Locked form** (`fieldset.locked disabled` on `-loading`).

**Race picker**
- **List intro** (`.list-intro`, "Past races in the race catalog", or "…matching “q”").

**Result detail**
- **Proof URL and note** (`.proof-url`, the full link; `.proof-note`, "Onrace doesn’t verify results. The official result is the evidence.").

**Sign in / Sign up**
- **Forgot password? link** (Sign in mode only).
- **Form note** (`.form-note`, "We’ll send a link to confirm your email.", Create account mode).

**New password**
- **Expired-link message** (`section.state-msg`, `-error?cause=expired`: no form, "Reset password again").

**Profile**
- **Identity block** (`.identity`: initials `MR`, name, email). Photo: no (deferred; initials instead).
- **Grouped settings rows** (`.group`, `.group-heading` "Account", `.rows` with Name, Country, Language, Email read-only; `.group-footer`). Native: [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables).
- **Sign out button** (`.signout`, its own group).
- **Confirm alert** (`dialog.alert`: "Sign out of Onrace?", Cancel, Sign out). Native: [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts).

---

## Closed (designer, 2026-10-18)

- **"Qualifier" tag:** no such element exists in any wireframe, CSS or microcopy row (the word appears only in prose: `wireframes/_screens.md:80`, `research/research.md:251`). Closed; not an open decision.
- **"Filtered, with results":** kept as it is: `race-browse.html` plus URL parameters (`region`, `from`, `to`, `sport`, `q`), no page of its own. It's now a state in the wireframes viewer tree, **Race browse · Filtered** → `race-browse.html?sport=hyrox&sport=marathon` (`scripts/build_wireframes_viewer.py` → `URL_STATES`).
- **G21 (Sort with two options):** the control is decided in the markup pass.
- **HIG gaps on the eight grayscale screens:** checked per group in step 5. Until then, the Gaps column lists only gaps that share markup with the two Podium screens. **Discovery done 2026-10-22** (Race detail: G34–G39, `concept/concept.md` → Step 5, Discovery).
