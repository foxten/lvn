from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class UserAccessDto(BaseModel):
    term_name: Optional[str]
    payment_billing_plan: Optional[str]
    billing_plan: Optional[str]
    image_url: Optional[str]
    resource_name: Optional[str]
    type: Optional[str]
    type_label: Optional[str]
    rid: Optional[str]
    term_id: Optional[str]
    create_date: Optional[str]
    expire_date: Optional[str]
    status: Optional[str]
    status_localized: Optional[str]
    access_id: Optional[str]


UserAccessDto.update_forward_refs()
