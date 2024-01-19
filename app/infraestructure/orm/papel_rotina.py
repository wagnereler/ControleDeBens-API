# coding: utf-8
# app/infraestructure/papel_rotina.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.extensions import db
from app.infraestructure.orm.papel import Papel
from app.infraestructure.orm.rotina import Rotina

Base = db.Model

class PapelRotina(Base):
    __tablename__ = 'papel_rotina'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_papel = Column(ForeignKey(Papel.id), nullable=False)
    id_rotina = Column(ForeignKey(Rotina.id), nullable=False)

    papel = relationship(Papel)
    rotina = relationship(Rotina)

