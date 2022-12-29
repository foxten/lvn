from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class InstrumentDTO(BaseModel):
    require_3ds: Optional[bool]
    instrument_id: Optional[str]
    token: Optional[str]
    transaction_id: Optional[str]
    redirect_url: Optional[str]


InstrumentDTO.update_forward_refs()
