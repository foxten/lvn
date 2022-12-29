from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.period import Period
from typing import List


class Schedule(BaseModel):
    aid: Optional[str]
    name: Optional[str]
    schedule_id: Optional[str]
    deleted: Optional[bool]
    create_date: Optional[datetime]
    update_date: Optional[datetime]
    periods: Optional['List[Period]']


Schedule.update_forward_refs()
