#api/resources/__init__.py
from flask_restx import Namespace
name_space = Namespace('api/v1',
                       description='''Esta é uma API RestFull para uma aplicação de controle de bens''')