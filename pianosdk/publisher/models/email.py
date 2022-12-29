from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class Email(BaseModel):
    email_id: Optional[int]
    name: Optional[str]
    caption: Optional[str]
    description: Optional[str]
    publisher_config: Optional[str]
    default_template_id: Optional[str]


Email.update_forward_refs()
