'''API Routes implemetnation'''
from .get_dino_names import get_all_dino_names
from .get_dino_class import get_all_classification


def test():
    '''Test API Implementation'''
    return {"key": "value", "info": "This is another information - c"}


def dino_class_names():
    '''Dino Classification API'''
    url_link = "https://en.wikipedia.org/wiki/Dinosaur"
    base = "https://en.wikipedia.org"
    objects = get_all_classification(url_link, base)
    return objects


def dino_get_names():
    '''Dino Name API'''
    url_link = "https://en.wikipedia.org/wiki/List_of_dinosaur_genera"
    base = "https://en.wikipedia.org"
    objects = get_all_dino_names(url_link, base)
    return objects
