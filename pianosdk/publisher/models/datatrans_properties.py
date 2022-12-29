from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.currency import Currency
from typing import List


class DatatransProperties(BaseModel):
    currencies: Optional['List[Currency]']
    merch_id: Optional[str]


DatatransProperties.update_forward_refs()
