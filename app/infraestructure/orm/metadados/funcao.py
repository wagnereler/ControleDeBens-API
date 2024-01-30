#app/infraestructure/orm/metadados/funcao.py
from sqlalchemy import Column, String,  Integer
from app.utils.extensions import db


Base = db.Model
class Funcao(Base):
    __tablename__ = 'funcao'
    __bind_key__ = 'metadados'

    id = Column(Integer, primary_key=True, autoincrement=True)
    funcao = Column(String(60), unique=True, nullable=False)
