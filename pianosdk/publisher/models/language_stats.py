from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class LanguageStats(BaseModel):
    template_keys_count: Optional[int]
    template_keys_abandoned: Optional[int]
    unit_keys_count: Optional[int]
    unit_keys_abandoned: Optional[int]
    locale: Optional[str]


LanguageStats.update_forward_refs()
