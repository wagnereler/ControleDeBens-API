# coding: utf-8
# app/domain/models/logradouro.py
from sqlalchemy import Column, Integer, String, TIMESTAMP, BOOLEAN
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Logradouro(Base):
    __tablename__ = 'logradouro'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(60))
    ativo = Column(BOOLEAN)
    data_cadastro = Column(TIMESTAMP)
    data_alteracao = Column(TIMESTAMP)
