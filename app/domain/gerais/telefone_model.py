#app/domain/gerais/telefone_model.py
from flask_restx import fields
from app.domain import model_ms
inserir_telefone_model = model_ms.model('Telefone', {
    'id': fields.Integer(readonly=True),
    'ddi': fields.String(required=False),
    'ddd': fields.String(required=True),
    'numero': fields.String(required=True),
    'tipo': fields.Integer(required=True),
})

obter_telefones_model = model_ms.model('Obter Telefones', {
    'id': fields.Integer(readonly=True),
    'ddi': fields.String(required=False),
    'ddd': fields.String(required=False),
    'numero': fields.String(required=True),
    'tipo': fields.Integer(required=True),
})
