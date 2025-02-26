from pydantic import Field
from clasifiers.clasiffier_base import ClasiffierBase


class CodeClasifierTxtFile(ClasiffierBase):
    list_of_libraries: list[str] = Field(
        description="List of libraries used in the code"
    )
    list_of_deprecated_libraries: list[str] = Field(
        description="List of deprecated libraries used in the code"
    )
    list_of_unsecure_libraries: list[str] = Field(
        description="List of unsecure libraries used in the code"
    )

    def to_text(self):
        return (
            super().to_text()
            + f"\nList of libraries: {self.list_of_libraries}\nList of deprecated libraries: {self.list_of_deprecated_libraries}\nList of unsecure libraries: {self.list_of_unsecure_libraries}"
        )
