from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class ChurnPreventionTemplateVersion(BaseModel):
    template_id: Optional[str]
    version_id: Optional[int]
    version: Optional[int]
    name: Optional[str]


ChurnPreventionTemplateVersion.update_forward_refs()
