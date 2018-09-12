from threading import Thread
from threading import Lock
from queue import Queue
from PIL import Image
import numpy as np
import pytesseract as pyt
import cv2
import os
import sys

IMAGE_SAVE_LOCATION = ".." + os.sep + "distrib" + os.sep + "images"
PROCESSED_SAVE_LOC = "processed"
THREAD_COUNT = 10

class Worker(Thread):
    def __init__(self, queue, list, list_lock):
        Thread.__init__(self)
        self.queue = queue
        self.list = list
        self.list_lock = list_lock

    def run(self):
        while True:
            img_name = self.queue.get()
            print("Processing:", img_name)
            try:
                img_loc = os.path.join(IMAGE_SAVE_LOCATION, img_name)
                image = cv2.imread(img_loc)
                image[np.where((image != [0,0,0]).all(axis = 2))] = [255, 255, 255]
                image_filename = os.path.join(PROCESSED_SAVE_LOC, img_name)
                cv2.imwrite(image_filename, image)
                text_found = pyt.image_to_string(image).strip()
                if text_found:
                    with self.list_lock:
                        self.list.append((img_name, text_found))
            except (KeyboardInterrupt, SystemExit, pyt.TesseractError):
                # error likely to occur only when CTRL + C is sent to program or program ended
                os._exit(0)
            finally:
                self.queue.task_done()


def main():
    if not os.path.exists(PROCESSED_SAVE_LOC):
        os.makedirs(PROCESSED_SAVE_LOC)

    img_dir = os.listdir(IMAGE_SAVE_LOCATION)
    list = []
    list_lock = Lock()

    # make a Queue
    queue = Queue()
    # spawn threads
    for i in range(THREAD_COUNT):
        worker = Worker(queue, list, list_lock)
        worker.daemon = True
        worker.start()

    for img_name in img_dir:
        queue.put(img_name)

    queue.join()

    print("\n==========IMAGES WITH TEXT==========")
    if list:
        for img_name, text_found in list:
            print(img_name + ":", text_found)
    else:
        print("NONE FOUND")

if __name__ == "__main__":
    main()
