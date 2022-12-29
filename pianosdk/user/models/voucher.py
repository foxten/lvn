from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class Voucher(BaseModel):
    pub_id: Optional[str]
    code: Optional[str]
    state: Optional[str]
    state_label: Optional[str]
    recipient_name: Optional[str]
    recipient_email: Optional[str]
    recipient_message: Optional[str]
    send_date: Optional[datetime]
    create_date: Optional[datetime]
    expires: Optional[str]
    expire_date: Optional[datetime]
    redeemed: Optional[datetime]
    revoke_date: Optional[datetime]
    period: Optional[str]
    app_name: Optional[str]
    term_name: Optional[str]
    term_type: Optional[str]
    resource_name: Optional[str]
    price: Optional[str]
    is_refundable: Optional[bool]


Voucher.update_forward_refs()
