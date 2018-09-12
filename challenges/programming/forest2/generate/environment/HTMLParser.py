from config import MAXIMUM_LINKS_TO_PROCESS
from html.parser import HTMLParser
from urllib.request import Request
import urllib.request
import os
import re

RUN_COUNT = 1

class Parser(HTMLParser):
    src_links = []

    def handle_starttag(self, tag, attrs):
        global RUN_COUNT, scr_links

        if tag == "img":
            first_attr = attrs[0]
            if first_attr[0] == "srcset" and RUN_COUNT <= MAXIMUM_LINKS_TO_PROCESS:
                # split the urls in srcset attribute
                src_set = first_attr[1].split(",")
                # using first url in srcset, remove some stuff and append correct url parameters
                download_url = re.sub("(\\?.+1x)", "?cs=srgb&fm=jpg&w=720&dl=" + str(RUN_COUNT) + ".jpg", src_set[0])
                self.src_links.append(download_url)
                print(str(RUN_COUNT) + ":" , "Download URL:", download_url)
                # increment run count
                RUN_COUNT += 1
