
from datetime import datetime
from flask import abort, make_response
import requests
from bs4 import BeautifulSoup


def test():
    return {"key": "value", "info": "This is another information - c"}


def dino_class_names():
    url_link = "https://en.wikipedia.org/wiki/Dinosaur"
    base = "https://en.wikipedia.org"
    objects = getAllClassification(url_link, base)
    return objects


def getAllClassification(link, base, count=5):
    soup = getTheSoup(link)
    objects = []

    if soup:
        # Get all tags in the HTML document
        all_dl_tags = soup.find_all('dl')
        for tag in all_dl_tags:
            listItems = tag.find_all('li')
            for listItem in listItems:
                href = listItem.find('a')
                if len(objects) < count:
                    title = href.get('title')
                    link = href.get('href')
                    if title:
                        full_link = base + link
                        text = getSub(full_link, ".infobox")
                        newObject = {"title": title, "link": base +
                                     link, "header": str(text[0]), "fullInfo": str(text[1])}
                        objects.append(newObject)
                else:
                    break
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
