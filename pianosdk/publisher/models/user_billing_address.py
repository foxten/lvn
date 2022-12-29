from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.country_simple_model import CountrySimpleModel
from pianosdk.publisher.models.region_simple_model import RegionSimpleModel


class UserBillingAddress(BaseModel):
    line1: Optional[str]
    line2: Optional[str]
    line3: Optional[str]
    country: Optional['CountrySimpleModel']
    region: Optional['RegionSimpleModel']
    region_name: Optional[str]
    city: Optional[str]
    zip: Optional[str]
    type: Optional[str]
    verified: Optional[str]
    address_pub_id: Optional[str]


UserBillingAddress.update_forward_refs()
