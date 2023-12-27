# coding: utf-8
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PapelRotina(Base):
    __tablename__ = 'papel_rotina'

    id = Column(Integer, primary_key=True)
    id_papel = Column(ForeignKey('papel.id'), nullable=False)
    id_usuario = Column(Integer)
    rotina_id = Column(ForeignKey('rotina.id'), nullable=False)

    papel = relationship('Papel')
    rotina = relationship('Rotina')

