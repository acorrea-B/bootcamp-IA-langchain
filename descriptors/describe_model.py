from langchain_core.prompts import ChatPromptTemplate

from open_ai_client import chat
from descriptors.descriptor_metadata import CodeMetadata


class DescriptionModel:
    def __init__(self, model_name: str = "CodeMetadata"):
        self.model = globals()[model_name]
        self.system_prompt = (
            "Act as a software engineer. You are going to receive a code snippet. Your task is to describe the code snippet in a concise way. "
            "Describe the code snippet in a way that acts like metadata to imporve the searchability of the code snippet."
            "If the code snippet is not a code snippet or not known the response, return an empty string."
        )
        self.prompt = ChatPromptTemplate.from_messages(
            [("system", self.system_prompt), ("human", "{code_snippet}")]
        )
        self.chain = chat.with_structured_output(schema=self.model)

    def get_model_description(self, code_snippet: str):
        response = self.chain.invoke(self.prompt.format(code_snippet=code_snippet), config={"temperature": 0, "max_tokens": 1000} )
        return response
