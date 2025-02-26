from pydantic import  Field
from enum import Enum
from typing import Optional, List
from clasifiers.clasiffier_base import ClasiffierBase

class DocumentationEnum(str, Enum):
    DOCSTRING = "Docstring"
    COMMENT = "Comment"
    NONE = "None"


class CodeActionEnum(str, Enum):
    MODEL = "Model"
    INTERFACE = "Interface"
    CLASS = "Class"
    NONE = "None"


class CodeClasifierPythonFile(ClasiffierBase):
    """
    A model for classifying code snippets.
    """

    code_snippet: Optional[str] = Field(
        description="The code snippet to be classified.",
        default=None,
    )
    classification: str = Field(
        description="The classification of the code snippet with dominant library.",
    )
    documentation: DocumentationEnum = Field(
        description="The documentation of the code snippet.",
    )
    code_action: CodeActionEnum = Field(
        description="The action performed by the code.",
    )
    class_names: Optional[List[str]] = Field(
        description="The names of the classes in the code.",
        default=None,
    )
    function_names: Optional[List[str]] = Field(
        description="The names of the functions in the code.",
        default=None,
    )
    resume_code: str = Field(
        description="A resume of the code.",
    )
    library_list: Optional[List[str]] = Field(
        description="The list of libraries used in the code.",
        default=None,
    )
    sub_modules_library_list: Optional[List[str]] = Field(
        description="Imports of submodules of libraries used in the code, before the 'import' sentence.",
        default=None,
    )

    def to_text(self):
        return super().to_text + (
            f"Code Snippet:\n{self.code_snippet}\n\n" +
            f"Classification:\n{self.classification}\n\n"+
            f"Documentation:\n{self.documentation}\n\n"+
            f"Code Action:\n{self.code_action}\n\n"+
            f"Class Names:\n{self.class_names}\n\n"+
            f"Function Names:\n{self.function_names}\n\n"+
            f"Resume Code:\n{self.resume_code}\n\n"+
            f"Library List:\n{self.library_list}\n\n"+
            f"Sub Modules Library List:\n{self.sub_modules_library_list}"
        )

    def metadata(self):
        metadata = super().metadata()
        metadata["code_snippet"] = self.code_snippet
        return metadata
