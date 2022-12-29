from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class LinkTermSessionParams(BaseModel):
    tracking_id: Optional[str]
    tbc: Optional[str]
    pcid: Optional[str]


LinkTermSessionParams.update_forward_refs()
