from compare_2_courses.schemas.learning_platform import LearningPlatform
from compare_2_courses.schemas.course import Course


UDEMY_LEARNING_PLATFORM = LearningPlatform(
    landing_page="https://udemy.com", name="Udemy"
)

AWS_DEA_01_2024_HANDS_ON = Course(
    landing_page="https://www.udemy.com/course/aws-data-engineer/",
    title="AWS Certified Data Engineer Associate 2024 - Hands On!",
    learning_platform=UDEMY_LEARNING_PLATFORM,
)
ULTIMATE_AWS_SAA_C03 = Course(
    landing_page="https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/",
    title="Ultimate AWS Certified Solutions Architect Associate SAA-C03",
    learning_platform=UDEMY_LEARNING_PLATFORM,
)

ULTIMATE_AWS_SAP_C02_2024 = Course(
    landing_page="https://www.udemy.com/course/aws-solutions-architect-professional/",
    title="Ultimate AWS Certified Solutions Architect Professional 2024",
    learning_platform=UDEMY_LEARNING_PLATFORM,
)

AWS_2024_DOP_C02 = Course(
    landing_page="https://www.udemy.com/course/aws-certified-devops-engineer-professional-hands-on/",
    title="AWS Certified DevOps Engineer Professional 2024 - DOP-C02",
    learning_platform=UDEMY_LEARNING_PLATFORM,
)

ULTIMATE_AWS_NEW_2024_SCS_C02 = Course(
    landing_page="https://www.udemy.com/course/ultimate-aws-certified-security-specialty/",
    title="Ultimate AWS Certified Security Specialty [NEW 2024] SCS-C02",
    learning_platform=UDEMY_LEARNING_PLATFORM,
)

DEFAULT_CHROME_SELENIUM_OPTIONS = [
    "--incognito"
    , '--ignore-ssl-errors=yes'
    , '--ignore-certificate-errors'
    #, "--headless"
]