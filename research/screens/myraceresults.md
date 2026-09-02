# My Race Results — screenshot captured

Captured via Playwright MCP, 2026-09-02: `myraceresults-home.png` (full-page homepage, public, no login wall). Text below verified against the page's accessibility tree, not just the visual screenshot.

**Positioning:** "Your Race Diary — Never Lost. Find any race in 2 clicks, not 200 scrolls. A dedicated race-only app built for athletes who want their results at their fingertips." Light theme, hand-drawn/journal aesthetic (sticky-note graphics) — a deliberately different tone from the dark/bold HYROX-adjacent apps.

**FAQ, quoted exactly:**
- *"Can I add races that aren't in Athlinks?"* — "Yes! Unlike Athlinks, My Race Results lets you manually enter any race. You can type in the details, import a GPX file, or use our OCR feature to scan a screenshot of your results."
- *"How does the OCR screenshot import work?"* — "Simply take a screenshot of your race results (from an email, website, or app), upload it to My Race Results, and our AI will automatically extract your time, pace, placement, and other details. It takes about 30 seconds."
- *"Is My Race Results free?"* — "Yes! Our free tier includes unlimited race logging, basic search, timeline view, and PR tracking. Premium features like OCR import, interactive maps, and advanced analytics are available with a subscription."
- *"What's the difference between My Race Results and Strava?"* — "Strava is designed for tracking all your training activities. My Race Results is race-only—we focus on your official race results, chip times, and race-specific analytics without the clutter of daily training runs."

**Community stats shown on-page:** "0 Athletes · 0 Races Tracked · 0 Total Miles" — a live-looking counter reading zero across all three metrics, and the footer reads "© 2025 My Race Results" despite today being 2026-09-02. Concrete evidence of a very-early-stage or low-traction product, similar in kind to Athlinks' stale "(COMING SOON)" section found earlier — worth treating both as reminders that a polished landing page doesn't guarantee real usage.

**Relevance to Onrace:** trust model confirmed as pure self-report (manual entry, GPX import, or OCR scan) with **no required official source link and no auto-matching** — this is the clearest evidence yet that Onrace's mandatory-link requirement is genuinely uncommon even among products built specifically to solve "log your race results." The OCR-scan-a-screenshot pattern remains the single most-repeated friction-reduction idea across every results-archive competitor reviewed (also seen conceptually in RoxFit's results linking) and is worth prototyping for Onrace's result-entry flow even without adopting it at MVP.
