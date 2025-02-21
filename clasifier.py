from langchain_core.pydantic_v1 import BaseModel, Field


class CodeClasifier(BaseModel):
    """
    A model for classifying code snippets.
    """

    code_snippet: str = Field(
        ...,
        description="The code snippet to be classified.",
    )
    language: str = Field(
        ...,
        description="The programming language of the code snippet.",
        enum=["Python", "JavaScript", "PHP"],
    )
    classification: str = Field(
        ...,
        description="The classification of the code snippet with dominant library.",
    )
    documentation: str = Field(
        ...,
        description="The documentation of the code snippet.",
        enum=["Docstring", "Comment", "None"],
    )
    code_action: str = Field(
        ...,
        description="The action performed by the code.",
        enum=["Model", "Interface", "Class", "None"],
    )
    class_names: list[str] = Field(
        ...,
        description="The names of the classes in the code.",
    )
    function_names: list[str] = Field(
        ...,
        description="The names of the functions in the code.",
    )
    resume_code: str = Field(
        ...,
        description="A resume of the code.",
    )
    library_list: list[str] = Field(
        ...,
        description="The list of libraries used in the code.",
        )
    sub_modules_library_list: list[str] = Field(
        ...,
        description="imports of submodules of libraries used in the code, before off import sentece.",
        )