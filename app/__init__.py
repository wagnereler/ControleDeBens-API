#app/__init__.py
from flask import Flask
from app.utils.extensions import api, db, jwt, migrate
from app.utils.import_orm import ImportOrm, ImportOrmMetadados
from app.config import Config
from app.utils.import_resource import model_ms, bens_ns, empresa_ns, gerais_ns, api_ms


app = Flask(__name__)
app.config.from_object(Config)
api.init_app(app)
db.init_app(app)
migrate.init_app(app, db)
api.add_namespace(model_ms, path='/')
api.add_namespace(api_ms, path='/api')
api.add_namespace(bens_ns, path='/api/bens')
api.add_namespace(empresa_ns, path='/api/empresa')
api.add_namespace(gerais_ns, path='/api/gerais')



if __name__ == '__main__':
    app.run()
