from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.create_access_period_params import CreateAccessPeriodParams
from typing import List


class CreateDynamicTermRequest(BaseModel):
    aid: Optional[str]
    rid: Optional[str]
    name: Optional[str]
    currency: Optional[str]
    description: Optional[str]
    periods: Optional['List[CreateAccessPeriodParams]']


CreateDynamicTermRequest.update_forward_refs()
