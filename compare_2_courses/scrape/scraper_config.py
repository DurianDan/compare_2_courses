from pydantic import BaseModel, HttpUrl
from compare_2_courses.schemas.learning_platform import LearningPlatform

class ScraperConfig(BaseModel):
    course_landing_page: HttpUrl
    