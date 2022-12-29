from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class ImportUser(BaseModel):
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]


ImportUser.update_forward_refs()
