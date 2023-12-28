# coding: utf-8
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .logradouro import Logradouro
from .municipio import Municipio
from .estado import Estado

Base = declarative_base()

class Endereco(Base):
    __tablename__ = 'endereco'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_municipio = Column(ForeignKey(Municipio.id), nullable=False)
    id_estado = Column(ForeignKey(Estado.id), nullable=False)
    id_logradouro = Column(ForeignKey(Logradouro.id), nullable=False)
    endereco = Column(String(60))
    numero = Column(String(10))
    complemento = Column(String(60))
    bairro = Column(String(60))
    cep = Column(String(8))

    estado = relationship(Estado)
    logradouro = relationship(Logradouro)
    municipio = relationship(Municipio)
