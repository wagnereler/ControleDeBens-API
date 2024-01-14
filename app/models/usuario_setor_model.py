# coding: utf-8
# app/models/usuario_setor_model.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.extensions import db
from app.models.setor_model import Setor
from app.models.usuario_model import Usuario

Base = db.Model

class UsuarioSetor(Base):
    __tablename__ = 'usuario_setor'

    id = Column(Integer, primary_key=True)
    id_setor = Column(ForeignKey(Setor.id), nullable=False)
    id_usuario = Column(ForeignKey(Usuario.id), nullable=False)

    setor = relationship(Setor)
    usuario = relationship(Usuario)

