from typing import Optional
from pydantic import BaseModel, HttpUrl


class CourseMaterial(BaseModel):
    material_url: HttpUrl
    title: Optional[str]
    description: Optional[str]
    learning_order: int

    def is_same(self, other_material: "CourseMaterial") -> bool:
        return (
            self.title == other_material.title
            and self.description == other_material.description
        )
