import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

output_dir = "generated_store_assets"
os.makedirs(output_dir, exist_ok=True)

def create_glass_card(width, height, title, glow_color):
    # Base Gradient background (Dark Navy/Purple Aura Theme)
    base = Image.new('RGBA', (width, height), (15, 23, 42, 255))
    draw = ImageDraw.Draw(base)
    
    # Ambient Light Orbs
    glow = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(glow)
    g_draw.ellipse([width*0.2, height*0.1, width*0.8, height*0.7], fill=(glow_color[0], glow_color[1], glow_color[2], 120))
    glow = glow.filter(ImageFilter.GaussianBlur(radius=int(min(width, height)*0.15)))
    base = Image.alpha_composite(base, glow)
    
    draw = ImageDraw.Draw(base)
    
    # Clean Glass Card (No sidebar/menus)
    card_margin_x = int(width * 0.1)
    card_margin_y = int(height * 0.15)
    card_box = [card_margin_x, card_margin_y, width - card_margin_x, height - card_margin_y]
    
    draw.rounded_rectangle(card_box, radius=int(min(width, height)*0.05), fill=(30, 41, 59, 180), outline=(139, 92, 246, 200), width=4)
    
    # Center Player Ring (Glowing)
    cx, cy = width // 2, height // 2
    r = int(min(width, height) * 0.12)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(139, 92, 246, 220), outline=(236, 72, 153, 255), width=6)
    
    # Play Icon inside Ring
    pr = int(r * 0.4)
    draw.polygon([(cx - pr*0.5, cy - pr), (cx - pr*0.5, cy + pr), (cx + pr*0.8, cy)], fill=(255, 255, 255, 255))
    
    # Minimal Progress bar at bottom of card
    p_y = int(card_box[3] - height * 0.08)
    p_start = card_box[0] + int(width * 0.08)
    p_end = card_box[2] - int(width * 0.08)
    draw.rounded_rectangle([p_start, p_y, p_end, p_y + 8], radius=4, fill=(51, 65, 85, 255))
    draw.rounded_rectangle([p_start, p_y, p_start + int((p_end-p_start)*0.4), p_y + 8], radius=4, fill=(236, 72, 153, 255))
    
    return base.convert("RGB")

# Devices Resolutions (Clean Screens)
devices = [
    ("screenshot_phone_android.png", 1080, 1920, (239, 68, 68), "Cozy Fireplace"),    # Phone Android (Vertical)
    ("screenshot_phone_iphone.png", 1290, 2796, (14, 165, 233), "Gentle Rain"),      # iPhone (Vertical)
    ("screenshot_tablet.png", 2048, 1536, (124, 58, 237), "Deep Space"),            # Tablet (Horizontal)
    ("screenshot_firetv.png", 1920, 1080, (34, 197, 94), "Forest Nature")            # TV (Horizontal 16:9)
]

for filename, w, h, color, title in devices:
    img = create_glass_card(w, h, title, color)
    img.save(os.path.join(output_dir, filename))

# Standard Amazon Store Assets
basic_assets = [
    ("icon_512.png", 512, 512, (124, 58, 237)),
    ("icon_114.png", 114, 114, (124, 58, 237)),
    ("promo_1024x500.png", 1024, 500, (239, 68, 68)),
    ("firetv_icon_1280x720.png", 1280, 720, (14, 165, 233)),
    ("firetv_bg_1920x1080.jpg", 1920, 1080, (124, 58, 237)),
    ("featured_logo_640x260.png", 640, 260, (124, 58, 237)),
    ("featured_bg_1920x720.jpg", 1920, 720, (124, 58, 237))
]

for filename, w, h, color in basic_assets:
    img = create_glass_card(w, h, "Aura", color)
    img.save(os.path.join(output_dir, filename))

print("✅ All Device Screenshots Generated Successfully!")
