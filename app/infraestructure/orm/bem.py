# coding: utf-8
#app/infraestructure/empresa.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.utils.extensions import db
from app.infraestructure.orm.empresa import Empresa
from app.infraestructure.orm.setor import Setor

Base = db.Model

class Bem(Base):
    __tablename__ = 'bem'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_setor = Column(ForeignKey(Setor.id), nullable=False)
    id_empresa = Column(ForeignKey(Empresa.id), nullable=False)
    nome = Column(String(100))
    plaqueta = Column(String(30))
    data_compra = Column(Date)
    data_tombamento = Column(Date)
    data_baixa = Column(Date)
    valor_compra = Column(Numeric(10, 2))
    valor_depreciado = Column(Numeric(10, 2))
    valor_contabil = Column(Numeric(10, 2))

    empresa = relationship(Empresa)
    setor = relationship(Setor)
