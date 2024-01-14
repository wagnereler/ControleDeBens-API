# coding: utf-8
# app/models/usuario_papel_model.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.extensions import db
from app.models.papel_model import Papel
from app.models.usuario_model import Usuario

Base = db.Model

class UsuarioPapel(Base):
    __tablename__ = 'usuario_papel'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(ForeignKey(Usuario.id), nullable=False)
    id_papel = Column(ForeignKey(Papel.id), nullable=False)

    papel = relationship(Papel)
    usuario = relationship(Usuario)
