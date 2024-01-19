from flask_restx import fields
from app.domain import api_ms
from app.domain.empresa.empresa_model import inserir_empresa
from app.domain.empresa.setor_model import inserir_setor

inserir_bem_model = api_ms.model('Bem', {
    'id': fields.Integer(readonly=True),
    'id_empresa': fields.Integer(required=True),
    'id_setor': fields.Integer(required=True),
    'nome': fields.String(required=True),
    'plaqueta': fields.String(required=True),
    'data_compra': fields.Date(required=True),
    'data_tombamento': fields.DateTime(required=True),
    'data_baixa': fields.DateTime(required=True),
    'valor_compra': fields.Float(required=True),
    'valor_depreciado': fields.Float(required=False),
    'valor_contabil': fields.Float(required=True)
})

obter_bens_model = api_ms.model('Bem', {
    'id': fields.Integer(readonly=True),
    'id_empresa': fields.Nested(inserir_empresa, attribute='empresa'),
    'id_setor': fields.Nested(inserir_setor, attribute='setor'),
    'nome': fields.String(required=True),
    'plaqueta': fields.String(required=True),
    'data_compra': fields.Date(required=True),
    'data_tombamento': fields.DateTime(required=True),
    'data_baixa': fields.DateTime(required=True),
    'valor_compra': fields.Float(required=True),
    'valor_depreciado': fields.Float(required=False),
    'valor_contabil': fields.Float(required=True)
})
