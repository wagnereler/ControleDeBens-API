# coding: utf-8
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .empresa import Empresa
from .usuario import Usuario

Base = declarative_base()

class EmpresaUsuario(Base):
    __tablename__ = 'empresa_usuario'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_empresa = Column(ForeignKey(Empresa.id), nullable=False)
    id_usuario = Column(ForeignKey(Usuario.id), nullable=False)
    empresa_id1 = Column(Integer, nullable=False)

    empresa = relationship(Empresa)
    usuario = relationship(Usuario)
