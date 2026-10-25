# Visuals

Onrace's own race photos, replacing the Unsplash photos on the race cards (Lesson 7, step 4, 2026-10-20). They're generated illustrations of each format, not photos taken at the named race (`concept/references.md` → § 7).

- `visuals/`: images that passed the check. The screens link the **pre-cropped 3:1 sets** (`<scene>-684` and `<scene>-1026`, each as AVIF, WebP and JPEG; see Export below). The full 1200 × 800 JPEGs (quality 74) stay as the sources and for the history pages. `scripts/concept/build_stand.py` mirrors every `visuals/*.jpg`, `*.webp` and `*.avif` to `public/visuals/`.
- `visuals/incoming/`: new images waiting for the check, and the ones that failed it (kept here, never linked). Git-ignored. `visuals/incoming/work/` holds the retouch work files (sources, runs, masks, zooms) and the tools in `work/tool/`.

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
5. **If it fails on a few small marks: retouch locally** (since round 3, 2026-10-21), before regenerating:
   - choose the card's 3:1 crop and focus point first; marks outside the visible band need no retouching;
   - for each mark inside the band: mask it by hand (a small ellipse on the mark), fill the mask from the surrounding fabric or surface (OpenCV Telea inpainting), and add grain matched to the flat fabric around it, feathered at the edge (`visuals/incoming/work/tool/retouch.py`);
   - verify each patch by its pixel values before and after, not by eye alone, and re-check the whole band at full size afterwards;
   - build a before/after review page and get the designer's OK before any image goes on a card.
6. **If it passes:** compress (JPEG, longest side 1200, quality about 74) and save it in `visuals/` under its scene name. Then set its focus class on the card (`photo--low`, `--mid`, `--lower`, `--center` or `--high`, see `ui/kit.css`), and check the crop at 390 wide. If it fails, leave it in `incoming/` and regenerate.

ChatGPT names the downloads after its own title for the image (in the interface language). Rename each file to its scene name; the table below keeps the original names.

## Style block

Send this with every scene, verbatim:

> Black and white documentary sports photography, high contrast, deep blacks and bright highlights, fine film grain, natural light, shot with a 35mm lens from eye level or slightly above. Wide landscape format. The main action sits in the middle third of the frame vertically, with calm space above and below. Absolutely no text anywhere: no logos, no banners with print, no signs, no brand names, no numbers on race bibs. All clothing and equipment plain and unbranded: solid colors, no logos, no swooshes, no printed lettering; race bibs completely blank. Cities are a generic city with no recognizable landmarks or famous buildings.

The clothing sentence was added on 2026-10-21, after rounds 1 and 2: both rounds' failures were almost all clothing and shoe logos, which the "no text" line alone didn't prevent. Images generated before that date didn't have it.

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

## Round 2 (2026-10-21): targeted edits of the six rejected images

**The fixes.** The designer edited each rejected image in the same ChatGPT conversation, aiming at round 1's failures, with this edit prompt (verbatim):

> Edit this image. Remove every brand mark and every piece of text, wherever it is: logos and swooshes on clothing, shoes, caps and bags; numbers and text on race bibs (make the bibs completely blank); printed lettering on shirts, backs and sleeves; lettering and logos on equipment (bikes, rowers, sleds, barriers, banners). Replace each with plain fabric or a plain surface in the same tone. Keep everything else exactly the same: people, poses, composition, light, contrast, grain, black and white.

ChatGPT named the downloads after its own titles again (not the scene names), so the table maps them by content.

**Checked 2026-10-21**, the same way as round 1: each image at full size (1536 × 1024), with close crops of every person, shoe and piece of equipment. Positions are pixels in the 1536 × 1024 file (x, y).

| Scene | ChatGPT file name | Fixed since round 1 | Still fails, exactly where | Result |
|---|---|---|---|---|
| marathon-city-1 | `Марафон до Тріумфальної брами.png` | Bibs are blank | A swoosh on the front-left runner's white vest (190, 560); a swoosh on the leading woman's shorts (855, 720); a printed patch on a runner's shorts (1205, 665). Also shows the Brandenburg Gate and the Berlin TV tower (see below) | **Failed** |
| marathon-city-2 | `Монохромний марафон міською вулицею.png` | Bibs are blank | Swooshes on the right runner's white vest (1410, 495), on the dark vest beside him (1155, 500) and on his shorts (1165, 705); a logo on a cap (585, 405). Also shows Boston's skyline with the Prudential Tower (see below) | **Failed** |
| hyrox-sled-hall-1 | `Змагання на санях у арені.png` | The sports bra is plain | A small swoosh at the hem of the front athlete's shorts (670, 535) | **Failed** (the only mark) |
| hyrox-wallball-hall-1 | `Чорно-біле змагання з кросфіту.png` | The judge's back is plain | A swoosh on the kneeling judge's right shoe (515, 985) | **Failed** (the only clear mark) |
| deka-airbike-1 | `Напружений заїзд на аеробайках.png` | No lettering on the bikes; the athlete's top is plain | A swoosh stripe on the kneeling judge's shoe (213, 1014); small lettering on his sock cuff (258, 936) | **Failed** |
| ocr-wall-1 | `Брудний штурм дерев’яної перешкоди.png` | The racer's sports bra is plain | A faint swoosh-shaped mark on the man's T-shirt, left chest (1340, 450), about 10 px wide | **Failed** (borderline; the only mark) |

None passed, so no card changed in round 2. All six stay in `visuals/incoming/`.

**Real landmarks (not a check criterion, flagged for a decision).** The round-2 Berlin image shows the Brandenburg Gate and the Fernsehturm, and the Boston image shows the Prudential Tower skyline. The scene prompts don't ask for landmarks. A recognizable landmark makes a generated image read as a photo of that race, which `concept/references.md` § 7 says these aren't. If they're kept, the cards would show a generated Berlin as if it were the Berlin Marathon.
**Decided 2026-10-21 (designer):** the landmarks stay. They match each card's city. They're generated, not photographed at the race (`concept/references.md` → § 7). Checked for plausibility at full size: the gate has its six columns and the quadriga, the TV tower its sphere and mast, and the Boston skyline a tall tower and a domed building. None looks distorted. Future images use a generic city instead (the style block's last sentence).

## Round 3 (2026-10-21): local retouching, no new generation

The six round-2 images, retouched locally (the workflow's step 5). For each card, the 3:1 crop and focus point came first, so marks outside the visible band were left alone. Work files are in `visuals/incoming/work/` (sources under scene names in `src/`, the final run in `run8/`, card-ready JPEGs in `final/`). The review page is `visuals/review-round3.html`: before/after of every retouched spot and each final 3:1 crop.

| Scene | Card | Focus (band in the 1536 × 1024 file) | Retouched inside the band | Outside the band, left as is |
|---|---|---|---|---|
| marathon-city-1 | Berlin Marathon | `photo--lower`, 74% (y 379–891) | 16: swooshes on 7 vests and 5 pairs of shorts, logos on a white cap and a dark cap, a printed patch on shorts, a shoe swoosh | the landmarks (above the band) |
| marathon-city-2 | Boston Marathon | `photo--low`, 72% (y 369–881) | 18: swooshes on 4 vests and 5 pairs of shorts, lettering on a dark cap, a logo on a white cap, a mark on a waistband, a logo on a sock, a shoe swoosh (outline, fill and tail) | the skyline (above the band) |
| hyrox-sled-hall-1 | HYROX London | `photo--mid`, 60% (y 307–819) | 2: the swoosh on the front athlete's shorts, a stripe on her shoe | none |
| hyrox-wallball-hall-1 | HYROX Dallas | `photo--center`, 44% (y 225–737) | 1: a three-stripe panel on the second athlete's sports-bra band (found in round 3) | the judge's shoe swoosh (515, 985) |
| deka-airbike-1 | DEKA STRONG Chicago | new `photo--upper`, 18% (y 92–604) | none | the judge's shoe swoosh (213, 1014) and sock lettering (258, 936) |
| ocr-wall-1 | Spartan Race Beast — Killington | new `photo--upper`, 18% (y 92–604) | 1: the mark on the man's T-shirt chest | none |

**Status: approved by the designer (2026-10-21) and on their cards** (Race browse, `first-screen.html`, `ui/kit.html`, the stand). The full files still carry the marks outside their bands, so a different crop would need another pass.

## Export (step 7, 2026-10-25)

Each card photo is pre-cropped to its 3:1 band, so the screens download only what they show, and the marks outside the band that round 3 left unretouched are no longer in any file a screen loads.

- **Crop:** the full width of the 1200 × 800 source, a band 400 px tall at its focus (the band's top at `(800 − 400) × focus`):

| Scene | Card | Focus | Band (y) |
|---|---|---|---|
| marathon-city-1 | Berlin Marathon | 74% | 296–696 |
| hyrox-sled-hall-1 | HYROX London | 60% | 240–640 |
| hyrox-wallball-hall-1 | HYROX Dallas | 44% | 176–576 |
| deka-airbike-1 | DEKA STRONG Chicago | 18% | 72–472 |
| marathon-city-2 | Boston Marathon | 72% | 288–688 |
| ocr-wall-1 | Spartan Race Beast — Killington | 18% | 72–472 |
| trail-ultra-ridge-1 | UTMB | 72% | 288–688 |

These are the focus values the cards used before as `object-position` (`--photo-focus-*`); with the crop in the file, those tokens and the `.photo--*` classes are gone.

- **Sizes:** 1026 × 342 (3× the 342 px card band) and 684 × 228 (2×).
- **Formats:** AVIF (macOS `sips`, `formatOptions 60`, from a lossless PNG), WebP (quality 0.74) and JPEG (quality 0.78), the last two encoded by Chrome's canvas (`toDataURL`), drawn with `imageSmoothingQuality: high`. The script that made them: a headless Chrome run over the DevTools protocol, the same pattern as `scripts/check_overflow.mjs`.
- **Weight at 1026:** 24–67 KB AVIF, 24–64 KB WebP, 45–87 KB JPEG, against 116–236 KB for the full JPEGs.
- **Markup:** `<picture>` with an AVIF and a WebP `<source>`, then `<img class="photo" src="<scene>-1026.jpg" srcset="<scene>-684.jpg 684w, <scene>-1026.jpg 1026w" sizes="calc(100vw - 32px)" width="1026" height="342">`. The `picture` takes no box (`display: contents`). The black-and-white treatment stays in CSS (`--photo-filter`).
- **Loading:** on Race browse the first three cards load eagerly (the third is the first screen's largest image, `fetchpriority="high"`), the rest lazily. On Race detail only the shown race's photo loads: its sources wait in `data-*` until the page script picks the race.

