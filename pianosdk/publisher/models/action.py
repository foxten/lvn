from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.change_subscription_term_step import ChangeSubscriptionTermStep
from pianosdk.publisher.models.send_email_step import SendEmailStep
from pianosdk.publisher.models.upgrade_subscription_step import UpgradeSubscriptionStep


class Action(BaseModel):
    action_id: Optional[str]
    type: Optional[str]
    number_of_items: Optional[int]
    status: Optional[str]
    schedule_time: Optional[datetime]
    change_subscription_term_step: Optional['ChangeSubscriptionTermStep']
    readonly: Optional[bool]
    send_email_step: Optional['SendEmailStep']
    upgrade_subscription_step: Optional['UpgradeSubscriptionStep']


Action.update_forward_refs()
