# main.py
from app.infrastructure.persistence.sqlalchemy.database import Database

if __name__ == "__main__":
    db = Database()
    db.create_tables()
