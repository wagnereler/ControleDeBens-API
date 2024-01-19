# coding: utf-8
# app/infraestructure/municipio.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.extensions import db
from app.infraestructure.orm.estado import Estado

Base = db.Model

class Municipio(Base):
    __tablename__ = 'municipio'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_estado = Column(ForeignKey(Estado.id), nullable=False)
    nome = Column(String(100))
    codigo_ibge = Column(String(8))

    estado = relationship(Estado)
