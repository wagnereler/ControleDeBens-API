# coding: utf-8
# app/infraestructure/logradouro.py

from datetime import datetime
from sqlalchemy import Column, String, Boolean, Integer
from app.utils.extensions import db

Base = db.Model

class Logradouro(Base):
    __tablename__ = 'logradouro'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    ativo = Column(Boolean, nullable=False)
