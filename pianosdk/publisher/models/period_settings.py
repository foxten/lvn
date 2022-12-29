from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.term import Term
from typing import List


class PeriodSettings(BaseModel):
    period_id: Optional[str]
    title_editable: Optional[bool]
    sell_date_editable: Optional[bool]
    begin_date_editable: Optional[bool]
    end_date_editable: Optional[bool]
    period_deletable: Optional[bool]
    dependent_terms: Optional['List[Term]']


PeriodSettings.update_forward_refs()
