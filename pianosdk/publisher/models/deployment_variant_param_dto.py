from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.deployment_content_fields import DeploymentContentFields
from typing import List


class DeploymentVariantParamDto(BaseModel):
    offer_template_variant_id: Optional[str]
    name: Optional[str]
    content_field_list: Optional['List[DeploymentContentFields]']


DeploymentVariantParamDto.update_forward_refs()
