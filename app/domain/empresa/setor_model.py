from flask_restx import fields
from app.domain import api_ms
inserir_setor = api_ms.model('Setor', {
    'id': fields.Integer(readonly=True),
    'id_empresa': fields.Integer(required=True),
    'nome': fields.String(required=False),
})
