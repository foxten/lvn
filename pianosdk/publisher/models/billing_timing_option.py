from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class BillingTimingOption(BaseModel):
    value: Optional[str]
    name: Optional[str]
    secure_enabled: Optional[bool]


BillingTimingOption.update_forward_refs()
