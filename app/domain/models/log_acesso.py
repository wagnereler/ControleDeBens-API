# coding: utf-8
from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class LogAcesso(Base):
    __tablename__ = 'log_acesso'

    id = Column(Integer, primary_key=True)
    id_usuario = Column(ForeignKey('usuario.id'), nullable=False)
    data_acesso = Column(Date)
    status = Column(Integer)

    usuario = relationship('Usuario')
