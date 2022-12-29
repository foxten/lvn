from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class TemplateVariable(BaseModel):
    template_variable_id: Optional[str]
    name: Optional[str]
    description: Optional[str]
    test_value: Optional[str]
    parent_id: Optional[str]


TemplateVariable.update_forward_refs()
