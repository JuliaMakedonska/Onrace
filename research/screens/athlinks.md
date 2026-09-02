# Athlinks — screenshot captured

Captured via Playwright MCP browser automation, 2026-09-02: `athlinks-home.png` (full-page homepage). Public homepage does render with a real browser — the earlier WebFetch-based pass reported "no usable content" because the page is client-rendered, not because it requires login; only the personal claimed-results history is actually account-gated.

**Visual observations:**
- Dark navy hero over a marathon-crowd photo: "All of Your Results in One Place" / "The pain you endured to cross the finish line is temporary. But your race results are forever. Claim, share and celebrate them here." — single search bar ("Results" dropdown + "Enter an athlete name") is the primary homepage action, i.e. **search-first, not browse-first** (no map, no event list on the homepage at all).
- Feature sections below the fold pair a photo with a headline+CTA: "Claim Results" (finish-line photo), "Connect With Friends and Rivals" (profile card showing "237 FOLLOWERS · 25 CHEERS" — explicit social layer, the opposite of Onrace's no-social-features MVP scope), "Athlinks Exclusive Events" (US map silhouette + "LIVE RESULTS" badge).
- **"What's Happening on Athlinks?" section is explicitly labeled "(COMING SOON)"** and the sample newsfeed cards inside it show a real but stale date — a 2017 Miami Marathon countdown — still live on the page today. This is a concrete, visible signal of an unmaintained/legacy product, stronger evidence than the earlier "dated UX" description inferred from text-only research.
- Footer credits "Powered by Life Time" and links to ChronoTrack — visually confirms the B2B-timing-company ownership structure noted in `../research.md`'s deep-dive table.

**To capture later**: race search/results list (public, but wasn't queried this pass), claimed-results personal history page (needs a logged-in account).
