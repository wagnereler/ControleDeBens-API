from flask_restx import fields
from app.domain import api_ms
insert_municipio_model = api_ms.model('Municipio', {
    'id': fields.Integer(readonly=True),
    'id_estado': fields.Integer(required=True),
    'nome': fields.String(required=True),
    'codigo_ibge': fields.String(required=True),
})

obter_municipios_model = api_ms.model('Obter Municipios', {
    'id': fields.Integer(readonly=True),
    'id_estado': fields.Integer(required=True),
    'nome': fields.String(required=True),
    'codigo_ibge': fields.String(required=True),
})

