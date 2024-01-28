#app/domain/bem/bem_model.py
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


# Definindo o modelo para 'bens'
bens_model = api_ms.model('Bens', {
    'id_bem': fields.Integer,
    'id_empresa': fields.Integer,
    'id_setor': fields.Integer,
    'nome': fields.String,
    'plaqueta': fields.String,
    'data_compra': fields.Date,
    'data_tombamento': fields.DateTime,
    'data_baixa': fields.DateTime,
    'valor_compra': fields.Float,
    'valor_depreciado': fields.Float,
    'valor_contabil': fields.Float,
})

# Definindo o modelo para 'setores'
setores_model = api_ms.model('Setores', {
    'id_setor': fields.Integer,
    'id_empresa': fields.Integer,
    'nome': fields.String,
    'bens': fields.List(fields.Nested(bens_model)),  # Usando o modelo 'bens' aqui
})

# Definindo o modelo principal 'ListarBensPorEmpresa'
listar_bens_por_empresa_model = api_ms.model('ListarBensPorEmpresa', {
    'id_empresa': fields.Integer,
    'nome_fantasia': fields.String,
    'razao_social':  fields.String,
    'cnpj':  fields.String,
    'id_endereco': fields.Integer,
    'setores': fields.List(fields.Nested(setores_model)),  # Usando o modelo 'setores' aqui
})