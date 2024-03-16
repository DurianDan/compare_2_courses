from typing import Optional, Literal
from pydantic import BaseModel, HttpUrl
from difflib import SequenceMatcher

def similarity(a:str, b:str) -> float:
    return SequenceMatcher(None, a, b).ratio()

COURSE_MATERIAL_TYPE = Literal[
    "VIDEO",
    "TEST",
    "READING",
    "LAB",
]


class CourseMaterial(BaseModel):
    material_url: Optional[HttpUrl] = None
    title: Optional[str] = None
    description: Optional[str] = None
    learning_order: int


    def same_title(self, title1: str, title2: str) -> bool:
        return similarity(title1, title2) >= 0.6

    def is_same(self, other_material: "CourseMaterial") -> bool:
        if self.material_type != other_material.material_type:
            return False
        return (self.same_title(self.title,other_material.title)
            and self.description == other_material.description
        )
