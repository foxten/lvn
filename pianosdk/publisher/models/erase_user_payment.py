from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class EraseUserPayment(BaseModel):
    user_payment_id: Optional[str]
    tax: Optional[str]
    billing_region: Optional[str]
    residence_region: Optional[str]
    ui_caption: Optional[str]
    name: Optional[str]
    address: Optional[str]
    geo_location: Optional[str]


EraseUserPayment.update_forward_refs()
