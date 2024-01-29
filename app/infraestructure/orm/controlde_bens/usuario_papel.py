# coding: utf-8
# app/infraestructure/orm/controle_bens/usuario_papel.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.extensions import db
from app.infraestructure.orm.controlde_bens.papel import Papel
from app.infraestructure.orm.controlde_bens.usuario import Usuario

Base = db.Model

class UsuarioPapel(Base):
    __tablename__ = 'usuario_papel'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(ForeignKey(Usuario.id), nullable=False)
    id_papel = Column(ForeignKey(Papel.id), nullable=False)

    papel = relationship(Papel)
    usuario = relationship(Usuario)
