from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class WebhookConfig(BaseModel):
    key: Optional[str]
    label: Optional[str]
    enabled: Optional[bool]


WebhookConfig.update_forward_refs()
