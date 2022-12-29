from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class Mail(BaseModel):
    email_subject: Optional[str]
    email_body: Optional[str]


Mail.update_forward_refs()
