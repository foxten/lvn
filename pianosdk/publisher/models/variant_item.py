from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class VariantItem(BaseModel):
    name: Optional[str]
    update_date: Optional[int]


VariantItem.update_forward_refs()
