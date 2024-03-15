from typing import List
from abc import ABC, abstractmethod

from compare_2_courses.schemas.course_content.video import CourseVideo
from compare_2_courses.schemas.course_content.reading import CourseReading
from compare_2_courses.schemas.course_content.test import CourseTest
from compare_2_courses.schemas.course_content.course_material import CourseMaterial
from compare_2_courses.schemas.learning_platform import LearningPlatform


class CoursePlatformScraper(ABC):
    learning_platform: LearningPlatform

    @abstractmethod
    def get_course_videos(self) -> List[CourseVideo]: ...
    @abstractmethod
    def get_course_readings(self) -> List[CourseReading]: ...
    @abstractmethod
    def get_course_tests(self) -> List[CourseTest]: ...

    def get_course_materials(self) -> List[CourseMaterial]:
        return (
            self.get_course_readings()
            + self.get_course_tests()
            + self.get_course_videos()
        )
