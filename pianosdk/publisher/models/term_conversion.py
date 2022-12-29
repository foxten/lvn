from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.access import Access
from pianosdk.publisher.models.period import Period
from pianosdk.publisher.models.promo_code import PromoCode
from pianosdk.publisher.models.schedule import Schedule
from pianosdk.publisher.models.term import Term
from pianosdk.publisher.models.user_payment import UserPayment
from pianosdk.publisher.models.user_payment_info import UserPaymentInfo
from pianosdk.publisher.models.user_subscription import UserSubscription


class TermConversion(BaseModel):
    term_conversion_id: Optional[str]
    term: Optional['Term']
    type: Optional[str]
    aid: Optional[str]
    user_access: Optional['Access']
    user_payment: Optional['UserPayment']
    create_date: Optional[datetime]
    browser_id: Optional[str]
    subscription: Optional['UserSubscription']
    promo_code: Optional['PromoCode']
    user_payment_info: Optional['UserPaymentInfo']
    billing_plan: Optional[str]
    price_after_discount: Optional[str]
    schedule: Optional['Schedule']
    period: Optional['Period']


TermConversion.update_forward_refs()
