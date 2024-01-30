#app/domain/api/controle_versao_resource.py
from flask_restx import Namespace, Resource, fields
from app.domain.api import api_ms
from app.domain.api.controle_versao_model import versao_model
from app.domain.api.controle_versao_service import get_versao


@api_ms.route('/')
class Versao(Resource):
    @api_ms.marshal_with(versao_model)
    def get(self):
        get_versao()
        return {'versao': get_versao()}