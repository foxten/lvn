from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class VoucheringPolicy(BaseModel):
    vouchering_policy_id: Optional[str]
    vouchering_policy_billing_plan: Optional[str]
    vouchering_policy_billing_plan_description: Optional[str]
    vouchering_policy_redemption_url: Optional[str]


VoucheringPolicy.update_forward_refs()
