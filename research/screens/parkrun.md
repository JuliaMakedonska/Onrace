# Parkrun — access restricted

Attempted via Playwright MCP and WebFetch, 2026-09-02, on both `parkrun.com` and `parkrun.org.uk`: both returned an HTTP 405 "Human Verification" bot-check page (`parkrun-blocked.png`) instead of any site content. WebFetch hit the same wall (405, no body). No attempt was made to bypass the bot check.

**Result: access restricted — no material gathered this session.** Everything below is general public knowledge already implied by the original audit's one-line description, not verified against the live site this pass, and should be treated as **data not confirmed** until a real visit succeeds:
- Free, weekly, volunteer-run timed 5K events at 2,000+ locations across ~23 countries.
- Results are generated from a barcode/token scan at the finish (timing-system-generated, not self-reported) and published to a permanent personal results history page.
- No paid tier is publicly known to exist; the organization is funded via sponsorship and event-host partnerships rather than athlete subscriptions.

**Relevance to Onrace:** the original audit used Parkrun as the ASPIRATIONAL benchmark for "how clean and low-friction a personal result/history page can be." That framing still stands as a design goal, but none of the specifics above were re-confirmed this session — flag before citing any of them as fact in a future pass, and retry the live site (or try again later, since bot walls can be temporary/IP-dependent) if firmer sourcing is needed.
