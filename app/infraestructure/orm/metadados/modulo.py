#app/infraestructure/orm/metadados/modulo.py
from sqlalchemy import Column, String,  Integer
from app.utils.extensions import db


Base = db.Model
class Modulo(Base):
    __tablename__ = 'modulo'
    __bind_key__ = 'metadados'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(80), unique=True, nullable=False)
