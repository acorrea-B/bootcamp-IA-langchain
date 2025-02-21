from langchain_openai import ChatOpenAI
from os import environ


open_ai_key = environ.get("OPEN_API_KEY")

chat = ChatOpenAI(api_key=open_ai_key)
