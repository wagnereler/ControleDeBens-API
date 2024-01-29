# coding: utf-8
#app/infraestructure/orm/controle_bens/log_acao.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.extensions import db
from app.infraestructure.orm.controlde_bens.usuario import Usuario
from app.infraestructure.orm.controlde_bens.empresa import Empresa
from app.infraestructure.orm.controlde_bens.rotina import Rotina

Base = db.Model

class LogAcao(Base):
    __tablename__ = 'log_acao'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(ForeignKey(Usuario.id), nullable=False)
    id_empresa = Column(ForeignKey(Empresa.id), nullable=False)
    id_rotina = Column(ForeignKey(Rotina.id), nullable=False)
    acao = Column(String(255), nullable=False)
    data_acao = Column(Date, nullable=False)
    status = Column(Integer, nullable=False, comment="1 = Sucesso, 2 = Falha, 3 = Não autorizado")


    usuario = relationship(Usuario)
    rotina = relationship(Rotina)
    empresa = relationship(Empresa)


