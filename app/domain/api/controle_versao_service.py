# app/domain/api/controle_versao_service.py
from flask_restx import Namespace, Resource, fields
from app.infraestructure.orm.metadados.funcao import Funcao as OrmFuncao
from app.infraestructure.orm.metadados.responsavel import Responsavel as OrmResponsavel
from app.infraestructure.orm.metadados.controle_versao import ControleVersao as OrmControleVersao
from app.infraestructure.orm.metadados.versao import Versao as OrmVersao
from app.utils.extensions import db
from datetime import datetime


def get_versao():
    versao = '1.0'
    return versao


def inserir_funcao(descricao: str):
    funcao = OrmFuncao()
    funcao.funcao = descricao
    db.session.add(funcao)
    db.session.commit()
    return funcao


def listar_funcoes():
    listaFuncoes = OrmFuncao
    return listaFuncoes.query.all()


def inserir_responsavel(id_funcao: int, nome: str, email: str):
    responsavel = OrmResponsavel()
    responsavel.id_funcao = id_funcao
    responsavel.nome = nome
    responsavel.email = email
    db.session.add(responsavel)
    db.session.commit()
    return responsavel


def listar_responsaveis():
    listaResponsaveis = OrmResponsavel()
    return listaResponsaveis.query.all()


def inserir_versao(id_responsavel: int,
                   id_modulo: int,
                   versao: str,
                   descricao: str,
                   data_commit):
    _versao = OrmControleVersao()
    _versao.id_responsavel = id_responsavel
    _versao.id_modulo = id_modulo
    _versao.versao = versao
    _versao.descricao = descricao
    _versao.data_commit = datetime.strptime(data_commit, "%Y-%m-%d %H:%M:%S")
    db.session.add(_versao)
    db.session.commit()
    return _versao


def listar_versoes():
    listar_versoes = OrmControleVersao()
    return listar_versoes.query.all()


def controle_versao(major: int, minor: int, patch: int):
    ultima_versao = OrmVersao()
    dados = ultima_versao.query.filter_by(id=1).first()

    if not dados:
        criar_versao_inicial()
        dados = ultima_versao.query.filter_by(id=1).first()
    if major == True:
        dados.major += 1
        dados.minor = 0
        dados.patch = 0
    if minor == True:
        dados.minor += 1
        dados.patch = 0
    if patch == True:
        dados.patch += 1

    db.session.commit()
    nova_versao = f'{str(dados.major)}.{str(dados.minor)}.{str(dados.patch)}'
    return nova_versao


def criar_versao_inicial():
    versao_inicial = OrmVersao(major=0, minor=0, patch=0)
    db.session.add(versao_inicial)
    db.session.commit()
