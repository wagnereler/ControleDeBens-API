## app/domain/gerais/endereco_model.py
from flask_restx import fields
from app.domain import model_ms
from app.domain.gerais.estado_model import obter_estados_model
from app.domain.gerais.municipio_model import obter_municipios_model
from app.domain.gerais.logradouro_model import obter_logradouros_model


insert_endereco_model = model_ms.model('Endereco', {
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

obter_enderecos_model = model_ms.model('Obter Enderecos', {
    'id': fields.Integer(readonly=True),
    'municipio': fields.Nested(obter_municipios_model, required=True),
    'estado': fields.Nested(obter_estados_model, required=True),
    'logradouro': fields.Nested(obter_logradouros_model, required=True),
    'endereco': fields.String(required=False),
    'numero': fields.String(required=True),
    'complemento': fields.String(required=False),
    'bairro': fields.String(required=True),
    'cep': fields.String(required=True)
})
