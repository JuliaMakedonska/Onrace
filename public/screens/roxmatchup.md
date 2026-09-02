# RoxMatchUp — App Store listing + web app (login-gated)

Captured via Playwright MCP, 2026-09-02: `roxmatchup-appstore.png` (App Store listing, primary source — no dedicated public marketing site was found via search) and `roxmatchup-home.png` (the product's own web app at `roxmatchup.bubbleapps.io`, which drops straight into a login screen — **access restricted**, no logged-out marketing content to capture there).

**From the App Store description (French, developer: Hugues Dormoy — an individual/small dev, not a company):**
- "RoxMatchUp est l'application dédiée aux athlètes et passionnés de sports hybrides (HYROX, hybrid races, fitness races)." Goal: connect practitioners, centralize events, structure the community.
- **Partner matching**: find training/competition partners via an in-app chat.
- **Event discovery**: browse upcoming HYROX/hybrid events, ticket-opening dates, formats/categories; organizers can list their races.
- **Classifieds**: post/search listings for HYROX Flex/Lyte tickets, spectator tickets, or a race/training partner — RoxMatchUp is explicitly only the intermediary; transactions happen privately outside the app.
- **Rankings**: rolling 1-year, ATP-style leaderboard based on the average of each athlete's top 2 performances per category — described as "transparent, fair, verified performances" (mechanism behind "verified" not specified — **data not confirmed**).
- **RoxCoins**: an internal currency to unlock a contact, get exclusive notifications, boost a listing's visibility, or add an event.
- Free with in-app purchases (RoxCoins), iPad-designed, category "Sport."

**Relevance to Onrace:** genuinely combines event discovery *and* partner-matching *and* a lightweight leaderboard in one small, single-developer app — more feature-complete than the one-line "centralizes/discovers HYROX + hybrid events" description in the original audit suggested. The RoxCoins micro-transaction model (pay to unlock a contact/boost a listing) is a monetization pattern not seen in any of the other 14 competitors reviewed — worth noting as a possible future direction if Onrace ever needs revenue beyond subscription/B2B.
