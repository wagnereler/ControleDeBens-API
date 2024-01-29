# app/domain/gerais/estado_service.py
from app.infraestructure.orm.controlde_bens.estado import Estado
from app.utils.extensions import db


def inserir_estado(uf: str, nome: str, codigo_ibge: str):

    estado = Estado()
    estado.uf = uf
    estado.nome = nome
    estado.codigo_ibge = codigo_ibge

    db.session.add(estado)
    db.session.commit()
    return estado


def obter_estados():
    return Estado.query.all()


def obter_estado_por_id(id):
    return Estado.query.filter_by(id)
