#app/domain/api/controle_versao_model.py
from flask_restx import Namespace, Resource, fields
from app.domain.api import api_ms

versao_model = api_ms.model('Versao', {
    'versao': fields.String(),
})

listar_funcoes_model = api_ms.model('ListarFuncoes', {
    'id': fields.Integer,
    'funcao': fields.String,
})

inserir_funcao_model = api_ms.model('InserirFuncao', {
    'funcao': fields.String(required=True)
})

listar_responsaveis_model = api_ms.model('ListarResponsaveis', {
    'id': fields.Integer,
    'id_funcao': fields.Integer,
    'nome': fields.String,
    'email': fields.String,
})

inserir_responsavel_model = api_ms.model('InserirResponsavel', {
    'id_funcao': fields.Integer(required=True),
    'nome': fields.String(required=True),
    'email': fields.String(required=True),
})