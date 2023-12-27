# coding: utf-8
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UsuarioSetor(Base):
    __tablename__ = 'usuario_setor'

    id = Column(Integer, primary_key=True)
    id_setor = Column(ForeignKey('setor.id'), nullable=False)
    id_usuario = Column(ForeignKey('usuario.id'), nullable=False)

    setor = relationship('Setor')
    usuario = relationship('Usuario')

