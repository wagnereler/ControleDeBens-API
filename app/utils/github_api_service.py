#app/utils/github_api_service.py
from github import Github, Auth

class IntegracaoGithubAPI():
    def __init__(self, repositorio: str, usuario: str, token: str) -> None:
        self.auth = Auth.Token(token)
        self.repositorio = repositorio
        self.usuario = usuario
        self.retorno = None
    def obter_dados(self, sha_start) -> list:
        github = Github(auth=self.auth)
        repositorio = github.get_user(self.usuario).get_repo(self.repositorio)

        for commit in repositorio.get_commits():
            if commit.sha.startswith(sha_start):
                data_commit = commit.commit.author.date
                comentario = commit.commit.message
                nome_autor = commit.commit.author.name
                email_autor = commit.commit.author.email
                self.retorno = [data_commit, nome_autor, email_autor, comentario]
                break
        return self.retorno



