from bson.objectid import ObjectId
import api
from datetime import datetime

class Client():
    def __init__(self):
        self.connection = api.database
        self.collection = "client"

    def create(self, name, email):
        try:
            dateCreated = datetime.utcnow()
            self.model = {
                "name" : str(name),
                "email" : str(email),
                "dateCreated": dateCreated
            }
            
            self.connection.insert(self.model, self.collection).inserted_id
            
            return self.model
            
        except Exception as e:
            raise(str(e));
        
    def find(self, id):
        try:
            return self.connection.find({"_id" : ObjectId(id)}, self.collection)[0]
        except Exception as e:
            raise(str(e));
        
    def list(self):
        try:
            return self.connection.find({}, self.collection)
        except Exception as e:
            raise(str(e));
        
    def delete(self, id):
        try:
            delete = (self.connection.remove({"_id" : ObjectId(id)}, {"justOne" : True}, self.collection))
            
            if(delete["n"] != 1):
                raise BaseException("")
            
        except Exception as e:
            raise(str(e));