# coding: utf-8
#app/domain/models/log_acesso.py
from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .usuario import Usuario

Base = declarative_base()

class LogAcesso(Base):
    __tablename__ = 'log_acesso'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(ForeignKey(Usuario.id), nullable=False)
    data_acesso = Column(Date)
    status = Column(Integer)

    usuario = relationship(Usuario)
