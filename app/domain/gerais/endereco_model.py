## app/domain/gerais/endereco_model.py
from flask_restx import fields
from app.domain import api_ms
insert_endereco_model = api_ms.model('Endereco', {
    'id': fields.Integer(readonly=True),
    'id_municipio': fields.Integer(required=True),
    'id_estado': fields.Integer(required=True),
    'id_logradouro': fields.Integer(required=True),
    'endereco': fields.String(required=True),
    'numero': fields.String(required=True),
    'complemento': fields.String(required=False),
    'bairro': fields.String(required=True),
    'cep': fields.String(required=True)
})

obter_enderecos_model = api_ms.model('Obter Enderecos', {
    'id': fields.Integer(readonly=True),
    'id_municipio': fields.Integer(required=True),
    'id_estado': fields.Integer(required=True),
    'id_logradouro': fields.Integer(required=True),
    'endereco': fields.String(required=False),
    'numero': fields.String(required=True),
    'complemento': fields.String(required=False),
    'bairro': fields.String(required=True),
    'cep': fields.String(required=True)
})
