# coding: utf-8
# app/infraestructure/orm/controle_bens/telefone.py
from sqlalchemy import Column, Integer, String, text
from app.utils.extensions import db

Base = db.Model
metadata = Base.metadata


class Telefone(Base):
    __tablename__ = 'telefone'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ddi = Column(String(4), nullable=False)
    ddd = Column(String(2), nullable=False)
    numero = Column(String(9), nullable=False)
    tipo = Column(Integer, nullable=False)
