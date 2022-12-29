from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class EraseTransaction(BaseModel):
    tracking_id: Optional[str]
    sender_email: Optional[str]


EraseTransaction.update_forward_refs()
