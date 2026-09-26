# Microcopy — source of truth

**Status: transcription, 2026-09-26.** Every piece of interface text in `wireframes/*.html` (35 pages, including every hidden `?cause=` / `?mode=` / `?reason=` variant and the few strings only a script writes), collected into one table. Nothing has been rewritten yet. The table flags where screens describe the same thing differently. Later it becomes the table every product line is checked against: a new line either reuses a row here or adds one.

## How it was built

- Extracted from the HTML (not by eye): each text-bearing element becomes one line, typed by its role, and placed in the **zone** named by the nearest `<!-- ZONE: … -->` comment in the page. A few zones had no comment of their own and were corrected by hand (Race browse's Filters sheet, the form fields on the Sign in and Reset password error pages).
- One row per line **per screen**. Identical lines on a screen's state pages are merged, and **States** lists where each appears (`base`, `empty`, `error`, `loading`, `check-inbox`, plus the variant, e.g. `error (cause=link)`).
- Script-only strings (the filter count "Filters · 2", "N races match your filters", "Remove filter: …", "Enter your password.") are added from the page scripts. Everything else a script changes is real, hidden markup and was captured directly.
- `<search text>` / `<race name>` mark where the page inserts what the user typed or picked.

**Type:** heading · button · button (nav) — back/close/cancel in a bar · tab label · link · field label · field placeholder · option · helper text · body text · body text (in tappable row) · state message — empty/error/alert copy · status (a11y / live) — spoken or live-region text · a11y label — `aria-label`, heard not seen.

**Source** — who writes the line:

| Source | Meaning | Ours to rewrite? |
|---|---|---|
| UI copy | Onrace's interface text | **Yes**, this is what the table governs |
| UI copy + user data / + catalog data | Our sentence around a value we don't write (an email, a domain) | The sentence yes, the value no |
| catalog data | Race listings Onrace curates and seeds via SQL (`CLAUDE.md` → Race data): names, dates, cities, descriptions, sites | Edited as data, not as microcopy |
| reference data / user selection | Option lists from the data model (sport types, regions, countries, languages) and the user's picks from them | Only as data vocabulary |
| **user-written** | Text the user types themselves (below) | **No — never flagged for rewriting** |
| wireframe annotation | Wireframe scaffolding (map placeholder, page labels) | Not product copy: gets replaced, not rewritten |

## Text the user writes (don't rewrite)

From `CLAUDE.md` → Data model. The only free-text a person types are these. Onrace displays them, but doesn't write them. Rows showing them are marked **user-written**, and they are never flagged.

| Field | Where they type it | Where it's shown back |
|---|---|---|
| `race_name` | Log result → Race name (when no catalog race is linked; a linked race's name is catalog data) | Results list rows, Result detail heading, "Saved: <race name>" |
| `finish_time` | Log result → Finish time | Results list rows, Result detail |
| `official_result_url` | Log result → Official result link | Result detail (URL text), the domain in "Self-reported · via <domain>", "Open official result on <domain>" |
| `name` (profile) | Profile → Name | Profile identity, initials, "Couldn't save — back to <name>." |
| email | Sign in / Sign up → Email (and Reset password) | Profile, Check inbox lines ("We sent a link to <email>") |
| search text | Race picker → search | "No catalog race matches “<search text>”" |

`date` and `sport_type` are picked from controls, and country and language from lists, so they're reference data rather than free text. There's no `notes` or `category` field (both were cut, `CLAUDE.md` → Data model), so a logged result has no other free text.

## Flags

Flags mark a problem to decide on, not a rewrite: nothing below has been changed. Each row in the full table carries its flag codes.

| Code | What's inconsistent | Rows |
|---|---|---:|
| **T1** | Same object — the archive: "My Results" / "results archive" / "archive" / "logged results" / "your official race results" | 16 |
| **T2** | Same object — the proof link: "Official result link" / "official result" / "source link" / "link to the timing site" / "official timing page" / "timing site" / "your proof" | 14 |
| **T3** | Same object — a result called a "time": "proof of a past time" vs "result" everywhere else | 1 |
| **T4** | Same object — the catalog: "race catalog" / "Onrace catalog" / "catalog race" / "the catalog" | 9 |
| **T5** | Same object — the account: "account" vs "profile" for the same thing (Profile screen, sign-in context lines) | 27 |
| **T6** | Same object — the emailed link vs the email: "Resend email" (sign-up) vs "Resend link" (reset) for the same kind of message; "confirm your address" vs "email" | 5 |
| **A1** | Same action — re-send the emailed link, four labels: "Resend email" / "Resend link" / "Send a new link" / "Request a new link" | 9 |
| **A2** | Same word, two actions — "sign-up" means race registration on Race detail ("sign-up and payment happen there", "Register on …") but account creation is "Create account"; the screen itself is named "Sign in / Sign up" | 14 |
| **A3** | Same action — leave a modal/sheet: "Close" (Sign in modal, Filters sheet) vs "Cancel" (Race picker, sign-out alert) vs "Dismiss" (inline alerts) | 6 |
| **A4** | Same destination, two back labels — "Back to My Results" (Result detail) vs "My Results" (Log result); "Back to races" vs "Sign in" (no "Back to") — documented rule (§ 1: shortened when the bar holds a title), still two labels for one place | 5 |
| **A5** | Same action — clear every filter: "Clear all" (chips bar) vs "Clear all filters" (empty state) | 2 |
| **C1** | Same field, different labels — "Race date" (Log result) vs "Date" (Race detail, Result detail) | 3 |
| **C2** | Near-duplicate copy that drifts — the expired-link explanation is worded three ways; "Sent — check your inbox again." (visible) vs "Sent. Check your inbox again." (screen reader) | 6 |
| **C3** | Mixed apostrophes — curly ’ on Log result, Race picker, Result detail; straight ' everywhere else | 13 |
| **C4** | Required marking disagrees with itself — only the link field carries "Required" while the intro says every field is needed | 2 |
| **V1** | Tone — minimizer "just" ("it just isn't confirmed yet") | 1 |
| **P1** | Placeholder — wireframe annotation, not product copy (must be replaced: a real map, no page labels) | 39 |
| **P2** | Placeholder — a real-looking value as a field placeholder (reads as pre-filled; "e.g." missing) | 1 |

**Searched for and not found:**
- **AI clichés and upbeat tone:** no "Oops", "Something went wrong", "Congratulations", "Awesome/Great/Yay", "Sorry/Unfortunately/Please", no exclamation marks and no emoji in any visible or spoken line. The one tone note is **V1**.
- **"Race" called something else:** it's never "event", "listing" or "competition" in the interface ("listing" only appears in the docs). A result is never "entry", "submission" or "record".
- **Lorem ipsum, "Heading 1", "Label", TODO:** none. The only placeholders are **P1** and **P2**.

Apostrophes (**C3**): 13 lines use curly ’, 32 use straight '. Only the curly ones are flagged, as the minority.

## Full table

| # | Screen | Zone | Line | Type | States | Source | Flags |
|---:|---|---|---|---|---|---|---|
| 1 | Race browse | (page) | Onrace — Race browse, empty state (wireframe) | a11y label | empty | wireframe annotation | P1 |
| 2 | Race browse | large title | Discover | heading | empty; error; loading (state=loading); base | UI copy |  |
| 3 | Race browse | shared controls | Filters · 3 | button | empty | UI copy |  |
| 4 | Race browse | shared controls | Choose view | a11y label | empty; error; loading (state=loading); base | UI copy |  |
| 5 | Race browse | shared controls | List | button | empty; error; loading (state=loading); base | UI copy |  |
| 6 | Race browse | shared controls | Map | button | empty; error; loading (state=loading); base | UI copy |  |
| 7 | Race browse | active filter chips | Active filters | a11y label | empty; error; loading (state=loading); base | UI copy |  |
| 8 | Race browse | active filter chips | Remove filter: Middle East | a11y label | empty | UI copy + user selection |  |
| 9 | Race browse | active filter chips | Middle East × | button | empty | user selection (from option list) |  |
| 10 | Race browse | active filter chips | Remove filter: Triathlon | a11y label | empty | UI copy + user selection |  |
| 11 | Race browse | active filter chips | Triathlon × | button | empty | user selection (from option list) |  |
| 12 | Race browse | active filter chips | Remove filter: 1 Oct – 30 Nov 2026 | a11y label | empty | UI copy + user selection |  |
| 13 | Race browse | active filter chips | 1 Oct – 30 Nov 2026 × | button | empty | user selection (from option list) |  |
| 14 | Race browse | active filter chips | Clear all | button | empty; error; loading (state=loading); base | UI copy | A5 |
| 15 | Race browse | results row | 0 races match your filters | body text | empty | UI copy |  |
| 16 | Race browse | results row | Map or list view | a11y label | empty; error; loading (state=loading); base | UI copy |  |
| 17 | Race browse | empty state | No races match your current filters | heading | empty | UI copy |  |
| 18 | Race browse | empty state | Remove a filter above, or try a wider date range, another region, or more sport types. | state message | empty | UI copy |  |
| 19 | Race browse | empty state | Loosen filters | button | empty | UI copy |  |
| 20 | Race browse | empty state | Clear all filters | button | empty | UI copy | A5 |
| 21 | Race browse | empty state | [ map placeholder — no pins: 0 races match ] | state message | empty | wireframe annotation | P1 |
| 22 | Race browse | global nav | Global navigation | a11y label | empty; error; loading (state=loading); base | UI copy |  |
| 23 | Race browse | global nav | Discover | tab label | empty; error; loading (state=loading); base | UI copy |  |
| 24 | Race browse | global nav | My Results | tab label | empty; error; loading (state=loading); base | UI copy | T1 |
| 25 | Race browse | global nav | Profile | tab label | empty; error; loading (state=loading); base | UI copy |  |
| 26 | Race browse | filters sheet | Filters | heading | empty; error; loading (state=loading); base | UI copy |  |
| 27 | Race browse | filters sheet | Region | field label | empty; error; loading (state=loading); base | UI copy |  |
| 28 | Race browse | filters sheet | All regions | option | empty; error; loading (state=loading); base | UI copy |  |
| 29 | Race browse | filters sheet | Europe | option | empty; error; loading (state=loading); base | reference data (option list) |  |
| 30 | Race browse | filters sheet | North America | option | empty; error; loading (state=loading); base | reference data (option list) |  |
| 31 | Race browse | filters sheet | Middle East | option | empty; error; loading (state=loading); base | reference data (option list) |  |
| 32 | Race browse | filters sheet | Asia-Pacific | option | empty; error; loading (state=loading); base | reference data (option list) |  |
| 33 | Race browse | filters sheet | Africa | option | empty; error; loading (state=loading); base | reference data (option list) |  |
| 34 | Race browse | filters sheet | Date from | field label | empty; error; loading (state=loading); base | UI copy |  |
| 35 | Race browse | global nav | 2026-10-01 | field value (prefilled) | empty | user-written |  |
| 36 | Race browse | filters sheet | Date to | field label | empty; error; loading (state=loading); base | UI copy |  |
| 37 | Race browse | global nav | 2026-11-30 | field value (prefilled) | empty | user-written |  |
| 38 | Race browse | filters sheet | Sport type | field label | empty; error; loading (state=loading); base | UI copy |  |
| 39 | Race browse | global nav | HYROX | field label | empty; error; loading (state=loading); base | catalog data |  |
| 40 | Race browse | global nav | DEKA / functional fitness | field label | empty; error; loading (state=loading); base | catalog data |  |
| 41 | Race browse | global nav | Marathon | field label | empty; error; loading (state=loading); base | catalog data |  |
| 42 | Race browse | global nav | Half marathon | field label | empty; error; loading (state=loading); base | catalog data |  |
| 43 | Race browse | global nav | Triathlon | field label | empty; error; loading (state=loading); base | catalog data |  |
| 44 | Race browse | global nav | Ultra | field label | empty; error; loading (state=loading); base | catalog data |  |
| 45 | Race browse | global nav | OCR | field label | empty; error; loading (state=loading); base | catalog data |  |
| 46 | Race browse | filters sheet | Close | button | empty; error; loading (state=loading); base | UI copy | A3 |
| 47 | Race browse | filters sheet | Apply filters | button | empty; error; loading (state=loading); base | UI copy |  |
| 48 | Race browse | (page) | Onrace — Race browse, error state (wireframe) | a11y label | error | wireframe annotation | P1 |
| 49 | Race browse | shared controls | Filters | button | error; loading (state=loading); base | UI copy |  |
| 50 | Race browse | results row | Races couldn't be loaded | body text | error | UI copy |  |
| 51 | Race browse | error state | Couldn't load races | heading | error | UI copy |  |
| 52 | Race browse | error state | Check your connection and try again. Your filters will stay as they are. | state message | error | UI copy |  |
| 53 | Race browse | error state | Try again | button | error | UI copy |  |
| 54 | Race browse | error state | [ map placeholder — no pins: races failed to load ] | state message | error | wireframe annotation | P1 |
| 55 | Race browse | global nav | 2026-09-23 | field value (prefilled) | error; loading (state=loading); base | user-written |  |
| 56 | Race browse | global nav | 2027-09-23 | field value (prefilled) | error; loading (state=loading); base | user-written |  |
| 57 | Race browse | (page) | Onrace — Race browse, loading state (wireframe) | a11y label | loading | wireframe annotation | P1 |
| 58 | Race browse | results row | Loading races… | body text | loading (state=loading) | UI copy |  |
| 59 | Race browse | results row | Sort: | field label | loading (state=loading); base | UI copy |  |
| 60 | Race browse | results row | Soonest first | option | loading (state=loading); base | UI copy |  |
| 61 | Race browse | results row | Farthest first | option | loading (state=loading); base | UI copy |  |
| 62 | Race browse | loading state | Map loading; race pins appear once races have loaded | a11y label | loading (state=loading) | UI copy |  |
| 63 | Race browse | loading state | [ map placeholder — loading race pins… ] | body text | loading (state=loading) | wireframe annotation | P1 |
| 64 | Race browse | (page) | Onrace — Race browse (wireframe) | a11y label | base | wireframe annotation | P1 |
| 65 | Race browse | results row | 7 upcoming races | body text | base | UI copy |  |
| 66 | Race browse | results row | Berlin Marathon | heading | base | catalog data |  |
| 67 | Race browse | results row | Marathon | body text (in tappable row) | base | catalog data |  |
| 68 | Race browse | results row | 27 Sep 2026 | body text (in tappable row) | base | catalog data |  |
| 69 | Race browse | results row | Berlin, Germany | body text (in tappable row) | base | catalog data |  |
| 70 | Race browse | results row | HYROX London | heading | base | catalog data |  |
| 71 | Race browse | results row | HYROX | body text (in tappable row) | base | catalog data |  |
| 72 | Race browse | results row | 6 Dec 2026 | body text (in tappable row) | base | catalog data |  |
| 73 | Race browse | results row | London, UK | body text (in tappable row) | base | catalog data |  |
| 74 | Race browse | results row | HYROX Dallas | heading | base | catalog data |  |
| 75 | Race browse | results row | 17 Jan 2027 | body text (in tappable row) | base | catalog data |  |
| 76 | Race browse | results row | Dallas, USA | body text (in tappable row) | base | catalog data |  |
| 77 | Race browse | results row | DEKA STRONG Chicago | heading | base | catalog data |  |
| 78 | Race browse | results row | DEKA | body text (in tappable row) | base | catalog data |  |
| 79 | Race browse | results row | 14 Mar 2027 | body text (in tappable row) | base | catalog data |  |
| 80 | Race browse | results row | Chicago, USA | body text (in tappable row) | base | catalog data |  |
| 81 | Race browse | results row | Boston Marathon | heading | base | catalog data |  |
| 82 | Race browse | results row | 20 Apr 2027 | body text (in tappable row) | base | catalog data |  |
| 83 | Race browse | results row | Boston, USA | body text (in tappable row) | base | catalog data |  |
| 84 | Race browse | results row | Spartan Race Beast — Killington | heading | base | catalog data |  |
| 85 | Race browse | results row | OCR | body text (in tappable row) | base | catalog data |  |
| 86 | Race browse | results row | 11 Jul 2027 | body text (in tappable row) | base | catalog data |  |
| 87 | Race browse | results row | Killington, USA | body text (in tappable row) | base | catalog data |  |
| 88 | Race browse | results row | UTMB — Ultra-Trail du Mont-Blanc | heading | base | catalog data |  |
| 89 | Race browse | results row | Ultra | body text (in tappable row) | base | catalog data |  |
| 90 | Race browse | results row | 24 Aug 2027 | body text (in tappable row) | base | catalog data |  |
| 91 | Race browse | results row | Chamonix, France | body text (in tappable row) | base | catalog data |  |
| 92 | Race browse | results row | Map of the filtered races | a11y label | base | UI copy |  |
| 93 | Race browse | results row | Berlin Marathon, Berlin, 27 Sep 2026 | a11y label | base | catalog data |  |
| 94 | Race browse | results row | Berlin | button | base | catalog data |  |
| 95 | Race browse | results row | HYROX London, London, 6 Dec 2026 | a11y label | base | catalog data |  |
| 96 | Race browse | results row | London | button | base | catalog data |  |
| 97 | Race browse | results row | UTMB — Ultra-Trail du Mont-Blanc, Chamonix, 24 Aug 2027 | a11y label | base | catalog data |  |
| 98 | Race browse | results row | Chamonix | button | base | catalog data |  |
| 99 | Race browse | results row | HYROX Dallas, Dallas, 17 Jan 2027 | a11y label | base | catalog data |  |
| 100 | Race browse | results row | Dallas | button | base | catalog data |  |
| 101 | Race browse | results row | DEKA STRONG Chicago, Chicago, 14 Mar 2027 | a11y label | base | catalog data |  |
| 102 | Race browse | results row | Chicago | button | base | catalog data |  |
| 103 | Race browse | results row | Spartan Race Beast — Killington, Killington, 11 Jul 2027 | a11y label | base | catalog data |  |
| 104 | Race browse | results row | Killington | button | base | catalog data |  |
| 105 | Race browse | results row | Boston Marathon, Boston, 20 Apr 2027 | a11y label | base | catalog data |  |
| 106 | Race browse | results row | Boston | button | base | catalog data |  |
| 107 | Race browse | results row | [ map placeholder — pin positions are approximate; pan/zoom changes what's visible, not which races match ] | helper text | base | wireframe annotation | P1 |
| 108 | Race browse | shared controls | Filters · 2 | button | base,empty (when filters are on) | UI copy |  |
| 109 | Race browse | results row | 3 races match your filters | body text | base (filtered) | UI copy |  |
| 110 | Race browse | results row | 1 race matches your filters | body text | base (filtered) | UI copy |  |
| 111 | Race detail | (page) | Onrace — Race detail, error state (wireframe) | a11y label | error | wireframe annotation | P1 |
| 112 | Race detail | top bar | Back | a11y label | error; loading; base | UI copy |  |
| 113 | Race detail | top bar | Back to races | button (nav) | error; loading; base | UI copy | A4 |
| 114 | Race detail | race | Couldn't load race details | heading | error (cause=detail) | UI copy |  |
| 115 | Race detail | race | Check your connection and try again. | state message | error (cause=detail) | UI copy |  |
| 116 | Race detail | race | Try again | button | error (cause=detail) | UI copy |  |
| 117 | Race detail | race | Berlin Marathon | heading | error (cause=registration); base | catalog data |  |
| 118 | Race detail | race | Sport type | field label | error (cause=registration); base | UI copy |  |
| 119 | Race detail | race | Marathon | body text | error (cause=registration); base | catalog data |  |
| 120 | Race detail | race | Date | field label | error (cause=registration); base | UI copy | C1 |
| 121 | Race detail | race | 27 September 2026 | body text | error (cause=registration); base | catalog data |  |
| 122 | Race detail | race | Location | field label | error (cause=registration); base | UI copy |  |
| 123 | Race detail | race | Berlin, Germany | body text | error (cause=registration); base | catalog data |  |
| 124 | Race detail | race | About this race | heading | error (cause=registration); base | UI copy |  |
| 125 | Race detail | race | 42.2 km flat, fast World Marathon Major course through central Berlin. | body text | error (cause=registration); base | catalog data |  |
| 126 | Race detail | race | Official race website | heading | error (cause=registration); base | UI copy |  |
| 127 | Race detail | race | bmw-berlin-marathon.com | link | error (cause=registration); base | catalog data |  |
| 128 | Race detail | race | HYROX London | heading | error (cause=registration); base | catalog data |  |
| 129 | Race detail | race | HYROX | body text | error (cause=registration); base | catalog data |  |
| 130 | Race detail | race | 6 December 2026 | body text | error (cause=registration); base | catalog data |  |
| 131 | Race detail | race | London, England, United Kingdom | body text | error (cause=registration); base | catalog data |  |
| 132 | Race detail | race | Indoor HYROX event combining 8 × 1 km runs with functional stations, held at ExCeL London. | body text | error (cause=registration); base | catalog data |  |
| 133 | Race detail | race | hyrox.com | link | error (cause=registration); base | catalog data |  |
| 134 | Race detail | race | HYROX Dallas | heading | error (cause=registration); base | catalog data |  |
| 135 | Race detail | race | 17 January 2027 | body text | error (cause=registration); base | catalog data |  |
| 136 | Race detail | race | Dallas, Texas, United States | body text | error (cause=registration); base | catalog data |  |
| 137 | Race detail | race | North American HYROX stop; the standard 8 × 1 km run + station format. | body text | error (cause=registration); base | catalog data |  |
| 138 | Race detail | race | DEKA STRONG Chicago | heading | error (cause=registration); base | catalog data |  |
| 139 | Race detail | race | DEKA / functional fitness | body text | error (cause=registration); base | catalog data |  |
| 140 | Race detail | race | 14 March 2027 | body text | error (cause=registration); base | catalog data |  |
| 141 | Race detail | race | Chicago, Illinois, United States | body text | error (cause=registration); base | catalog data |  |
| 142 | Race detail | race | 10-zone functional-fitness circuit race; DEKA’s strength-focused format. | body text | error (cause=registration); base | catalog data |  |
| 143 | Race detail | race | spartan.com | link | error (cause=registration); base | catalog data |  |
| 144 | Race detail | race | Boston Marathon | heading | error (cause=registration); base | catalog data |  |
| 145 | Race detail | race | 20 April 2027 | body text | error (cause=registration); base | catalog data |  |
| 146 | Race detail | race | Boston, Massachusetts, United States | body text | error (cause=registration); base | catalog data |  |
| 147 | Race detail | race | 42.2 km World Marathon Major through Boston’s historic Newton Hills; requires a qualifying time or charity entry. | body text | error (cause=registration); base | catalog data |  |
| 148 | Race detail | race | baa.org | link | error (cause=registration); base | catalog data |  |
| 149 | Race detail | race | Spartan Race Beast — Killington | heading | error (cause=registration); base | catalog data |  |
| 150 | Race detail | race | OCR | body text | error (cause=registration); base | catalog data |  |
| 151 | Race detail | race | 11 July 2027 | body text | error (cause=registration); base | catalog data |  |
| 152 | Race detail | race | Killington, Vermont, United States | body text | error (cause=registration); base | catalog data |  |
| 153 | Race detail | race | 21+ km obstacle course race across Killington’s mountain terrain; part of the Spartan Trifecta. | body text | error (cause=registration); base | catalog data |  |
| 154 | Race detail | race | UTMB — Ultra-Trail du Mont-Blanc | heading | error (cause=registration); base | catalog data |  |
| 155 | Race detail | race | Ultra | body text | error (cause=registration); base | catalog data |  |
| 156 | Race detail | race | 24 August 2027 | body text | error (cause=registration); base | catalog data |  |
| 157 | Race detail | race | Chamonix, France | body text | error (cause=registration); base | catalog data |  |
| 158 | Race detail | race | 170 km ultra-trail circling Mont Blanc through France, Italy, and Switzerland. | body text | error (cause=registration); base | catalog data |  |
| 159 | Race detail | race | utmb.world | link | error (cause=registration); base | catalog data |  |
| 160 | Race detail | sticky action bar | Couldn't open the link | heading | error (cause=registration) | UI copy |  |
| 161 | Race detail | sticky action bar | The registration link didn't open in a new tab. Your browser may have blocked it. Try again, or come back to this race later. | state message | error (cause=registration) | UI copy |  |
| 162 | Race detail | sticky action bar | Dismiss | button | error (cause=registration) | UI copy | A3 |
| 163 | Race detail | sticky action bar | Register on bmw-berlin-marathon.com | button | error (cause=registration); base | UI copy + catalog data (domain) | A2 |
| 164 | Race detail | sticky action bar | Opens in a new tab — sign-up and payment happen there. | helper text | error (cause=registration); base | UI copy | A2 |
| 165 | Race detail | sticky action bar | Register on hyrox.com | button | error (cause=registration); base | UI copy + catalog data (domain) | A2 |
| 166 | Race detail | sticky action bar | Register on spartan.com | button | error (cause=registration); base | UI copy + catalog data (domain) | A2 |
| 167 | Race detail | sticky action bar | Register on baa.org | button | error (cause=registration); base | UI copy + catalog data (domain) | A2 |
| 168 | Race detail | sticky action bar | Register on utmb.world | button | error (cause=registration); base | UI copy + catalog data (domain) | A2 |
| 169 | Race detail | (page) | Onrace — Race detail, loading state (wireframe) | a11y label | loading | wireframe annotation | P1 |
| 170 | Race detail | race | Loading race details… | status (a11y / live) | loading | UI copy |  |
| 171 | Race detail | (page) | Onrace — Race detail (wireframe) | a11y label | base | wireframe annotation | P1 |
| 172 | Results list | (page) | Onrace — Results list, empty state (wireframe) | a11y label | empty | wireframe annotation | P1 |
| 173 | Results list | header | My Results | heading | empty; error; loading (state=loading); base | UI copy | T1 |
| 174 | Results list | header | Log result | button | empty; error; loading (state=loading); base | UI copy |  |
| 175 | Results list | results row | 0 logged results | body text | empty | UI copy | T1 |
| 176 | Results list | empty state | Logged results | a11y label | empty | UI copy |  |
| 177 | Results list | empty state | No results logged yet | heading | empty | UI copy |  |
| 178 | Results list | empty state | Keep your official race results here, each with a link to the timing site that published it. When an elite race asks for proof of a past time, it's ready to pull up. | state message | empty | UI copy | T1 T2 T3 |
| 179 | Results list | empty state | Log your first result | button | empty | UI copy |  |
| 180 | Results list | global nav | Global navigation | a11y label | empty; error; loading (state=loading); base | UI copy |  |
| 181 | Results list | global nav | Discover | tab label | empty; error; loading (state=loading); base | UI copy |  |
| 182 | Results list | global nav | My Results | tab label | empty; error; loading (state=loading); base | UI copy | T1 |
| 183 | Results list | global nav | Profile | tab label | empty; error; loading (state=loading); base | UI copy |  |
| 184 | Results list | (page) | Onrace — Results list, error state (wireframe) | a11y label | error | wireframe annotation | P1 |
| 185 | Results list | results row | Results couldn't be loaded | body text | error | UI copy |  |
| 186 | Results list | error state | Logged results | a11y label | error | UI copy |  |
| 187 | Results list | error state | Couldn't load your logged results | heading | error | UI copy | T1 |
| 188 | Results list | error state | Check your connection and try again. Nothing in your archive has changed. | state message | error | UI copy | T1 |
| 189 | Results list | error state | Try again | button | error | UI copy |  |
| 190 | Results list | (page) | Onrace — Results list, loading state (wireframe) | a11y label | loading | wireframe annotation | P1 |
| 191 | Results list | results row | Loading your logged results… | body text | loading (state=loading) | UI copy | T1 |
| 192 | Results list | loading state | Logged results | a11y label | loading (state=loading) | UI copy |  |
| 193 | Results list | (page) | Onrace — Results list (wireframe) | a11y label | base | wireframe annotation | P1 |
| 194 | Results list | saved confirmation | Saved: <race name> | status (a11y / live) | base | UI copy |  |
| 195 | Results list | results row | 4 logged results Newest first | body text | base | UI copy | T1 |
| 196 | Results list | logged results | Logged results | a11y label | base | UI copy |  |
| 197 | Results list | logged results | DEKA STRONG Chicago | heading | base | user-written |  |
| 198 | Results list | logged results | 24:36 | body text (in tappable row) | base | user-written |  |
| 199 | Results list | logged results | DEKA | body text (in tappable row) | base | catalog data |  |
| 200 | Results list | logged results | 14 Mar 2026 | body text (in tappable row) | base | catalog data |  |
| 201 | Results list | logged results | Self-reported · via athlinks.com | body text (in tappable row) | base | UI copy + user data (domain) |  |
| 202 | Results list | logged results | HYROX London | heading | base | user-written |  |
| 203 | Results list | logged results | 1:18:42 | body text (in tappable row) | base | user-written |  |
| 204 | Results list | logged results | HYROX | body text (in tappable row) | base | catalog data |  |
| 205 | Results list | logged results | 6 Dec 2025 | body text (in tappable row) | base | catalog data |  |
| 206 | Results list | logged results | Self-reported · via results.hyrox.com | body text (in tappable row) | base | UI copy + user data (domain) |  |
| 207 | Results list | logged results | Valencia Half Marathon | heading | base | user-written |  |
| 208 | Results list | logged results | 1:28:05 | body text (in tappable row) | base | user-written |  |
| 209 | Results list | logged results | Half marathon | body text (in tappable row) | base | catalog data |  |
| 210 | Results list | logged results | 26 Oct 2025 | body text (in tappable row) | base | catalog data |  |
| 211 | Results list | logged results | Self-reported · via valenciaciudaddelrunning.com | body text (in tappable row) | base | UI copy + user data (domain) |  |
| 212 | Results list | logged results | Berlin Marathon | heading | base | user-written |  |
| 213 | Results list | logged results | 3:12:48 | body text (in tappable row) | base | user-written |  |
| 214 | Results list | logged results | Marathon | body text (in tappable row) | base | catalog data |  |
| 215 | Results list | logged results | 21 Sep 2025 | body text (in tappable row) | base | catalog data |  |
| 216 | Results list | logged results | Self-reported · via berlin.r.mikatiming.com | body text (in tappable row) | base | UI copy + user data (domain) |  |
| 217 | Log result | (page) | Onrace — Log result, error state (wireframe) | a11y label | error | wireframe annotation | P1 |
| 218 | Log result | top bar | My Results | button (nav) | error; loading; base | UI copy | T1 A4 |
| 219 | Log result | top bar | Log result | heading | error; loading; base | UI copy |  |
| 220 | Log result | top bar | Save | button | error; base | UI copy |  |
| 221 | Log result | form | Result details | heading (screen-reader only) | error; loading; base | UI copy |  |
| 222 | Log result | save error | Couldn’t save your result | heading | error (cause=submit) | UI copy | C3 |
| 223 | Log result | save error | Nothing was saved — Onrace couldn’t reach the server. Check your connection, then tap Save to try again. Everything you entered is still here. | state message | error (cause=submit) | UI copy | C3 |
| 224 | Log result | intro | Every field is needed to save a result. | helper text | error; loading; base | UI copy | C4 |
| 225 | Log result | catalog link | Find in race catalog | body text (in tappable row) | error; loading; base | UI copy | T4 |
| 226 | Log result | catalog link | Optional. Fills in the race name, date and sport type for you. | body text (in tappable row) | error; loading; base | UI copy |  |
| 227 | Log result | linked race | From the Onrace catalog | body text | error; loading; base | UI copy | T4 |
| 228 | Log result | linked race | Unlink | button | error; loading; base | UI copy |  |
| 229 | Log result | race facts | Race name | field label | error; loading; base | UI copy |  |
| 230 | Log result | race facts | e.g. Berlin Marathon | field placeholder | error; loading; base | UI copy |  |
| 231 | Log result | race facts | Add the race name. | state message | error (cause=fields) | UI copy |  |
| 232 | Log result | race facts | Race date | field label | error; loading; base | UI copy | C1 |
| 233 | Log result | race facts | Add the date you raced. | state message | error (cause=fields) | UI copy |  |
| 234 | Log result | race facts | Sport type | field label | error; loading; base | UI copy |  |
| 235 | Log result | race facts | Choose a sport type | option | error; loading; base | UI copy |  |
| 236 | Log result | race facts | HYROX | option | error; loading; base | catalog data |  |
| 237 | Log result | race facts | DEKA / functional fitness | option | error; loading; base | catalog data |  |
| 238 | Log result | race facts | Marathon | option | error; loading; base | catalog data |  |
| 239 | Log result | race facts | Half marathon | option | error; loading; base | catalog data |  |
| 240 | Log result | race facts | Triathlon | option | error; loading; base | catalog data |  |
| 241 | Log result | race facts | Ultra | option | error; loading; base | catalog data |  |
| 242 | Log result | race facts | OCR | option | error; loading; base | catalog data |  |
| 243 | Log result | race facts | Choose a sport type. | state message | error (cause=fields) | UI copy |  |
| 244 | Log result | finish time | Finish time | field label | error; loading; base | UI copy |  |
| 245 | Log result | finish time | e.g. 3:12:48 | field placeholder | error; loading; base | UI copy |  |
| 246 | Log result | finish time | Add your finish time, e.g. 3:12:48. | state message | error (cause=fields) | UI copy |  |
| 247 | Log result | finish time | Hours:minutes:seconds, exactly as the official results show it. | helper text | error; loading; base | UI copy |  |
| 248 | Log result | proof | Required | body text | error; loading; base | UI copy | C4 |
| 249 | Log result | proof | Official result link | field label | error; loading; base | UI copy |  |
| 250 | Log result | proof | https://berlin.r.mikatiming.com/2025/ | field placeholder | error; loading; base | UI copy | P2 |
| 251 | Log result | proof | Add the link to your official result — it’s the proof this result is yours. | state message | error (cause=link) | UI copy | T2 C3 |
| 252 | Log result | proof | Paste the link to this result on the official timing site. It’s your proof — elite races like Boston ask for exactly this. Onrace doesn’t check it: the result shows as self-reported, with this link as its source. | helper text | error; loading; base | UI copy | T2 C3 |
| 253 | Log result | (page) | Onrace — Log result, loading state (wireframe) | a11y label | loading | wireframe annotation | P1 |
| 254 | Log result | top bar | Saving… | button | loading | UI copy |  |
| 255 | Log result | top bar | Saving your result… | status (a11y / live) | loading | UI copy |  |
| 256 | Log result | (page) | Onrace — Log result (wireframe) | a11y label | base | wireframe annotation | P1 |
| 257 | Race picker | (page) | Onrace — Race picker, empty state (wireframe) | a11y label | empty | wireframe annotation | P1 |
| 258 | Race picker | modal top bar | Cancel | button (nav) | empty; error; loading; base | UI copy | A3 |
| 259 | Race picker | modal top bar | Find a race | heading | empty; error; loading; base | UI copy |  |
| 260 | Race picker | search | Search past races by name or city | field label | empty; error; loading; base | UI copy |  |
| 261 | Race picker | search | Race name or city | field placeholder | empty; error; loading; base | UI copy |  |
| 262 | Race picker | empty state | No catalog race matches “<search text>” | heading | empty | UI copy | T4 |
| 263 | Race picker | empty state | The catalog only lists races that have already happened, and it may not have this one yet. Try another name or city, or type the race in yourself. | state message | empty | UI copy |  |
| 264 | Race picker | empty state | Type it in instead | button | empty | UI copy |  |
| 265 | Race picker | (page) | Onrace — Race picker, error state (wireframe) | a11y label | error | wireframe annotation | P1 |
| 266 | Race picker | error state | Couldn’t load the race catalog | heading | error | UI copy | T4 C3 |
| 267 | Race picker | error state | Check your connection and try again, or type the race in yourself. What you’ve entered on the form is kept. | state message | error | UI copy | C3 |
| 268 | Race picker | error state | Try again | button | error | UI copy |  |
| 269 | Race picker | error state | Type it in instead | button | error | UI copy |  |
| 270 | Race picker | (page) | Onrace — Race picker, loading state (wireframe) | a11y label | loading | wireframe annotation | P1 |
| 271 | Race picker | loading | Past races in the Onrace catalog | helper text | loading | UI copy | T4 |
| 272 | Race picker | loading | Loading past races from the Onrace catalog… | status (a11y / live) | loading | UI copy | T4 |
| 273 | Race picker | (page) | Onrace — Race picker (wireframe) | a11y label | base | wireframe annotation | P1 |
| 274 | Race picker | past races | Past races in the Onrace catalog | helper text | base | UI copy | T4 |
| 275 | Race picker | past races | Past races in the Onrace catalog matching “<search text>” | helper text | base | UI copy | T4 |
| 276 | Race picker | past races | Past catalog races | a11y label | base | UI copy | T4 |
| 277 | Race picker | past races | UTMB — Ultra-Trail du Mont-Blanc | heading | base | catalog data |  |
| 278 | Race picker | past races | Ultra | body text (in tappable row) | base | catalog data |  |
| 279 | Race picker | past races | 28 Aug 2026 | body text (in tappable row) | base | catalog data |  |
| 280 | Race picker | past races | Chamonix, France | body text (in tappable row) | base | catalog data |  |
| 281 | Race picker | past races | Boston Marathon | heading | base | catalog data |  |
| 282 | Race picker | past races | Marathon | body text (in tappable row) | base | catalog data |  |
| 283 | Race picker | past races | 20 Apr 2026 | body text (in tappable row) | base | catalog data |  |
| 284 | Race picker | past races | Boston, USA | body text (in tappable row) | base | catalog data |  |
| 285 | Race picker | past races | DEKA STRONG Chicago | heading | base | catalog data |  |
| 286 | Race picker | past races | DEKA | body text (in tappable row) | base | catalog data |  |
| 287 | Race picker | past races | 14 Mar 2026 | body text (in tappable row) | base | catalog data |  |
| 288 | Race picker | past races | Chicago, USA | body text (in tappable row) | base | catalog data |  |
| 289 | Race picker | past races | HYROX Dallas | heading | base | catalog data |  |
| 290 | Race picker | past races | HYROX | body text (in tappable row) | base | catalog data |  |
| 291 | Race picker | past races | 17 Jan 2026 | body text (in tappable row) | base | catalog data |  |
| 292 | Race picker | past races | Dallas, USA | body text (in tappable row) | base | catalog data |  |
| 293 | Race picker | past races | HYROX London | heading | base | catalog data |  |
| 294 | Race picker | past races | 6 Dec 2025 | body text (in tappable row) | base | catalog data |  |
| 295 | Race picker | past races | London, UK | body text (in tappable row) | base | catalog data |  |
| 296 | Race picker | past races | Valencia Half Marathon | heading | base | catalog data |  |
| 297 | Race picker | past races | Half marathon | body text (in tappable row) | base | catalog data |  |
| 298 | Race picker | past races | 26 Oct 2025 | body text (in tappable row) | base | catalog data |  |
| 299 | Race picker | past races | Valencia, Spain | body text (in tappable row) | base | catalog data |  |
| 300 | Race picker | past races | Berlin Marathon | heading | base | catalog data |  |
| 301 | Race picker | past races | 21 Sep 2025 | body text (in tappable row) | base | catalog data |  |
| 302 | Race picker | past races | Berlin, Germany | body text (in tappable row) | base | catalog data |  |
| 303 | Race picker | past races | Spartan Race Beast — Killington | heading | base | catalog data |  |
| 304 | Race picker | past races | OCR | body text (in tappable row) | base | catalog data |  |
| 305 | Race picker | past races | 13 Sep 2025 | body text (in tappable row) | base | catalog data |  |
| 306 | Race picker | past races | Killington, USA | body text (in tappable row) | base | catalog data |  |
| 307 | Result detail | (page) | Onrace — Result detail, error state (wireframe) | a11y label | error | wireframe annotation | P1 |
| 308 | Result detail | top bar | Back | a11y label | error; loading; base | UI copy |  |
| 309 | Result detail | top bar | Back to My Results | button (nav) | error; loading; base | UI copy | T1 A4 |
| 310 | Result detail | result | Couldn’t load this result | heading | error (cause=detail) | UI copy | C3 |
| 311 | Result detail | result | Check your connection and try again. | state message | error (cause=detail) | UI copy |  |
| 312 | Result detail | result | Try again | button | error (cause=detail) | UI copy |  |
| 313 | Result detail | result | DEKA STRONG Chicago | heading | error (cause=link); base | user-written |  |
| 314 | Result detail | result | Finish time | field label | error (cause=link); base | UI copy |  |
| 315 | Result detail | result | 24:36 | body text | error (cause=link); base | user-written |  |
| 316 | Result detail | result | Date | field label | error (cause=link); base | UI copy | C1 |
| 317 | Result detail | result | 14 March 2026 | body text | error (cause=link); base | catalog data |  |
| 318 | Result detail | result | Sport type | field label | error (cause=link); base | UI copy |  |
| 319 | Result detail | result | DEKA / functional fitness | body text | error (cause=link); base | catalog data |  |
| 320 | Result detail | result | Official result | heading | error (cause=link); base | UI copy |  |
| 321 | Result detail | result | https://www.athlinks.com/event/deka-strong-chicago-2026/results | body text | error (cause=link); base | user-written |  |
| 322 | Result detail | result | Self-reported · via athlinks.com | body text | error (cause=link); base | UI copy + user data (domain) |  |
| 323 | Result detail | result | Onrace doesn’t verify results. The official timing page is the evidence. | helper text | error (cause=link); base | UI copy | T2 C3 |
| 324 | Result detail | result | HYROX London | heading | error (cause=link); base | user-written |  |
| 325 | Result detail | result | 1:18:42 | body text | error (cause=link); base | user-written |  |
| 326 | Result detail | result | 6 December 2025 | body text | error (cause=link); base | catalog data |  |
| 327 | Result detail | result | HYROX | body text | error (cause=link); base | catalog data |  |
| 328 | Result detail | result | https://results.hyrox.com/season-8/london | body text | error (cause=link); base | user-written |  |
| 329 | Result detail | result | Self-reported · via results.hyrox.com | body text | error (cause=link); base | UI copy + user data (domain) |  |
| 330 | Result detail | result | Valencia Half Marathon | heading | error (cause=link); base | user-written |  |
| 331 | Result detail | result | 1:28:05 | body text | error (cause=link); base | user-written |  |
| 332 | Result detail | result | 26 October 2025 | body text | error (cause=link); base | catalog data |  |
| 333 | Result detail | result | Half marathon | body text | error (cause=link); base | catalog data |  |
| 334 | Result detail | result | https://www.valenciaciudaddelrunning.com/en/half/results-2025/ | body text | error (cause=link); base | user-written |  |
| 335 | Result detail | result | Self-reported · via valenciaciudaddelrunning.com | body text | error (cause=link); base | UI copy + user data (domain) |  |
| 336 | Result detail | result | Berlin Marathon | heading | error (cause=link); base | user-written |  |
| 337 | Result detail | result | 3:12:48 | body text | error (cause=link); base | user-written |  |
| 338 | Result detail | result | 21 September 2025 | body text | error (cause=link); base | catalog data |  |
| 339 | Result detail | result | Marathon | body text | error (cause=link); base | catalog data |  |
| 340 | Result detail | result | https://berlin.r.mikatiming.com/2025/ | body text | error (cause=link); base | user-written |  |
| 341 | Result detail | result | Self-reported · via berlin.r.mikatiming.com | body text | error (cause=link); base | UI copy + user data (domain) |  |
| 342 | Result detail | sticky action bar | Couldn’t open the link | heading | error (cause=link) | UI copy | C3 |
| 343 | Result detail | sticky action bar | The link to your result on athlinks.com didn’t open in a new tab. Your browser may have blocked it. Try again. | state message | error (cause=link) | UI copy + user data (domain) | T2 C3 |
| 344 | Result detail | sticky action bar | Try again | button | error (cause=link) | UI copy |  |
| 345 | Result detail | sticky action bar | Dismiss | button | error (cause=link) | UI copy | A3 |
| 346 | Result detail | sticky action bar | Open official result on athlinks.com | button | error (cause=link); base | UI copy + user data (domain) | T2 |
| 347 | Result detail | sticky action bar | Opens in a new tab. | helper text | error (cause=link); base | UI copy |  |
| 348 | Result detail | sticky action bar | The link to your result on results.hyrox.com didn’t open in a new tab. Your browser may have blocked it. Try again. | state message | error (cause=link) | UI copy + user data (domain) | T2 C3 |
| 349 | Result detail | sticky action bar | Open official result on results.hyrox.com | button | error (cause=link); base | UI copy + user data (domain) | T2 |
| 350 | Result detail | sticky action bar | The link to your result on valenciaciudaddelrunning.com didn’t open in a new tab. Your browser may have blocked it. Try again. | state message | error (cause=link) | UI copy + user data (domain) | T2 C3 |
| 351 | Result detail | sticky action bar | Open official result on valenciaciudaddelrunning.com | button | error (cause=link); base | UI copy + user data (domain) | T2 |
| 352 | Result detail | sticky action bar | The link to your result on berlin.r.mikatiming.com didn’t open in a new tab. Your browser may have blocked it. Try again. | state message | error (cause=link) | UI copy + user data (domain) | T2 C3 |
| 353 | Result detail | sticky action bar | Open official result on berlin.r.mikatiming.com | button | error (cause=link); base | UI copy + user data (domain) | T2 |
| 354 | Result detail | (page) | Onrace — Result detail, loading state (wireframe) | a11y label | loading | wireframe annotation | P1 |
| 355 | Result detail | result | Loading result details… | status (a11y / live) | loading | UI copy |  |
| 356 | Result detail | (page) | Onrace — Result detail (wireframe) | a11y label | base | wireframe annotation | P1 |
| 357 | Sign in / Sign up | (page) | Onrace — Sign in / Sign up, check inbox (wireframe) | a11y label | check-inbox | wireframe annotation | P1 |
| 358 | Sign in / Sign up | modal top bar | Close | button (nav) | check-inbox; error; loading; base | UI copy | A3 |
| 359 | Sign in / Sign up | modal top bar | Check your inbox | heading | check-inbox | UI copy |  |
| 360 | Sign in / Sign up | what to do | Confirm your email | heading | check-inbox | UI copy |  |
| 361 | Sign in / Sign up | what to do | We sent a link to maya.rossi@example.com. Open it on this device to finish creating your account. | body text | check-inbox (reason=new) | UI copy + user data | T5 A2 |
| 362 | Sign in / Sign up | what to do | Your account isn't confirmed yet. Open the link we sent to maya.rossi@example.com to finish, or send a new one. | body text | check-inbox (reason=unconfirmed) | UI copy + user data | T5 A1 |
| 363 | Sign in / Sign up | resend | Resend the confirmation email | a11y label | check-inbox | UI copy | T6 |
| 364 | Sign in / Sign up | resend | Sending… | button | check-inbox | UI copy |  |
| 365 | Sign in / Sign up | resend | Resend email | button | check-inbox | UI copy | T6 A1 |
| 366 | Sign in / Sign up | resend | Sent — check your inbox again. | helper text | check-inbox | UI copy | C2 |
| 367 | Sign in / Sign up | resend | Sending a new confirmation email… | status (a11y / live) | check-inbox | UI copy | T6 |
| 368 | Sign in / Sign up | resend | Sent. Check your inbox again. | status (a11y / live) | check-inbox | UI copy | C2 |
| 369 | Sign in / Sign up | use a different email | Use a different email | button | check-inbox | UI copy |  |
| 370 | Sign in / Sign up | expiry note | The link works once and expires after a while. If it doesn't work, send a new one. | helper text | check-inbox | UI copy | A1 C2 |
| 371 | Sign in / Sign up | (page) | Onrace — Sign in / Sign up, error state (wireframe) | a11y label | error | wireframe annotation | P1 |
| 372 | Sign in / Sign up | modal top bar | Sign in | heading | error (mode=signin); loading (mode=signin); base (mode=signin) | UI copy |  |
| 373 | Sign in / Sign up | modal top bar | Create account | heading | error (mode=signup); loading (mode=signup); base (mode=signup) | UI copy | T5 A2 |
| 374 | Sign in / Sign up | modal top bar | Check your inbox | heading | error (cause=confirm) | UI copy |  |
| 375 | Sign in / Sign up | why you're signing in | Sign in to see your results archive. | helper text | error (mode=signin); loading (mode=signin); base (mode=signin) | UI copy | T1 |
| 376 | Sign in / Sign up | why you're signing in | Create an account to start your results archive. | helper text | error (mode=signup); loading (mode=signup); base (mode=signup) | UI copy | T1 T5 A2 |
| 377 | Sign in / Sign up | why you're signing in | Sign in to see your account. | helper text | error (mode=signin); loading (mode=signin); base (mode=signin) | UI copy | T5 |
| 378 | Sign in / Sign up | why you're signing in | Create an account to set up your profile. | helper text | error (mode=signup); loading (mode=signup); base (mode=signup) | UI copy | T5 A2 |
| 379 | Sign in / Sign up | why you're signing in | Sign in to keep your official race results, with their source links, in one place. | helper text | error (mode=signin); loading (mode=signin); base (mode=signin) | UI copy | T1 T2 |
| 380 | Sign in / Sign up | why you're signing in | Create an account to keep your official race results, with their source links, in one place. | helper text | error (mode=signup); loading (mode=signup); base (mode=signup) | UI copy | T1 T2 T5 A2 |
| 381 | Sign in / Sign up | expired or used confirmation link | This confirmation link has expired | heading | error (cause=confirm) | UI copy |  |
| 382 | Sign in / Sign up | expired or used confirmation link | Or it was already used: each link works once. Your account is still there, it just isn't confirmed yet. | state message | error (cause=confirm) | UI copy | T5 C2 V1 |
| 383 | Sign in / Sign up | expired or used confirmation link | We'll send a new link to maya.rossi@example.com. | state message | error (cause=confirm) | UI copy + user data |  |
| 384 | Sign in / Sign up | expired or used confirmation link | Send a new link | button | error (cause=confirm) | UI copy | A1 |
| 385 | Sign in / Sign up | Sign in \| Create account | Sign in or create an account | a11y label | error; loading; base | UI copy | T5 |
| 386 | Sign in / Sign up | Sign in \| Create account | Sign in | button | error; loading; base | UI copy |  |
| 387 | Sign in / Sign up | Sign in \| Create account | Create account | button | error; loading; base | UI copy | T5 A2 |
| 388 | Sign in / Sign up | inline alert | Couldn't sign you in | heading | error (cause=signin,mode=signin) | UI copy |  |
| 389 | Sign in / Sign up | inline alert | Check your email and password and try again. If they're right, check your connection. | state message | error (cause=signin,mode=signin) | UI copy |  |
| 390 | Sign in / Sign up | inline alert | Couldn't create your account | heading | error (cause=signup,mode=signup) | UI copy | T5 |
| 391 | Sign in / Sign up | inline alert | This email may already have an account. If so, switch to Sign in. Otherwise, check that your password is at least 8 characters and that you're connected, then try again. | state message | error (cause=signup,mode=signup) | UI copy | T5 |
| 392 | Sign in / Sign up | credentials form | Email | field label | error | UI copy |  |
| 393 | Sign in / Sign up | credentials form | you@example.com | field placeholder | error | UI copy |  |
| 394 | Sign in / Sign up | inline alert | maya.rossi@example.com | field value (prefilled) | error | user-written |  |
| 395 | Sign in / Sign up | credentials form | Password | field label | error | UI copy |  |
| 396 | Sign in / Sign up | under the password field | At least 8 characters. | helper text | error (mode=signup); loading (mode=signup); base (mode=signup) | UI copy |  |
| 397 | Sign in / Sign up | under the password field | Forgot password? | link | error (mode=signin); loading (mode=signin); base (mode=signin) | UI copy |  |
| 398 | Sign in / Sign up | under the password field | Sign in | button | error (mode=signin); base (mode=signin) | UI copy |  |
| 399 | Sign in / Sign up | under the password field | Create account | button | error (mode=signup); base (mode=signup) | UI copy | T5 A2 |
| 400 | Sign in / Sign up | under the password field | We'll email you a link to confirm your address. | helper text | error (mode=signup); loading (mode=signup); base (mode=signup) | UI copy | T6 |
| 401 | Sign in / Sign up | (page) | Onrace — Sign in / Sign up, loading state (wireframe) | a11y label | loading | wireframe annotation | P1 |
| 402 | Sign in / Sign up | credentials form | Email | field label | loading; base | UI copy |  |
| 403 | Sign in / Sign up | credentials form | you@example.com | field placeholder | loading; base | UI copy |  |
| 404 | Sign in / Sign up | credentials form | maya.rossi@example.com | field value (prefilled) | loading | user-written |  |
| 405 | Sign in / Sign up | credentials form | Password | field label | loading; base | UI copy |  |
| 406 | Sign in / Sign up | credentials form | •••••••• | field placeholder | loading | UI copy |  |
| 407 | Sign in / Sign up | credentials form | Password, hidden while it sends | a11y label | loading | UI copy |  |
| 408 | Sign in / Sign up | under the password field | Signing in… | button | loading (mode=signin) | UI copy |  |
| 409 | Sign in / Sign up | under the password field | Creating account… | button | loading (mode=signup) | UI copy | T5 A2 |
| 410 | Sign in / Sign up | status | Signing in… | status (a11y / live) | loading (mode=signin) | UI copy |  |
| 411 | Sign in / Sign up | status | Creating your account… | status (a11y / live) | loading (mode=signup) | UI copy | T5 |
| 412 | Sign in / Sign up | (page) | Onrace — Sign in / Sign up (wireframe) | a11y label | base | wireframe annotation | P1 |
| 413 | Sign in / Sign up | password changed | Password changed. Sign in with your new password. | status (a11y / live) | base | UI copy |  |
| 414 | Sign in / Sign up | credentials form | Enter your password. | state message | base,error (empty password) | UI copy |  |
| 415 | Reset password | (page) | Onrace — Reset password, check inbox (wireframe) | a11y label | check-inbox | wireframe annotation | P1 |
| 416 | Reset password | top bar | Sign in | button (nav) | check-inbox; error; loading; base | UI copy | A4 |
| 417 | Reset password | top bar | Check your inbox | heading | check-inbox | UI copy |  |
| 418 | Reset password | what to do | Reset your password | heading | check-inbox | UI copy |  |
| 419 | Reset password | what to do | If an account exists for maya.rossi@example.com, we've sent a link to set a new password. Open it on this device. | body text | check-inbox | UI copy + user data | T5 |
| 420 | Reset password | resend | Resend link | button | check-inbox | UI copy | T6 A1 |
| 421 | Reset password | use a different email | Use a different email | button | check-inbox | UI copy |  |
| 422 | Reset password | expiry note | The link works once and expires after a while. If it doesn't work, send a new one. | helper text | check-inbox | UI copy | A1 C2 |
| 423 | Reset password | (page) | Onrace — Reset password, error state (wireframe) | a11y label | error | wireframe annotation | P1 |
| 424 | Reset password | top bar | Reset password | heading | error; loading; base | UI copy |  |
| 425 | Reset password | what this does | Enter the email you signed up with and we'll send a link to set a new password. | helper text | error; loading; base | UI copy |  |
| 426 | Reset password | inline alert | Couldn't send the reset link | heading | error (cause=request) | UI copy |  |
| 427 | Reset password | inline alert | Check your connection and try again. | state message | error (cause=request) | UI copy |  |
| 428 | Reset password | inline alert | Too many requests | heading | error (cause=rate) | UI copy |  |
| 429 | Reset password | inline alert | Wait a minute, then try again. | state message | error (cause=rate) | UI copy |  |
| 430 | Reset password | request form | Email | field label | error | UI copy |  |
| 431 | Reset password | request form | you@example.com | field placeholder | error | UI copy |  |
| 432 | Reset password | inline alert | maya.rossi@example.com | field value (prefilled) | error | user-written |  |
| 433 | Reset password | request form | Send reset link | button | error | UI copy |  |
| 434 | Reset password | (page) | Onrace — Reset password, loading state (wireframe) | a11y label | loading | wireframe annotation | P1 |
| 435 | Reset password | request form, submitted | Email | field label | loading | UI copy |  |
| 436 | Reset password | request form, submitted | you@example.com | field placeholder | loading | UI copy |  |
| 437 | Reset password | request form, submitted | maya.rossi@example.com | field value (prefilled) | loading | user-written |  |
| 438 | Reset password | request form, submitted | Sending… | button | loading | UI copy |  |
| 439 | Reset password | status | Sending the reset link… | status (a11y / live) | loading | UI copy |  |
| 440 | Reset password | (page) | Onrace — Reset password (wireframe) | a11y label | base | wireframe annotation | P1 |
| 441 | Reset password | request form | Email | field label | base | UI copy |  |
| 442 | Reset password | request form | you@example.com | field placeholder | base | UI copy |  |
| 443 | Reset password | request form | Send reset link | button | base | UI copy |  |
| 444 | New password | (page) | Onrace — New password, error state (wireframe) | a11y label | error | wireframe annotation | P1 |
| 445 | New password | top bar | Sign in | button (nav) | error; loading; base | UI copy | A4 |
| 446 | New password | top bar | New password | heading | error; loading; base | UI copy |  |
| 447 | New password | expired link | This reset link has expired | heading | error (cause=expired) | UI copy |  |
| 448 | New password | expired link | Reset links work once and only for a short time, so this one has expired or was already used. Request a new link and we'll email you a fresh one. | body text | error (cause=expired) | UI copy | A1 C2 |
| 449 | New password | expired link | Request a new link | button | error (cause=expired) | UI copy | A1 |
| 450 | New password | what this is | Choose a new password for your Onrace account. | helper text | error; loading; base | UI copy | T5 |
| 451 | New password | save error | Couldn't save your new password | heading | error (cause=submit) | UI copy |  |
| 452 | New password | save error | Your password wasn't changed. Check your connection, enter it again and tap Save new password. If this reset link has timed out, you'll need a new one. | state message | error (cause=submit) | UI copy |  |
| 453 | New password | save error | Request a new link | button | error (cause=submit) | UI copy | A1 |
| 454 | New password | new password form | New password | field label | error | UI copy |  |
| 455 | New password | new password form | Use at least 8 characters. | state message | error (cause=short) | UI copy |  |
| 456 | New password | new password form | That's your current password. Choose a different one. | state message | error (cause=same) | UI copy |  |
| 457 | New password | new password form | At least 8 characters. | helper text | error | UI copy |  |
| 458 | New password | new password form | Confirm new password | field label | error | UI copy |  |
| 459 | New password | new password form | The two passwords don't match. | state message | error (cause=mismatch) | UI copy |  |
| 460 | New password | new password form | Save new password | button | error | UI copy |  |
| 461 | New password | (page) | Onrace — New password, loading state (wireframe) | a11y label | loading | wireframe annotation | P1 |
| 462 | New password | new password form, locked | New password | field label | loading | UI copy |  |
| 463 | New password | new password form, locked | •••••••• | field placeholder | loading | UI copy |  |
| 464 | New password | new password form, locked | Password, hidden while it sends | a11y label | loading | UI copy |  |
| 465 | New password | new password form, locked | At least 8 characters. | helper text | loading | UI copy |  |
| 466 | New password | new password form, locked | Confirm new password | field label | loading | UI copy |  |
| 467 | New password | new password form, locked | Saving… | button | loading | UI copy |  |
| 468 | New password | status | Saving your new password… | status (a11y / live) | loading | UI copy |  |
| 469 | New password | (page) | Onrace — New password (wireframe) | a11y label | base | wireframe annotation | P1 |
| 470 | New password | new password form | New password | field label | base | UI copy |  |
| 471 | New password | new password form | At least 8 characters. | helper text | base | UI copy |  |
| 472 | New password | new password form | Confirm new password | field label | base | UI copy |  |
| 473 | New password | new password form | Save new password | button | base | UI copy |  |
| 474 | Profile | (page) | Onrace — Profile, error state (wireframe) | a11y label | error | wireframe annotation | T5 P1 |
| 475 | Profile | large title | Profile | heading | error (state=error); loading (state=loading); base | UI copy | T5 |
| 476 | Profile | load error | Profile | a11y label | error (state=error) | UI copy | T5 |
| 477 | Profile | load error | Couldn't load your profile | heading | error (state=error) | UI copy | T5 |
| 478 | Profile | load error | Check your connection and try again. Your account and results haven't changed. | state message | error (state=error) | UI copy | T5 |
| 479 | Profile | load error | Try again | button | error (state=error) | UI copy |  |
| 480 | Profile | identity | Maya Rossi | heading | error (state=error); base | user-written |  |
| 481 | Profile | identity | maya.rossi@example.com | body text | error (state=error); base | user-written |  |
| 482 | Profile | account fields | Account | heading | error (state=error); base | UI copy | T5 |
| 483 | Profile | account fields | Name | field label | error (state=error); base | UI copy |  |
| 484 | Profile | account fields | Maya Rossi | field value (prefilled) | error (state=error); base | user-written |  |
| 485 | Profile | account fields | Saving… | helper text | error (state=error); base | UI copy |  |
| 486 | Profile | account fields | Saved | helper text | error (state=error); base | UI copy |  |
| 487 | Profile | account fields | Try again | link | error (state=error) | UI copy |  |
| 488 | Profile | account fields | Couldn't save — back to Maya Rossi. | state message | error (state=error) | UI copy + user data |  |
| 489 | Profile | account fields | Country | field label | error (state=error); base | UI copy |  |
| 490 | Profile | account fields | Australia | option | error (state=error); base | reference data (option list) |  |
| 491 | Profile | account fields | Brazil | option | error (state=error); base | reference data (option list) |  |
| 492 | Profile | account fields | Canada | option | error (state=error); base | reference data (option list) |  |
| 493 | Profile | account fields | France | option | error (state=error); base | reference data (option list) |  |
| 494 | Profile | account fields | Germany | option | error (state=error); base | reference data (option list) |  |
| 495 | Profile | account fields | Italy | option | error (state=error); base | reference data (option list) |  |
| 496 | Profile | account fields | Japan | option | error (state=error); base | reference data (option list) |  |
| 497 | Profile | account fields | Netherlands | option | error (state=error); base | reference data (option list) |  |
| 498 | Profile | account fields | Spain | option | error (state=error); base | reference data (option list) |  |
| 499 | Profile | account fields | United Arab Emirates | option | error (state=error); base | reference data (option list) |  |
| 500 | Profile | account fields | United Kingdom | option | error (state=error); base | reference data (option list) |  |
| 501 | Profile | account fields | United States | option | error (state=error); base | reference data (option list) |  |
| 502 | Profile | account fields | Couldn't save — back to Italy. | state message | error (state=error) | UI copy |  |
| 503 | Profile | account fields | Language | field label | error (state=error); base | UI copy |  |
| 504 | Profile | account fields | Deutsch | option | error (state=error); base | reference data (option list) |  |
| 505 | Profile | account fields | English | option | error (state=error); base | reference data (option list) |  |
| 506 | Profile | account fields | Español | option | error (state=error); base | reference data (option list) |  |
| 507 | Profile | account fields | Français | option | error (state=error); base | reference data (option list) |  |
| 508 | Profile | account fields | Italiano | option | error (state=error); base | reference data (option list) |  |
| 509 | Profile | account fields | Couldn't save — back to English. | state message | error (state=error) | UI copy |  |
| 510 | Profile | account fields | Email | field label | error (state=error); base | UI copy |  |
| 511 | Profile | account fields | maya.rossi@example.com | body text | error (state=error); base | user-written |  |
| 512 | Profile | account fields | Changes save as you make them. Email comes from sign-in. | helper text | error (state=error); base | UI copy |  |
| 513 | Profile | sign out | Sign out | a11y label | error (state=error); base | UI copy |  |
| 514 | Profile | sign out | Sign out | button | error (state=error); base | UI copy |  |
| 515 | Profile | sign out | MR | body text | error (state=error) | user-written |  |
| 516 | Profile | sign-out confirm | Sign out of Onrace? | heading | error (state=error); base | UI copy |  |
| 517 | Profile | sign-out confirm | Your results stay saved. Sign back in anytime to see them. | state message | error (state=error); base | UI copy |  |
| 518 | Profile | sign-out confirm | Cancel | button | error (state=error); base | UI copy | A3 |
| 519 | Profile | sign-out confirm | Sign out | button | error (state=error); base | UI copy |  |
| 520 | Profile | global nav | Global navigation | a11y label | error (state=error); loading (state=loading); base | UI copy |  |
| 521 | Profile | global nav | Discover | tab label | error (state=error); loading (state=loading); base | UI copy |  |
| 522 | Profile | global nav | My Results | tab label | error (state=error); loading (state=loading); base | UI copy | T1 |
| 523 | Profile | global nav | Profile | tab label | error (state=error); loading (state=loading); base | UI copy | T5 |
| 524 | Profile | (page) | Onrace — Profile, loading state (wireframe) | a11y label | loading | wireframe annotation | T5 P1 |
| 525 | Profile | loading state | Loading your profile… | status (a11y / live) | loading (state=loading) | UI copy | T5 |
| 526 | Profile | (page) | Onrace — Profile (wireframe) | a11y label | base | wireframe annotation | T5 P1 |
| 527 | Profile | identity | MR | text | base | user-written |  |

*527 rows. 291 are ours (UI copy, some around a value we don't write); the rest are catalog data, reference data, user-written text or wireframe annotations.*
