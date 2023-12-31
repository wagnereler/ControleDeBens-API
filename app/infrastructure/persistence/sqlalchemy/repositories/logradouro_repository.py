# app/infrastructure/persistence/sqlalchemy/repositories/logradouro_repository.py
from app.infrastructure.persistence.sqlalchemy.database import db_session
from app.domain.models.logradouro import Logradouro

class LogradouroRepository:
    def create(self, logradouro):
        db_session.add(logradouro)
        db_session.commit()
        return logradouro

    def get_by_id(self, logradouro_id):
        return Logradouro.query.get(logradouro_id)

    def update(self, logradouro):
        db_session.merge(logradouro)
        db_session.commit()
        return logradouro
