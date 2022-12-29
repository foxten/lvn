from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.country import Country
from pianosdk.publisher.models.region import Region
from pianosdk.publisher.models.user import User


class UserAddressHistory(BaseModel):
    create_date: Optional[datetime]
    update_date: Optional[datetime]
    revision: Optional[datetime]
    revision_type: Optional[int]
    user: Optional['User']
    first_name: Optional[str]
    last_name: Optional[str]
    company_name: Optional[str]
    address1: Optional[str]
    address2: Optional[str]
    city: Optional[str]
    postal_code: Optional[str]
    phone: Optional[str]
    user_address_id: Optional[str]
    deleted: Optional[bool]
    region: Optional['Region']
    additional_fields: Optional[str]
    country: Optional['Country']
    update_by: Optional[str]
    create_by: Optional[str]


UserAddressHistory.update_forward_refs()
