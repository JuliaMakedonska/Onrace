"""One scale for every shot on the review pages (2026-11-20, designer): a 390 shot and an 820 shot are drawn at the same
factor, so their sizes compare honestly. The shots are taken 1:1 (one CSS pixel, one image pixel; scripts/review_layout.mjs)
and shown at SCALE by their width and height attributes, never shrunk by the page: a row too wide for the window scrolls
sideways instead. Each shot links to its file at 1:1.
Older shots taken at another factor (0.75 at 390, 0.5 at 820 and 1440, until 2026-11-20) are drawn at SCALE all the same:
their size on the page comes from the device width, not from the file."""
import os, struct

SCALE = 0.5
LABEL = 'Scale: every shot 1:2 (half size), the same for every width, so sizes compare honestly: a 390 shot is 195 px wide here, an 820 shot 410, a 1440 shot 720. Open a shot to see it 1:1.'
CSS = '''  .rv-shots { overflow-x: auto; }
  .rv-shots figure { max-width: none; flex: none; }
  .rv-shots img { max-width: none; }
  .rv-scale { font-size: var(--size-proof); color: var(--text-secondary); }'''


def webp_size(path):
    """(width, height) of a WebP file, read from its header."""
    with open(path, 'rb') as f:
        b = f.read(30)
    kind = b[12:16]
    if kind == b'VP8 ':
        w, h = struct.unpack('<HH', b[26:30])
        return w & 0x3FFF, h & 0x3FFF
    if kind == b'VP8L':
        v = int.from_bytes(b[21:25], 'little')
        return (v & 0x3FFF) + 1, ((v >> 14) & 0x3FFF) + 1
    if kind == b'VP8X':
        return int.from_bytes(b[24:27], 'little') + 1, int.from_bytes(b[27:30], 'little') + 1
    raise ValueError(path)


def img(src, device_w, alt, root):
    """The shot at SCALE of the device width it was taken at, linked to the file at 1:1."""
    fw, fh = webp_size(os.path.join(root, src))
    w = round(device_w * SCALE)
    h = round(fh * w / fw)
    return f'<a href="{src}"><img src="{src}" width="{w}" height="{h}" alt="{alt}" loading="lazy"></a>'
