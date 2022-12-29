from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class BraintreeMerchantAccountIdEntry(BaseModel):
    currency: Optional[str]
    merchant_account_id: Optional[str]


BraintreeMerchantAccountIdEntry.update_forward_refs()
