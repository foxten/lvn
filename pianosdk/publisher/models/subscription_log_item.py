from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.term import Term


class SubscriptionLogItem(BaseModel):
    subscription_id: Optional[str]
    email: Optional[str]
    uid: Optional[str]
    rid: Optional[str]
    term: Optional['Term']
    billing_plan: Optional[str]
    start_date: Optional[datetime]
    next_bill_date: Optional[datetime]
    status_name_in_reports: Optional[str]
    child_access: Optional[str]


SubscriptionLogItem.update_forward_refs()
