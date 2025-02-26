from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from chroma_manager import vectorstore
from open_ai_client import chat


def get_code_explanation(retriever):
    system_prompt = (
        "You are an assistant for question-answering tasks. "
        "Use the following pieces of retrieved context to answer "
        "the question. If you don't know the answer, say that you "
        "don't know. Use three sentences maximum and keep the "
        "answer concise."
        "\n\n"
        "{context}"
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )

    question_answer_chain = create_stuff_documents_chain(chat, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    print(rag_chain.invoke({"input": "Can you resume the readme?"}) )


get_code_explanation(vectorstore.as_retriever())
