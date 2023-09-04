from pymongo import MongoClient


def getDatabase(): 
  CONNECTION_STRING = "mongodb://localhost:27017"
  client = MongoClient(CONNECTION_STRING)
  if client: 
    return "SUCCESS"
  else: 
    return "FAILURE"
