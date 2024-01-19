# coding: utf-8
# app/infraestructure/papel.py
from sqlalchemy import Column, Integer, String
from app.utils.extensions import db

Base = db.Model
metadata = Base.metadata


class Papel(Base):
    __tablename__ = 'papel'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(60), nullable=False)

