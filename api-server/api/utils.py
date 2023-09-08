'''file to store all utils'''


from bs4 import BeautifulSoup
import requests


def get_the_soup(link):
    '''Getting web by using Soup'''
    response = requests.get(link, timeout=1000)
    soup = None
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
    else:
        print(
            f"Failed to retrieve the web page. Status code: {response.status_code}")
    return soup
