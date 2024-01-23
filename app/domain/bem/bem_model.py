from flask_restx import fields
from app.domain import api_ms
from app.domain.empresa.setor_model import obter_setor_bem_model
from app.domain.empresa.empresa_model import obter_empresa_bem_model

inserir_bem_model = api_ms.model('Bem', {
    'id_empresa': fields.Integer(required=True),
    'id_setor': fields.Integer(required=True),
    'nome': fields.String(required=True),
    'plaqueta': fields.String(required=True),
    'data_compra': fields.Date(required=True),
    'data_tombamento': fields.DateTime(required=True),
    'data_baixa': fields.DateTime(required=False),
    'valor_compra': fields.Float(required=True),
    'valor_depreciado': fields.Float(required=False),
    'valor_contabil': fields.Float(required=False)
})

obter_bens_model = api_ms.model('Obter Bem', {
    'id': fields.Integer(readonly=True),
    'empresa': fields.Nested(obter_empresa_bem_model, attribute='empresa'),
    'setor': fields.Nested(obter_setor_bem_model, attribute='setor'),
    'nome': fields.String(required=True),
    'plaqueta': fields.String(required=True),
    'data_compra': fields.Date(required=True),
    'data_tombamento': fields.DateTime(required=True),
    'data_baixa': fields.DateTime(required=True),
    'valor_compra': fields.Float(required=True),
    'valor_depreciado': fields.Float(required=False),
    'valor_contabil': fields.Float(required=True)
})
