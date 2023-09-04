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
                                     link, "header": text[0], "fullInfo": text[1]}
                        objects.append(newObject)
                else:
                    break
    return objects


def getDyanmicHtml(objects):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Render HTML</title>
    </head>
    <body>
    """

    ending = """        
    </body>
    </html>
    """

    dynamic = "<table><tr><th>Name</th><th>Header</th><th>Full Info</th></tr>"

    for object in objects:
        print(object.get('title'))
        dynamic += "<tr>"
        dynamic += "<td><a href=" + \
            object.get("link") + ">" + object.get("title") + "</a></td>"
        dynamic += "<td>"
        if object.get('header'):
            dynamic += str(object.get('header'))
        dynamic += "</td>"
        dynamic += "<td>"
        if object.get('fullInfo'):
            dynamic += str(object.get('fullInfo'))
        dynamic += "</td></tr>"
    dynamic += "</table>"
    return html_content + dynamic + ending
