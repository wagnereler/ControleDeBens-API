# app/services/database_service.py
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from app.config.data_base import CONFIG_POSTGRES, AMBIENTE

HOST = CONFIG_POSTGRES[AMBIENTE]['HOST']
PORTA = CONFIG_POSTGRES[AMBIENTE]['PORTA']
DATABASE = CONFIG_POSTGRES[AMBIENTE]['DATABASE']
USUARIO = CONFIG_POSTGRES[AMBIENTE]['USUARIO']
SENHA = CONFIG_POSTGRES[AMBIENTE]['SENHA']

class DatabaseService:
    def __init__(self):
        self.engine = create_engine(f'postgresql://{USUARIO}:{SENHA}@{HOST}:{PORTA}/{DATABASE}')
        self.Session = sessionmaker(bind=self.engine)
        self.metadata = MetaData(bind=self.engine)

    def get_session(self):
        return self.Session()

    def execute_query(self, query):
        with self.engine.connect() as connection:
            result = connection.execute(query)
            return result

    def insert_entity(self, session, entity):
        session.add(entity)
        session.commit()

    def update_entity(self, session, entity):
        session.merge(entity)
        session.commit()

    def delete_entity(self, session, entity):
        session.delete(entity)
        session.commit()

    def query_entity(self, session, entity_type, filters=None):
        query = session.query(entity_type)
        if filters:
            query = query.filter_by(**filters)
        return query.all()
