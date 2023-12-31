# coding: utf-8
# app/domain/models/movimentacao.py
from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .bem import Bem
from .empresa import Empresa
from .setor import Setor
from .usuario import Usuario

Base = declarative_base()

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
