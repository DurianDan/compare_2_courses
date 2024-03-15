from compare_2_courses.schemas.course_content.course_material import CourseMaterial
from typing import Optional, Dict, Any


class CourseVideo(CourseMaterial):
    size_mb: Optional[int] = None
    length_seconds: int

    def is_same(self, other_material: "CourseVideo") -> bool:
        return (
            self.length_seconds == other_material.length_seconds
            and self.title == self.title
        )
    
    def to_json(self) -> Dict[str, Any]:
        out = super().to_json()
        out['material_type'] = "VIDEO"
        return out