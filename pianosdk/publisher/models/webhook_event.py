from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.user import User
from pianosdk.publisher.models.webhook_response import WebhookResponse


class WebhookEvent(BaseModel):
    webhook_id: Optional[str]
    status: Optional[str]
    status_localized: Optional[str]
    retried: Optional[str]
    create_date: Optional[datetime]
    update_date: Optional[datetime]
    last_webhook_response: Optional['WebhookResponse']
    user: Optional['User']
    type: Optional[str]
    type_localized: Optional[str]
    event: Optional[str]
    event_localized: Optional[str]
    event_type: Optional[str]
    responses_count: Optional[int]


WebhookEvent.update_forward_refs()
