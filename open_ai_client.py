from langchain_openai import ChatOpenAI
from env_variables import Envs

chat = ChatOpenAI(api_key=Envs.OPEN_AI_API_KEY, model_name="gpt-4-1106-preview")
