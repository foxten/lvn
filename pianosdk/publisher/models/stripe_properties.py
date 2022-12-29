from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class StripeProperties(BaseModel):
    public_key: Optional[str]


StripeProperties.update_forward_refs()
