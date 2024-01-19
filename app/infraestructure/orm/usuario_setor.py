# coding: utf-8
# app/infraestructure/usuario_setor.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.extensions import db
from app.infraestructure.orm.setor import Setor
from app.infraestructure.orm.usuario import Usuario

Base = db.Model

class UsuarioSetor(Base):
    __tablename__ = 'usuario_setor'

    id = Column(Integer, primary_key=True)
    id_setor = Column(ForeignKey(Setor.id), nullable=False)
    id_usuario = Column(ForeignKey(Usuario.id), nullable=False)

    setor = relationship(Setor)
    usuario = relationship(Usuario)

