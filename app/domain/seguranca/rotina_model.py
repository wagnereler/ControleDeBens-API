#app/domain/seguranca/rotina_model.py
from flask_restx import fields
from app.domain import api_ms
insert_rotina = api_ms.model('Rotina', {
    'id': fields.Integer(readonly=True),
    'nome': fields.String(required=True),
})
