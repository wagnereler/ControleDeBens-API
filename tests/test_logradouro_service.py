# tests/test_logradouro_service.py

from app.application.services.logradouro_service import LogradouroService

def test_criar_logradouro():
    # Crie uma instância do serviço para Logradouro
    logradouro_service = LogradouroService()

    # Dados do logradouro para teste
    dados_logradouro = {
        'nome': 'Rua Teste',
        'ativo': True,
        'data_cadastro': '2023-12-26 12:25:23',
        'data_alteracao': '2023-12-26 12:25:23',
    }

    # Chame o método de criar logradouro
    novo_logradouro = logradouro_service.criar_logradouro(**dados_logradouro)

    # Verifique se o logradouro foi criado corretamente
    assert novo_logradouro is not None
    assert novo_logradouro['nome'] == dados_logradouro['nome']
    assert novo_logradouro['ativo'] == dados_logradouro['ativo']
    assert novo_logradouro['data_cadastro'] == dados_logradouro['data_cadastro']
    assert novo_logradouro['data_alteracao'] == dados_logradouro['data_alteracao']
