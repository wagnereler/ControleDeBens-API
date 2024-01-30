# coding: utf-8
# app/infraestructure/orm/metadados/controle_versao.py
from sqlalchemy import Column, String, Text, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.infraestructure.orm.metadados.modulo import Modulo
from app.utils.extensions import db
from app.infraestructure.orm.metadados.responsavel import Responsavel

Base = db.Model


class ControleVersao(Base):
    __tablename__ = 'controle_versao'
    __bind_key__ = 'metadados'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_responsavel = Column(ForeignKey(Responsavel.id))
    id_modulo = Column(ForeignKey(Modulo.id))
    versao = Column(String(15), unique=True, nullable=False)
    descricao = Column(Text(500), nullable=False)
    data_commit = Column(Date, nullable=False)

    responsavel = relationship(Responsavel)
    modulo = relationship(Modulo)
