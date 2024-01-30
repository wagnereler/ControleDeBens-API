#app/domain/seguranca/rotina_model.py
from flask_restx import fields
from app.domain import model_ms
insert_rotina = model_ms.model('Rotina', {
    'id': fields.Integer(readonly=True),
    'nome': fields.String(required=True),
})
