# app/infrastructure/database.py
from sqlalchemy import MetaData

from app.services.database_service import DatabaseService

class Database:
    def __init__(self):
        self.service = DatabaseService()
        self.metadata = MetaData(bind=self.service.engine)

    def create_tables(self):
        self.service.create_tables()

    def get_session(self):
        return self.service.get_session()
