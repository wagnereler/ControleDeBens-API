#app/domain/api/controle_versao_service.py
from flask_restx import Namespace, Resource, fields


def get_versao():
    versao = '1.0'
    return versao