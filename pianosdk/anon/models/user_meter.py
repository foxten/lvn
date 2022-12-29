from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class UserMeter(BaseModel):
    paywall_id: Optional[int]
    views: Optional[int]
    views_left: Optional[int]
    max_views: Optional[int]
    cookie_name: Optional[str]
    cookie_domain: Optional[str]
    cookie_value: Optional[str]
    cookie_expires: Optional[int]
    track_page_view: Optional[bool]
    state: Optional[str]
    offer_id: Optional[str]
    curtain_template_id: Optional[str]
    reminder_template_id: Optional[str]
    show_close_button: Optional[bool]
    show_reminder: Optional[bool]
    expires: Optional[int]
    can_renew: Optional[bool]
    renewal_days_remaining: Optional[int]
    country_code: Optional[str]
    region: Optional[str]
    reason: Optional[str]
    meter_name: Optional[str]


UserMeter.update_forward_refs()
