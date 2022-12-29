from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class PaySourceDTO(BaseModel):
    id: Optional[int]
    identifier: Optional[str]
    caption: Optional[str]
    title: Optional[str]
    custom_title: Optional[str]


PaySourceDTO.update_forward_refs()
