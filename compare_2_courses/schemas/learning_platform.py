from pydantic import BaseModel, HttpUrl


class LearningPlatform(BaseModel):
    landing_page: HttpUrl
    name: str