from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class ExternalAPIField(BaseModel):
    field_name: Optional[str]
    field_title: Optional[str]
    description: Optional[str]
    mandatory: Optional[bool]
    hidden: Optional[bool]
    default_value: Optional[str]
    order: Optional[int]
    type: Optional[str]
    editable: Optional[str]


ExternalAPIField.update_forward_refs()
