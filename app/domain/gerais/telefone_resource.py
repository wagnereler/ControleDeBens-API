# app/domain/gerais/telefone_resource.py
from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource
from app.domain.gerais.telefone_service import inserir_telefone, obter_telefones
from app.domain.gerais.telefone_model import inserir_telefone_model, obter_telefones_model
from app.domain.gerais import gerais_ns

@gerais_ns.route('/telefone')
@gerais_ns.doc({'telefone'})
class Telefone(Resource):  # Renomear a classe para TelefoneResource

    @gerais_ns.marshal_list_with(obter_telefones_model)
    def get(self):
        telefone = obter_telefones()
        return telefone

    @gerais_ns.expect(obter_telefones_model)
    @gerais_ns.marshal_with(inserir_telefone_model, code=201)
    def post(self):
        data = request.json
        telefone = inserir_telefone(data['ddi'], data['ddd'], data['numero'], data['tipo'])
        return telefone, 201
