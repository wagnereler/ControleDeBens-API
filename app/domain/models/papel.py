# coding: utf-8
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Papel(Base):
    __tablename__ = 'papel'

    id = Column(Integer, primary_key=True)
    id_rotina = Column(Integer)
