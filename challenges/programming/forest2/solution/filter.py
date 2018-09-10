import numpy as np
import cv2
import os

IMAGE_SAVE_LOCATION = ".." + os.sep + "distrib" + os.sep + "images"
PROCESSED_SAVE_LOC = "processed"

if __name__ == "__main__":
    imgDir = os.listdir(IMAGE_SAVE_LOCATION)

    if not os.path.exists(PROCESSED_SAVE_LOC):
        os.mkdir(PROCESSED_SAVE_LOC)

    for img in imgDir:
        imgPath = os.path.join(IMAGE_SAVE_LOCATION, img)
        image = cv2.imread(imgPath)
        image[np.where((image != [0, 0, 0]).all(axis = 2))] = [255, 255, 255]
        saveLoc = os.path.join(PROCESSED_SAVE_LOC, img)
        cv2.imwrite(saveLoc, image)
