from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class SchedulePeriod(BaseModel):
    period_id: Optional[str]
    name: Optional[str]
    sell_date: Optional[datetime]
    begin_date: Optional[datetime]
    end_date: Optional[datetime]
    status: Optional[str]


SchedulePeriod.update_forward_refs()
