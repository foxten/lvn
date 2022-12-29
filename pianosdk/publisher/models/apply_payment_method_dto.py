from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class ApplyPaymentMethodDTO(BaseModel):
    updated_subscription_count: Optional[int]
    update_failed_subscription_count: Optional[int]


ApplyPaymentMethodDTO.update_forward_refs()
