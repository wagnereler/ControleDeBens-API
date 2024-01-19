from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields
from app.utils.extensions import db
from app.domain.empresa.empresa_service import inserir_empresa
from app.domain.empresa.empresa_model import inserir_empresa, obter_empresa
from app.domain.empresa import empresa_ns


@empresa_ns.route('/')
@empresa_ns.doc({'empresa'})
class Bem(Resource):

    @empresa_ns.marshal_list_with(obter_empresa)
    def get(self):
        empresa = obter_empresa()
        return empresa

    @empresa_ns.expect(obter_empresa)
    @empresa_ns.marshal_with(inserir_empresa, code=201)
    def post(self):
        data = request.json
        empresa = inserir_empresa(data['nome_fantasia'],
                        data['razao_social'],
                        data['cnpj'],
                        data['id_endereco']
                        )
        return empresa, 201