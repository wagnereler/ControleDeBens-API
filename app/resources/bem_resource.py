from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields
from app.utils.extensions import db
from app.resources import name_space
from app.services.bem_service import criar_bem, obter_bem_por_id, obter_bem_por_descricao, obter_bens

bem_model = name_space.model('Bem', {
    'id': fields.Integer(readonly=True),
    'id_empresa': fields.Integer(required=True),
    'id_setor': fields.Integer(required=True),
    'nome': fields.String(required=True),
    'plaqueta': fields.String(required=True),
    'data_compra': fields.Date(required=True),
    'data_tombamento': fields.DateTime(required=True),
    'data_baixa': fields.DateTime(required=True),
    'valor_compra': fields.Float(required=True),
    'valor_depreciado': fields.Float(required=False),
    'valor_contabil': fields.Float(required=True)
})


@name_space.route('/bem')
class Bem(Resource):
    @name_space.expect(bem_model)
    @name_space.marshal_with(bem_model, code=201)
    def post(self):
        data = request.json
        bem = criar_bem(data['id_empresa'],
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

    @name_space.marshal_list_with(bem_model)
    def get(self):
        bens = obter_bens()
        return bens


@name_space.route('/bem/<int:id>')
class BemPorId(Resource):
    @name_space.marshal_with(bem_model)
    def get(self, id):
        bem = obter_bem_por_id(id)
        return bem

    @name_space.marshal_with(bem_model)
    def delete(self, id):
        bem = obter_bem_por_id(id)
        db.session.delete(bem)
        db.session.commit()
        return '', 204

    @jwt_required()
    @name_space.expect(bem_model)
    @name_space.marshal_with(bem_model)
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
