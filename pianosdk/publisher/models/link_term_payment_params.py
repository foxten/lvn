from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class LinkTermPaymentParams(BaseModel):
    amount: Optional[float]
    currency: Optional[str]


LinkTermPaymentParams.update_forward_refs()
