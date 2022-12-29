from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class LightExperience(BaseModel):
    experience_id: Optional[str]
    title: Optional[str]
    aid: Optional[str]
    app_name: Optional[str]


LightExperience.update_forward_refs()
