from compare_2_courses.analytics.compare_report import CompareReport, CourseMaterial
from compare_2_courses.schemas.course import Course

from typing import List


class Analyzer():
    def __init__(
        self,
        left_course: Course,
        right_course: Course,
    ) -> None:
        self.left_course = left_course
        self.right_course = right_course
        self.left_course.materials = self.sort_by_title(self.left_course.materials)
        self.right_course.materials = self.sort_by_title(self.right_course.materials)
    
    def init_report(self) -> CompareReport:
        return CompareReport()

    def sort_by_title(self, materials: List[CourseMaterial]) -> List[CourseMaterial]:
        return sorted(materials, key=lambda x: x.title)

    def analyze(self) -> CompareReport:
        report = self.init_report()
        # Check each object in list_a for uniqueness or sameness
        for material_left in self.sort_by_title(self.left_course.materials):
            found_same = False
            for material_right in self.right_course.materials:
                if material_left.is_same(material_right):
                    report.same_materials.append(material_left)
                    found_same = True
                    break
            if not found_same:
                report.course_left_unique_materials.append(material_left)

        # Check each object in list_b for uniqueness
        for material_right in self.right_course.materials:
            if all(not material_right.is_same(material) for material in report.same_materials):
                report.course_right_unique_materials.append(material_right)
        return report