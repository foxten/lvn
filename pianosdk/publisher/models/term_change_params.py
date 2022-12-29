from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class TermChangeParams(BaseModel):
    billing_timing: Optional[str]
    immediate_access: Optional[bool]
    prorate_access: Optional[bool]


TermChangeParams.update_forward_refs()
