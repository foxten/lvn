from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class WebhookResponse(BaseModel):
    status: Optional[str]
    status_localized: Optional[str]
    response_headers: Optional[str]
    response_body: Optional[str]
    create_date: Optional[datetime]
    request_url: Optional[str]
    request_data: Optional[str]


WebhookResponse.update_forward_refs()
