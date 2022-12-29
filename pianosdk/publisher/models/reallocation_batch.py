from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class ReallocationBatch(BaseModel):
    subscribers_count: Optional[int]
    access_end_date: Optional[datetime]
    renewal_date: Optional[datetime]


ReallocationBatch.update_forward_refs()
