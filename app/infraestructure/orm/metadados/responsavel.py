#app/infraestructure/orm/metadados/responsavel.py
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.extensions import db
from app.infraestructure.orm.metadados.funcao import Funcao

Base = db.Model
class Responsavel(Base):
    __tablename__ = 'responsavel'
    __bind_key__ = 'metadados'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_funcao = Column(ForeignKey(Funcao.id), nullable=False)
    nome = Column(String(60), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    funcao = relationship(Funcao)
