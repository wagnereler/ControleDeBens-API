# app/application/services/logradouro_service.py

from app.infrastructure.database import Database
from app.domain.models.logradouro import Logradouro
from sqlalchemy.orm import Session

class LogradouroService:
    def __init__(self):
        self.db = Database()

    def criar_logradouro(self, nome, ativo, data_cadastro, data_alteracao):
        novo_logradouro = Logradouro(
            nome=nome,
            ativo=ativo,
            data_cadastro=data_cadastro,
            data_alteracao=data_alteracao
        )
        # Adicione o novo logradouro à sessão e persista no banco de dados
        with self.db.get_session() as session:
            session.add(novo_logradouro)
            session.commit()
            # Recarregue os dados da entidade para evitar instâncias desanexadas
            session.refresh(novo_logradouro)
            # Retorne os dados da entidade
            return {
                'id': novo_logradouro.id,
                'nome': novo_logradouro.nome,
                'ativo': novo_logradouro.ativo,
                'data_cadastro': str(novo_logradouro.data_cadastro),
                'data_alteracao': str(novo_logradouro.data_alteracao),
            }
