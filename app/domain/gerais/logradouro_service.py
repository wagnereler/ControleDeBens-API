# app/domain/gerais/logradouro_service.py
from app.infraestructure.orm.controlde_bens.logradouro import Logradouro
from app.utils.extensions import db


def inserir_logradouro(nome: str, ativo: bool):

    logradouro = Logradouro()
    logradouro.nome = nome
    logradouro.ativo = ativo

    db.session.add(logradouro)
    db.session.commit()
    return logradouro


def obter_logradouros():
    return Logradouro.query.all()


def obter_logradouro_por_id(id):
    return Logradouro.query.filter_by(id)
