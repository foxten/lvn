from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.term_short import TermShort


class ChangeSubscriptionTermStep(BaseModel):
    from_term: Optional['TermShort']
    to_term: Optional['TermShort']
    optional: Optional[bool]
    enabled: Optional[bool]


ChangeSubscriptionTermStep.update_forward_refs()
