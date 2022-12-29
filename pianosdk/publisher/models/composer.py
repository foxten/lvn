from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class Composer(BaseModel):
    enabled: Optional[bool]


Composer.update_forward_refs()
