# app/application/services/logradouro_service.py
from datetime import datetime
from app.domain.models.logradouro import Logradouro
from app.infrastructure.persistence.sqlalchemy.repositories.logradouro_repository import LogradouroRepository
from app.infrastructure.persistence.sqlalchemy.database import db_session





class LogradouroService:
    def __init__(self):
        self.logradouro_repository = LogradouroRepository()

    def criar_logradouro(self, nome, ativo):
        novo_logradouro = Logradouro(
            nome=nome,
            ativo=ativo,
            data_cadastro=datetime.now(),
            data_alteracao=datetime.now()
        )
        return self.logradouro_repository.create(novo_logradouro)

    def obter_logradouro_por_id(self, logradouro_id):
        # Utilize a sessão do SQLAlchemy para realizar a consulta
        with db_session() as session:
            # Utilize o método query para buscar um Logradouro por ID
            logradouro = session.query(Logradouro).filter_by(id=logradouro_id).first()

            # Verifique se o logradouro foi encontrado
            if logradouro is not None:
                return logradouro  # Retorna diretamente a instância de Logradouro

            return None

    def atualizar_logradouro(self, logradouro_id, nome=None, ativo=None):
        logradouro = self.logradouro_repository.get_by_id(logradouro_id)
        if logradouro:
            if nome is not None:
                logradouro.nome = nome
            if ativo is not None:
                logradouro.ativo = ativo
            logradouro.data_alteracao = datetime.now()
            try:
                self.logradouro_repository.update(logradouro)
                return logradouro
            except Exception as e:
                raise Exception(f"Erro ao atualizar logradouro: {str(e)}")
        return None
