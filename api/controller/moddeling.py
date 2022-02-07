from flask import make_response
import json
class Moddeling_res():
    def __init__(self) -> None:
        self.res = dict()
        pass
    
    def response(self, body, http_status):
        self.res = make_response(json.dumps(body), http_status)
        self.res.headers["Content-Type"] = "application/json; charset=utf-8"
        
        return self.res
        