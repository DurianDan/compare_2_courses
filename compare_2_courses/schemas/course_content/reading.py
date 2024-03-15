from typing import Any, Dict
from compare_2_courses.schemas.course_content.course_material import CourseMaterial


class CourseReading(CourseMaterial):
    def to_json(self) -> Dict[str, Any]:
        out = super().to_json()
        out['material_type'] = "READING"
        return out