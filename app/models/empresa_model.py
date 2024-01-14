# coding: utf-8
#app/models/empresa_model.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.extensions import db
from app.models.endereco_model import Endereco

Base = db.Model

class Empresa(Base):
    __tablename__ = 'empresa'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_fantasia = Column(String(60))
    razao_social = Column(String(100))
    cnpj = Column(String(14))
    id_endereco = Column(ForeignKey(Endereco.id), nullable=False)

    endereco = relationship(Endereco)

