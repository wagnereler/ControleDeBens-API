# coding: utf-8
#app/models/empresa_usuario_model.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.extensions import db
from app.models.empresa_model import Empresa
from app.models.usuario_model import Usuario

Base = db.Model

class EmpresaUsuario(Base):
    __tablename__ = 'empresa_usuario'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_empresa = Column(ForeignKey(Empresa.id), nullable=False)
    id_usuario = Column(ForeignKey(Usuario.id), nullable=False)
    empresa_id1 = Column(Integer, nullable=False)

    empresa = relationship(Empresa)
    usuario = relationship(Usuario)
