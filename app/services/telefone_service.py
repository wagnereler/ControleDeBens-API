from app.models.telefone_model import Telefone
from app.utils.extensions import db

def criar_telefone(tipo, ddi, dd, numero):
    try:
        telefone = Telefone(tipo=tipo, ddi=ddi, dd=dd, numero=numero)
        db.session.add(telefone)
        db.session.commit()
        return telefone
    except Exception as e:
        db.session.rollback()
        raise e
    finally:
        db.session.close()

def obter_telefone_por_id():
    return Telefone.query.all()