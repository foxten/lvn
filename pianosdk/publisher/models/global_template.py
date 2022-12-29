from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.offer_template_content_field import OfferTemplateContentField
from pianosdk.publisher.models.offer_template_variant import OfferTemplateVariant
from pianosdk.publisher.models.user import User
from typing import List


class GlobalTemplate(BaseModel):
    offer_template_id: Optional[str]
    token_type: Optional[str]
    aid: Optional[str]
    name: Optional[str]
    app_logo: Optional[str]
    offer_template_name: Optional[str]
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
    category_id: Optional[str]
    thumbnail_image_url: Optional[str]
    live_thumbnail_image_url: Optional[str]
    status: Optional[str]
    is_published: Optional[bool]
    count_variants: Optional[int]
    variant_list: Optional['List[OfferTemplateVariant]']
    count_content_fields: Optional[int]
    content_field_list: Optional['List[OfferTemplateContentField]']
    count_inherited_templates: Optional[int]
    deployment_id: Optional[str]


GlobalTemplate.update_forward_refs()
