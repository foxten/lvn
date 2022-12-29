from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class DeploymentApp(BaseModel):
    aid: Optional[str]
    name: Optional[str]
    app_logo: Optional[str]


DeploymentApp.update_forward_refs()
