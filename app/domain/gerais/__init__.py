# app/domain/gerais/__init__.py
from flask_restx import Namespace
from app.domain import api_ms

gerais_ns = Namespace('gerais', description='''gerais''',)
