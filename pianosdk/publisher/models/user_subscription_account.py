from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class UserSubscriptionAccount(BaseModel):
    account_id: Optional[str]
    user_id: Optional[str]
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    personal_name: Optional[str]
    redeemed: Optional[datetime]


UserSubscriptionAccount.update_forward_refs()
