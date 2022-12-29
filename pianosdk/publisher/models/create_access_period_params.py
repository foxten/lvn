from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.duration import Duration


class CreateAccessPeriodParams(BaseModel):
    name: Optional[str]
    type: Optional[str]
    access_end_date: Optional[date]
    total_iterations: Optional[int]
    duration: Optional['Duration']
    amount: Optional[float]
    billing_type: Optional[str]
    billing_duration: Optional['Duration']
    billing_day: Optional[int]
    billing_month: Optional[int]


CreateAccessPeriodParams.update_forward_refs()
