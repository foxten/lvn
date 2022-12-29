from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class RenderedEmail(BaseModel):
    body: Optional[str]
    subject: Optional[str]


RenderedEmail.update_forward_refs()
