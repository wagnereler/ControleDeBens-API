# coding: utf-8
# app/models/rotina_model.py
from sqlalchemy import Column, Integer, String
from app.utils.extensions import db

Base = db.Model
metadata = Base.metadata


class Rotina(Base):
    __tablename__ = 'rotina'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(60))