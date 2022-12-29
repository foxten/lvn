from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.user_address import UserAddress


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
    term_id: Optional[str]
    resource_name: Optional[str]
    price: Optional[str]
    transaction_id: Optional[str]
    is_revocable: Optional[bool]
    is_refundable: Optional[bool]
    is_resendable: Optional[bool]
    refund_amount: Optional[str]
    refund_amount_recalculated: Optional[bool]
    user_address: Optional['UserAddress']


Voucher.update_forward_refs()
