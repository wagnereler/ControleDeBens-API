#app/utils/import_models.py
from app.infraestructure.orm.bem import Bem
from app.infraestructure.orm.empresa import Empresa
from app.infraestructure.orm.empresa_telefone import EmpresaTelefone
from app.infraestructure.orm.empresa_usuario import EmpresaUsuario
from app.infraestructure.orm.endereco import Endereco
from app.infraestructure.orm.estado import Estado
from app.infraestructure.orm.log_acao import LogAcao
from app.infraestructure.orm.log_acesso import LogAcesso
from app.infraestructure.orm.logradouro import Logradouro
from app.infraestructure.orm.movimentacao import Movimentacao
from app.infraestructure.orm.municipio import Municipio
from app.infraestructure.orm.papel import Papel
from app.infraestructure.orm.papel_rotina import PapelRotina
from app.infraestructure.orm.rotina import Rotina
from app.infraestructure.orm.setor import Setor
from app.infraestructure.orm.telefone import Telefone
from app.infraestructure.orm.usuario import Usuario
from app.infraestructure.orm.usuario_papel import UsuarioPapel
from app.infraestructure.orm.usuario_setor import UsuarioSetor
from app.infraestructure.orm.usuario_telefone import UsuarioTelefone
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
