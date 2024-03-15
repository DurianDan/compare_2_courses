from pydantic import BaseModel
from compare_2_courses.schemas.course import Course

class ScraperConfig(BaseModel):
    course_config: Course
    