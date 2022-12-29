from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.offer_template import OfferTemplate
from typing import List


class OfferTemplateCategories(BaseModel):
    category_id: Optional[str]
    category_id_localized: Optional[str]
    count_templates: Optional[int]
    offer_template_models: Optional['List[OfferTemplate]']


OfferTemplateCategories.update_forward_refs()
