from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class ExperienceScript(BaseModel):
    script_id: Optional[str]
    script_name: Optional[str]
    script_code: Optional[str]


ExperienceScript.update_forward_refs()
