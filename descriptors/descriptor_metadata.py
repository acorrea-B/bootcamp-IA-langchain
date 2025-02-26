from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime


class CodeMetadata(BaseModel):
    """
    Metadata for code documents stored in a vector store.
    All fields are optional with default values.
    """

    source: Optional[str] = Field(
        None,
        description="Source URL or location of the code (e.g., GitHub repository)",
        default=None,
    )
    category: Optional[str] = Field(
        None,
        description="Category of the code (e.g., algorithm, library, utility)",
        default="utility",
    )
    author: Optional[str] = Field(
        None, description="Author of the code", default="Unknown"
    )
    created_at: Optional[datetime] = Field(
        None,
        description="Creation timestamp of the code",
        default_factory=datetime.now,
    )
    updated_at: Optional[datetime] = Field(
        None,
        description="Last update timestamp of the code",
        default_factory=datetime.now,
    )
    file_path: Optional[str] = Field(
        None,
        description="Path of the file within the repository (e.g., `src/module.py`)",
        default="",
    )
    class_names: Optional[List[str]] = Field(
        [], description="List of class names in the code", default=[]
    )
    function_names: Optional[List[str]] = Field(
        [], description="List of function names in the code", default=[]
    )
    docstring: Optional[str] = Field(
        None,
        description="Docstring or summary for the code",
        default="No docstring provided",
    )
    length: Optional[int] = Field(
        0, description="Length of the code in lines or words", default=0
    )
    relevance_score: Optional[float] = Field(
        0.0,
        description="Relevance score based on the code's content or context",
        default=0.0,
    )
    language: Optional[str] = Field(
        "Python", description="Programming language of the code", default="Python"
    )
    status: Optional[str] = Field(
        "active",
        description="Status of the code (e.g., active, deprecated)",
        default="active",
    )
    repository: Optional[str] = Field(
        None, description="GitHub or repository name for the code", default=""
    )
    related_docs: Optional[List[str]] = Field(
        [], description="IDs of related code documents for context", default=[]
    )
    context: Optional[str] = Field(
        None,
        description="Context or description of where this code fits in a larger project",
        default="",
    )
