# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Logradouro(Base):
    __tablename__ = 'logradouro'

    id = Column(Integer, primary_key=True)
    nome = Column(String(60))
    codigo_ibge = Column(String(3))
