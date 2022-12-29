from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class SubscriptionReallocationError(BaseModel):
    error_message: Optional[str]
    error_element_index: Optional[int]
    field_name: Optional[str]


SubscriptionReallocationError.update_forward_refs()
