from compare_2_courses.schemas.course_content.course_material import (
    CourseMaterial,
    COURSE_MATERIAL_TYPE,
)
from typing import Optional, Dict, Any


class CourseVideo(CourseMaterial):
    size_mb: Optional[int] = None
    length_seconds: int
    material_type: COURSE_MATERIAL_TYPE = "VIDEO"

    def same_video_length(self, l1, l2) -> bool:
        if l1 == l2: return True
        greater, smaller = l1,l2
        if greater < smaller: greater,smaller = smaller,greater
        return smaller/greater > 0.8
        
    def is_same(self, other_material: "CourseVideo") -> bool:
        if self.material_type != other_material.material_type:
            return False
        return (
            self.same_title(self.title,other_material.title)
            and self.same_video_length(self.length_seconds, other_material.length_seconds)
        )
