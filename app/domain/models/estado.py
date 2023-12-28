# coding: utf-8
from sqlalchemy import Column, Integer, CHAR, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Estado(Base):
    __tablename__ = 'estado'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uf = Column(CHAR(2))
    nome = Column(String(40))
    codigo_ibge = Column(String(2))
