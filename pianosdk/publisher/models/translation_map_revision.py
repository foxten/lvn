from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class TranslationMapRevision(BaseModel):
    version: Optional[int]
    create_date: Optional[datetime]
    update_date: Optional[datetime]
    published: Optional[bool]
    editing: Optional[bool]
    draft: Optional[bool]


TranslationMapRevision.update_forward_refs()
