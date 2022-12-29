from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.term import Term
from pianosdk.publisher.models.user import User
from typing import List


class OfferModel(BaseModel):
    aid: Optional[str]
    name: Optional[str]
    offer_id: Optional[str]
    status: Optional[str]
    deleted: Optional[bool]
    create_date: Optional[datetime]
    create_by: Optional['User']
    update_date: Optional[datetime]
    update_by: Optional['User']
    terms: Optional['List[Term]']


OfferModel.update_forward_refs()
