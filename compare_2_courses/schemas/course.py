from pydantic import BaseModel, HttpUrl
from typing import List

from compare_2_courses.schemas.course_content.course_material import CourseMaterial
from compare_2_courses.schemas.learning_platform import LearningPlatform

class Course(BaseModel):
    landing_page: HttpUrl
    title: str
    learning_platform: LearningPlatform
    materials: List[CourseMaterial] = []