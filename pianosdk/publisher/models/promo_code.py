from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.user import User


class PromoCode(BaseModel):
    promo_code_id: Optional[str]
    promotion_id: Optional[str]
    code: Optional[str]
    assigned_email: Optional[str]
    reserve_date: Optional[datetime]
    state: Optional[str]
    state_value: Optional[str]
    claimed_user: Optional['User']
    claimed_date: Optional[datetime]
    create_date: Optional[datetime]
    create_by: Optional[str]
    update_date: Optional[datetime]
    update_by: Optional[str]
    deleted: Optional[bool]
    last_original_price: Optional[str]


PromoCode.update_forward_refs()
