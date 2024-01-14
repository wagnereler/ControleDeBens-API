# coding: utf-8
# app/models/papel_rotina_model.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.extensions import db
from app.models.papel_model import Papel
from app.models.rotina_model import Rotina

Base = db.Model

class PapelRotina(Base):
    __tablename__ = 'papel_rotina'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_papel = Column(ForeignKey(Papel.id), nullable=False)
    id_usuario = Column(Integer)
    rotina_id = Column(ForeignKey(Rotina.id), nullable=False)

    papel = relationship(Papel)
    rotina = relationship(Rotina)

