from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class ResourceTag(BaseModel):
    resource_tag_id: Optional[str]
    name: Optional[str]
    type: Optional[str]


ResourceTag.update_forward_refs()
