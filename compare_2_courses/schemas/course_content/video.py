from compare_2_courses.schemas.course_content.course_material import CourseMaterial
from typing import Optional


class CourseVideo(CourseMaterial):
    size_mb: Optional[int] = None
    length_seconds: int

    def is_same(self, other_material: "CourseVideo") -> bool:
        return (
            self.length_seconds == other_material.length_seconds
            and self.title == self.title
        )
