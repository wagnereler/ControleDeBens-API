# app/application/services/usuario_service.py

from app.infrastructure.database import Database
from app.domain.models.usuario import Usuario
from sqlalchemy.orm import Session

class UsuarioService:
    def __init__(self):
        self.db = Database()

    def criar_usuario(self, nome, cpf, usuario, email, data_cadastro, id_endereco):
        novo_usuario = Usuario(
            nome=nome,
            cpf=cpf,
            usuario=usuario,
            email=email,
            data_cadastro=data_cadastro,
            id_endereco=id_endereco
        )

        # Adicione o novo usuário à sessão e persista no banco de dados
        with self.db.get_session() as session:  # Garante o uso adequado da sessão
            session.add(novo_usuario)
            session.commit()

        return novo_usuario
