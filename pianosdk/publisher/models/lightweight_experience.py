from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class LightweightExperience(BaseModel):
    experience_id: Optional[str]
    title: Optional[str]


LightweightExperience.update_forward_refs()
