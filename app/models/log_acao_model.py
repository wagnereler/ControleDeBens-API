# coding: utf-8
#app/models/log_acao_model.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.extensions import db
from app.models.usuario_model import Usuario
from app.models.rotina_model import Rotina

Base = db.Model

class LogAcao(Base):
    __tablename__ = 'log_acao'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(ForeignKey(Usuario.id), nullable=False)
    id_rotina = Column(ForeignKey(Rotina.id), nullable=False)
    acao = Column(String(255))
    data_acao = Column(Date)
    status = Column(Integer)

    usuario = relationship(Usuario)
    rotina = relationship(Rotina)
