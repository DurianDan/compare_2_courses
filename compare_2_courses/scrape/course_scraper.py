from typing import List, Literal
from abc import ABC, abstractmethod

from compare_2_courses.schemas.course_content.video import CourseVideo
from compare_2_courses.schemas.course_content.reading import CourseReading
from compare_2_courses.schemas.course_content.test import CourseTest
from compare_2_courses.schemas.course_content.course_material import CourseMaterial, COURSE_MATERIAL_TYPE
from compare_2_courses.schemas.learning_platform import LearningPlatform


class CoursePlatformScraper(ABC):
    learning_platform: LearningPlatform

    @abstractmethod
    def detect_material_type(self) -> COURSE_MATERIAL_TYPE: ...
    @abstractmethod
    def access(self) -> None:
        """Request the URL, to get the HTML"""
        ...

    @abstractmethod
    def get_course_materials(self) -> List[CourseMaterial]: ...
