from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class Duration(BaseModel):
    value: Optional[int]
    unit: Optional[str]


Duration.update_forward_refs()
