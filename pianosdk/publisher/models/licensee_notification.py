from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class LicenseeNotification(BaseModel):
    notification_id: Optional[str]
    licensee_id: Optional[str]
    contract_id: Optional[str]
    message: Optional[str]
    parameter: Optional[str]
    condition: Optional[str]
    condition_value: Optional[int]
    create_date: Optional[datetime]


LicenseeNotification.update_forward_refs()
