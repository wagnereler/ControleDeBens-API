# app/domain/gerais/__init__.py
from flask_restx import Namespace
from app.domain import model_ms

gerais_ns = Namespace('gerais', description='''gerais''',)
