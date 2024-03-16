from compare_2_courses.schemas.course import Course
from compare_2_courses.schemas.course_content import (
    CourseReading,
    CourseVideo,
    CourseTest,
    CourseMaterial,
    CourseLab,
    COURSE_MATERIAL_TYPE,
)
from compare_2_courses.scrape.scraper_config import ScraperConfig
from compare_2_courses.scrape.course_scraper import CoursePlatformScraper
from compare_2_courses.constants import UDEMY_LEARNING_PLATFORM

import time
from typing import List, Union, Dict, Any
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from seleniumwire.undetected_chromedriver import Chrome


class UdemyScraper(CoursePlatformScraper):
    learning_platform = UDEMY_LEARNING_PLATFORM

    def __init__(self, scraper_config: ScraperConfig, driver: Chrome) -> None:
        self.config = scraper_config
        self.driver = driver

    def minutes_str_to_seconds(self, minutes:str) -> int:
        minutes, seconds = map(int, minutes.split(':'))
        return minutes * 60 + seconds
    
    def click_expand_course_content(self) -> None:
        expand_button = self.driver.find_element(
            By.CSS_SELECTOR, 'button[data-purpose="expand-toggle"]'
        )
        if "Expand all sections" == expand_button.text.strip():
            expand_button.click()

    def get_course_materials_elements(self) -> List[WebElement]:
        return self.driver.find_elements(
            By.XPATH,
            '//div[@data-purpose="course-curriculum"]/div[2]/div[*]/div[2]/div/ul/li[*]/div',
        )

    def detect_material_type(
        self, element: WebElement
    ) -> COURSE_MATERIAL_TYPE:
        found_icon_type = (element
            .find_element(By.TAG_NAME, "use")
            .get_attribute("xlink:href"))
        icon_type_map = {
            '#icon-article': "READING"
            , '#icon-lightbulb-off': "TEST"
            , '#icon-quiz': "TEST"
            , '#icon-video': "VIDEO"
            , "#icon-code": "LAB"
        }
        return icon_type_map.get(found_icon_type)

    def get_material_common_info_from_element(self, element: WebElement, learning_order: int) -> CourseMaterial:
        return CourseMaterial(
            title=element.find_element(
                By.CSS_SELECTOR,
                'div[class="ud-block-list-item-content"]>div>div'
            ).text,
            learning_order=learning_order
        )
    
    def get_video_length_seconds(self, element: WebElement) -> int:
        video_length_str = element.find_elements(
            By.CSS_SELECTOR,
            'div[class="ud-block-list-item-content"]>span'
        )[-1].text
        return self.minutes_str_to_seconds(video_length_str)

    def get_course_video_from_element(
        self, element: WebElement, learning_order: int
    ) -> CourseVideo:
        common_material = self.get_material_common_info_from_element(
            element, learning_order
        )
        video_material = CourseVideo(
            title=common_material.title,
            learning_order=common_material.learning_order,
            length_seconds=self.get_video_length_seconds(element)
        )
        return video_material

    def get_course_test_from_element(
        self, element: WebElement, learning_order: int
    ) -> CourseTest:
        common_material = self.get_material_common_info_from_element(
            element, learning_order
        )
        return CourseTest(**dict(common_material))

    def get_course_reading_from_element(
        self, element: WebElement, learning_order: int
    ) -> CourseReading:
        common_material = self.get_material_common_info_from_element(
            element, learning_order
        )
        return CourseReading(**dict(common_material))
    
    def get_course_lab_from_element(
        self, element: WebElement, learning_order: int
    ) -> CourseLab:
        common_material = self.get_material_common_info_from_element(
            element, learning_order
        )
        return CourseLab(**dict(common_material))
    
    def get_course_material_from_element(
        self, element: WebElement, learning_order: int
    ) -> Union[CourseReading,CourseTest, CourseVideo]:
        material_type = self.detect_material_type(element)
        material_extractor: Dict[COURSE_MATERIAL_TYPE, Any] = {
            "READING": self.get_course_reading_from_element,
            "TEST":self.get_course_test_from_element,
            "VIDEO":self.get_course_video_from_element,
            "LAB":self.get_course_lab_from_element
        }
        return material_extractor[material_type](
            element, learning_order
        )
    
    def get_course_materials(self) -> List[CourseMaterial]:
        material_elements = self.get_course_materials_elements()
        material_from_elements = [
            self.get_course_material_from_element(
                element, idx+1
            )
            for idx,element
            in enumerate(material_elements)
        ]
        return material_from_elements

    def get_course_title(self) -> str:
        return self.driver.find_element(
            By.XPATH, 
            '//h1[@data-purpose="lead-title"]'
        ).text.strip()
    
    def access(self) -> None:
        self.driver.get(str(self.config.course_landing_page))

    def scrape(self) -> Course:
        self.access()
        last_err = None
        for _ in range(5):
            try:
                self.click_expand_course_content()
                return Course(
                    landing_page=self.config.course_landing_page,
                    learning_platform=self.learning_platform,
                    title=self.get_course_title(),
                    materials=self.get_course_materials()
                )
            except Exception as err:
                last_err = err
                time.sleep(1)
        raise last_err