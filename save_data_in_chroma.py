from env_variables import Envs
from github_repo_loader import GitHubPI
from chroma_manager import vectorstore

document_split = GitHubPI().get_repository_contents(Envs.REPOSITORY_NAME)


vectorstore.add_documents(
    documents=document_split,
)
