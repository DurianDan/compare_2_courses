from typing import List
from pydantic import BaseModel

from compare_2_courses.schemas.course_content.course_material import CourseMaterial


class CompareReport(BaseModel):
    course_left_unique_materials: List[CourseMaterial] = []
    course_right_unique_materials: List[CourseMaterial] = []
    same_materials: List[CourseMaterial] = []
