from pydantic import Field
from compare_2_courses.schemas.course_content.course_material import CourseMaterial, COURSE_MATERIAL_TYPE


class CourseLab(CourseMaterial):
    material_type: COURSE_MATERIAL_TYPE = "LAB"
