from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.webhook_config import WebhookConfig
from typing import List


class WebhookSettings(BaseModel):
    url: Optional[str]
    enabled: Optional[bool]
    configs: Optional['List[WebhookConfig]']


WebhookSettings.update_forward_refs()
