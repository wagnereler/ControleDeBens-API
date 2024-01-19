# coding: utf-8
# app/infraestructure/movimentacao.py
from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.extensions import db
from app.infraestructure.orm.bem import Bem
from app.infraestructure.orm.empresa import Empresa
from app.infraestructure.orm.setor import Setor
from app.infraestructure.orm.usuario import Usuario

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
    setor_saida = relationship(Setor, foreign_keys=[id_setor_saida])
    setor_entrada = relationship(Setor, foreign_keys=[id_setor_entrada])
    empresa_saida = relationship(Empresa, foreign_keys=[id_empresa_saida])
    empresa_entrada = relationship(Empresa, foreign_keys=[id_empresa_entrada])
    usuario = relationship(Usuario)



