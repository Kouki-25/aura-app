import os
from PIL import Image, ImageDraw

output_dir = "generated_store_assets"
os.makedirs(output_dir, exist_ok=True)

def create_gradient(width, height, start_color, end_color):
    base = Image.new('RGBA', (width, height), start_color)
    top = Image.new('RGBA', (width, height), end_color)
    mask = Image.new('L', (width, height))
    mask_data = [int(255 * (y / height)) for y in range(height) for _ in range(width)]
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

def draw_logo(draw, cx, cy, size):
    r = size // 2
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 140, 0, 230))
    draw.polygon([(cx, cy - r//2), (cx - r//2, cy + r//2), (cx + r//2, cy + r//2)], fill=(255, 255, 255, 250))

assets = [
    ("icon_512.png", 512, 512, True),
    ("icon_114.png", 114, 114, True),
    ("promo_1024x500.png", 1024, 500, False),
    ("firetv_icon_1280x720.png", 1280, 720, False),
    ("firetv_bg_1920x1080.jpg", 1920, 1080, False),
    ("featured_logo_640x260.png", 640, 260, True),
    ("featured_bg_1920x720.jpg", 1920, 720, False)
]

for name, w, h, trans in assets:
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0)) if trans else create_gradient(w, h, (15, 23, 42, 255), (88, 28, 135, 255))
    draw = ImageDraw.Draw(img)
    draw_logo(draw, w // 2, h // 2, min(w, h) // 3)
    if name.endswith(".jpg"):
        img = img.convert("RGB")
    img.save(os.path.join(output_dir, name))

scenes = [
    ("Cozy Cabin Fireplace", (239, 68, 68)),
    ("Deep Space Galaxy", (99, 102, 241)),
    ("Gentle Rain Sound", (14, 165, 233)),
    ("Relaxing Nature", (34, 197, 94))
]

for i, (title, color) in enumerate(scenes, 1):
    shot = create_gradient(1920, 1080, (10, 15, 29, 255), (30, 41, 59, 255))
    draw = ImageDraw.Draw(shot)
    draw.rounded_rectangle([120, 120, 1800, 960], radius=24, fill=(15, 23, 42, 230), outline=color, width=4)
    draw_logo(draw, 960, 500, 160)
    shot_rgb = shot.convert("RGB")
    shot_rgb.save(os.path.join(output_dir, f"screenshot_tablet_{i}.png"))
    shot_rgb.save(os.path.join(output_dir, f"screenshot_firetv_{i}.png"))

print("✅ Finished!")
