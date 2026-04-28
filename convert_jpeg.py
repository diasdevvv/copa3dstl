import os
from PIL import Image

jpeg_files = [f for f in os.listdir('.') if f.endswith('.jpeg') or f.endswith('.jpg')]
for f in jpeg_files:
    webp_name = f.replace('.jpeg', '.webp').replace('.jpg', '.webp')
    try:
        img = Image.open(f)
        img.save(webp_name, 'webp')
        print(f"Converted {f} to {webp_name}")
    except Exception as e:
        print(f"Error converting {f}: {e}")
