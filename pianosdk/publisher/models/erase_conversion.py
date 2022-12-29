from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class EraseConversion(BaseModel):
    term_conversion_id: Optional[str]
    browser: Optional[str]
    experience: Optional[str]
    user_address: Optional[str]
    geo_location: Optional[str]
    zone: Optional[str]


EraseConversion.update_forward_refs()
