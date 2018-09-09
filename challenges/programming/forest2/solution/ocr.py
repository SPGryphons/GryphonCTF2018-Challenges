import pytesseract as ocr
import cv2
import os

IMG_STORE_PATH = "processed"

if __name__ == "__main__":
    imgDir = os.listdir(IMG_STORE_PATH)

    text = ""
    list = []
    for img in imgDir:
        print("Processing:", img)
        imgPath = os.path.join(IMG_STORE_PATH, img)
        image = cv2.imread(imgPath)
        found = ocr.image_to_string(image).strip()
        if found:
            list.append((img, found))
            text += found

    for img, textFound in list:
        print(img + ":", textFound)
    print(text)
