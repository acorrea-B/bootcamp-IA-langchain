from pydantic import Field
from clasifiers.clasiffier_base import ClasiffierBase


class CodeClasifierMdFile(ClasiffierBase):
    
    resume: str = Field( description="A brief summary of the repository.")
    code: str = Field( description="The repository's code to be classified.")

    def to_text(self):
        return super().to_text() + f"\nResume: {self.resume}\nCode: {self.code}"