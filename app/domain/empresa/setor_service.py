#app/domain/empresa/setor_service.py
from app.infraestructure.orm.controlde_bens.setor import Setor
from app.utils.extensions import db


def inserir_setor(nome: str, id_empresa: int):
    setor = Setor()
    setor.nome = nome
    setor.id_empresa = id_empresa
    db.session.add(setor)
    db.session.commit()
    return setor

def obter_setores():
    return Setor.query.all()

def obter_setor_por_empresa_id(id_empresa):
    return Setor.query.filter_by(id_empresa=id_empresa)

def obter_setor_por_descricao(nome):
    return Setor.query.filter_by(nome=nome)
