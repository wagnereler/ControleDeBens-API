# coding: utf-8
# app/models/telefone_model.py
from sqlalchemy import Column, Integer, String, text
from app.utils.extensions import db

Base = db.Model
metadata = Base.metadata


class Telefone(Base):
    __tablename__ = 'telefone'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ddi = Column(String(4), server_default=text("'+55'::character varying"))
    dd = Column(String(2))
    numero = Column(String(9))
    tipo = Column(Integer)
