from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.user import User


class LightGlobalTemplate(BaseModel):
    offer_template_id: Optional[str]
    aid: Optional[str]
    name: Optional[str]
    offer_template_name: Optional[str]
    description: Optional[str]
    create_date: Optional[datetime]
    create_by: Optional['User']
    update_date: Optional[datetime]
    update_by: Optional['User']
    publish_date: Optional[datetime]
    version: Optional[int]
    thumbnail_image_url: Optional[str]
    live_thumbnail_image_url: Optional[str]
    is_published: Optional[bool]
    count_variants: Optional[int]
    count_content_fields: Optional[int]
    count_inherited_templates: Optional[int]
    deployment_id: Optional[str]
    status: Optional[str]


LightGlobalTemplate.update_forward_refs()
