from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class AccessPeriodStats(BaseModel):
    access_period_id: Optional[str]
    active_subscription_count: Optional[int]


AccessPeriodStats.update_forward_refs()
