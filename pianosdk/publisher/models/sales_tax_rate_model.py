from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class SalesTaxRateModel(BaseModel):
    charged: Optional[bool]
    charge_rate: Optional[float]
    state_abbr: Optional[str]
    state_id: Optional[str]
    state_name: Optional[str]


SalesTaxRateModel.update_forward_refs()
