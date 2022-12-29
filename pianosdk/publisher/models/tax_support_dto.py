from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class TaxSupportDTO(BaseModel):
    caption: Optional[str]
    tax_format: Optional[str]


TaxSupportDTO.update_forward_refs()
