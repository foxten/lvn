from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class OfferTemplateSubHistory(BaseModel):
    history_content: Optional[str]
    offer_template_history_event: Optional[str]
    offer_template_id: Optional[str]
    offer_template_variant_id: Optional[str]
    offer_template_version_id: Optional[str]


OfferTemplateSubHistory.update_forward_refs()
