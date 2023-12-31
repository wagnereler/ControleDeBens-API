# tests/test_logradouro_service.py
from app.application.services.logradouro_service import LogradouroService
from app.domain.models.logradouro import Logradouro
from datetime import datetime

def test_criar_logradouro():
    # Crie uma instância do serviço para Logradouro
    logradouro_service = LogradouroService()

    # Dados do logradouro para teste
    dados_logradouro = {
        'nome': 'Rua Teste',
        'ativo': True,
    }

    # Chame o método de criar logradouro
    novo_logradouro = logradouro_service.criar_logradouro(
        nome=dados_logradouro['nome'],
        ativo=dados_logradouro['ativo'],
    )

    # Verifique se o logradouro foi criado corretamente
    assert novo_logradouro is not None
    assert novo_logradouro.nome == dados_logradouro['nome']
    assert novo_logradouro.ativo == dados_logradouro['ativo']

def test_atualizar_logradouro_id():
    # Crie uma instância do serviço para Logradouro
    logradouro_service = LogradouroService()

    # Verificar se o registro com ID 70 existe antes de tentar atualizá-lo
    logradouro_existente = logradouro_service.obter_logradouro_por_id(70)

    if logradouro_existente is not None:
        # Dados para atualização
        dados_atualizados = {
            'nome': 'Rua Atualizada',
            'ativo': False,
        }

        # Chamar o método de atualizar logradouro com o ID específico (neste caso, 70)
        logradouro_atualizado = logradouro_service.atualizar_logradouro(
            logradouro_id=70,
            nome=dados_atualizados['nome'],
            ativo=dados_atualizados['ativo'],
        )

        # Verificar se o logradouro foi atualizado corretamente
        assert logradouro_atualizado is not None
        assert logradouro_atualizado.nome == dados_atualizados['nome']
        assert logradouro_atualizado.ativo == dados_atualizados['ativo']
        assert logradouro_atualizado.data_alteracao is not None
    else:
        # Se o registro com ID 70 não existe, você pode imprimir uma mensagem ou lidar de outra forma
        print("Registro com ID 70 não encontrado. Certifique-se de que o registro existe antes de executar este teste.")

# tests/test_logradouro_service.py

def test_obter_logradouro_por_id():
    # Crie uma instância do serviço para Logradouro
    logradouro_service = LogradouroService()

    # Crie um logradouro para teste
    dados_logradouro = {
        'nome': 'Estação',
        'ativo': True,
    }
    # Chame o método de criar logradouro e obtenha o logradouro criado
    novo_logradouro = logradouro_service.criar_logradouro(
        nome=dados_logradouro['nome'],
        ativo=dados_logradouro['ativo'],
    )

    # Adicione prints para debug
    print("Logradouro ID criado:", novo_logradouro.id)
    print("Conteúdo do módulo 'app.domain.models.logradouro':", dir(Logradouro))

    # Chame o método de obter logradouro por id, utilizando o ID retornado pelo criar_logradouro
    logradouro_obtido = logradouro_service.obter_logradouro_por_id(novo_logradouro.id)

    # Adicione prints para debug
    print("Logradouro obtido:", logradouro_obtido)

    # Verifique se o logradouro foi obtido corretamente
    assert logradouro_obtido is not None

    # Adicione prints para verificar o conteúdo do logradouro obtido
    print("Tipo de Logradouro:", type(logradouro_obtido))
    print("Conteúdo do Logradouro:", logradouro_obtido.__dict__)

    # Verifique se o logradouro é uma instância de Logradouro
    assert isinstance(logradouro_obtido, Logradouro), f"Tipo de logradouro obtido: {type(logradouro_obtido)}"

    assert logradouro_obtido.id == novo_logradouro.id  # Certifique-se de que o ID está correto
    assert logradouro_obtido.nome == dados_logradouro['nome']
    assert logradouro_obtido.ativo == dados_logradouro['ativo']