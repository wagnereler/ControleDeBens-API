from flask import Flask
from app.utils.extensions import api, db, jwt, migrate
from app.utils.import_models import ImportModels
from app.config import Config
from app.resources import name_space
from app.utils.import_resource import ImportResource
from flask import jsonify

app = Flask(__name__)
app.config.from_object(Config)
api.init_app(app)
db.init_app(app)
migrate.init_app(app, db)
api.add_namespace(name_space)


if __name__ == '__main__':
    app.run()
