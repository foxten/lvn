from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.pay_source_dto import PaySourceDTO
from pianosdk.publisher.models.user import User
from typing import List


class CheckoutFlow(BaseModel):
    checkout_flow_id: Optional[str]
    name: Optional[str]
    checkout_flow_type: Optional[str]
    description: Optional[str]
    create_date: Optional[datetime]
    create_by: Optional['User']
    update_date: Optional[datetime]
    update_by: Optional['User']
    is_passwordless: Optional[bool]
    is_single_step_enabled: Optional[bool]
    is_auto_detect_email: Optional[bool]
    is_custom_checkout_modules_enabled: Optional[bool]
    deleted: Optional[bool]
    pay_sources: Optional['List[PaySourceDTO]']
    inline_checkout_modules: Optional[List[str]]
    modal_checkout_modules: Optional[List[str]]


CheckoutFlow.update_forward_refs()
