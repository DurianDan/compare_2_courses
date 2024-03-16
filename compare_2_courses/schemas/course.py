from pydantic import BaseModel, HttpUrl
from typing import List, Any, Dict, Union
from json import loads

from compare_2_courses.schemas.course_content import (
    CourseVideo, CourseLab, CourseReading, CourseTest
)
from compare_2_courses.schemas.learning_platform import LearningPlatform


class Course(BaseModel):
    landing_page: HttpUrl
    title: str
    learning_platform: LearningPlatform
    materials: List[Union[CourseVideo, CourseLab, CourseReading, CourseTest]] = []

    def to_json_dict(self) -> Dict[str,Any]:
        return loads(self.model_dump_json())