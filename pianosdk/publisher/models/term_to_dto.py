from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.billing_timing_option import BillingTimingOption
from pianosdk.publisher.models.term_change_params import TermChangeParams
from typing import List


class TermToDto(BaseModel):
    to_term_id: Optional[str]
    to_term_name: Optional[str]
    to_resource_id: Optional[str]
    to_resource_name: Optional[str]
    to_billing_plan: Optional[str]
    collect_address: Optional[bool]
    shared_account_count: Optional[int]
    term_change_option: Optional['TermChangeParams']
    available_billing_timings: Optional['List[BillingTimingOption]']
    changable: Optional[bool]
    tooltip: Optional[str]
    term_change_option_id: Optional[str]
    prorate_restricted: Optional[bool]
    to_term_amount: Optional[float]
    to_term_amount_display: Optional[str]
    to_term_currency: Optional[str]
    prorate_amount: Optional[float]
    prorate_amount_display: Optional[str]
    prorate_refund_amount: Optional[float]


TermToDto.update_forward_refs()
