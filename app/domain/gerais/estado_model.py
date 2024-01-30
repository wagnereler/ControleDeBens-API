#app/domain/gerais/estado_model.py
from flask_restx import fields
from app.domain import model_ms
insert_estado_model = model_ms.model('Estado', {
    'id': fields.Integer(readonly=True),
    'nome': fields.String(required=True),
    'uf': fields.String(required=True),
    'codigo_ibge': fields.String(required=True),
})

obter_estados_model = model_ms.model('Obter Estados', {
    'id': fields.Integer(readonly=True),
    'nome': fields.String(required=True),
    'uf': fields.String(required=True),
    'codigo_ibge': fields.String(required=True),
})
