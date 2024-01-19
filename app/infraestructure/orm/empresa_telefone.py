# coding: utf-8
#app/infraestructure/empresa_telefone.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.extensions import db
from app.infraestructure.orm.empresa import Empresa
from app.infraestructure.orm.telefone import Telefone

Base = db.Model

class EmpresaTelefone(Base):
    __tablename__ = 'empresa_telefone'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_empresa = Column(ForeignKey(Empresa.id), nullable=False)
    id_telefone = Column(ForeignKey(Telefone.id), nullable=False)

    empresa = relationship(Empresa)
    telefone = relationship(Telefone)

