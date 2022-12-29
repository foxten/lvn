from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class Rule(BaseModel):
    field_id: Optional[int]
    validator_id: Optional[int]
    rule_id: Optional[int]
    name: Optional[str]
    rule: Optional[str]
    rvalue: Optional[str]
    create_date: Optional[datetime]
    update_date: Optional[datetime]


Rule.update_forward_refs()
