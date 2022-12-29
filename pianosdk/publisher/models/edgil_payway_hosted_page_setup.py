from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class EdgilPaywayHostedPageSetup(BaseModel):
    request_id: Optional[str]
    reply_url: Optional[str]
    action_url: Optional[str]


EdgilPaywayHostedPageSetup.update_forward_refs()
