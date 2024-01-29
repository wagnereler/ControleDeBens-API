# coding: utf-8
# app/infraestructure/orm/metadados/versao_api.py
from sqlalchemy import Column, String, Text, Integer, Date
from app.utils.extensions import db

Base = db.Model


class ControleVersaoAPI(Base):
    __tablename__ = 'controle_versao_api'
    __bind_key__ = 'metadado'

    id = Column(Integer, primary_key=True, autoincrement=True)
    versao = Column(String(15), unique=True, nullable=False)
    descricao = Column(Text(500), nullable=False)
    responsavel = Column(String(40), nullable=False)
    data_atualizacao = Column(Date, nullable=False)
