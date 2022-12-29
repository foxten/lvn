from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.user import User


class InquiryComment(BaseModel):
    comment_id: Optional[str]
    submitter_type: Optional[int]
    create_date: Optional[str]
    message: Optional[str]
    user: Optional['User']
    email: Optional[str]
    name: Optional[str]
    personal_name: Optional[str]
    internal: Optional[str]


InquiryComment.update_forward_refs()
