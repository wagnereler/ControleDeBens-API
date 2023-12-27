# coding: utf-8
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EmpresaUsuario(Base):
    __tablename__ = 'empresa_usuario'

    id = Column(Integer, primary_key=True)
    id_empresa = Column(ForeignKey('empresa.id'), nullable=False)
    id_usuario = Column(ForeignKey('usuario.id'), nullable=False)
    empresa_id1 = Column(Integer, nullable=False)

    empresa = relationship('Empresa')
    usuario = relationship('Usuario')
