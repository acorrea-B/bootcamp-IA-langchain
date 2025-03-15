from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from env_variables import Envs


collection_name_default="example_collection"
persist_directory_default="./chroma_langchain_db"

collection_name_custom="code_snippets"
persist_directory_custom="./chroma_langchain_wit_metadata_db"

vectorstore = Chroma(
    collection_name=collection_name_custom,
    persist_directory=persist_directory_custom,
    embedding_function=OpenAIEmbeddings(
        model="text-embedding-3-large", openai_api_key=Envs.OPEN_AI_API_KEY
    ),
)
