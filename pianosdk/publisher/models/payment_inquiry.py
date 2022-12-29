from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.app import App
from pianosdk.publisher.models.inquiry_comment import InquiryComment
from pianosdk.publisher.models.resource import Resource
from pianosdk.publisher.models.user import User
from typing import List


class PaymentInquiry(BaseModel):
    payment_inquiry_id: Optional[str]
    resource: Optional['Resource']
    app: Optional['App']
    state: Optional[int]
    inquiry_reason: Optional[str]
    create_date: Optional[str]
    inquiry_comments: Optional['List[InquiryComment]']
    category: Optional[str]
    update_state_by: Optional['User']
    update_state_date: Optional[str]
    start_date: Optional[str]
    expire_date: Optional[str]
    transaction_date: Optional[str]
    transaction_id: Optional[str]
    spent_money: Optional[float]
    spent_money_display: Optional[str]
    source: Optional[str]
    currency: Optional[str]
    refunded_date: Optional[str]
    is_access_expired: Optional[bool]
    is_access_revoked: Optional[bool]
    is_access_unlimited: Optional[bool]
    refund_amount: Optional[str]
    refund_amount_recalculated: Optional[bool]


PaymentInquiry.update_forward_refs()
