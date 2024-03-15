from typing import Optional, Any, Dict, Literal
from pydantic import BaseModel, HttpUrl


COURSE_MATERIAL_TYPE = Literal["VIDEO", "TEST", "READING"]


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
    
    def to_json(self) -> Dict[str,Any]:
        out = dict(self)
        if self.material_url is not None:
            out["material_url"] = str(self.material_url)
        return out