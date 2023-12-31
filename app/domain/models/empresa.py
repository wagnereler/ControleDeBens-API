# coding: utf-8
#app/domain/models/empresa.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .endereco import Endereco

Base = declarative_base()

class Empresa(Base):
    __tablename__ = 'empresa'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_fantasia = Column(String(60))
    razao_social = Column(String(100))
    cnpj = Column(String(14))
    id_endereco = Column(ForeignKey(Endereco.id), nullable=False)

    endereco = relationship(Endereco)

