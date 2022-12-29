from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class TemplateUserModel(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    uid: Optional[str]


TemplateUserModel.update_forward_refs()
