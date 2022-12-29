from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class TermChangeOption(BaseModel):
    term_change_option_id: Optional[str]
    from_term_id: Optional[str]
    from_term_name: Optional[str]
    from_resource_id: Optional[str]
    from_resource_name: Optional[str]
    from_billing_plan: Optional[str]
    to_term_id: Optional[str]
    to_term_name: Optional[str]
    to_resource_id: Optional[str]
    to_resource_name: Optional[str]
    to_billing_plan: Optional[str]
    billing_timing: Optional[str]
    immediate_access: Optional[bool]
    prorate_access: Optional[bool]
    description: Optional[str]
    include_trial: Optional[bool]
    to_scheduled: Optional[bool]
    from_scheduled: Optional[bool]
    shared_account_count: Optional[int]
    collect_address: Optional[bool]


TermChangeOption.update_forward_refs()
