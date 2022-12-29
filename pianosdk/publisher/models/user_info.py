from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.price_dto import PriceDTO
from typing import List


class UserInfo(BaseModel):
    name: Optional[str]
    personal_name: Optional[str]
    last_name: Optional[str]
    first_name: Optional[str]
    uid: Optional[str]
    image1: Optional[str]
    create_date: Optional[str]
    access_count: Optional[int]
    next_bill: Optional[str]
    spent_money: Optional['List[PriceDTO]']
    has_trial: Optional[bool]
    last_unresolved_inquiry_id: Optional[str]
    last_issue_id: Optional[str]
    last_comment: Optional[str]
    email: Optional[str]
    last_visit: Optional[datetime]


UserInfo.update_forward_refs()
