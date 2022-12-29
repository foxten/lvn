from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class C2ExperienceConfig(BaseModel):
    aid: Optional[str]
    version: Optional[int]
    js: Optional[str]
    published: Optional[bool]
    published_date: Optional[datetime]


C2ExperienceConfig.update_forward_refs()
