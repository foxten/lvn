from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class DynamicSubscriptionAccessPeriodInfo(BaseModel):
    access_period_id: Optional[str]
    name: Optional[str]
    total_iterations: Optional[int]
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    converted: Optional[bool]
    iteration: Optional[int]
    payment_billing_plan: Optional[str]
    length: Optional[str]
    virtual: Optional[bool]
    id: Optional[str]


DynamicSubscriptionAccessPeriodInfo.update_forward_refs()
