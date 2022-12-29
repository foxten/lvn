from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.reallocation_batch import ReallocationBatch
from typing import List


class TermPeriodReallocation(BaseModel):
    term_pub_id: Optional[str]
    name: Optional[str]
    period_pub_id: Optional[str]
    next_period_sell_date: Optional[datetime]
    access_end_date: Optional[datetime]
    renewal_date: Optional[datetime]
    total_subscribers: Optional[int]
    subscribers_batches: Optional['List[ReallocationBatch]']
    batches_with_pending_changes: Optional['List[ReallocationBatch]']
    is_reallocation_in_progress: Optional[bool]


TermPeriodReallocation.update_forward_refs()
