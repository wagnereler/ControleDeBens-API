# app/domain/gerais/municipio_service.py
from app.infraestructure.orm.municipio import Municipio
from app.utils.extensions import db


def inserir_municipio(id_estado: int,
                     nome: str,
                     condigo_ibge: str):
    municipio = Municipio()
    municipio.id_estado = id_estado
    municipio.nome = nome
    municipio.condigo_ibge = condigo_ibge

    db.session.add(municipio)
    db.session.commit()
    return municipio


def obter_municipios():
    return Municipio.query.all()


def obter_municipio_por_id(id):
    return Municipio.query.filter_by(id)
