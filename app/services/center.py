from PIL import Image

def center_image(pil_img):
    # original size
    w, h = pil_img.size

    # add padding (important)
    new_w = int(w * 1.3)
    new_h = int(h * 1.3)

    # white background
    bg = Image.new("RGB", (new_w, new_h), (255, 255, 255))

    # center position
    x = (new_w - w) // 2
    y = (new_h - h) // 2

    bg.paste(pil_img, (x, y))

    return bg