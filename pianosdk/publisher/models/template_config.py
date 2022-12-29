from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class TemplateConfig(BaseModel):
    name: Optional[str]
    content1_type: Optional[str]
    content2_type: Optional[str]
    content3_type: Optional[str]
    content1_value: Optional[str]
    content2_value: Optional[str]
    content3_value: Optional[str]
    history_list: Optional[str]
    template_type: Optional[str]
    boilerplate_type: Optional[str]


TemplateConfig.update_forward_refs()
