
import os
from PIL import Image, ImageDraw, ImageFilter

# مجلد الحفظ
output_dir = "generated_store_assets"
os.makedirs(output_dir, exist_ok=True)

def create_gradient(width, height, start_color, end_color):
    """توليد خلفية بتدرج لوني عصري"""
    base = Image.new('RGBA', (width, height), start_color)
    top = Image.new('RGBA', (width, height), end_color)
    mask = Image.new('L', (width, height))
    mask_data = [int(255 * (y / height)) for y in range(height) for _ in range(width)]
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

def draw_logo(draw, cx, cy, size):
    """رسم شعار احترافي رمزي للتطبيق"""
    r = size // 2
    # دائرة مضيئة
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 140, 0, 230))
    # رمز الأجواء والموقد
    draw.polygon([(cx, cy - r//2), (cx - r//2, cy + r//2), (cx + r//2, cy + r//2)], fill=(255, 255, 255, 250))

# 1. إعداد القياسات المطلوبة لـ Tablet و Fire TV (حسب الشروط exact)
assets_config = [
    ("icon_512.png", 512, 512, True),           # Tablet App Icon
    ("icon_114.png", 114, 114, True),           # Small Icon
    ("promo_1024x500.png", 1024, 500, False),     # Promotional Image
    ("firetv_icon_1280x720.png", 1280, 720, False), # FireTV App Icon
    ("firetv_bg_1920x1080.jpg", 1920, 1080, False), # FireTV Background
    ("featured_logo_640x260.png", 640, 260, True),  # Featured Content Logo
    ("featured_bg_1920x720.jpg", 1920, 720, False)   # Featured Content Background
]

for name, w, h, trans in assets_config:
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0)) if trans else create_gradient(w, h, (15, 23, 42, 255), (88, 28, 135, 255))
    draw = ImageDraw.Draw(img)
    draw_logo(draw, w // 2, h // 2, min(w, h) // 3)
    if name.endswith(".jpg"):
        img = img.convert("RGB")
    img.save(os.path.join(output_dir, name))

# 2. إنشاء 4 سكرينات موك آب (Screenshots) عصرية بدقة 1920x1080
scenes = [
    ("Cozy Cabin Fireplace", (239, 68, 68)),
    ("Deep Space Galaxy", (99, 102, 241)),
    ("Gentle Rain & Thunder", (14, 165, 233)),
    ("Relaxing Forest Stream", (34, 197, 94))
]

for i, (title, accent_color) in enumerate(scenes, 1):
    shot = create_gradient(1920, 1080, (10, 15, 29, 255), (30, 41, 59, 255))
    draw = ImageDraw.Draw(shot)
    
    # إطار الموك آب للشاشة
    draw.rounded_rectangle([120, 120, 1800, 960], radius=24, fill=(15, 23, 42, 230), outline=accent_color, width=4)
    draw_logo(draw, 960, 500, 160)
    
    shot_rgb = shot.convert("RGB")
    # حفظ النسخ لكل من التابلت و Fire TV
    shot_rgb.save(os.path.join(output_dir, f"screenshot_tablet_{i}.png"))
    shot_rgb.save(os.path.join(output_dir, f"screenshot_firetv_{i}.png"))

print("✅ Complete: Generated all Amazon Appstore assets successfully!")
