# coding: utf-8
# app/infraestructure/setor.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.extensions import db
from app.infraestructure.orm.empresa import Empresa

Base = db.Model

class Setor(Base):
    __tablename__ = 'setor'

    id = Column(Integer, primary_key=True)
    id_empresa = Column(ForeignKey(Empresa.id), nullable=False)
    nome = Column(String(100))

    empresa = relationship(Empresa)

