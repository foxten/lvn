from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class Link(BaseModel):
    term_id: Optional[str]
    name: Optional[str]
    type: Optional[str]
    payment_billing_plan_description: Optional[str]
    rid: Optional[str]
    resource_name: Optional[str]


Link.update_forward_refs()
