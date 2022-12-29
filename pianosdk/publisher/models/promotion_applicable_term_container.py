from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.term import Term
from pianosdk.publisher.models.term_stats import TermStats
from typing import List


class PromotionApplicableTermContainer(BaseModel):
    terms: Optional['List[Term]']
    termstats: Optional['List[TermStats]']


PromotionApplicableTermContainer.update_forward_refs()
