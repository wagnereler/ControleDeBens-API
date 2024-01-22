#app/domain/empresa/empresa_service.py
from app.infraestructure.orm.empresa import Empresa
from app.utils.extensions import db
from datetime import datetime, date

def inserir_empresa(nome_fantasia: str,
              razao_social: str,
              cnpj: str,
              id_endereco: int):
    empresa = Empresa()
    empresa.nome_fantasia = nome_fantasia
    empresa.razao_social = razao_social
    empresa.cnpj = cnpj
    empresa.id_endereco = id_endereco
    db.session.add(empresa)
    db.session.commit()
    return empresa

def obter_empresas():
    return Empresa.query.all()

def obter_empresa_por_id(id):
    return Empresa.query.filter_by(id)

def obter_empresa_por_descricao(nome):
    return Empresa.query.filter_by(nome_fantasia=nome)
