#app/domain/gerais/estado_model.py
from flask_restx import fields
from app.domain import api_ms
insert_estado_model = api_ms.model('Estado', {
    'id': fields.Integer(readonly=True),
    'nome': fields.String(required=True),
    'uf': fields.String(required=True),
    'codigo_ibge': fields.String(required=True),
})

obter_estados_model = api_ms.model('Obter Estados', {
    'id': fields.Integer(readonly=True),
    'nome': fields.String(required=True),
    'uf': fields.String(required=True),
    'codigo_ibge': fields.String(required=True),
})
