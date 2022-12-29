from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class SubscriptionUpgradeStatus(BaseModel):
    from_term_name: Optional[str]
    to_term_name: Optional[str]
    from_term_id: Optional[str]
    to_term_id: Optional[str]
    change_date: Optional[str]
    create_date_from: Optional[str]
    create_date_to: Optional[str]
    billing_plan_to: Optional[str]
    billing_plan_from: Optional[str]
    status: Optional[int]
    error_message: Optional[str]
    prorate_amount: Optional[str]
    prorate_refund_amount: Optional[str]


SubscriptionUpgradeStatus.update_forward_refs()
