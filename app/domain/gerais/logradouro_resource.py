# app/domain/gerais/logradouro_resource.py
from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource
from app.domain.gerais.logradouro_service import inserir_logradouro, obter_logradouros
from app.domain.gerais.logradouro_model import insert_logradouro_model, obter_logradouros_model
from app.domain.gerais import gerais_ns

@gerais_ns.route('/logradouro')
@gerais_ns.doc({'logradouro'})
class Logradouro(Resource):

    @gerais_ns.marshal_list_with(obter_logradouros_model)
    def get(self):
        logradouro = obter_logradouros()
        return logradouro

    @gerais_ns.expect(obter_logradouros_model)
    @gerais_ns.marshal_with(insert_logradouro_model, code=201)
    def post(self):
        data = request.json
        logradouro = inserir_logradouro(data['nome'], data['ativo'])
        return logradouro, 201
