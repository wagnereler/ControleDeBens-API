# coding: utf-8
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Endereco(Base):
    __tablename__ = 'endereco'

    id = Column(Integer, primary_key=True)
    id_empresa = Column(Integer)
    id_usuario = Column(Integer)
    id_municipio = Column(ForeignKey('municipio.id'), nullable=False)
    id_estado = Column(ForeignKey('estado.id'), nullable=False)
    id_logradouro = Column(ForeignKey('logradouro.id'), nullable=False)
    endereco = Column(String(60))
    numero = Column(String(10))
    complemento = Column(String(60))
    bairro = Column(String(60))
    cep = Column(String(8))

    estado = relationship('Estado')
    logradouro = relationship('Logradouro')
    municipio = relationship('Municipio')
