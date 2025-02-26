from os import environ

class Envs:
    OPEN_AI_API_KEY = environ.get("OPEN_API_KEY")
    GITHUB_TOKEN = environ.get("GITHUB_TOKEN")
    REPOSITORY_NAME = environ.get("REPOSITORY_NAME")
    REPOSITORY_OWNER = environ.get("REPOSITORY_OWNER")