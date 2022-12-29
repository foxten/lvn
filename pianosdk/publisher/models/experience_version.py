from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class ExperienceVersion(BaseModel):
    experience_id: Optional[str]
    version: Optional[int]
    committed: Optional[bool]
    committed_date: Optional[datetime]
    revision_notes: Optional[str]


ExperienceVersion.update_forward_refs()
