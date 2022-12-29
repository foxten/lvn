from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.deployment_app_details import DeploymentAppDetails
from pianosdk.publisher.models.user import User
from typing import List


class DeploymentDetails(BaseModel):
    deployment_id: Optional[str]
    status: Optional[str]
    offer_template_id: Optional[str]
    offer_template_name: Optional[str]
    description: Optional[str]
    version: Optional[int]
    update_date: Optional[datetime]
    update_by: Optional['User']
    applications: Optional['List[DeploymentAppDetails]']


DeploymentDetails.update_forward_refs()
