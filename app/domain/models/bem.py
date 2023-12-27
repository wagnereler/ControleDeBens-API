# coding: utf-8
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Numeric, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Bem(Base):
    __tablename__ = 'bem'

    id = Column(Integer, primary_key=True, server_default=text("nextval('bem_id_seq'::regclass)"))
    id_setor = Column(ForeignKey('setor.id'), nullable=False)
    id_empresa = Column(ForeignKey('empresa.id'), nullable=False)
    plaqueta = Column(String(30))
    data_compra = Column(Date)
    data_tombamento = Column(Date)
    data_baixa = Column(Date)
    valor_compra = Column(Numeric(10, 2))
    valor_depreciado = Column(Numeric(10, 2))
    valor_contabil = Column(Numeric(10, 2))

    empresa = relationship('Empresa')
    setor = relationship('Setor')
