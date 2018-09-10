from downloader import *
from htmlparser import Parser
from queue import Queue
import threading
import os

# configuration
IMAGE_SAVE_LOCATION = ".." + os.sep + ".." + os.sep + "distrib" + os.sep + "images"
MAXIMUM_LINKS_TO_PROCESS = 1250
THREAD_COUNT = 15

def main():
    # make directories
    if not os.path.exists(IMAGE_SAVE_LOCATION):
        os.makedirs(IMAGE_SAVE_LOCATION)

    # start parsing html for download urls
    parser = Parser()
    with open(".." + os.sep + "page.html", encoding="utf8") as file:
        content = file.read()
        parser.feed(content)

    ## multi-threading starts here
    # create a queue and a few workers
    queue = Queue()
    for x in range(THREAD_COUNT):
        worker = DownloaderWorker(queue)
        worker.daemon = True
        worker.start()

    # work on downloading the images
    for link in parser.src_links:
        queue.put(link)

    # let's wait
    queue.join()

    # write the links we got to a file
    with open("links.txt", "w") as file:
        total = 0
        for link in VALID_LINKS:
            file.write(link + "\n")
            total += 1
        file.write(str(total))

if __name__ == "__main__":
    main()
    print("Program Ended")
