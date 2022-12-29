from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.access import Access
from pianosdk.publisher.models.period import Period
from pianosdk.publisher.models.promo_code import PromoCode
from pianosdk.publisher.models.schedule import Schedule
from pianosdk.publisher.models.term import Term
from pianosdk.publisher.models.term_conversion_subscription import TermConversionSubscription
from pianosdk.publisher.models.user_payment_dto import UserPaymentDTO
from pianosdk.publisher.models.user_payment_info import UserPaymentInfo


class TermConversionDTO(BaseModel):
    term_conversion_id: Optional[str]
    term: Optional['Term']
    type: Optional[str]
    aid: Optional[str]
    user_access: Optional['Access']
    user_payment: Optional['UserPaymentDTO']
    create_date: Optional[datetime]
    browser_id: Optional[str]
    subscription: Optional['TermConversionSubscription']
    promo_code: Optional['PromoCode']
    user_payment_info: Optional['UserPaymentInfo']
    schedule: Optional['Schedule']
    period: Optional['Period']


TermConversionDTO.update_forward_refs()
