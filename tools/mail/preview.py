"""Maakt een mail-preview (1200px breed) van een concept in 3 stijlen. Gebruik: python3 preview.py <slug> <uit.png> [nl|en]"""
import sys
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw, ImageFont
slug, uit = sys.argv[1], sys.argv[2]; taal = sys.argv[3] if len(sys.argv) > 3 else "nl"
import os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
namen = ("Klassiek", "Modern", "Minimal") if taal == "nl" else ("Classic", "Modern", "Minimal")
shots = []
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1280, "height": 860}, device_scale_factor=1)
    for s in (1, 2, 3):
        pg.goto(f"file://{os.path.abspath(ROOT)}/src/concept/{slug}/index.html?stijl={s}"); pg.wait_for_timeout(500)
        pg.add_style_tag(content=".cbar,.wm,.stempel{display:none!important}")
        f = f"/tmp/prev-{slug}-{s}.png"; pg.screenshot(path=f, clip={"x": 0, "y": 0, "width": 1280, "height": 820}); shots.append(f)
    b.close()
W = 1200; pad = 28; gap = 18; cw = (W - 2 * pad - 2 * gap) // 3; ch = int(cw * 820 / 1280)
H = pad + 34 + ch + 28 + pad
img = Image.new("RGB", (W, H), "#0f1726"); d = ImageDraw.Draw(img)
def font(sz, bold=False):
    for f in (["/root/.fonts/Inter[opsz,wght].ttf"] if True else []):
        try:
            ft = ImageFont.truetype(f, sz)
            try: ft.set_variation_by_axes([14, 600 if bold else 400])
            except Exception: pass
            return ft
        except Exception: pass
    return ImageFont.load_default()
for i, f in enumerate(shots):
    x = pad + i * (cw + gap); y = pad + 34
    im = Image.open(f).convert("RGB").resize((cw, ch), Image.LANCZOS)
    m = Image.new("L", (cw, ch), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, cw, ch), 10, fill=255)
    img.paste(im, (x, y), m)
    d.text((x, pad + 4), f"{i+1}  {namen[i]}", fill="#f2b705", font=font(19, True))
d.text((pad, H - pad - 16), "collensgroup.com/concept/" + slug, fill="#8fa0b8", font=font(15))
img.save(uit, optimize=True); print(uit, img.size)
