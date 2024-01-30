#app/domain/seguranca/papel_model.py
from flask_restx import fields
from app.domain import model_ms
inserir_papel = model_ms.model('Papel', {
    'id': fields.Integer(readonly=True),
    'id_rotina': fields.Integer(required=True),
    'nome': fields.String(required=False),
})
