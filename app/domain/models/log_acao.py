# coding: utf-8
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class LogAcao(Base):
    __tablename__ = 'log_acao'

    id = Column(Integer, primary_key=True)
    id_usuario = Column(ForeignKey('usuario.id'), nullable=False)
    id_rotina = Column(Integer)
    acao = Column(String(255))
    data_acao = Column(Date)
    status = Column(Integer)

    usuario = relationship('Usuario')
