#app/domain/api/controle_versao_resource.py
from flask_restx import Namespace, Resource, fields
from flask import request
from app.domain.api import api_ms
from app.domain.api.controle_versao_model import (versao_model,
                                                  inserir_funcao_model,
                                                  listar_funcoes_model,
                                                  inserir_responsavel_model,
                                                  listar_responsaveis_model)

from app.domain.api.controle_versao_service import (get_versao,
                                                    inserir_funcao,
                                                    listar_funcoes,
                                                    listar_responsaveis,
                                                    inserir_responsavel)


@api_ms.route('/')
class Versao(Resource):
    @api_ms.marshal_with(versao_model)
    def get(self):
        get_versao()
        return {'versao': get_versao()}

@api_ms.route('/funcao')
class Funcao(Resource):

    @api_ms.expect(inserir_funcao_model)
    @api_ms.marshal_with(listar_funcoes_model)
    def post(self):
        data = request.json
        funcao = inserir_funcao(data['funcao'])
        return funcao

    @api_ms.marshal_list_with(listar_funcoes_model)
    def get(self):
        funcao = listar_funcoes()
        return funcao, 201


@api_ms.route('/responsavel')
class Responsavel(Resource):

    @api_ms.expect(inserir_responsavel_model)
    @api_ms.marshal_with(listar_responsaveis_model)
    def post(self):
        data = request.json
        responsavel = inserir_responsavel(
            data['id_funcao'],
            data['nome'],
            data['email']
        )
        return responsavel, 201

    @api_ms.marshal_list_with(listar_responsaveis_model)
    def get(self):
        responsavel = listar_responsaveis()
        return responsavel, 200
