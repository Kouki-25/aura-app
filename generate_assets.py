import os
from PIL import Image, ImageDraw, ImageFont

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
    # Outer glow / circle
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(139, 92, 246, 230))
    # Inner wave / aura shape
    draw.ellipse([cx - r*0.6, cy - r*0.6, cx + r*0.6, cy + r*0.6], fill=(236, 72, 153, 240))
    draw.polygon([(cx, cy - r*0.4), (cx - r*0.35, cy + r*0.35), (cx + r*0.35, cy + r*0.35)], fill=(255, 255, 255, 250))

# 1. Generate Basic Assets
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

# 2. Generate Professional App Screenshots (UI Mockup)
scenes = [
    ("Cozy Fireplace Sound", (239, 68, 68), "FIREPLACE"),
    ("Deep Space Ambiance", (124, 58, 237), "GALAXY"),
    ("Gentle Rain & Thunder", (14, 165, 233), "RAIN"),
    ("Relaxing Forest Nature", (34, 197, 94), "NATURE")
]

for i, (title, color, scene_type) in enumerate(scenes, 1):
    # Main Background
    shot = create_gradient(1920, 1080, (10, 15, 30, 255), (20, 10, 40, 255))
    draw = ImageDraw.Draw(shot)
    
    # Header Bar
    draw.rectangle([0, 0, 1920, 120], fill=(15, 23, 42, 200))
    draw_logo(draw, 100, 60, 60)
    
    # Active Sound Banner / Center Card
    draw.rounded_rectangle([150, 180, 1100, 850], radius=30, fill=(30, 41, 59, 220), outline=color, width=4)
    
    # Draw Visual Art inside Card
    art_box = [200, 230, 1050, 650]
    draw.rounded_rectangle(art_box, radius=20, fill=(color[0]//3, color[1]//3, color[2]//3, 255))
    draw_logo(draw, 625, 440, 220)
    
    # Player Controls (Bottom)
    draw.rounded_rectangle([150, 880, 1770, 1020], radius=25, fill=(15, 23, 42, 240))
    # Progress bar
    draw.rounded_rectangle([200, 910, 1720, 920], radius=5, fill=(51, 65, 85, 255))
    draw.rounded_rectangle([200, 910, 800, 920], radius=5, fill=color)
    # Play / Pause Buttons
    draw.ellipse([930, 935, 990, 995], fill=color)
    draw.polygon([(952, 952), (952, 978), (975, 965)], fill=(255, 255, 255, 255))
    
    # Sidebar Grid (Other Sounds)
    sidebar_x = 1150
    for idx, (s_title, s_color, _) in enumerate(scenes):
        sy = 180 + idx * 160
        is_active = (idx == i - 1)
        bg_col = (45, 55, 72, 255) if is_active else (23, 32, 51, 200)
        draw.rounded_rectangle([sidebar_x, sy, 1770, sy + 140], radius=20, fill=bg_col, outline=s_color if is_active else None, width=3)
        draw.ellipse([sidebar_x + 30, sy + 35, sidebar_x + 100, sy + 105], fill=s_color)

    # Save PNGs
    shot_rgb = shot.convert("RGB")
    shot_rgb.save(os.path.join(output_dir, f"screenshot_tablet_{i}.png"))
    shot_rgb.save(os.path.join(output_dir, f"screenshot_firetv_{i}.png"))

print("✅ Professional screenshots generated successfully!")
