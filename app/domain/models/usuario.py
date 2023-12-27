# coding: utf-8
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, server_default=text("nextval('usuario_id_seq'::regclass)"))
    nome = Column(String(100), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    usuario = Column(String(40), nullable=False, unique=True)
    email = Column(String(60), nullable=False, unique=True)
    id_endereco = Column(ForeignKey('endereco.id'), nullable=False)
    data_cadastro = Column(Date)
    data_atualizacao = Column(Date)

    endereco = relationship('Endereco')
