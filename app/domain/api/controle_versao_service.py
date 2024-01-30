#app/domain/api/controle_versao_service.py
from flask_restx import Namespace, Resource, fields
from app.infraestructure.orm.metadados.funcao import Funcao as OrmFuncao
from app.infraestructure.orm.metadados.responsavel import Responsavel as OrmResponsavel
from app.utils.extensions import db


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
