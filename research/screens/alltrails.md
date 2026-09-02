# AllTrails — screenshots captured

Captured via Playwright MCP browser automation, 2026-09-02.

- `alltrails-home.png` — marketing homepage (not analyzed in depth; the `/explore` map is the relevant reference page).
- `alltrails-explore-map.png` — `/explore`, the public trail map/directory (no login wall, confirmed reachable). **This is the closest visual template found for unifying Onrace's map + personal log**, matching the hypothesis already recorded in `../research.md`'s ASPIRATIONAL section.

**Visual observations from the explore map:**
- **True split-pane layout**: collapsible left panel ("Explore trails", chevron to hide) shows a scrollable card list (photo carousel with dot indicators + heart/save icon, name, park/area, star rating, difficulty dot, distance, estimated time) synced live to whatever the right-hand map viewport currently shows — this is a stronger pattern than ocrbase's either/or List-vs-Map toggle.
- Filter bar sits above the map, not in a sidebar: All / Difficulty / Length / Elevation / Activity / Features, each a dropdown — horizontal, compact, doesn't compete for space with the results list.
- Map itself: Mapbox/OSM base, **numbered distance badges directly on pins** (e.g., "5.8 km", "9.5 km") rather than plain markers or count clusters — lets you gauge trail length before opening a card, a discovery-affordance ocrbase's map doesn't have.
- Right-side floating controls: a "Map layers" flyout (satellite/heatmap/trail-type layer swatches), 3D toggle, zoom, and a locate-me control — more layered/mature than ocrbase's plain zoom+fullscreen.
- Standard cookie/consent banner at the bottom with granular toggles (Targeted Advertising / Personalization / Analytics) — not core UX, but a compliance-pattern reference given Onrace is global from day one.

**Relevance to Onrace**: the split-pane list+map-in-sync (vs. ocrbase's toggle) is worth a real UX decision — a toggle is cheaper to build for MVP, split-pane is the more polished target if time allows. The pin-shows-distance affordance maps directly onto a race-map equivalent (e.g., pin shows date or days-until-race instead of km).

**To capture later**: the personal "Completed" activity log/map view — account-gated, not reached this pass.
