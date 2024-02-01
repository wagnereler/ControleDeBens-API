#app/config.py
from os import environ, path

basedir = path.abspath(path.dirname(__file__))

class Config:
    SECRET_KEY = environ.get('SECRET_KEY')
    #SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres:dbamv@192.168.1.99:5432/controle_bens')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{basedir}/infraestructure/data/controle_bens.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = int(environ.get('JWT_ACCESS_TOKEN_EXPIRES', 3600))
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_DEBUG = environ.get('FLASK_DEBUG')
    SQLALCHEMY_BINDS = {
        'metadados': f'sqlite:///{basedir}/infraestructure/data/metadados.db',
    }
    GIT_TOKEN = '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'
    GIT_USER = 'wagnereler'
    GIT_REPOSITORY = 'ControleDeBens-API'
    # GIT_TOKEN = environ.get('GIT_TOKEN')
    # GIT_USER = environ.get('GIT_USER')
    # GIT_REPOSITORY = environ.get('GIT_REPOSITORY')