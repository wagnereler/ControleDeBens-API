# coding: utf-8
#app/infraestructure/log_acao.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.extensions import db
from app.infraestructure.orm.usuario import Usuario
from app.infraestructure.orm.rotina import Rotina

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
