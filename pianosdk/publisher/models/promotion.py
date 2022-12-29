from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.promotion_fixed_discountt import PromotionFixedDiscountt
from typing import List


class Promotion(BaseModel):
    promotion_id: Optional[str]
    aid: Optional[str]
    name: Optional[str]
    status: Optional[str]
    fixed_promotion_code: Optional[str]
    unlimited_uses: Optional[bool]
    promotion_code_prefix: Optional[str]
    new_customers_only: Optional[bool]
    discount_amount: Optional[float]
    discount_currency: Optional[str]
    discount: Optional[str]
    percentage_discount: Optional[float]
    discount_type: Optional[str]
    uses_allowed: Optional[int]
    uses: Optional[int]
    never_allow_zero: Optional[bool]
    term_dependency_type: Optional[str]
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    create_date: Optional[datetime]
    create_by: Optional[str]
    update_date: Optional[datetime]
    update_by: Optional[str]
    deleted: Optional[bool]
    fixed_discount_list: Optional['List[PromotionFixedDiscountt]']
    apply_to_all_billing_periods: Optional[bool]
    can_be_applied_on_renewal: Optional[bool]
    billing_period_limit: Optional[int]


Promotion.update_forward_refs()
