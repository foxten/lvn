from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.template_version import TemplateVersion
from typing import List


class AdvancedEmailModel(BaseModel):
    email_id: Optional[int]
    name: Optional[str]
    caption: Optional[str]
    description: Optional[str]
    publisher_config: Optional[str]
    xdays: Optional[int]
    default_xdays: Optional[int]
    template_versions: Optional['List[TemplateVersion]']
    default_template_id: Optional[str]
    system_template_id: Optional[str]


AdvancedEmailModel.update_forward_refs()
