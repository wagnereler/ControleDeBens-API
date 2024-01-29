#app/utils/import_orm.py

#imports relacionados ao orm do banco principal
from app.infraestructure.orm.controlde_bens.bem import Bem
from app.infraestructure.orm.controlde_bens.empresa import Empresa
from app.infraestructure.orm.controlde_bens.empresa_telefone import EmpresaTelefone
from app.infraestructure.orm.controlde_bens.empresa_usuario import EmpresaUsuario
from app.infraestructure.orm.controlde_bens.endereco import Endereco
from app.infraestructure.orm.controlde_bens.estado import Estado
from app.infraestructure.orm.controlde_bens.log_acao import LogAcao
from app.infraestructure.orm.controlde_bens.log_acesso import LogAcesso
from app.infraestructure.orm.controlde_bens.logradouro import Logradouro
from app.infraestructure.orm.controlde_bens.movimentacao import Movimentacao
from app.infraestructure.orm.controlde_bens.municipio import Municipio
from app.infraestructure.orm.controlde_bens.papel import Papel
from app.infraestructure.orm.controlde_bens.papel_rotina import PapelRotina
from app.infraestructure.orm.controlde_bens.rotina import Rotina
from app.infraestructure.orm.controlde_bens.setor import Setor
from app.infraestructure.orm.controlde_bens.telefone import Telefone
from app.infraestructure.orm.controlde_bens.usuario import Usuario
from app.infraestructure.orm.controlde_bens.usuario_papel import UsuarioPapel
from app.infraestructure.orm.controlde_bens.usuario_setor import UsuarioSetor
from app.infraestructure.orm.controlde_bens.usuario_telefone import UsuarioTelefone

#imports relacionado ao banco de dados metadados
from app.infraestructure.orm.metadados.controle_versao_api import ControleVersaoAPI

class ImportOrm:
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



class ImportOrmMetadado:
    controleVersaoAPI = ControleVersaoAPI