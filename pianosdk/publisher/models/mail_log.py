from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.app import App
from pianosdk.publisher.models.user import User


class MailLog(BaseModel):
    email_id: Optional[str]
    app: Optional['App']
    user: Optional['User']
    sender: Optional[str]
    recipient: Optional[str]
    reply_to: Optional[str]
    create_date: Optional[str]
    open_date: Optional[str]
    status: Optional[str]
    status_localized: Optional[str]
    reject_reason: Optional[str]
    email_name: Optional[str]
    subject: Optional[str]
    body: Optional[str]


MailLog.update_forward_refs()
