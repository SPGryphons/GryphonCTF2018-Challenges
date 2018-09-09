from PIL import Image
import numpy as np
import pytesseract as ocr
import cv2
import os

IMG_STORE_PATH = ".." + os.sep + ".." + os.sep + "distrib" + os.sep + "images"
IMG_PROCESSED_PATH = "processed"

if __name__ == "__main__":
    imgDir = os.listdir(IMG_STORE_PATH)

    if not os.path.exists(IMG_PROCESSED_PATH):
        os.makedirs(IMG_PROCESSED_PATH)

    text = ""
    pics = range(1, 1001)
    count = 303
    for img in pics:
        if img < count:
            continue

        print("Processing:", img)
        imgPath = os.path.join(IMG_STORE_PATH, str(img) + ".jpg")
        image = cv2.imread(imgPath)

        try:
            image[np.where((image != [0,0,0]).all(axis = 2))] = [255, 255, 255]
            savePath = os.path.join(IMG_PROCESSED_PATH, "test.jpg")
            cv2.imwrite(savePath, image)
            text += ocr.image_to_string(image).strip()
        except AttributeError:
            continue

        if text:
            os.remove(imgPath)
            text = ""
