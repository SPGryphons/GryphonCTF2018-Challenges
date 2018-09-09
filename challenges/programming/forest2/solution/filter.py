import numpy as np
import cv2
import os

IMG_STORE_PATH = ".." + os.sep + "distrib" + os.sep + "images"
PROCESSED_IMG_LOC = "processed"

if __name__ == "__main__":
    imgDir = os.listdir(IMG_STORE_PATH)

    if not os.path.exists(PROCESSED_IMG_LOC):
        os.mkdir(PROCESSED_IMG_LOC)

    for img in imgDir:
        imgPath = os.path.join(IMG_STORE_PATH, img)
        image = cv2.imread(imgPath)
        image[np.where((image != [0, 0, 0]).all(axis = 2))] = [255, 255, 255]
        saveLoc = os.path.join(PROCESSED_IMG_LOC, img)
        cv2.imwrite(saveLoc, image)
