# coding: utf-8
# app/infraestructure/usuario.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.extensions import db
from app.infraestructure.orm.endereco import Endereco

Base = db.Model

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    usuario = Column(String(40), nullable=False, unique=True)
    email = Column(String(60), nullable=False, unique=True)
    data_cadastro = Column(Date, nullable=False)
    data_atualizacao = Column(Date, nullable=False)
    id_endereco = Column(ForeignKey(Endereco.id), nullable=False)

    endereco = relationship(Endereco)

