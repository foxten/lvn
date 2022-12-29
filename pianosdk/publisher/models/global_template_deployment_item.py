from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class GlobalTemplateDeploymentItem(BaseModel):
    item_id: Optional[str]
    template_id: Optional[str]
    aid: Optional[str]
    status: Optional[str]


GlobalTemplateDeploymentItem.update_forward_refs()
