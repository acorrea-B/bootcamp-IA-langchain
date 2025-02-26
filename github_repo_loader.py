import requests
from github import Auth, Github
from env_variables import Envs

from langchain.document_loaders import GithubFileLoader


class Loader(GithubFileLoader):

    def get_file_content_by_path(self, path: str) -> str:

        extension = None if not "." in path else path.split(".")[-1]
        if not extension in ["py", "js", "php", "java", "md", "txt"]:
            return ""

        githube_auth = Auth.Token(Envs.GITHUB_TOKEN)
        github_conection = Github(auth=githube_auth)
        repo = github_conection.get_repo(
            Envs.REPOSITORY_OWNER + "/" + Envs.REPOSITORY_NAME
        )

        file_content = repo.get_contents(path)

        if file_content is not None:
            return file_content.decoded_content.decode()

        return ""


class GitHubPI:
    def __init__(self):

        self.githube_auth = Auth.Token(Envs.GITHUB_TOKEN)
        self.github_conection = Github(auth=self.githube_auth)

    def get_repository_contents(self, repo_name):

        loader = Loader(
            access_token=Envs.GITHUB_TOKEN,
            repo=Envs.REPOSITORY_OWNER + "/" + repo_name,
            branch="main",
            file_filter=None,
        )

        return loader.load_and_split()
