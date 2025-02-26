from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from env_variables import Envs


vectorstore = Chroma(
    collection_name="example_collection",
    persist_directory="./chroma_langchain_db",
    embedding_function=OpenAIEmbeddings(
        model="text-embedding-3-large", openai_api_key=Envs.OPEN_AI_API_KEY
    ),
)
