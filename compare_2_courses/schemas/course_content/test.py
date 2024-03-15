from compare_2_courses.schemas.course_content.course_material import CourseMaterial
from typing import Any, Dict

class CourseTest(CourseMaterial):
    def to_json(self) -> Dict[str, Any]:
        out = super().to_json()
        out['material_type'] = "TEST"
        return out