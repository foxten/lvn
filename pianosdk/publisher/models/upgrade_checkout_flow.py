from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.user import User


class UpgradeCheckoutFlow(BaseModel):
    checkout_flow_id: Optional[str]
    name: Optional[str]
    checkout_flow_type: Optional[str]
    description: Optional[str]
    create_date: Optional[datetime]
    create_by: Optional['User']
    update_date: Optional[datetime]
    update_by: Optional['User']
    deleted: Optional[bool]
    billing_timing: Optional[str]
    immediate_access: Optional[bool]
    prorate_access: Optional[bool]


UpgradeCheckoutFlow.update_forward_refs()
