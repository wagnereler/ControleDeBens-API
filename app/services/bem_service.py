#app/services/bem_service.py
from app.models.bem_model import Bem
from app.utils.extensions import db
from datetime import datetime, date

def criar_bem(id_empresa: int,
              nome: str,
              plaqueta: str,
              data_compra: date,
              data_tombamento: datetime,
              data_baixa: datetime,
              valor_compra: float,
              valor_depreciado: float,
              valor_contabil: float):
    bem = Bem()
    bem.id_empresa = id_empresa
    bem.nome = nome
    bem.plaqueta = plaqueta
    bem.data_compra = data_compra
    bem.data_tombamento = data_tombamento
    bem.data_baixa = data_baixa
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
