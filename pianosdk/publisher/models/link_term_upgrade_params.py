from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class LinkTermUpgradeParams(BaseModel):
    from_subscription_id: Optional[str]


LinkTermUpgradeParams.update_forward_refs()
