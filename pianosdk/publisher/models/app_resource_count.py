from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class AppResourceCount(BaseModel):
    aid: Optional[str]
    resource_count: Optional[int]


AppResourceCount.update_forward_refs()
