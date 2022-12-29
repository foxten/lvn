from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.update_access_period_params import UpdateAccessPeriodParams
from typing import List


class UpdateDynamicTermRequest(BaseModel):
    aid: Optional[str]
    term_pub_id: Optional[str]
    rid: Optional[str]
    name: Optional[str]
    currency: Optional[str]
    description: Optional[str]
    periods: Optional['List[UpdateAccessPeriodParams]']
    new_customers_only: Optional[bool]


UpdateDynamicTermRequest.update_forward_refs()
