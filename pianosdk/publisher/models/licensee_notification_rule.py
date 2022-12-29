from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from typing import List


class LicenseeNotificationRule(BaseModel):
    notification_rule_id: Optional[str]
    licensee_id: Optional[str]
    contract_id_list: Optional[List[str]]
    parameter: Optional[str]
    condition: Optional[str]
    condition_value: Optional[int]
    is_for_all_contracts: Optional[bool]


LicenseeNotificationRule.update_forward_refs()
