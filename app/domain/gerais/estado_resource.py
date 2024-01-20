# app/domain/gerais/estado_resource.py
from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource
from app.domain.gerais.estado_service import inserir_estado, obter_estados
from app.domain.gerais.estado_model import insert_estado_model, obter_estados_model
from app.domain.gerais import gerais_ns

@gerais_ns.route('/estado')
@gerais_ns.doc({'estado'})
class Estado(Resource):

    @gerais_ns.marshal_list_with(obter_estados_model)
    def get(self):
        estado = obter_estados()
        return estado

    @gerais_ns.expect(obter_estados_model)
    @gerais_ns.marshal_with(insert_estado_model, code=201)
    def post(self):
        data = request.json
        estado = inserir_estado(data['uf'], data['nome'], data['codigo_ibge'])
        return estado, 201
