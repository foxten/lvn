from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class PromotionFixedDiscountt(BaseModel):
    fixed_discount_id: Optional[str]
    currency: Optional[str]
    amount: Optional[str]


PromotionFixedDiscountt.update_forward_refs()
