from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class DeploymentContentFields(BaseModel):
    name: Optional[str]
    value: Optional[str]
    description: Optional[str]


DeploymentContentFields.update_forward_refs()
