#app/domain/bem/movimentacao_model.py
from flask_restx import fields
from app.domain import api_ms
insert_movimentacao = api_ms.model('Movimentacao', {
    'id': fields.Integer(readonly=True),
    'id_bem': fields.Integer(required=True),
    'id_setor_saida': fields.Integer(required=True),
    'id_setor_entrada': fields.Integer(required=True),
    'id_empresa_saida': fields.Integer(required=True),
    'id_empresa_entrada': fields.Integer(required=True),
    'data_movimentacao': fields.DateTime(required=True),
})
