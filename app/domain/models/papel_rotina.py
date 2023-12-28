# coding: utf-8
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .papel import Papel
from .rotina import Rotina

Base = declarative_base()

class PapelRotina(Base):
    __tablename__ = 'papel_rotina'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_papel = Column(ForeignKey(Papel.id), nullable=False)
    id_usuario = Column(Integer)
    rotina_id = Column(ForeignKey(Rotina.id), nullable=False)

    papel = relationship(Papel)
    rotina = relationship(Rotina)

