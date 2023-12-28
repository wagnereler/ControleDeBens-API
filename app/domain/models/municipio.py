# coding: utf-8
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .estado import Estado

Base = declarative_base()

class Municipio(Base):
    __tablename__ = 'municipio'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_estado = Column(ForeignKey(Estado.id), nullable=False)
    nome = Column(String(100))
    codigo_ibge = Column(String(8))

    estado = relationship(Estado)
