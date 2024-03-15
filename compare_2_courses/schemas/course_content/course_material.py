from typing import Optional
from pydantic import BaseModel, HttpUrl


class CourseMaterial(BaseModel):
    material_url: Optional[HttpUrl] = None
    title: Optional[str] = None
    description: Optional[str] = None
    learning_order: int

    def is_same(self, other_material: "CourseMaterial") -> bool:
        return (
            self.title == other_material.title
            and self.description == other_material.description
        )
