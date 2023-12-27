# coding: utf-8
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Setor(Base):
    __tablename__ = 'setor'

    id = Column(Integer, primary_key=True)
    id_empresa = Column(ForeignKey('empresa.id'), nullable=False)
    nome = Column(String(100))

    empresa = relationship('Empresa')

