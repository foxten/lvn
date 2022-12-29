from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class Reminder(BaseModel):
    reminder_id: Optional[str]
    paywall_id: Optional[int]
    offer_template_id: Optional[str]
    version: Optional[str]
    show_reminder_initial: Optional[int]
    show_reminder_recur: Optional[int]


Reminder.update_forward_refs()
