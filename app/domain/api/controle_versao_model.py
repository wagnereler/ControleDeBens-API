#app/domain/api/controle_versao_model.py
from flask_restx import Namespace, Resource, fields
from app.domain.api import api_ms

versao_model = api_ms.model('Versao', {
    'versao': fields.String(),
})