# tests/test_usuario_service.py

from app.application.services.usuario_service import UsuarioService

def test_criar_usuario():
    # Crie uma instância do serviço do usuário
    usuario_service = UsuarioService()

    # Dados do usuário para teste
    dados_usuario = {
        'nome': 'John Doe',
        'cpf': '12345678901',
        'usuario': 'john_doe',
        'email': 'john.doe@example.com',
        'data_cadastro': '2023-12-26',
        'id_endereco': 1,
    }

    # Chame o método de criar usuário
    novo_usuario = usuario_service.criar_usuario(**dados_usuario)

    # Verifique se o usuário foi criado corretamente
    assert novo_usuario is not None
    assert novo_usuario.nome == dados_usuario['nome']
    assert novo_usuario.cpf == dados_usuario['cpf']
    assert novo_usuario.usuario == dados_usuario['usuario']
    assert novo_usuario.email == dados_usuario['email']
    assert str(novo_usuario.data_cadastro) == dados_usuario['data_cadastro']
    assert novo_usuario.id_endereco == dados_usuario['id_endereco']

    # Agora você pode adicionar mais verificações ou testar outras operações (recuperar, atualizar, excluir, etc.)
