from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class CountryModel(BaseModel):
    country_name: Optional[str]
    country_code: Optional[str]


CountryModel.update_forward_refs()
