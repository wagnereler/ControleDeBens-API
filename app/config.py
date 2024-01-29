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
    #rescentemente incluir essa instrução abaixo, na esperanca de criar um novo banco
    SQLALCHEMY_BINDS = {
        'metadado': f'sqlite:///{basedir}/infraestructure/data/metadado.db',
    }


"""    CASO TENHA NECESSIDADE DE USAR OUTRO BANCOS PARA CONEXÃO
    SQLALCHEMY_BINDS = {
        'outro_banco': os.environ.get('OUTRO_BANCO_URI', 'sqlite:///outro_banco.db'),
        'terceiro_banco': os.environ.get('TERCEIRO_BANCO_URI', 'postgresql://usuario:senha@localhost/terceiro_banco')
    }
"""