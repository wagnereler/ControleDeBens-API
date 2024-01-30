#app/domain/api/controle_versao_service.py
from flask_restx import Namespace, Resource, fields
from app.infraestructure.orm.metadados.funcao import Funcao as OrmFuncao
from app.infraestructure.orm.metadados.responsavel import Responsavel as OrmResponsavel
from app.infraestructure.orm.metadados.controle_versao import ControleVersao as OrmControleVersao
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
                   versao: str,
                   descricao: str,
                   data_atualizacao: datetime):
    _versao = OrmControleVersao()
    _versao.id_responsavel = id_responsavel
    _versao.versao = versao
    _versao.descricao = descricao
    _versao.data_atualizacao = datetime.strptime(data_atualizacao, "%Y-%m-%d %H:%M").date()
    db.session.add(_versao)
    db.session.commit()
    return _versao

def listar_versoes():
    listar_versoes = OrmControleVersao()
    return listar_versoes.query.all()
