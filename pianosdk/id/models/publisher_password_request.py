from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class PublisherPasswordRequest(BaseModel):
    aid: Optional[str]
    uid: Optional[str]
    password: Optional[str]
    current_password: Optional[str]


PublisherPasswordRequest.update_forward_refs()
