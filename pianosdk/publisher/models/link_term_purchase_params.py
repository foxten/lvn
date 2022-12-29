from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class LinkTermPurchaseParams(BaseModel):
    trial: Optional[str]


LinkTermPurchaseParams.update_forward_refs()
