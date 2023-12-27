from flask import Flask
from app.infrastructure.database import Database

app = Flask(__name__)

db = Database('postgresql://postgres:dbamv@192.168.1.99:5432/controle_bens')
db.reflect_database()
db.prepare_models()

# Exemplo de uso
Usuario = db.get_model_class('usuario')

# Agora você pode usar a classe User para interagir com o banco de dados
#user = db.session.query(User).filter_by(username='postgres').first()
