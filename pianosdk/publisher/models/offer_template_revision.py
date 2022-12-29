from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.user import User


class OfferTemplateRevision(BaseModel):
    offer_template_id: Optional[str]
    token_type: Optional[str]
    aid: Optional[str]
    name: Optional[str]
    description: Optional[str]
    deleted: Optional[bool]
    create_date: Optional[datetime]
    create_by: Optional['User']
    update_date: Optional[datetime]
    update_by: Optional['User']
    publish_date: Optional[datetime]
    version: Optional[int]
    type: Optional[str]
    type_id: Optional[str]
    is_published: Optional[bool]
    content_loaded: Optional[bool]
    content1_type: Optional[str]
    content2_type: Optional[str]
    content1_value: Optional[str]
    content2_value: Optional[str]


OfferTemplateRevision.update_forward_refs()
