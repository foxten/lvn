from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class Mandate(BaseModel):
    reference: Optional[str]
    id: Optional[str]
    next_charge_date: Optional[datetime]


Mandate.update_forward_refs()
