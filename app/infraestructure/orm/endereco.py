# coding: utf-8
#app/infraestructure/orm/endereco.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.extensions import db
from app.infraestructure.orm.logradouro import Logradouro
from app.infraestructure.orm.municipio import Municipio
from app.infraestructure.orm.estado import Estado

Base = db.Model

class Endereco(Base):
    __tablename__ = 'endereco'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_municipio = Column(ForeignKey(Municipio.id), nullable=False)
    id_estado = Column(ForeignKey(Estado.id), nullable=False)
    id_logradouro = Column(ForeignKey(Logradouro.id), nullable=False)
    endereco = Column(String(60), nullable=False)
    numero = Column(String(10), nullable=False)
    complemento = Column(String(60))
    bairro = Column(String(60), nullable=False)
    cep = Column(String(8), nullable=False)

    estado = relationship(Estado)
    logradouro = relationship(Logradouro)
    municipio = relationship(Municipio)
