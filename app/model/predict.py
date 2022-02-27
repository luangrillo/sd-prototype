from bson.objectid import ObjectId
import app
import uuid
from datetime import datetime

class Predict():
    def __init__(self):
        self.connection = app.database
        self.collection = "predict"

    def create(self, address, predict):
        try:
            dateCreated = datetime.utcnow()
            self.model = {
                "id" : uuid.uuid4(),
                "address" : str(address),
                "dateCreated": dateCreated
            }
            self.model |= predict
            
            self.connection.insert(self.model, self.collection).inserted_id
            
            return self.model
            
        except Exception as e:
            raise(str(e));
        
    def find(self, id):
        try:
            return self.connection.find({"id" : id}, self.collection)[0]
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
    def updatePredition(self, _id, returnPred, collection):
        try:
            dateCreated = datetime.utcnow()
            self.model = {
                "datePredicted": dateCreated
            }
            self.model |= returnPred
            
            self.connection.update({"_id" : _id}, self.model, collection).inserted_id
            
            return self.model
            
        except Exception as e:
            raise(str(e));
        