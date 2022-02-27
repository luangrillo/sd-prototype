from pymongo import MongoClient
from os import environ

class db():
    def __init__(self):
        self.mdb_server = MongoClient(environ.get("MONGODB_END"), authSource='admin')
        self.mdb_database = self.mdb_server[environ.get("MONGODB_DB")]

    def insert(self, data, collection = "main"):
        inserts = self.mdb_database[collection].insert_one(data)
        
        return inserts
    
    def find(self, query, collection = "main"):
        temp_data = []
        
        finds = self.mdb_database[collection].find(query)
        
        for data in finds:
            temp_data.append(data)

        return temp_data
    
    def update(self, query, update, collection = "main"):
        updated = self.database[collection].update(query, update, upsert=False)
        
        return updated
        
    def remove(self, query, params, collection = "main"):

        return self.mdb_database[collection].remove(query, params)
      