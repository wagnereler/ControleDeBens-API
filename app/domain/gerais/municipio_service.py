# app/domain/gerais/municipio_service.py
from app.infraestructure.orm.municipio import Municipio
from app.utils.extensions import db


def inserir_municipio(ddi: str,
                     ddd: str,
                     numero: str,
                     tipo: int):
    municipio = Municipio()
    municipio.ddi = ddi
    municipio.ddd = ddd
    municipio.numero = numero
    municipio.tipo = tipo

    db.session.add(municipio)
    db.session.commit()
    return municipio


def obter_municipios():
    return Municipio.query.all()


def obter_municipio_por_id(id):
    return Municipio.query.filter_by(id)
