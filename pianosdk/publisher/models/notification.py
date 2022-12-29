from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class Notification(BaseModel):
    text: Optional[str]
    create_date: Optional[datetime]
    type: Optional[str]
    object_type: Optional[str]
    object_id: Optional[str]
    initiator: Optional[str]


Notification.update_forward_refs()
