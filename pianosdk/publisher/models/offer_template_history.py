from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.offer_template_sub_history import OfferTemplateSubHistory
from typing import List


class OfferTemplateHistory(BaseModel):
    history_content: Optional[str]
    history_comment: Optional[str]
    offer_template_history_event: Optional[str]
    offer_template_id: Optional[str]
    history_list: Optional['List[OfferTemplateSubHistory]']


OfferTemplateHistory.update_forward_refs()
