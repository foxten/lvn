from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class Bill(BaseModel):
    bill_id: Optional[str]
    type: Optional[str]
    creation_date: Optional[str]
    status: Optional[str]
    url: Optional[str]
    rid: Optional[str]
    resource_name: Optional[str]
    resource_image_url: Optional[str]
    name: Optional[str]
    payment_billing_plan: Optional[str]
    cancelable: Optional[str]


Bill.update_forward_refs()
