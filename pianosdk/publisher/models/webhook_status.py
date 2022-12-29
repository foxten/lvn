from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class WebhookStatus(BaseModel):
    status: Optional[str]
    description: Optional[str]


WebhookStatus.update_forward_refs()
