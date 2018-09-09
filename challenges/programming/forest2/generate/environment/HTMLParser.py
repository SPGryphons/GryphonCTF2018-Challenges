from html.parser import HTMLParser
from urllib.request import Request
import os
import re
import urllib.request

# global vars
COUNT = 1
IMG_STORE_PATH = ".." + os.sep + ".." + os.sep + "distrib" + os.sep + "images"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"

class ImgHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global COUNT
        if tag == "img":
            firstAttr = attrs[0]

            if firstAttr[0] == "srcset" and COUNT <= 1000:
                # split the urls in srcset attribute
                sources = firstAttr[1].split(",")
                # using first url in srcset, remove some stuff and append correct url parameters
                downloadUrl = re.sub("(\\?.+1x)", "?cs=srgb&fm=jpg&dl=" + str(COUNT) + ".jpg", sources[0])
                print("Download URL:", downloadUrl)

                # make request to download image
                request = Request(downloadUrl, data=None, headers={"User-Agent": USER_AGENT})
                with urllib.request.urlopen(request) as response:
                    image = response.read()
                    saveDir = os.path.join(IMG_STORE_PATH, str(COUNT) + ".jpg")
                    print("Save Directory:", saveDir, "\n")
                    with open(saveDir, "wb") as imgFile:
                        imgFile.write(image)
                        imgFile.flush()
                COUNT += 1

if __name__ == "__main__":
    if not os.path.exists(IMG_STORE_PATH):
        os.makedirs(IMG_STORE_PATH)

    with open(".." + os.sep + "page.html", encoding="utf8") as file:
        content = file.read()
        parser = ImgHTMLParser()
        parser.feed(content)

    print("Program ended!")
