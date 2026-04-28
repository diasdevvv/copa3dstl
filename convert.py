import os
from PIL import Image

png_files = [f for f in os.listdir('.') if f.endswith('.png')]
for f in png_files:
    webp_name = f.replace(' ', '_').replace('.png', '.webp')
    try:
        img = Image.open(f)
        img.save(webp_name, 'webp')
        print(f"Converted {f} to {webp_name}")
    except Exception as e:
        print(f"Error converting {f}: {e}")
