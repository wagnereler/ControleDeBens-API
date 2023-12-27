# coding: utf-8
from sqlalchemy import Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Telefone(Base):
    __tablename__ = 'telefone'

    id = Column(Integer, primary_key=True)
    ddi = Column(String(4), server_default=text("'+55'::character varying"))
    dd = Column(String(2))
    numero = Column(String(9))
    tipo = Column(Integer)
