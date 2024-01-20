# app/domain/gerais/endereco_resource.py
from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource
from app.domain.gerais.endereco_service import inserir_endereco, obter_enderecos
from app.domain.gerais.endereco_model import insert_endereco_model, obter_enderecos_model
from app.domain.gerais import gerais_ns

@gerais_ns.route('/endereco')
@gerais_ns.doc({'endereco'})
class Endereco(Resource):

    @gerais_ns.marshal_list_with(obter_enderecos_model)
    def get(self):
        endereco = obter_enderecos()
        return endereco

    @gerais_ns.expect(obter_enderecos_model)
    @gerais_ns.marshal_with(insert_endereco_model, code=201)
    def post(self):
        data = request.json
        _endereco = inserir_endereco(data['id_municipio'],
                                    data['id_estado'],
                                    data['id_logradouro'],
                                    data['endereco'],
                                    data['numero'],
                                    data['complemento'],
                                    data['bairro'],
                                    data['cep'])
        return _endereco, 201
