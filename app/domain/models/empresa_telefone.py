# coding: utf-8
#app/domain/models/empresa_telefone.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .empresa import Empresa
from .telefone import Telefone

Base = declarative_base()

class EmpresaTelefone(Base):
    __tablename__ = 'empresa_telefone'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_empresa = Column(ForeignKey(Empresa.id), nullable=False)
    id_telefone = Column(Integer)
    telefone_id = Column(ForeignKey(Telefone.id), nullable=False)

    empresa = relationship(Empresa)
    telefone = relationship(Telefone)

