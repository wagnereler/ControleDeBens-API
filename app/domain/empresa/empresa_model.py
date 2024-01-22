#app/domain/empresa/empresa_model.py
from flask_restx import fields
from app.domain import api_ms
from app.domain.gerais.endereco_model import obter_enderecos_model

inserir_empresa_model = api_ms.model('Empresa', {
    'id': fields.Integer(readonly=True),
    'id_endereco': fields.Integer(required=True),
    'nome_fantasia': fields.String(required=True),
    'razao_social': fields.String(required=True),
    'cnpj': fields.String(required=True),
})

obter_empresa_model = api_ms.model('Obter Empresa', {
    'id': fields.Integer(readonly=True),
    'endereco': fields.Nested(obter_enderecos_model),
    'nome_fantasia': fields.String(required=True),
    'razao_social': fields.String(required=True),
    'cnpj': fields.String(required=True),
})
