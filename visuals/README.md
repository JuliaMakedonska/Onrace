# Visuals

Onrace's own race photos, replacing the Unsplash photos on the race cards (Lesson 7, step 4, 2026-10-20). They're generated illustrations of each format, not photos taken at the named race (`concept/references.md` → § 7).

- `visuals/`: images that passed the check, compressed for the web (JPEG, 1200 × 800, quality 74). The screens link them as `../visuals/<file>`; `scripts/concept/build_stand.py` mirrors every `visuals/*.jpg` to `public/visuals/`.
- `visuals/incoming/`: new images waiting for the check, and the ones that failed it (kept here, never linked).

## Tool

ChatGPT image generation, in the chat (not the API).

## Workflow

1. **One conversation for all images**, so the look stays consistent.
2. **Image 1 is the style reference.** Generate image 1 from the style block plus its scene; for every later image, send the style block plus the next scene and ask ChatGPT to match image 1's style.
3. **The fix for text.** When an image comes back with text, numbers or logos, reply in the same conversation: "Remove all text, numbers and logos, keep everything else the same".
4. **Check every image before it's used** (the step 4 check):
   - on topic for its format;
   - black and white;
   - no text, race numbers, logos or brand names, checked at full size, including small marks on clothing, shoes, bibs and equipment;
   - the crop works at 3:1 (the race card's photo band).
5. **If it passes:** compress (JPEG, longest side 1200, quality about 74) and save it in `visuals/` under its scene name. Then set its focus class on the card (`photo--low`, `--mid`, `--lower`, `--center` or `--high`, see `ui/kit.css`), and check the crop at 390 wide. If it fails, leave it in `incoming/` and regenerate.

ChatGPT names the downloads after its own title for the image (in the interface language). Rename each file to its scene name; the table below keeps the original names.

## Style block

Send this with every scene, verbatim:

> Black and white documentary sports photography, high contrast, deep blacks and bright highlights, fine film grain, natural light, shot with a 35mm lens from eye level or slightly above. Wide landscape format. The main action sits in the middle third of the frame vertically, with calm space above and below. Absolutely no text anywhere: no logos, no banners with print, no signs, no brand names, no numbers on race bibs.

## Scene prompts

Verbatim, in the order they were generated (image 1 first):

- **marathon-city-1** (Berlin Marathon): a wide avenue packed with runners mid-race, seen from slightly above, city buildings on both sides, morning light from the left.
- **marathon-city-2** (Boston Marathon): a tree-lined boulevard, a small group of runners in the foreground, the crowd behind, morning light from the left.
- **hyrox-sled-hall-1** (HYROX London): a huge exhibition hall, parallel lanes with athletes pushing weighted sleds, spectators behind barriers, overhead arena lighting.
- **hyrox-wallball-hall-1** (HYROX Dallas): an indoor fitness race hall, athletes in a row doing wall-ball throws, overhead arena lighting.
- **deka-airbike-1** (DEKA Strong Chicago): an athlete on an air bike in full effort, rowers behind, a judge nearby, overhead lighting.
- **ocr-wall-1** (Spartan Killington): a racer climbing a tall wooden wall, mud, forest behind, light from the left.
- **trail-ultra-ridge-1** (UTMB): a single runner on a rocky ridge trail, snow-capped peaks and a glacier behind.

## Files

Checked 2026-10-20, each at full size (1536 × 1024) with close crops of every figure.

| Scene prompt | ChatGPT file name | Result | File in use | Card |
|---|---|---|---|---|
| marathon-city-1 | `Марафон крізь монументальне місто.png` | **Failed:** race bibs with numbers on the mid-ground runners; swoosh logos on the front runners' tops and shorts | none | Berlin Marathon keeps its Unsplash photo |
| marathon-city-2 | `Ранкова гонка крізь тіні дерев.png` | **Failed:** two swoosh logos on the central runner's vest; bibs with numbers on the runners behind | none | Boston Marathon keeps its Unsplash photo |
| hyrox-sled-hall-1 | `Інтенсивні перегони на санях у промисловій арені.png` | **Failed:** a swoosh logo on the front athlete's sports bra | none | HYROX London keeps its Unsplash photo |
| hyrox-wallball-hall-1 | `Запекла арена_ кидки медболів.png` | **Failed:** printed lettering across the kneeling judge's back | none | HYROX Dallas keeps its Unsplash photo |
| deka-airbike-1 | `Напружене змагання на аеробайках.png` | **Failed:** lettering down the air bike's upright; a logo on the judge's shirt; a swoosh on the athlete's sports bra | none | DEKA STRONG Chicago keeps its Unsplash photo |
| ocr-wall-1 | `Мудрий прорив крізь перешкоду.png` | **Failed:** a swoosh logo on the racer's sports bra; a small chest logo on the man's shirt | none | Spartan Race Beast — Killington keeps its Unsplash photo |
| trail-ultra-ridge-1 | `Самотня бігунка серед альпійських вершин.png` | **Passed:** on topic, black and white, no text or logos, a clean 3:1 crop | `trail-ultra-ridge-1.jpg` | UTMB — Ultra-Trail du Mont-Blanc, `photo--low` (50% 72%): the runner centered in the band, the glacier behind |
