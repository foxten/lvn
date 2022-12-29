from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.action_step_dto import ActionStepDTO


class ActionDTO(BaseModel):
    action_id: Optional[str]
    type: Optional[str]
    number_of_items: Optional[int]
    status: Optional[str]
    schedule_time: Optional[datetime]
    change_subscription_term_step: Optional['ActionStepDTO']
    upgrade_subscription_step: Optional['ActionStepDTO']
    readonly: Optional[bool]
    send_email_step: Optional['ActionStepDTO']
    progress: Optional[int]


ActionDTO.update_forward_refs()
