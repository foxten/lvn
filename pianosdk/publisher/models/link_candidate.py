from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class LinkCandidate(BaseModel):
    term_id: Optional[str]
    name: Optional[str]
    type: Optional[str]
    payment_billing_plan_description: Optional[str]
    current_logic_id: Optional[str]
    current_logic_name: Optional[str]


LinkCandidate.update_forward_refs()
