import cv2
import numpy as np
from PIL import Image

def enhance_image(pil_img):
    img = np.array(pil_img)

    # detail enhance
    img = cv2.detailEnhance(img, sigma_s=10, sigma_r=0.15)

    # brightness + contrast
    img = cv2.convertScaleAbs(img, alpha=1.2, beta=10)

    # sharpening
    kernel = np.array([[0, -1, 0],
                       [-1, 5,-1],
                       [0, -1, 0]])
    img = cv2.filter2D(img, -1, kernel)

    return Image.fromarray(img)