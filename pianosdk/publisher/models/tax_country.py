from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class TaxCountry(BaseModel):
    country_name: Optional[str]
    country_code: Optional[str]
    requires_zip_code: Optional[bool]
    need_residence: Optional[bool]
    include_billing: Optional[bool]
    tax_support: Optional[str]


TaxCountry.update_forward_refs()
