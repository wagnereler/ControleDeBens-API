# coding: utf-8
# app/models/logradouro_model.py

from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime, Integer
from app.utils.extensions import db

Base = db.Model

class Logradouro(Base):
    __tablename__ = 'logradouro'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    ativo = Column(Boolean)
    data_cadastro = Column(DateTime)
    data_alteracao = Column(DateTime)

    def __init__(self, nome, ativo, data_cadastro=None, data_alteracao=None):
        self.nome = nome
        self.ativo = ativo
        self.data_cadastro = data_cadastro or datetime.now()
        self.data_alteracao = data_alteracao or datetime.now()

    def serialize(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'ativo': self.ativo,
            'data_cadastro': str(self.data_cadastro),
            'data_alteracao': str(self.data_alteracao),
        }
