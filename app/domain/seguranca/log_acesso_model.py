from flask_restx import fields
from app.domain import api_ms
inserir_log_acesso = api_ms.model('LogAcesso', {
    'id': fields.Integer(readonly=True),
    'id_usuario': fields.Integer(required=True),
    'id_empresa': fields.Integer(required=True),
    'data_acao': fields.DateTime(required=True),
    'status': fields.Integer(requered=True),
})
