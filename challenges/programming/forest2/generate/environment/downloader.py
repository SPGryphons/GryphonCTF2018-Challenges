from config import USER_AGENT
from config import IMAGE_SAVE_LOCATION
from ocr import image_valid
from queue import Queue
from threading import Lock
from threading import Thread
from urllib.request import Request
from pytesseract import TesseractError
import urllib
import os

VALID_LINKS_LOCK = Lock()
VALID_LINKS = []
DOWNLOAD_COUNT_LOCK = Lock()
DOWNLOAD_COUNT = 1

class Downloader(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    # get work from queue
    def run(self):
        global DOWNLOAD_COUNT
        while True:
            link = self.queue.get()
            print("Processing:", link)
            try:
                image = download_image(link)
                # if contain text, throw it out
                if not image_valid(image):
                    with DOWNLOAD_COUNT_LOCK:
                        IMAGE_FILE_PATH = os.path.join(IMAGE_SAVE_LOCATION, str(DOWNLOAD_COUNT) + ".jpg")
                        with open(IMAGE_FILE_PATH, "wb") as image_file:
                            image_file.write(image)
                        DOWNLOAD_COUNT += 1
                    with VALID_LINKS_LOCK:
                        VALID_LINKS.append(link)
            except (KeyboardInterrupt, TesseractError):
                # error likely to occur only when CTRL + C is sent to program or program ended
                os._exit(0)
            finally:
                self.queue.task_done()

def download_image(link):
    request = Request(link, data=None, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request) as response:
        image = response.read()
        return image
