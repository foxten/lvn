from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class EraseUser(BaseModel):
    uid: Optional[str]
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]


EraseUser.update_forward_refs()
