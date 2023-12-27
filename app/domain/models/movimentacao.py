# coding: utf-8
from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Movimentacao(Base):
    __tablename__ = 'movimentacao'

    id = Column(Integer, primary_key=True)
    id_bem = Column(ForeignKey('bem.id'), nullable=False)
    data_movimentacao = Column(Date)
    id_setor_saida = Column(ForeignKey('setor.id'), nullable=False)
    id_setor_entrada = Column(ForeignKey('setor.id'), nullable=False)
    id_empresa_saida = Column(ForeignKey('empresa.id'), nullable=False)
    id_empresa_entrada = Column(ForeignKey('empresa.id'), nullable=False)
    id_usuario = Column(ForeignKey('usuario.id'), nullable=False)

    bem = relationship('Bem')
    empresa = relationship('Empresa', primaryjoin='Movimentacao.id_empresa_entrada == Empresa.id')
    empresa_saida = relationship('Empresa', primaryjoin='Movimentacao.id_empresa_saida == Empresa.id')
    setor_entrada = relationship('Setor', primaryjoin='Movimentacao.id_setor_entrada == Setor.id')
    setor_saida = relationship('Setor', primaryjoin='Movimentacao.id_setor_saida == Setor.id')
    usuario = relationship('Usuario')
