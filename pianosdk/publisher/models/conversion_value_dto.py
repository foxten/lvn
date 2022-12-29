from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class ConversionValueDTO(BaseModel):
    currency: Optional[str]
    conversion_category: Optional[str]
    value: Optional[float]


ConversionValueDTO.update_forward_refs()
