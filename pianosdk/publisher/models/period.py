from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class Period(BaseModel):
    name: Optional[str]
    period_id: Optional[str]
    sell_date: Optional[datetime]
    begin_date: Optional[datetime]
    end_date: Optional[datetime]
    deleted: Optional[bool]
    create_date: Optional[datetime]
    update_date: Optional[datetime]
    is_sale_started: Optional[bool]
    is_active: Optional[bool]


Period.update_forward_refs()
