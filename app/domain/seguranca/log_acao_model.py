from flask_restx import fields
from app.domain import api_ms
inserir_log_acao = api_ms.model('LogAcao', {
    'id': fields.Integer(readonly=True),
    'id_usuario': fields.Integer(required=True),
    'id_rotina': fields.Integer(required=True),
    'acao': fields.String(required=True),
    'data_acao': fields.DateTime(required=True)
})