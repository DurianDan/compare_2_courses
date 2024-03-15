from pydantic import BaseModel, HttpUrl
from typing import List, Any, Dict

from compare_2_courses.schemas.course_content.course_material import CourseMaterial
from compare_2_courses.schemas.learning_platform import LearningPlatform


class Course(BaseModel):
    landing_page: HttpUrl
    title: str
    learning_platform: LearningPlatform
    materials: List[CourseMaterial] = []

    def to_json(self) -> Dict[str, Any]:
        parent_dict = dict(self)
        parent_dict["landing_page"] = str(self.landing_page)
        parent_dict["learning_platform"] = self.learning_platform.to_json()
        parent_dict["materials"] = [
            material.to_json()
            for material
            in self.materials]
        return parent_dict
