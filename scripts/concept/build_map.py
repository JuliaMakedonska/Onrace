"""Static Map background for Race browse (designer decision, concept.md → Map).

Projects Natural Earth 1:110m land and country borders (public domain,
naturalearthdata.com; GeoJSON from github.com/nvkelso/natural-earth-vector)
with Mercator, the whole world from 84°N to 60°S (framed by CSS: static-map.css), into two SVG masks:
land fill, and coastlines + borders as hairlines. Colors come from the map roles
in design-system/tokens/tokens.css (the masks only carry shape). Also writes each race pin's
position from its real latitude/longitude. Output goes between the map markers in
design-system/map-data.css (linked only by the Race browse pages and the showcase, design-system/docs/index.html).

Usage, from the repo root:  python3 scripts/concept/build_map.py
"""
import json, math, os, re, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
NE = os.path.join(HERE, 'naturalearth')

# The mask (Lesson 10 step 6 layout pass, 2026-11-18): the whole world's longitudes, from 84°N down to 60°S (Mercator
# grows without end towards the poles; below 60°S is ocean on this map), so any frame of any pane is filled with map.
# Until then it was cropped to lon -110..25, centred on 43°N, the phone's crop, and a wide pane stretched that crop.
LON_MIN, LON_MAX = -180.0, 180.0
LAT_TOP, LAT_BOTTOM = 84.0, -60.0
W = 1000.0                                   # viewBox width
def merc_y(lat):
    lat = max(min(lat, 85.0), -85.0)
    return math.log(math.tan(math.pi / 4 + math.radians(lat) / 2))
X_SPAN = math.radians(LON_MAX - LON_MIN)
Y_TOP, Y_BOTTOM = merc_y(LAT_TOP), merc_y(LAT_BOTTOM)
H = W * (Y_TOP - Y_BOTTOM) / X_SPAN           # viewBox height
RATIO = H / W                                 # map height = map width × RATIO
def project(lon, lat):
    x = (math.radians(lon - LON_MIN)) / X_SPAN * W
    y = (Y_TOP - merc_y(lat)) / (Y_TOP - Y_BOTTOM) * H
    return x, y
# Two frames, each a box on the map that a map view shows whole, centred, scaled to fit (static-map.css):
# the phone's: the crop the phone has always drawn (lon -110..25 across the screen's width, centred on 43°N), so a phone
# doesn't change; the wide one (a map pane from --bp-tablet): the box round the pins, widened by a margin so the
# continents that hold them show whole (North America from its west coast, Europe to the Black Sea), never cut at a pin.
PHONE = (-110.0, 25.0, 43.0)                   # lon from, lon to, centre latitude
FIT_MARGIN_LON, FIT_MARGIN_LAT = 28.0, 12.0
def in_view(points):
    xs = [p[0] for p in points]; ys = [p[1] for p in points]
    return max(xs) >= -50 and min(xs) <= W + 50 and max(ys) >= -50 and min(ys) <= H + 50

def path_d(rings, close):
    out = []
    for ring in rings:
        pts = [project(lon, lat) for lon, lat in ring]
        if len(pts) < 2 or not in_view(pts):
            continue
        out.append('M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in pts) + ('Z' if close else ''))
    return ''.join(out)

def rings_of(geom):
    t, c = geom['type'], geom['coordinates']
    if t == 'Polygon': return c
    if t == 'MultiPolygon': return [r for poly in c for r in poly]
    if t == 'LineString': return [c]
    if t == 'MultiLineString': return c
    return []

land = json.load(open(os.path.join(NE, 'ne_110m_land.geojson')))
borders = json.load(open(os.path.join(NE, 'ne_110m_admin_0_boundary_lines_land.geojson')))
land_d = path_d([r for f in land['features'] for r in rings_of(f['geometry'])], close=True)
coast_d = land_d
border_d = path_d([r for f in borders['features'] for r in rings_of(f['geometry'])], close=False)

vb = f'0 0 {W:.0f} {H:.1f}'
STROKE = 2.4 * (PHONE[1] - PHONE[0]) / (LON_MAX - LON_MIN)   # the hairline the phone has always drawn (2.4 units of the old 135° crop), in units of the whole world's width
svg_land = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}"><path fill="#000" fill-rule="evenodd" d="{land_d}"/></svg>'
svg_lines = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}"><g fill="none" stroke="#000" stroke-width="{STROKE:.2f}" stroke-linejoin="round">'
             f'<path d="{coast_d}"/><path d="{border_d}"/></g></svg>')
uri = lambda svg: 'url("data:image/svg+xml,' + urllib.parse.quote(svg, safe=' =:/,.-') + '")'

# Race pins: real coordinates (city centres; venue for Killington and Chamonix)
PINS = [('berlin-marathon', 'Berlin', 52.520, 13.405), ('hyrox-london', 'London', 51.507, -0.128),
        ('utmb', 'Chamonix', 45.924, 6.869), ('hyrox-dallas', 'Dallas', 32.777, -96.797),
        ('deka-strong-chicago', 'Chicago', 41.878, -87.630), ('spartan-beast-killington', 'Killington', 43.620, -72.814),
        ('boston-marathon', 'Boston', 42.360, -71.059)]
lats = [p[2] for p in PINS]; lons = [p[3] for p in PINS]
fx0, fy1 = project(min(lons) - FIT_MARGIN_LON, min(lats) - FIT_MARGIN_LAT)
fx1, fy0 = project(max(lons) + FIT_MARGIN_LON, max(lats) + FIT_MARGIN_LAT)
px0, _ = project(PHONE[0], PHONE[2]); px1, pcy = project(PHONE[1], PHONE[2])
frames = [
    f'  --map-phone-fw: {(px1 - px0) / W:.5f};  --map-phone-cx: {(px0 + px1) / 2 / W:.5f};  --map-phone-cy: {pcy / H:.5f};   /* the phone frame: lon {PHONE[0]:g}..{PHONE[1]:g} across the width, centred on {PHONE[2]:g}°N */',
    f'  --map-fit-fw: {(fx1 - fx0) / W:.5f};  --map-fit-fh: {(fy1 - fy0) / W:.5f};  --map-fit-cx: {(fx0 + fx1) / 2 / W:.5f};  --map-fit-cy: {(fy0 + fy1) / 2 / H:.5f};   /* the wide frame: the pins, lon {min(lons) - FIT_MARGIN_LON:.0f}..{max(lons) + FIT_MARGIN_LON:.0f}, lat {min(lats) - FIT_MARGIN_LAT:.0f}..{max(lats) + FIT_MARGIN_LAT:.0f} (fw, fh in map widths; cx, cy fractions of the map) */']
pin_lines = []
for slug, city, lat, lon in PINS:
    x, y = project(lon, lat)
    pin_lines.append(f'  --pin-{slug}-xf: {x / W:.5f};  --pin-{slug}-yf: {y / H:.4f};   /* {city} {lat:.3f}, {lon:.3f} */')

block = '\n'.join([
    '  /* map:start (generated by scripts/concept/build_map.py; do not edit by hand) */',
    f'  /* Natural Earth 1:110m land and admin-0 borders, public domain. Mercator, lon {LON_MIN:g}..{LON_MAX:g}, {LAT_TOP:g}°N to {-LAT_BOTTOM:g}°S. */',
    f'  --map-ratio: {RATIO:.5f};   /* map height ÷ map width */',
    *frames,
    f'  --map-land-mask: {uri(svg_land)};',
    f'  --map-lines-mask: {uri(svg_lines)};',
    *pin_lines,
    '  /* map:end */'])

p = os.path.join(ROOT, 'design-system/map-data.css')
t = open(p).read()
assert '/* map:start' in t
t = re.sub(r'  /\* map:start.*?/\* map:end \*/', lambda m: block, t, flags=re.S)
open(p, 'w').write(t)
print(f'map: viewBox {vb}, ratio {RATIO:.4f}, land {len(land_d) // 1024} KB, borders {len(border_d) // 1024} KB')
for slug, city, lat, lon in PINS:
    x, y = project(lon, lat)
    print(f'  {city:11s} xf {x / W:.4f}  yf {y / H:.4f}')
