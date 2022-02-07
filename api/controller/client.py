from flask import request
from api.model.client import Client as Client_Model
from api.controller.moddeling import Moddeling_res


class Client():
    def __init__(self) -> None:
        pass

    def get(self, id):
        try:
            person = Client_Model().find(id)
            
            response={"_id": str(person["_id"]),
                "name": str(person["name"]),
                "email": str(person["email"]),
                "dateCreated": str(person["dateCreated"].isoformat())}
            
        except BaseException as error:
            return Moddeling_res().response({"message" : "Id `" + str(id) + "` not found"}, 400)

        else:
            return Moddeling_res().response(response, 200)
        
        

    def post(self):
        person = Client_Model().create(request.json["name"], request.json["email"])

        response={"_id": str(person["_id"]),
               "name": str(person["name"]),
               "email": str(person["email"]),
               "dateCreated": str(person["dateCreated"].isoformat())}

        return Moddeling_res().response(response, 200)

    def list(self):
        response = list()
        
        list_client = Client_Model().list()

        for person in list_client: 
            response.append({"_id": str(person["_id"]),
               "name": str(person["name"]),
               "email": str(person["email"]),
               "dateCreated": str(person["dateCreated"].isoformat())})

        return Moddeling_res().response(response, 200)

    def delete(self, id):
        try:
            person = Client_Model().delete(id)
            
            response={"message" : str(id) + " deleted successfully"}
            
        except BaseException:
            return Moddeling_res().response({"message" : "Id `" + str(id) + "` not found"}, 400)

        else:
            return Moddeling_res().response(response, 200)
