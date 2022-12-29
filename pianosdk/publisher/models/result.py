from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.error_code import ErrorCode
from pianosdk.publisher.models.error_codes import ErrorCodes
from typing import Any
from typing import List


class Result(BaseModel):
    errors: Optional['List[ErrorCode]']
    error: Optional['ErrorCode']
    or_fail: Optional['Any']
    ok: Optional[bool]
    error_codes: Optional['ErrorCodes']


Result.update_forward_refs()
