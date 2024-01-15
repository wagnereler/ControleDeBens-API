#app/utils/import_models.py
from app.models.bem_model import Bem
from app.models.empresa_model import Empresa
from app.models.empresa_telefone_model import EmpresaTelefone
from app.models.empresa_usuario_model import EmpresaUsuario
from app.models.endereco_model import Endereco
from app.models.estado_model import Estado
from app.models.log_acao_model import LogAcao
from app.models.log_acesso_model import LogAcesso
from app.models.logradouro_model import Logradouro
from app.models.movimentacao_model import Movimentacao
from app.models.municipio_model import Municipio
from app.models.papel_model import Papel
from app.models.papel_rotina_model import PapelRotina
from app.models.rotina_model import Rotina
from app.models.setor_model import Setor
from app.models.telefone_model import Telefone
from app.models.usuario_model import Usuario
from app.models.usuario_papel_model import UsuarioPapel
from app.models.usuario_setor_model import UsuarioSetor
from app.models.usuario_telefone_model import UsuarioTelefone
class ImportModels:
    bem = Bem
    empresa = Empresa
    empresaTelefone = EmpresaTelefone
    empresaUsuario = EmpresaUsuario
    endereco = Endereco
    estado = Estado
    logAcao = LogAcao
    logAcesso = LogAcesso
    logradouro = Logradouro
    movimentacao = Movimentacao
    municipio = Municipio
    papel = Papel
    papelRotina = PapelRotina
    rotina = Rotina
    setor = Setor
    telefone = Telefone
    usuario = Usuario
    usuarioPapel = UsuarioPapel
    usuarioSetor = UsuarioSetor
    usuarioTelefone = UsuarioTelefone
