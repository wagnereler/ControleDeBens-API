FLASK_APP=app.py
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=MinhaSenhaParaCookies
SQLALCHEMY_DATABASE_URI=postgresql://postgres:dbamv@192.168.1.99:5432/controle_bens
SQLALCHEMY_TRACK_MODIFICATIONS=True
JWT_SECRET_KEY=MinhaSenhaSecretaParaJWT
JWT_ACCESS_TOKEN_EXPIRES=3600
SQLALCHEMY_BINDS = {
    'metadado': f'sqlite:///{basedir}/infraestructure/data/metadado.db',
}