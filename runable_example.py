from langchain.schema import SystemMessage, HumanMessage
from open_ai_client import chat
from descriptors.clasifier import CodeClasifier


def get_file_data(file_path):
    with open(file_path, "r") as file:
        return file.read()



def get_code_explanation(code):
    messages = [
        SystemMessage("Developert expert in code review and code explanation."),
        HumanMessage(get_file_data("model_example.py")),
    ]
    llm = chat.with_structured_output(schema=CodeClasifier)
    return  llm.invoke(messages)

