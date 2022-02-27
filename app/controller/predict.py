from flask import request
from app.model.predict import Predict as Predict_Model
from app.controller.moddeling import Moddeling_res
import threading
import paho.mqtt.publish as publish
import requests
import json
import uuid

class Predict():
    def __init__(self) -> None:
        pass

    def get(self):
        requestId = str(uuid.uuid4())
        response={"_id": str(requestId),
               "status": "created"}


        def make_predict(requestId, image, address, clientFilepath):
            req = requests.post("http://image-predict:5000/model/predict?threshold=0.6", files=dict(image=image))
            #plotboxed = make_image(request.files["image"], req.json(),)
            clientJson = json.loads(req.text)
            clientJson["requestId"] =  str(requestId)
            clientJson["filename"] = clientFilepath["filename"]
            
            Predict_Model().create(address, clientJson)
            
            publish.single("predictions", json.dumps(clientJson), hostname="rabbitmq")
            

        threading.Thread(target=make_predict, args=(requestId, request.files["image"].read(),str(request.remote_addr), json.loads(request.files["json"].read()))).start()
        
        return Moddeling_res().response(response, 200)
