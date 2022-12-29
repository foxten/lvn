from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class TermBrief(BaseModel):
    term_id: Optional[str]
    name: Optional[str]
    disabled: Optional[bool]


TermBrief.update_forward_refs()
