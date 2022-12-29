from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from typing import List


class WorldpayPaymentMethod(BaseModel):
    card: Optional[List[str]]
    apm: Optional[List[str]]


WorldpayPaymentMethod.update_forward_refs()
