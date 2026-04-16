from PIL import Image, ImageFilter

def add_shadow(pil_img):
    if pil_img.mode != "RGBA":
        pil_img = pil_img.convert("RGBA")

    # create shadow
    shadow = pil_img.copy()

    # lighter shadow
    shadow = shadow.point(lambda p: p * 0.1)

    # soft blur
    shadow = shadow.filter(ImageFilter.GaussianBlur(9))

    # background bigger
    bg = Image.new("RGBA", (pil_img.width + 30, pil_img.height + 30), (255, 255, 255, 255))

    # shadow offset
    bg.paste(shadow, (12, 12), shadow)

    # original image
    bg.paste(pil_img, (0, 0), pil_img)

    return bg.convert("RGB")