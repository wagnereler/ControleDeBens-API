# coding: utf-8
# app/domain/models/rotina.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Rotina(Base):
    __tablename__ = 'rotina'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(60))
