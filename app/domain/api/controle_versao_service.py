# app/domain/api/controle_versao_service.py
from flask_restx import Namespace, Resource, fields

from app import Config
from app.infraestructure.orm.metadados.funcao import Funcao as OrmFuncao
from app.infraestructure.orm.metadados.responsavel import Responsavel as OrmResponsavel
from app.infraestructure.orm.metadados.controle_versao import ControleVersao as OrmControleVersao
from app.infraestructure.orm.metadados.versao import Versao as OrmVersao
from app.utils.extensions import db
from datetime import datetime

from app.utils.github_api_service import IntegracaoGithubAPI


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
                   data_commit: datetime,
                   git_sha: str):
    _versao = OrmControleVersao()
    _versao.id_responsavel = id_responsavel
    _versao.id_modulo = id_modulo
    _versao.versao = versao
    _versao.descricao = descricao
    _versao.data_commit = data_commit
    _versao.git_sha = git_sha
    db.session.add(_versao)
    db.session.commit()
    return _versao


def listar_versoes():
    listar_versoes = OrmControleVersao()
    return listar_versoes.query.all()


def controle_versao(major: int, minor: int, patch: int, sha: str) ->dict:
    GIT_USER = Config.GIT_USER
    GIT_REPOSITORY = Config.GIT_REPOSITORY
    GIT_TOKEN = Config.GIT_TOKEN


    ultima_versao = OrmVersao()
    dados = ultima_versao.query.filter_by(id=1).first()

    github = IntegracaoGithubAPI(GIT_REPOSITORY, GIT_USER, GIT_TOKEN)

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
    dados_git = github.obter_dados(sha)


    nova_versao = f'{str(dados.major)}.{str(dados.minor)}.{str(dados.patch)}'
    #dados github
    data_commit = dados_git[0]
    nome_autor = dados_git[1]
    email_autor = dados_git[2]
    comentario = dados_git[3]
    id_responsavel = verifica_cadastro_responsavel(nome_autor, email_autor)

    return nova_versao, data_commit, id_responsavel, comentario


def criar_versao_inicial():
    versao_inicial = OrmVersao(major=0, minor=0, patch=0)
    db.session.add(versao_inicial)
    db.session.commit()


def verifica_cadastro_responsavel(nome: str, email, funcao=None):
    responsavel = OrmResponsavel()
    dados = responsavel.query.filter_by(email=email).first()
    if dados is None:
        retorno = cadastrar_responsavel(nome, email, funcao)
        return retorno
    else:
        return dados.id

def cadastrar_responsavel(nome: str, email, funcao=None):
    if funcao is None:
        funcao = 1
    novo_responsavel = OrmResponsavel()
    novo_responsavel.nome = nome
    novo_responsavel.email = email
    novo_responsavel.id_funcao = funcao
    db.session.add(novo_responsavel)
    db.session.commit()
    print('cadastrou')
    retorno = novo_responsavel.query.filter_by(email=email).first()
    print('após cadastro id', retorno.id)
    return retorno.id

