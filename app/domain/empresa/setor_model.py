from flask_restx import fields
from app.domain import api_ms
from app.domain.empresa.empresa_model import obter_empresa_setor_model

inserir_setor_model = api_ms.model('Setor', {
    'id_empresa': fields.Integer(required=True),
    'nome': fields.String(required=False),
})

obter_setor_model = api_ms.model('Obter Setor', {
    'id': fields.Integer(readonly=True),
    'nome': fields.String(required=False),
    'empresa': fields.Nested(obter_empresa_setor_model, required=True)

})

obter_setor_por_empresa_model = api_ms.model('ObterSetorPorEmpresa', {
    'id': fields.Integer(readonly=True),
    'nome': fields.String(required=False),
    'empresa': fields.List(fields.Nested(obter_empresa_setor_model, required=True))

})
