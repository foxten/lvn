from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.mail import Mail
from pianosdk.publisher.models.term_short import TermShort


class ActionStepDTO(BaseModel):
    action_id: Optional[str]
    type: Optional[str]
    from_term: Optional['TermShort']
    to_term: Optional['TermShort']
    optional: Optional[bool]
    enabled: Optional[bool]
    email: Optional['Mail']


ActionStepDTO.update_forward_refs()
