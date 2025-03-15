from github import Auth, Github
from env_variables import Envs
from langchain_core.documents import Document
from descriptors.describe_model import DescriptionModel

from langchain.document_loaders import GithubFileLoader

model_descriptor = DescriptionModel()


class Loader(GithubFileLoader):

    def lazy_load(self):
        files = self.get_file_paths()
        for file in files:
            content, metadata = self.get_file_content_by_path(file["path"])
            if content == "":
                continue

            metadata.update(
                {
                    "sha": file["sha"],
                    "url": f"{self.github_api_url}/{self.repo}/{file['type']}/"
                    f"{self.branch}/{file['path']}",
                }
            )
            yield Document(page_content=content, metadata=metadata)

    def get_file_content_by_path(self, path: str) -> str:

        extension = None if not "." in path else path.split(".")[-1]

        if "public/js" in path:
            return "Not allowed file type", {"path": path}

        if not extension in ["py", "js", "php", "java", "md", "txt"]:
            return "Not allowed file type", {"path": path}

        githube_auth = Auth.Token(self.access_token)
        github_conection = Github(auth=githube_auth)
        repo = github_conection.get_repo(
            Envs.REPOSITORY_OWNER + "/" + Envs.REPOSITORY_NAME
        )

        file_content = repo.get_contents(path)
        github_metadata = {
            "last_modified": file_content.last_modified,
            "repository": file_content.repository.name,
            "path": file_content.path,
            "owner": file_content.repository.owner.login,
        }

        if file_content is not None:
            content = file_content.decoded_content.decode()

            return content, github_metadata

        return "Not allowed file type", github_metadata


class GitHubPI:

    def get_repository_contents(self, repo_name):

        loader = Loader(
            access_token=Envs.GITHUB_TOKEN,
            repo=Envs.REPOSITORY_OWNER + "/" + repo_name,
            branch="main",
            file_filter=None,
        )

        return loader.load_and_split()
