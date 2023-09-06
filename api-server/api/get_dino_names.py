import requests
from bs4 import BeautifulSoup


def getTheSoup(link):
    response = requests.get(link)
    soup = None
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
    else:
        print(
            f"Failed to retrieve the web page. Status code: {response.status_code}")
    return soup


def get_all_dino_names(link, base, count=5):
    soup = getTheSoup(link)
    objects = []

    if soup:
        for tag in soup.find_all("a", {"class": "mw-redirect"}):                          
          if len(objects) < count:
              title = tag.get('title')
              link = tag.get('href')
              if title:
                  full_link = base + link                        
                  newObject = {"title": title, "link": base +
                                link}
                  objects.append(newObject)
          else:
              break
    return objects

if __name__ == "__main__":
    url_link = "https://en.wikipedia.org/wiki/List_of_dinosaur_genera"
    base = "https://en.wikipedia.org"
    objects = get_all_dino_names(url_link, base)
    print(objects)
