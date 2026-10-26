# Key decisions, in plain words

The cards at the top of the lesson overviews (`public/concept-overview.html`, `public/ui-overview.html`), read by `scripts/build_concept_overview.py` and `scripts/build_ui_overview.py`. Each summary is written for the card in one or two plain lines, and says no more than its record does; the record is the source and wins if they ever differ. The full register of each lesson stays on its page, folded, quoted from the records.

| Lesson | Decision | Summary | Date | Record |
|---|---|---|---|---|
| 06 | Podium, the chosen direction | Of three directions, Podium won: the clearest hierarchy, a scarce accent (once or twice per screen) and black-and-white photos. | 2026-10-13 | concept/concept.md#directions-step-3-chosen-2026-10-13 |
| 06 | Dark theme | Onrace is dark because the designer chose it, not because the brief or the artifact pages happen to be dark. | 2026-10-13 | concept/concept.md#designers-taste |
| 06 | The accent is scarce | Amber appears at most once or twice per screen, on the one thing that matters most: the main action or the active state. | 2026-10-13 | concept/concept.md#hierarchy-rules-designer |
| 06 | Where the accent goes | Amber only where you can act or where you are, never on a result, a finish time, a count or a status. The build checks this. | 2026-10-13 | concept/concept.md#color-rules-designer-2026-10-13 |
| 06 | No success color on results | Results are self-reported and Onrace can't verify them, so nothing marks them as verified: no green, no check mark, no "verified". | 2026-10-13 | concept/concept.md#color-rules-designer-2026-10-13 |
| 06 | A 3:1 photo band | Race photos sit in a short 3:1 band, so two full race cards fit on the first screen. | 2026-10-14 | concept/concept.md#race-card-anatomy-decided-by-the-designer-2026-10-13 |
| 06 | Uppercase format chips | Format chips look uppercase through CSS only; the markup keeps each format's real name, as the voice rules require. | 2026-10-13 | concept/concept.md#where-data-and-taste-pull-apart-decided-2026-10-13 |
| 07 | Native iOS | Anything iOS has a standard for (bars, sheets, search, 44pt targets) follows Apple's Human Interface Guidelines; Podium sets only the look. | 2026-10-18 | concept/concept.md#native-ios-designer-rule-2026-10-18 |
| 07 | Liquid Glass (C1) | Bars and the Filters sheet are translucent graphite with blur, as in iOS 26; cards and content stay flat. The glass values are still provisional. | 2026-10-18 | DESIGN.md#native-ios |
| 07 | Solar Linear for small glyphs | Back, chevrons, disclosure and the search magnifier use Solar's thin Linear style, as iOS thins small symbols; every other icon stays Bold. | 2026-10-25 | concept/concept.md#step-6-critique-fixes-designer-priorities-2026-10-25 |
| 07 | Our own race photos | Race cards show Onrace's own black-and-white photos, generated, checked for text and logos and retouched, instead of stock photos. | 2026-10-20 | visuals/README.md |
| 07 | The frozen wireframe snapshot | The Lesson 5 wireframes stay frozen in `wireframes/_wireframe/`; the viewer switches any screen between them and the current design. | 2026-10-18 | CLAUDE.md#wireframes |
| 07 | The finish time leads Result detail | On Result detail the finish time is the largest thing on the screen; the race name steps down to a normal heading above it. | 2026-10-25 | concept/concept.md#step-6-critique-fixes-designer-priorities-2026-10-25 |
| 07 | The "keep it" rule | A visual change the designer keeps goes into the kit and its showcase, its reason into `DESIGN.md`, and onto every screen that uses it. | 2026-10-25 | CLAUDE.md#ui-assembly |
