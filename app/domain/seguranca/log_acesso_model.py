#app/domain/seguranca/log_acesso_model.py
from flask_restx import fields
from app.domain import model_ms
inserir_log_acesso = model_ms.model('LogAcesso', {
    'id': fields.Integer(readonly=True),
    'id_usuario': fields.Integer(required=True),
    'id_empresa': fields.Integer(required=True),
    'data_acao': fields.DateTime(required=True),
    'status': fields.Integer(requered=True),
})
