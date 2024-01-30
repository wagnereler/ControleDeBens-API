#app/domain/__init__.py
from flask_restx import Namespace, Resource, fields
api_ms = Namespace('api', description='''Esta é uma API RestFull para uma aplicação de controle de bens''')

