from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class ReportResponse(BaseModel):
    error: Optional[str]
    message: Optional[str]
    report: Optional[str]


ReportResponse.update_forward_refs()
