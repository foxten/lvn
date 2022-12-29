from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.user import User


class CheckoutFlowLightModel(BaseModel):
    checkout_flow_id: Optional[str]
    name: Optional[str]
    checkout_flow_type: Optional[str]
    description: Optional[str]
    create_date: Optional[datetime]
    create_by: Optional['User']
    update_date: Optional[datetime]
    update_by: Optional['User']
    is_passwordless: Optional[bool]


CheckoutFlowLightModel.update_forward_refs()
