from rembg import remove
from PIL import Image
import io

def remove_background(image_bytes):
    output = remove(image_bytes)
    img = Image.open(io.BytesIO(output))

    # IMPORTANT: RGBA hi rehne do
    if img.mode != "RGBA":
        img = img.convert("RGBA")

    return img