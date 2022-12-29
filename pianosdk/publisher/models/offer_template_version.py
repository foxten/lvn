from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.external_css import ExternalCss
from pianosdk.publisher.models.offer_template_content_field import OfferTemplateContentField
from pianosdk.publisher.models.offer_template_variant import OfferTemplateVariant
from pianosdk.publisher.models.user import User
from typing import List


class OfferTemplateVersion(BaseModel):
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
    content1_type: Optional[str]
    content2_type: Optional[str]
    content1_value: Optional[str]
    content2_value: Optional[str]
    version: Optional[int]
    publish_date: Optional[datetime]
    type: Optional[str]
    type_id: Optional[str]
    boilerplate_type: Optional[str]
    boilerplate_type_id: Optional[str]
    category_id: Optional[str]
    thumbnail_image_url: Optional[str]
    live_thumbnail_image_url: Optional[str]
    published: Optional[bool]
    external_css_list: Optional['List[ExternalCss]']
    has_preview: Optional[bool]
    status: Optional[str]
    variant_list: Optional['List[OfferTemplateVariant]']
    content_field_list: Optional['List[OfferTemplateContentField]']
    is_global: Optional[bool]
    is_inherited: Optional[bool]


OfferTemplateVersion.update_forward_refs()
