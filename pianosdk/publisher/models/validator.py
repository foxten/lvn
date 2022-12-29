from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class Validator(BaseModel):
    fieldset_id: Optional[int]
    validator_id: Optional[int]
    name: Optional[str]
    rvalue: Optional[str]
    create_date: Optional[datetime]
    update_date: Optional[datetime]


Validator.update_forward_refs()
