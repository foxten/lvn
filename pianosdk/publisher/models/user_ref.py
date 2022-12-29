from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class UserRef(BaseModel):
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    uid: Optional[str]
    create_date: Optional[datetime]


UserRef.update_forward_refs()
