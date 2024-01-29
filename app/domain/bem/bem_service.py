#app/domain/bem/bem_service.py
from app.infraestructure.orm.controlde_bens.bem import Bem as OrmBem
from app.infraestructure.orm.controlde_bens.setor import Setor as OrmSetor
from app.infraestructure.orm.controlde_bens.empresa import Empresa as OrmEmpesa
from app.utils.extensions import db
from datetime import datetime

def inserir_bem(id_empresa: int,
                id_setor: int,
                nome: str,
                plaqueta: str,
                data_compra: str,
                data_tombamento: str,
                data_baixa: str,
                valor_compra: float,
                valor_depreciado: float,
                valor_contabil: float):
    bem = OrmBem()
    bem.id_empresa = id_empresa
    bem.id_setor = id_setor
    bem.nome = nome
    bem.plaqueta = plaqueta
    bem.data_compra = datetime.strptime(data_compra, "%Y-%m-%d").date()
    bem.data_tombamento = datetime.strptime(data_tombamento, "%Y-%m-%d %H:%M").date()
    if data_baixa is not None:
        bem.data_baixa = datetime.strptime(data_baixa, "%Y-%m-%d %H:%M").date()
    bem.valor_compra = valor_compra
    bem.valor_depreciado = valor_depreciado
    bem.valor_contabil = valor_contabil
    db.session.add(bem)
    db.session.commit()
    return bem

def obter_bens():
    return OrmBem.query.all()

def obter_bem_por_id(id_bem):
    return OrmBem.query.filter_by(id_bem)

def obter_bem_por_descricao(nome):
    return OrmBem.query.filter_by(nome=nome)

def obter_bem_por_empresa(id_empresa):
    return OrmBem.query.filter_by(id_empresa=id_empresa)

def listar_bens_por_empresa(id_empresa):
    empresa = OrmEmpesa.query.filter_by(id=id_empresa).first()
    retorno = {
        'id_empresa': empresa.id,
        'nome_fantasia': empresa.nome_fantasia,
        'razao_social': empresa.razao_social,
        'cnpj': empresa.cnpj,
        'id_endereco': empresa.id_endereco,
        'setores': [],
    }

    setores = OrmSetor.query.filter_by(id_empresa=id_empresa).all()

    for setor in setores:
        setor_dict = {
            'id_setor': setor.id,
            'id_empresa': setor.id_empresa,
            'nome': setor.nome,
            'bens': [],
        }

        bens = OrmBem.query.filter_by(id_setor=setor.id).all()

        for bem in bens:
            bem_dict = {
                'id_bem': bem.id,
                'id_empresa': bem.id_empresa,
                'id_setor': bem.id_setor,
                'nome': bem.nome,
                'plaqueta': bem.plaqueta,
                'data_compra': bem.data_compra,
                'data_tombamento': bem.data_tombamento,
                'data_baixa': bem.data_baixa,
                'valor_compra': bem.valor_compra,
                'valor_depreciado': bem.valor_depreciado,
                'valor_contabil': bem.valor_contabil,
            }
            setor_dict['bens'].append(bem_dict)

        retorno['setores'].append(setor_dict)

    return retorno


