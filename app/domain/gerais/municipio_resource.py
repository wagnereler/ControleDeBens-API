# app/domain/gerais/municpio_resource.py
from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource
from app.domain.gerais.municipio_service import inserir_municipio, obter_municipios
from app.domain.gerais.municipio_model import insert_municipio_model, obter_municipios_model
from app.domain.gerais import gerais_ns

@gerais_ns.route('/municipio')
@gerais_ns.doc({'municipio'})
class Municipio(Resource):

    @gerais_ns.marshal_list_with(obter_municipios_model)
    def get(self):
        municipio = obter_municipios()
        return municipio

    @gerais_ns.expect(obter_municipios_model)
    @gerais_ns.marshal_with(insert_municipio_model, code=201)
    def post(self):
        data = request.json
        municipio = inserir_municipio(data['id_estado'], data['nome'], data['codigo_ibge'])
        return municipio, 201
