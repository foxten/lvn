from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class PriceDTO(BaseModel):
    currency_code: Optional[str]
    amount: Optional[float]
    currency_symbol: Optional[str]
    display: Optional[str]


PriceDTO.update_forward_refs()
