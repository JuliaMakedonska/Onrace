# Strava — Events tab — access confirmed restricted

Attempted via Playwright MCP browser automation, 2026-09-02: navigating directly to `strava.com/events` **redirects to the logged-out marketing homepage** (`strava-home.png`) rather than showing any event content. This confirms — with an actual browser now available, not just an inference from missing tooling — that the Events tab genuinely requires an authenticated session and isn't reachable by URL alone; it lives inside the app under Groups → Events per prior WebSearch findings in `../research.md`.

**Visual observation from the homepage that did load**: top nav is Activities / Features / Maps / Challenges / Subscription — no "Events" entry in the public nav at all, reinforcing that Events is app-only/account-gated, not a discoverable public web section the way ocrbase's or AllTrails' map is.

**To capture later**: Events tab race list/filter UI, race detail card — requires a logged-in Strava mobile session (out of reach for this research pass; would need a real test account).
