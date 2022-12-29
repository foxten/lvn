from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class CountrySimpleModel(BaseModel):
    country_code: Optional[str]
    pub_id: Optional[str]


CountrySimpleModel.update_forward_refs()
