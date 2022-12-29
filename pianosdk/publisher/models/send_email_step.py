from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.mail import Mail


class SendEmailStep(BaseModel):
    optional: Optional[bool]
    enabled: Optional[bool]
    email: Optional['Mail']


SendEmailStep.update_forward_refs()
