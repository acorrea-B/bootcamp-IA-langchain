from pydantic import BaseModel, Field


class ClasiffierBase(BaseModel):

    language: str = Field(
        description="The programming language of the code snippet.",
        enum=["Python", "JavaScript", "PHP", "Markdown", "Text"],
    )
    repository_path: str = Field(description="The path of the repository.")
    data: str = Field(description="The input received.")

    def to_text(self) -> str:
        return f"Language: {self.language}\nRepository path: {self.repository_path}\nData: {self.data}"

    def metadata(self):
        return {
            "language": self.language,
            "path": self.repository_path,
        }
