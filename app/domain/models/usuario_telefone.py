# coding: utf-8
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UsuarioTelefone(Base):
    __tablename__ = 'usuario_telefone'

    id = Column(Integer, primary_key=True)
    id_usuario = Column(ForeignKey('usuario.id'), nullable=False)
    id_telefone = Column(ForeignKey('telefone.id'), nullable=False)
    telefone_id = Column(Integer, nullable=False)

    telefone = relationship('Telefone')
    usuario = relationship('Usuario')
