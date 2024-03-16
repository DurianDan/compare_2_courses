from pydantic import BaseModel, HttpUrl
from typing import List, Any, Dict, Union
from json import loads

from compare_2_courses.schemas.course_content import (
    CourseVideo, CourseLab, CourseReading, CourseTest, read_course_material
)
from compare_2_courses.schemas.learning_platform import LearningPlatform


class Course(BaseModel):
    landing_page: HttpUrl
    title: str
    learning_platform: LearningPlatform
    materials: List[Union[CourseVideo, CourseLab, CourseReading, CourseTest]] = []

    def to_json_dict(self) -> Dict[str,Any]:
        return loads(self.model_dump_json())
    
    @classmethod
    def read_json_dict(cls, data: Dict[str,Any]) -> 'Course':
        materials = [
            read_course_material(m)
            for m in data["materials"]
        ]
        return Course(
            landing_page=data['landing_page']
            , title=data['title']
            , learning_platform=LearningPlatform.read_json_dict(data['learning_platform'])
            , materials=materials
        )