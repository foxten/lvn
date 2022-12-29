from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.offer_template_content_field import OfferTemplateContentField
from pianosdk.publisher.models.offer_template_variant import OfferTemplateVariant
from pianosdk.publisher.models.user import User
from typing import List


class OfferTemplate(BaseModel):
    offer_template_id: Optional[str]
    token_type: Optional[str]
    aid: Optional[str]
    app_name: Optional[str]
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
    boilerplate_type: Optional[str]
    boilerplate_type_id: Optional[str]
    category_id: Optional[str]
    thumbnail_image_url: Optional[str]
    live_thumbnail_image_url: Optional[str]
    status: Optional[str]
    is_published: Optional[bool]
    count_variants: Optional[int]
    variant_list: Optional['List[OfferTemplateVariant]']
    archived_date: Optional[datetime]
    archived_by: Optional['User']
    content_field_list: Optional['List[OfferTemplateContentField]']
    can_be_global: Optional[bool]
    is_global: Optional[bool]
    is_inherited: Optional[bool]


OfferTemplate.update_forward_refs()
