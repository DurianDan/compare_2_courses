from typing import Dict, Any
from pydantic import BaseModel, HttpUrl


class LearningPlatform(BaseModel):
    landing_page: HttpUrl
    name: str

    def to_json(self) -> Dict[str,Any]:
        out = dict(self)
        out['landing_page'] = str(self.landing_page)
        return out