from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.price_dto import PriceDTO
from typing import List


class UserDetails(BaseModel):
    uid: Optional[str]
    name: Optional[str]
    personal_name: Optional[str]
    image1: Optional[str]
    access_count: Optional[int]
    spent_money: Optional['List[PriceDTO]']
    create_date: Optional[datetime]
    email: Optional[str]
    last_active_date: Optional[datetime]


UserDetails.update_forward_refs()
