# coding: utf-8
# app/infraestructure/orm/metadados/controle_versao.py
from sqlalchemy import Column, String, Text, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.utils.extensions import db
from app.infraestructure.orm.metadados.responsavel import Responsavel

Base = db.Model


class ControleVersao(Base):
    __tablename__ = 'controle_versao_api'
    __bind_key__ = 'metadados'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_responsavel = Column(ForeignKey(Responsavel.id))
    versao = Column(String(15), unique=True, nullable=False)
    descricao = Column(Text(500), nullable=False)
    responsavel = Column(String(40), nullable=False)
    data_atualizacao = Column(Date, nullable=False)

    responsavel = relationship(Responsavel)
