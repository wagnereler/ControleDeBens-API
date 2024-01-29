# app/domain/gerais/endereco_service.py
from app.infraestructure.orm.controlde_bens.endereco import Endereco
from app.utils.extensions import db


def inserir_endereco(id_municipio: int,
                     id_estado: int,
                     id_logradouro: int,
                     endereco: str,
                     numero: str,
                     complemento: str,
                     bairro: str,
                     cep: str
                     ):

    _endereco = Endereco()
    _endereco.id_municipio = id_municipio
    _endereco.id_estado = id_estado
    _endereco.id_logradouro = id_logradouro
    _endereco.endereco = endereco
    _endereco.numero = numero
    _endereco.complemento = complemento
    _endereco.bairro = bairro
    _endereco.cep = cep


    db.session.add(_endereco)
    db.session.commit()
    return _endereco


def obter_enderecos():
    return Endereco.query.all()


def obter_endereco_por_id(id):
    return Endereco.query.filter_by(id)
