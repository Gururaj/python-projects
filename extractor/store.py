''' To be implemented using mongo client'''
from pymongo import MongoClient


def get_database():
    '''Get database, as of now this just checkes connection'''
    connection_string = "mongodb://localhost:27017"
    client = MongoClient(connection_string)
    if client:
        return "SUCCESS"
    else:
        return "FAILURE"
