from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.country_model import CountryModel


class AvalaraOriginAddress(BaseModel):
    address_line1: Optional[str]
    country: Optional['CountryModel']
    city: Optional[str]
    postal_code: Optional[str]
    state: Optional[str]
    reference_field: Optional[str]


AvalaraOriginAddress.update_forward_refs()
