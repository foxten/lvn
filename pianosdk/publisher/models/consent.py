from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class Consent(BaseModel):
    consent_id: Optional[str]
    field_name: Optional[str]
    field_id: Optional[str]
    display_text: Optional[str]
    error_message: Optional[str]
    type: Optional[str]
    pre_checked: Optional[bool]
    required: Optional[bool]
    enabled: Optional[bool]
    field_id_enabled: Optional[bool]


Consent.update_forward_refs()
