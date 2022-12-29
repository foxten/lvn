from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class GlobalTemplateFilterSubItem(BaseModel):
    id: Optional[str]
    name: Optional[str]
    counter_value: Optional[int]


GlobalTemplateFilterSubItem.update_forward_refs()
