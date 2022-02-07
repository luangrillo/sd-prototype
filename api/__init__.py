from os import environ
from flask import Flask 

from api.connection.mdb import db

from api.controller import swagger_bp, api_docs_bp, api_client_bp


class initializer():
    def __init__(self) -> None:
        pass
    
    def loader(self, config_filename=None):
        global database
        
        application = Flask(__name__)

        application.register_blueprint(swagger_bp)
        application.register_blueprint(api_docs_bp)
        application.register_blueprint(api_client_bp)
        application.config
              
        database = db()
        
        return application
        
        
app = initializer.loader(".env")