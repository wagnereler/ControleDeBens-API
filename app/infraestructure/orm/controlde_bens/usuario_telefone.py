# coding: utf-8
# app/infraestructure/orm/controle_bens/usuario_telefone.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.extensions import db
from app.infraestructure.orm.controlde_bens.telefone import Telefone
from app.infraestructure.orm.controlde_bens.usuario import Usuario

Base = db.Model

class UsuarioTelefone(Base):
    __tablename__ = 'usuario_telefone'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(ForeignKey(Usuario.id), nullable=False)
    id_telefone = Column(ForeignKey(Telefone.id), nullable=False)
    telefone_id = Column(Integer, nullable=False)

    telefone = relationship(Telefone)
    usuario = relationship(Usuario)
