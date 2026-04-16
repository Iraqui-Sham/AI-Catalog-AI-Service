from PIL import Image

def add_white_bg(pil_img):
    if pil_img.mode != "RGBA":
        pil_img = pil_img.convert("RGBA")

    white_bg = Image.new("RGBA", pil_img.size, (235, 235, 235))

    combined = Image.alpha_composite(white_bg, pil_img)

    return combined.convert("RGB")