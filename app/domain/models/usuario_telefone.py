# coding: utf-8
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .telefone import Telefone
from .usuario import Usuario

Base = declarative_base()

class UsuarioTelefone(Base):
    __tablename__ = 'usuario_telefone'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(ForeignKey(Usuario.id), nullable=False)
    id_telefone = Column(ForeignKey(Telefone.id), nullable=False)
    telefone_id = Column(Integer, nullable=False)

    telefone = relationship(Telefone)
    usuario = relationship(Usuario)
