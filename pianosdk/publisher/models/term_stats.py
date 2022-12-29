from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class TermStats(BaseModel):
    pub_id: Optional[str]
    total_sale: Optional[str]
    total_sale_str: Optional[str]
    conversion: Optional[str]
    currency: Optional[str]


TermStats.update_forward_refs()
