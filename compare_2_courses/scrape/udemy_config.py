from compare_2_courses.scrape.course_scraper import CoursePlatformScraper
from compare_2_courses.scrape.scraper_config import ScraperConfig
from compare_2_courses.constants import UDEMY_LEARNING_PLATFORM

import requests
from lxml import html
from lxml.html import HtmlElement


class UdemyScraper(CoursePlatformScraper):
    learning_platform = UDEMY_LEARNING_PLATFORM

    def __init__(self, scraper_config: ScraperConfig) -> None:
        self.config = scraper_config

    