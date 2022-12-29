from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.term import Term


class TermWrapper(BaseModel):
    term: Optional['Term']
    changable: Optional[bool]
    payment_billing_plan: Optional[str]
    tooltip: Optional[str]
    from_scheduled: Optional[bool]


TermWrapper.update_forward_refs()
