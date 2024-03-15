from compare_2_courses.constants import DEFAULT_CHROME_SELENIUM_OPTIONS

from typing import List
from undetected_chromedriver import ChromeOptions, Chrome


def get_chrome_options(
    options: List[str] = DEFAULT_CHROME_SELENIUM_OPTIONS
) -> ChromeOptions:
    op = ChromeOptions()
    for opt in options:
        op.add_argument(opt)
    return op


def get_default_chrome_driver(
    options: List[str] = DEFAULT_CHROME_SELENIUM_OPTIONS
) -> Chrome:
    return Chrome(
        options=get_chrome_options(options),
        seleniumwire_options={}
    )
