"""Practicing some basic web scraping

I am using the O'Reilly book, "Web Scraping with Python" by Ryan Mitchell.
It's a very readable book for a technical book.

This program will process the Beaverton, Oregon wikipedia page
"""

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys, logging, requests, re

__author__ = 'rnzucker'

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


def main():
    try:
        html = urlopen("https://en.wikipedia.org/wiki/Portland_Beavers")
    except HTTPError as e:
        print(e)
        return
    if html is None:
        print("URL is not found")
        return
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a",
                            href=re.compile("^(/wiki/)((?!:).)*$")):
        if 'href' in link.attrs:
            print(link.attrs['href'])


main()
