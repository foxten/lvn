from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class BrowserSegment(BaseModel):
    segment_id: Optional[str]
    name: Optional[str]
    sort_order: Optional[int]
    filter: Optional[str]


BrowserSegment.update_forward_refs()
