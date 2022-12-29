from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class ResourceDto(BaseModel):
    rid: Optional[str]
    aid: Optional[str]
    deleted: Optional[bool]
    disabled: Optional[bool]
    create_date: Optional[datetime]
    update_date: Optional[datetime]
    publish_date: Optional[datetime]
    name: Optional[str]
    description: Optional[str]
    image_url: Optional[str]
    type: Optional[str]
    type_label: Optional[str]
    bundle_type: Optional[str]
    bundle_type_label: Optional[str]
    purchase_url: Optional[str]
    resource_url: Optional[str]
    external_id: Optional[str]
    is_fbia_resource: Optional[bool]


ResourceDto.update_forward_refs()
