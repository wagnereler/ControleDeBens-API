# app/domain/bem/bem_resource.py
from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource

from app.domain.bem.bem_service import inserir_bem, obter_bens, listar_bens_por_empresa
from app.domain.bem.bem_model import inserir_bem_model, obter_bens_model, listar_bens_por_empresa_model
from app.domain.bem import bens_ns


@bens_ns.route('/')
@bens_ns.doc({'bens'})
class Bem(Resource):
    @bens_ns.marshal_list_with(obter_bens_model)
    def get(self):
        bens = obter_bens()
        return bens

    @bens_ns.expect(inserir_bem_model)
    @bens_ns.marshal_with(inserir_bem_model, code=201)
    def post(self):
        data = request.json
        bem = inserir_bem(data['id_empresa'],
                          data['id_setor'],
                          data['nome'],
                          data['plaqueta'],
                          data['data_compra'],
                          data['data_tombamento'],
                          data['data_baixa'],
                          data['valor_compra'],
                          data['valor_depreciado'],
                          data['valor_contabil']
                          )
        return bem, 201


@bens_ns.route('/<int:id_empresa>')
class ListarBensPorEmpresaId(Resource):
    "Listar Bens Por Empesa"

    @bens_ns.marshal_with(listar_bens_por_empresa_model)
    def get(self, id_empresa):
        return listar_bens_por_empresa(id_empresa)


"""
@bens_ns.route('/bem/<int:id>')
class BemPorId(Resource):
    @bens_ns.marshal_with(get_bem)
    def get(self, id):
        bem = obter_bem_por_id(id)
        return bem

    @bens_ns.marshal_with(get_bem)
    def delete(self, id):
        bem = obter_bem_por_id(id)
        db.session.delete(bem)
        db.session.commit()
        return '', 204

    @jwt_required()
    @bens_ns.expect(get_bem)
    @bens_ns.marshal_with(get_bem)
    def put(self, id):
        data = request.json
        bem = obter_bem_por_id(id)
        bem(data['id_empresa'],
            data['id_setor'],
            data['nome'],
            data['plaqueta'],
            data['data_compra'],
            data['data_tombamento'],
            data['data_baixa'],
            data['valor_compra'],
            data['valor_depreciado'],
            data['valor_contabil']
            )
        db.session.commit()
        return bem, 202
"""
