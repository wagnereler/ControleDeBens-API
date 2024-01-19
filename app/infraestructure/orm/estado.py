# coding: utf-8
#app/infraestructure/estado.py
from sqlalchemy import Column, Integer, CHAR, String
from app.utils.extensions import db

Base = db.Model

class Estado(Base):
    __tablename__ = 'estado'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uf = Column(CHAR(2), nullable=False)
    nome = Column(String(40), nullable=False)
    codigo_ibge = Column(String(2), nullable=False)
