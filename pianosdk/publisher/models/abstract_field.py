from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class AbstractField(BaseModel):
    fieldset_id: Optional[int]
    field_id: Optional[int]
    name: Optional[str]
    descr: Optional[str]
    kind: Optional[str]
    type: Optional[str]
    value: Optional[str]
    create_date: Optional[datetime]
    update_date: Optional[datetime]


AbstractField.update_forward_refs()
