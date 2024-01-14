# coding: utf-8
# app/models/movimentacao_model.py
from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.extensions import db
from app.models.bem_model import Bem
from app.models.empresa_model import Empresa
from app.models.setor_model import Setor
from app.models.usuario_model import Usuario

Base = db.Model

class Movimentacao(Base):
    __tablename__ = 'movimentacao'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_bem = Column(ForeignKey(Bem.id), nullable=False)
    data_movimentacao = Column(Date)
    id_setor_saida = Column(ForeignKey(Setor.id), nullable=False)
    id_setor_entrada = Column(ForeignKey(Setor.id), nullable=False)
    id_empresa_saida = Column(ForeignKey(Empresa.id), nullable=False)
    id_empresa_entrada = Column(ForeignKey(Empresa.id), nullable=False)
    id_usuario = Column(ForeignKey(Usuario.id), nullable=False)

    bem = relationship(Bem)
    empresa = relationship(Empresa)
    empresa_saida = relationship(Empresa)
    setor_entrada = relationship(Setor)
    setor_saida = relationship(Setor)
    usuario = relationship(Usuario)
