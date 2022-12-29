from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.currency import Currency


class Money(BaseModel):
    amount: Optional[float]
    currency: Optional['Currency']


Money.update_forward_refs()
