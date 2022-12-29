from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class SharedAccountParam(BaseModel):
    account_id: Optional[str]
    user_id: Optional[str]
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    personal_name: Optional[str]
    redeemed: Optional[datetime]


SharedAccountParam.update_forward_refs()
