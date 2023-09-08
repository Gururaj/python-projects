'''Get classifications'''
from .utils import get_the_soup


def get_sub(link, html_class):
    '''Get the sub html element'''
    soup = get_the_soup(link)
    final = []
    if soup:
        tags = soup.select(html_class)
        final[0] = tags[0]
        for tag in tags:
            th = tag.find_all('th')
            final[1] = th[0]
    return final


def get_all_classification(link, base, count=5):
    '''Get all classification'''
    soup = get_the_soup(link)
    all_objects = []

    if soup:
        # Get all tags in the HTML document
        all_dl_tags = soup.find_all('dl')
        for tag in all_dl_tags:
            list_items = tag.find_all('li')
            for list_item in list_items:
                href = list_item.find('a')
                if len(all_objects) < count:
                    title = href.get('title')
                    link = href.get('href')
                    if title:
                        full_link = base + link
                        text = get_sub(full_link, ".infobox")
                        new_object = {"title": title, "link": base +
                                      link, "header": text[0], "fullInfo": text[1]}
                        all_objects.append(new_object)
                else:
                    break
    return all_objects


def get_dynamic_html(all_objects):
    '''Get dynamic html for testing'''
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

    for one_object in all_objects:
        print(one_object.get('title'))
        dynamic += "<tr>"
        dynamic += "<td><a href=" + \
            one_object.get("link") + ">" + \
            one_object.get("title") + "</a></td>"
        dynamic += "<td>"
        if one_object.get('header'):
            dynamic += str(one_object.get('header'))
        dynamic += "</td>"
        dynamic += "<td>"
        if one_object.get('fullInfo'):
            dynamic += str(one_object.get('fullInfo'))
        dynamic += "</td></tr>"
    dynamic += "</table>"
    return html_content + dynamic + ending
