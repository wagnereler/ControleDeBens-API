# coding: utf-8
#app/models/log_acesso_model.py
from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.extensions import db
from app.models.usuario_model import Usuario

Base = db.Model

class LogAcesso(Base):
    __tablename__ = 'log_acesso'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(ForeignKey(Usuario.id), nullable=False)
    data_acesso = Column(Date)
    status = Column(Integer)

    usuario = relationship(Usuario)
