from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.term_period_reallocation import TermPeriodReallocation
from typing import List


class TermReallocation(BaseModel):
    name: Optional[str]
    term_type: Optional[str]
    term_pub_id: Optional[str]
    periods: Optional['List[TermPeriodReallocation]']
    active_period_count: Optional[int]
    active_subscribers_count: Optional[int]


TermReallocation.update_forward_refs()
