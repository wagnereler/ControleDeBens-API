# coding: utf-8
#app/infraestructure/orm/empresa.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.extensions import db
from app.infraestructure.orm.endereco import Endereco

Base = db.Model

class Empresa(Base):
    __tablename__ = 'empresa'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_fantasia = Column(String(60), nullable=False)
    razao_social = Column(String(100), nullable=False)
    cnpj = Column(String(14), unique=True, nullable=False)
    id_endereco = Column(ForeignKey(Endereco.id), nullable=False)

    endereco = relationship(Endereco)

