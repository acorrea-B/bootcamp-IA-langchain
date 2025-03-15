from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class CodeMetadata(BaseModel):
    """
    Metadata for code documents stored in a vector store.
    All fields are optional with default values.
    """

    source: Optional[str] = Field(
        "unknown",
        description="Source URL or location of the code (e.g., GitHub repository), if not provided set unknown",
    )
    category: Optional[str] = Field(
        description="Category of the code (e.g., algorithm, library, utility), if not provided set 'utility'",
        default="utility",
    )
    author: Optional[str] = Field(
        "unknown",
        description="Author of the code, if not provided set unknown ",
    )
    created_at: Optional[str] = Field(
        str(datetime.now()),
        description="Creation timestamp of the code, in format 'YYYY-MM-DD HH:MM:SS' if not provided set unknown",
    )
    updated_at: Optional[str] = Field(
        str(datetime.now()),
        description="Last update timestamp of the code, in format 'YYYY-MM-DD HH:MM:SS' if not provided set unknown",
    )
    file_path: Optional[str] = Field(
        "unknown",
        description="Path of the file within the repository (e.g., `src/module.py`), if not provided set unknown",
    )
    class_names: Optional[str] = Field(
        "",
        description="List of class names in the code, separated by commas, if not provided set unknown",
    )
    function_names: Optional[str] = Field(
        "",
        description="List of function names in the code, separated by commas, if not provided set unknown",
    )
    docstring: Optional[str] = Field(
        description="Docstring or summary for the code, if not provided set 'No docstring provided",
        default="No docstring provided",
    )
    length: Optional[str] = Field(
        "0",
        description="Length of the code in lines or words, response only integer if not provided set to 0",
    )
    relevance_score: Optional[str] = Field(
        "0.0",
        description="Relevance score based on the code's content or context, response only type float, if not provided set to 0.0",
    )
    language: Optional[str] = Field(
        "Python",
        description="Programming language of the code, if not provided set unknown",
    )
    status: Optional[str] = Field(
        "active",
        description="Status of the code (e.g., active, deprecated), if not provided set unknown",
    )
    repository: Optional[str] = Field(
        description="GitHub or repository name for the code, if not provided set unknown",
        default="",
    )
    related_docs: Optional[str] = Field(
        "",
        description="IDs of related code documents for context, serparated by commas, if not provided set unknown",
    )
    context: Optional[str] = Field(
        description="Context or description of where this code fits in a larger project, if not provided set unknown",
        default="",
    )

    def to_dict(self):
        return {
            "function_names": self.normalize(self.function_names),
            "docstring": self.normalize(self.docstring),
            "length": self.normalize(self.length),
            "relevance_score": self.normalize(self.relevance_score),
            "language": self.normalize(self.language),
            "status": self.normalize(self.status),
            "repository": self.normalize(self.repository),
            "related_docs": self.normalize(self.related_docs),
            "context": self.normalize(self.context),
            "file_path": self.normalize(self.file_path),
            "context": self.normalize(self.context),
            "class_names": self.normalize(self.class_names),
            "author": self.normalize(self.author),
            "updated_at": self.normalize(self.updated_at),
            "created_at": self.normalize(self.created_at),
            "category": self.normalize(self.category),
            "source": self.normalize(self.source),
        }

    def normalize(self, value):
        if value is None:
            return "unknown"
        return value
