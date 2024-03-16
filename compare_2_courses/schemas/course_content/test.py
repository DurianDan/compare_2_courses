from compare_2_courses.schemas.course_content.course_material import CourseMaterial, COURSE_MATERIAL_TYPE
from typing import Any, Dict

class CourseTest(CourseMaterial):
    material_type: COURSE_MATERIAL_TYPE = "TEST"
