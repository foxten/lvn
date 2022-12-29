from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.deployment_app import DeploymentApp
from pianosdk.publisher.models.user import User
from typing import List


class DeploymentListItem(BaseModel):
    deployment_id: Optional[str]
    global_template_version: Optional[int]
    deployment_date: Optional[datetime]
    user: Optional['User']
    status: Optional[str]
    applications: Optional['List[DeploymentApp]']


DeploymentListItem.update_forward_refs()
