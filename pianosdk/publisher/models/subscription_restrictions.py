from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class SubscriptionRestrictions(BaseModel):
    allow_change_next_bill_date: Optional[bool]
    allow_enable_auto_renew: Optional[bool]
    allow_switch_payment_method: Optional[bool]
    allow_scheduler_renewals: Optional[bool]
    allow_future_renewals: Optional[bool]
    allow_verify_now: Optional[bool]


SubscriptionRestrictions.update_forward_refs()
