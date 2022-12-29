from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from typing import List


class TermConversionData(BaseModel):
    aid: Optional[str]
    offer_id: Optional[str]
    term_id: Optional[str]
    offer_template_id: Optional[str]
    template_id: Optional[str]
    uid: Optional[str]
    user_country: Optional[str]
    user_region: Optional[str]
    user_city: Optional[str]
    zip: Optional[str]
    latitude: Optional[str]
    longitude: Optional[str]
    user_agent: Optional[str]
    locale: Optional[str]
    hour: Optional[str]
    url: Optional[str]
    browser: Optional[str]
    platform: Optional[str]
    operating_system: Optional[str]
    tags: Optional[str]
    content_created: Optional[str]
    content_author: Optional[str]
    content_section: Optional[str]
    campaigns: Optional[List[str]]


TermConversionData.update_forward_refs()
