# run.py
from app.infrastructure.database import Database

if __name__ == "__main__":
    db = Database()
    db.create_tables()

# Exemplo de uso
#Usuario = db.get_model_class('usuario')

# Agora você pode usar a classe User para interagir com o banco de dados
#user = db.session.query(User).filter_by(username='postgres').first()
