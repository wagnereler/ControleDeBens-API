#app/domain/seguranca/papel_rotina_model.py
from flask_restx import fields
from app.domain import model_ms
insert_papel_rotina = model_ms.model('PapelRotina', {
    'id': fields.Integer(readonly=True),
    'id_papel': fields.Integer(required=True),
    'rotina_id': fields.Integer(required=True),
})
