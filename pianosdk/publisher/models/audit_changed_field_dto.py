from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class AuditChangedFieldDto(BaseModel):
    field_name: Optional[str]
    new_value: Optional[str]
    old_value: Optional[str]
    diff: Optional[str]


AuditChangedFieldDto.update_forward_refs()
