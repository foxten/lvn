from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class UserSubscriptionDto(BaseModel):
    term_name: Optional[str]
    term_id: Optional[str]
    type: Optional[str]
    payment_billing_plan: Optional[str]
    billing_plan: Optional[str]
    image_url: Optional[str]
    resource_name: Optional[str]
    rid: Optional[str]
    next_bill_date: Optional[str]
    subscription_last_payment: Optional[str]
    status: Optional[str]
    status_label: Optional[str]
    creadit_card_expire: Optional[str]
    creadit_card_expire_soon: Optional[bool]
    subscription_id: Optional[str]
    payment_method: Optional[str]
    access_expired: Optional[bool]
    in_app_payment: Optional[bool]
    psc_subscriber_number: Optional[str]
    conversion_result: Optional[str]
    external_api_name: Optional[str]
    charge_count: Optional[int]
    status_display: Optional[str]
    auto_renew: Optional[bool]


UserSubscriptionDto.update_forward_refs()
