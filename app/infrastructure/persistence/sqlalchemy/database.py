# app/infrastructure/persistence/sqlalchemy/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.config.data_base import AMBIENTE, CONFIG_POSTGRES

# Configuração do banco de dados
config = CONFIG_POSTGRES[AMBIENTE]
DATABASE_URL = f"postgresql://{config['USUARIO']}:{config['SENHA']}@{config['HOST']}:{config['PORTA']}/{config['DATABASE']}"
engine = create_engine(DATABASE_URL)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Database = declarative_base()
Database.query = db_session.query_property()

def init_db():
    Database.metadata.create_all(bind=engine)
