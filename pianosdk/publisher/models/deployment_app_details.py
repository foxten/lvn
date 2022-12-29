from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.deployment_content_fields import DeploymentContentFields
from pianosdk.publisher.models.deployment_variant_param_dto import DeploymentVariantParamDto
from pianosdk.publisher.models.user import User
from typing import List


class DeploymentAppDetails(BaseModel):
    item_id: Optional[str]
    status: Optional[str]
    aid: Optional[str]
    name: Optional[str]
    app_logo: Optional[str]
    offer_template_id: Optional[str]
    offer_template_name: Optional[str]
    version: Optional[int]
    update_date: Optional[datetime]
    update_by: Optional['User']
    content_field_list: Optional['List[DeploymentContentFields]']
    variant_list: Optional['List[DeploymentVariantParamDto]']
    selected: Optional[str]


DeploymentAppDetails.update_forward_refs()
