from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class OfferTemplateContentField(BaseModel):
    content_field_id: Optional[str]
    offer_template_variant_id: Optional[str]
    offer_template_id: Optional[str]
    name: Optional[str]
    description: Optional[str]
    deleted: Optional[bool]
    value: Optional[str]


OfferTemplateContentField.update_forward_refs()
