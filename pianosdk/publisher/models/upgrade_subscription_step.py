from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.term_short import TermShort


class UpgradeSubscriptionStep(BaseModel):
    from_term: Optional['TermShort']
    to_term: Optional['TermShort']


UpgradeSubscriptionStep.update_forward_refs()
