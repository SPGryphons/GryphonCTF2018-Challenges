from PIL import Image
import os
import re

IMG_STORE_PATH = ".." + os.sep + ".." + os.sep + "distrib" + os.sep + "images"
PROCESSED_IMG_LOC = IMG_STORE_PATH + os.sep + "resized"

def resize(imgPath, savePath):
    image = Image.open(imgPath)
    newWidth = 1280
    newHeight = (1280 / image.size[0]) * image.size[1]
    imgSize = (newWidth, int(newHeight))
    newImage = image.resize(imgSize, Image.ANTIALIAS)
    newImage.save(savePath, optimize=True)

if __name__ == "__main__":
    imgDir = os.listdir(IMG_STORE_PATH)

    if not os.path.exists(PROCESSED_IMG_LOC):
        os.mkdir(PROCESSED_IMG_LOC)

    count = 1
    for img in imgDir:
        print("Processing:", str(count))
        imgPath = os.path.join(IMG_STORE_PATH, img)
        savePath = os.path.join(PROCESSED_IMG_LOC, str(count) + ".jpg")

        if os.path.isdir(imgPath):
            continue

        resize(imgPath, savePath)
        count += 1
