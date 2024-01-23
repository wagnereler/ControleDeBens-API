#app/services/empresa_service.py
from app.infraestructure.orm.bem import Bem
from app.utils.extensions import db
from datetime import datetime, date

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
    bem = Bem()
    bem.id_empresa = id_empresa
    bem.id_setor = id_setor
    bem.nome = nome
    bem.plaqueta = plaqueta
    bem.data_compra = datetime.strptime(data_compra, "%Y-%m-%d").date()
    bem.data_tombamento = datetime.strptime(data_tombamento, "%Y-%m-%d %H:%M").date()
    if data_baixa == None:
        data_baixa
    else:
        datetime.strptime(data_baixa, "%Y-%m-%d %H:%M")
    bem.valor_compra = valor_compra
    bem.valor_depreciado = valor_depreciado
    bem.valor_contabil = valor_contabil
    db.session.add(bem)
    db.session.commit()
    return bem

def obter_bens():
    return Bem.query.all()

def obter_bem_por_id(id_bem):
    return Bem.query.filter_by(id_bem)

def obter_bem_por_descricao(nome):
    return Bem.query.filter_by(nome=nome)
