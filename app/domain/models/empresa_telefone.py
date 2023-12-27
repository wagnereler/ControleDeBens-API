# coding: utf-8
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EmpresaTelefone(Base):
    __tablename__ = 'empresa_telefone'

    id = Column(Integer, primary_key=True)
    id_empresa = Column(ForeignKey('empresa.id'), nullable=False)
    id_telefone = Column(Integer)
    telefone_id = Column(ForeignKey('telefone.id'), nullable=False)

    empresa = relationship('Empresa')
    telefone = relationship('Telefone')

