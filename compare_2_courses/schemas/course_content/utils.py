from compare_2_courses.schemas.course_content.lab import CourseLab
from compare_2_courses.schemas.course_content.reading import CourseReading
from compare_2_courses.schemas.course_content.video import CourseVideo
from compare_2_courses.schemas.course_content.test import CourseTest
from compare_2_courses.schemas.course_content.course_material import COURSE_MATERIAL_TYPE

from typing import Union, Dict, Any


MATERIAL_TYPE_MAP: Dict[COURSE_MATERIAL_TYPE, Any] = {
    "READING": CourseReading,
    "LAB": CourseLab,
    "VIDEO":CourseVideo,
    "TEST": CourseTest}


def read_course_material(
    data: Dict[str, Any]
) -> Union[CourseLab, CourseReading, CourseVideo, CourseTest]:
    return MATERIAL_TYPE_MAP[data['material_type']](
        **data
    )
