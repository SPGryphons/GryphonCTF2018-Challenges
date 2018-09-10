import os
import time

IMAGE_SAVE_LOCATION = ".." + os.sep + ".." + os.sep + "distrib" + os.sep + "images"

def main():
    dir_files = os.listdir(IMAGE_SAVE_LOCATION)

    for file in dir_files:
        file_path = os.path.join(IMAGE_SAVE_LOCATION, file)
        if os.path.isfile(file_path):
            print("Processing:", file_path)
            os.utime(file_path)

if __name__ == "__main__":
    main()
    print("Updated last modified times")
