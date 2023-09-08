'''File to get all dino names'''
import requests
from bs4 import BeautifulSoup


def get_the_soup(link):
    '''Using Soup to extract information'''
    response = requests.get(link, timeout=1000)
    soup = None
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
    else:
        print(
            f"Failed to retrieve the web page. Status code: {response.status_code}")
    return soup


def get_all_dino_names(link, base, count=5):
    '''Method to get all Dino names'''
    soup = get_the_soup(link)
    dino_objects = []

    if soup:
        for tag in soup.find_all("a", {"class": "mw-redirect"}):
            if len(objects) < count:
                title = tag.get('title')
                link = tag.get('href')
                if title:
                    full_link = base + link
                    new_object = {"title": title, "link": full_link}
                    dino_objects.append(new_object)
            else:
                break
    return objects


if __name__ == "__main__":
    URL_LINK = "https://en.wikipedia.org/wiki/List_of_dinosaur_genera"
    BASE_URL = "https://en.wikipedia.org"
    objects = get_all_dino_names(URL_LINK, BASE_URL)
    print(objects)
