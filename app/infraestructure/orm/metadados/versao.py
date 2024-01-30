#app/infraestructure/orm/metadados/versao.py
from sqlalchemy import Column, String,  Integer
from app.utils.extensions import db


Base = db.Model
class Versao(Base):
    __tablename__ = 'versao'
    __bind_key__ = 'metadados'

    id = Column(Integer, primary_key=True, autoincrement=True)
    major = Column(Integer,nullable=False)
    minor = Column(Integer, nullable=False)
    patch = Column(Integer, nullable=False)
