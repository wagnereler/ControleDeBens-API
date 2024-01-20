# coding: utf-8
#app/infraestructure/log_acesso.py
from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.extensions import db
from app.infraestructure.orm.usuario import Usuario
from app.infraestructure.orm.empresa import Empresa
Base = db.Model

class LogAcesso(Base):
    __tablename__ = 'log_acesso'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(ForeignKey(Usuario.id), nullable=False)
    id_empresa = Column(ForeignKey(Empresa.id), nullable=False)
    data_acesso = Column(Date)
    status = Column(Integer)

    usuario = relationship(Usuario)
    empresa = relationship(Empresa)