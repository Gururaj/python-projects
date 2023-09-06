
from datetime import datetime
from flask import abort, make_response
import requests
from bs4 import BeautifulSoup
from .get_dino_names import get_all_dino_names
from .get_dino_class import getAllClassification


def test():
    return {"key": "value", "info": "This is another information - c"}


def dino_class_names():
    url_link = "https://en.wikipedia.org/wiki/Dinosaur"
    base = "https://en.wikipedia.org"
    objects = getAllClassification(url_link, base)
    return objects

def dino_get_names():
    url_link = "https://en.wikipedia.org/wiki/List_of_dinosaur_genera"
    base = "https://en.wikipedia.org"
    objects = get_all_dino_names(url_link, base)
    return objects


def getTheSoup(link):
    response = requests.get(link)
    soup = None
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
    else:
        print(
            f"Failed to retrieve the web page. Status code: {response.status_code}")
    return soup


def getSub(link, htmlClass):
    soup = getTheSoup(link)
    final = [None, None]
    if soup:
        tags = soup.select(htmlClass)
        final[0] = tags[0]
        for tag in tags:
            th = tag.find_all('th')
            final[1] = th[0]
    return final
