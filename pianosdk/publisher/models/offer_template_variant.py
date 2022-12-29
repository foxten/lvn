from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.offer_template_content_field import OfferTemplateContentField
from pianosdk.publisher.models.template_user_model import TemplateUserModel
from typing import List


class OfferTemplateVariant(BaseModel):
    offer_template_variant_id: Optional[str]
    offer_template_id: Optional[str]
    name: Optional[str]
    description: Optional[str]
    live_thumbnail_image_url: Optional[str]
    deleted: Optional[bool]
    create_date: Optional[datetime]
    create_by: Optional['TemplateUserModel']
    update_date: Optional[datetime]
    update_by: Optional['TemplateUserModel']
    archived_date: Optional[datetime]
    archived_by: Optional['TemplateUserModel']
    status: Optional[str]
    content_field_list: Optional['List[OfferTemplateContentField]']
    is_inherited: Optional[bool]


OfferTemplateVariant.update_forward_refs()
