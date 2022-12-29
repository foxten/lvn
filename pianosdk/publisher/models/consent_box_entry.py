from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class ConsentBoxEntry(BaseModel):
    field_name: Optional[str]
    display_text: Optional[str]
    entry: Optional[bool]
    create_date: Optional[datetime]
    type: Optional[str]


ConsentBoxEntry.update_forward_refs()
