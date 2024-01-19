# app/domain/gerais/telefone_service.py
from app.infraestructure.orm.telefone import Telefone
from app.utils.extensions import db


def inserir_telefone(ddi: str,
                     ddd: str,
                     numero: str,
                     tipo: int):
    telefone = Telefone()
    telefone.ddi = ddi
    telefone.ddd = ddd
    telefone.numero = numero
    telefone.tipo = tipo

    db.session.add(telefone)
    db.session.commit()
    return telefone


def obter_telefones():
    return Telefone.query.all()


def obter_telefone_por_id(id):
    return Telefone.query.filter_by(id)
