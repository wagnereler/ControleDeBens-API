# coding: utf-8
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Empresa(Base):
    __tablename__ = 'empresa'

    id = Column(Integer, primary_key=True)
    nome_fantasia = Column(String(60))
    razao_social = Column(String(100))
    cnpj = Column(String(14))
    id_endereco = Column(ForeignKey('endereco.id'), nullable=False)
    id_telefone = Column(Integer)

    endereco = relationship('Endereco')

