# coding: utf-8
# app/domain/models/usuario_setor.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .setor import Setor
from .usuario import Usuario

Base = declarative_base()

class UsuarioSetor(Base):
    __tablename__ = 'usuario_setor'

    id = Column(Integer, primary_key=True)
    id_setor = Column(ForeignKey(Setor.id), nullable=False)
    id_usuario = Column(ForeignKey(Usuario.id), nullable=False)

    setor = relationship(Setor)
    usuario = relationship(Usuario)

