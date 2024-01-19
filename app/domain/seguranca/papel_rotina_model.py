from flask_restx import fields
from app.domain import api_ms
insert_papel_rotina = api_ms.model('PapelRotina', {
    'id': fields.Integer(readonly=True),
    'id_papel': fields.Integer(required=True),
    'rotina_id': fields.Integer(required=True),
})
