from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.user import User


class GlobalTemplateVersion(BaseModel):
    offer_template_id: Optional[str]
    token_type: Optional[str]
    name: Optional[str]
    description: Optional[str]
    aid: Optional[str]
    type: Optional[str]
    type_id: Optional[str]
    category_id: Optional[str]
    published: Optional[bool]
    publish_date: Optional[datetime]
    version: Optional[int]
    create_date: Optional[datetime]
    create_by: Optional['User']
    update_date: Optional[datetime]
    update_by: Optional['User']
    status: Optional[str]


GlobalTemplateVersion.update_forward_refs()
