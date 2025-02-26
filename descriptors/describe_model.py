from langchain_core.prompts import ChatPromptTemplate

from open_ai_client import chat
from descriptors import descriptor_metadata


class DescriptionModel:
    def __init__(self, model_name: str):
        self.model = globals()[model_name]
        self.system_prompt = (
            "Act as a software engineer. You are going to receive a code snippet. Your task is to describe the code snippet in a concise way. "
            "Describe the code snippet in a way that acts like metadata to imporve the searchability of the code snippet."
        )
        self.prompt = ChatPromptTemplate.from_messages(
            [("system", self.system_prompt), ("human", "{code_snippet}")]
        )
        self.chain = chat.with_structured_output(schema=self.model)

    def get_model_description(self, code_snippet: str):
        response = self.chain.invoke(self.prompt.format(code_snippet=code_snippet))
        return response
