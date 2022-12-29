from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class Fieldset(BaseModel):
    config_id: Optional[int]
    fieldset_id: Optional[int]
    name: Optional[str]
    create_date: Optional[datetime]
    update_date: Optional[datetime]


Fieldset.update_forward_refs()
