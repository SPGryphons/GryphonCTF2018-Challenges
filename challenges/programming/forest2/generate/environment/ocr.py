from PIL import Image
import numpy as np
import pytesseract as pyt
import cv2
import os

# images are only valid if they do not show any text
# when parsed with the OCR library we are using - Tesseract
def image_valid(image):
    # load image as numpy array
    image_nparr = np.fromstring(image, np.uint8)
    image_cv = cv2.imdecode(image_nparr, 1)

    # replace all non-bloack pixels with the color white
    image_cv[np.where((image_cv != [0,0,0]).all(axis = 2))] = [255, 255, 255]
    text_found = pyt.image_to_string(image_cv).strip()

    return text_found
