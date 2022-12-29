from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class AddressConfig(BaseModel):
    selected: Optional[bool]
    selected_by_default: Optional[bool]
    address_field: Optional[str]
    required: Optional[bool]
    default_value: Optional[str]
    field: Optional[str]


AddressConfig.update_forward_refs()
