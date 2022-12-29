from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class VersionItem(BaseModel):
    name: Optional[str]
    description: Optional[str]
    aid: Optional[str]
    type: Optional[str]
    published: Optional[bool]
    version: Optional[int]
    update_date: Optional[datetime]


VersionItem.update_forward_refs()
