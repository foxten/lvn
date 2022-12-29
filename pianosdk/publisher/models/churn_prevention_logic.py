from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class ChurnPreventionLogic(BaseModel):
    logic_id: Optional[str]
    name: Optional[str]
    description: Optional[str]
    create_date: Optional[datetime]
    update_date: Optional[datetime]
    default: Optional[bool]
    terms_count: Optional[int]
    scenarios: Optional[str]


ChurnPreventionLogic.update_forward_refs()
