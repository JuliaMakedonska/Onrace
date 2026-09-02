# fitnessracingcalendar.com — screenshot captured

Captured via Playwright MCP, 2026-09-02: `fitnessracingcalendar-home.png` (full-page homepage, public, no login wall).

**Confirmed via page text:** tagline is "Find your next hybrid race. Every Hyrox, DEKA, Turf Games and functional fitness race in one place — compare events across the UK and US, with more countries coming soon." This is more precise than the earlier one-line description in the original audit ("DEKA-focused page seen") — the real scope is UK+US today, explicitly multi-format (HYROX, DEKA, Turf Games, functional fitness), not DEKA-only.

**Homepage structure:**
- A "Find my race" CTA with geolocation ("Allow location to find your nearest event").
- A "Looking beyond Hyrox" section positioning the site as an alternative-events finder for athletes who can't get a HYROX ticket.
- Filter bar: All Categories / All Countries / All Months / Sort by Date — plus a search box and a Year toggle (2026/2027) and Upcoming/Past toggle seen in filter chips.
- A flat list of event cards (not a map) — each shows event name, date, venue, distance/format tags (e.g. HYROX, DEKA FIT, DYNAMICS, Deadly Dozen, ATHX, GRYTR, Battle Cancer, Nuclear Fit, Wild Hybrid, Level Sevens, MacTuffit, Hybrid Games, Ultimate Athlete), a starting price ("From $207"), and a **"Book now" / "Sold out"** button.
- Footer CTA: "Want to get your race listed for free?" — free community/organizer submission, same self-service listing model as ocrbase.

**Not confirmed:** whether "Book now" hands off to the official registration page (link-out, like Onrace's planned model) or processes booking/payment in-house — not clicked through this pass, **data not confirmed**.

**Relevance to Onrace:** the real tagline confirms this is a closer direct competitor on the map/list-discovery half than the original one-line description suggested — multi-format, price-forward event cards, and a "Book now" CTA are all worth comparing against once Onrace's own race-card design is built.
