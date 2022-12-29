from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.schedule_period import SchedulePeriod
from typing import List


class Contract(BaseModel):
    contract_id: Optional[str]
    aid: Optional[str]
    name: Optional[str]
    create_date: Optional[datetime]
    landing_page_url: Optional[str]
    licensee_id: Optional[str]
    seats_number: Optional[int]
    is_hard_seats_limit_type: Optional[bool]
    rid: Optional[str]
    schedule_id: Optional[str]
    contract_is_active: Optional[bool]
    contract_type: Optional[str]
    contract_conversions_count: Optional[int]
    contract_periods: Optional['List[SchedulePeriod]']


Contract.update_forward_refs()
