#app/domain/empresa/__init__.py
from flask_restx import Namespace
empresa_ns = Namespace('empresas', description='''empresas''')