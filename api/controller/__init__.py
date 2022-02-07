from flask import Blueprint
from flask_swagger_ui import get_swaggerui_blueprint

from api.controller.client import Client

#Swagger blueprints
swagger_bp = get_swaggerui_blueprint("/swagger", "/docs/swagger.yml",config = {"app_name" : "SD - Proto Flask Doc"})

api_docs_bp = Blueprint('docs','api', template_folder="/api/views/", static_folder="docs", static_url_path="/docs")

api_client_bp = Blueprint('client', 'api', template_folder="/api/views/")
api_client_bp.add_url_rule('/client/<id>', view_func=Client().get, methods=['GET'])
api_client_bp.add_url_rule('/client/<id>', view_func=Client().delete, methods=['DELETE'])
api_client_bp.add_url_rule('/client/', view_func=Client().post, methods=['POST'])
api_client_bp.add_url_rule('/client/list/', view_func=Client().list, methods=['GET'])
