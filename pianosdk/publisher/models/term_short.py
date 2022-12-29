from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class TermShort(BaseModel):
    term_id: Optional[str]
    name: Optional[str]
    disabled: Optional[bool]
    tooltip: Optional[str]


TermShort.update_forward_refs()
