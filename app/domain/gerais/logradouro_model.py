#app/domain/gerais/logradouro_model.py
from flask_restx import fields
from app.domain import model_ms

insert_logradouro_model = model_ms.model('Logradouro', {
    'id': fields.Integer(readonly=True),
    'nome': fields.String(required=True),
    'ativo': fields.Boolean(default=True),
})

obter_logradouros_model = model_ms.model('Obter Logradouros', {
    'id': fields.Integer(readonly=True),
    'nome': fields.String(required=True),
    'ativo': fields.Boolean(default=True),
})
