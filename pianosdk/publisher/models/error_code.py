from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from typing import Any
from typing import List


class ErrorCode(BaseModel):
    code: Optional[int]
    message: Optional[str]
    params: Optional['List[Any]']
    parent_code: Optional[int]


ErrorCode.update_forward_refs()
