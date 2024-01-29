# coding: utf-8
#app/infraestructure/orm/controle_bens/empresa_usuario.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.extensions import db
from app.infraestructure.orm.controlde_bens.empresa import Empresa
from app.infraestructure.orm.controlde_bens.usuario import Usuario

Base = db.Model

class EmpresaUsuario(Base):
    __tablename__ = 'empresa_usuario'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_empresa = Column(ForeignKey(Empresa.id), nullable=False)
    id_usuario = Column(ForeignKey(Usuario.id), nullable=False)

    empresa = relationship(Empresa)
    usuario = relationship(Usuario)
