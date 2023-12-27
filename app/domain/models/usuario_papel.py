# coding: utf-8
# coding: utf-8
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UsuarioPapel(Base):
    __tablename__ = 'usuario_papel'

    id = Column(Integer, primary_key=True)
    id_usuario = Column(ForeignKey('usuario.id'), nullable=False)
    id_papel = Column(ForeignKey('papel.id'), nullable=False)

    papel = relationship('Papel')
    usuario = relationship('Usuario')
