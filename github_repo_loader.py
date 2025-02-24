from github import Auth, Github
from env_variables import Envs


class GitHubPI:
    def __init__(self):

        self.githube_auth = Auth.Token(Envs.GITHUB_TOKEN)
        self.github_conection = Github(auth=self.githube_auth)

    def get_repository_contents(self, repo_name):

        # Initialize the loader with authentication
        repo = self.github_conection.get_repo(repo_name)

        contents = repo.get_contents("")

        # Now you can work with the loaded documents
        while contents:
            file_content = contents.pop(0)
            if file_content.type == "dir":
                contents.extend(repo.get_contents(file_content.path))

            extension = file_content.name.split(".")[-1]

            match extension:
                case "py":
                    print(file_content.decoded_content.decode())
                case "md":
                    print(file_content.decoded_content.decode())
                case "txt":
                    print(file_content.decoded_content.decode())
                case _:
                    print("Unsupported file type")
