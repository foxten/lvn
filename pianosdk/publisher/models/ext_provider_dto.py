from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.external_api_field import ExternalAPIField
from pianosdk.publisher.models.external_api_property_schema import ExternalAPIPropertySchema
from typing import List


class ExtProviderDTO(BaseModel):
    name: Optional[str]
    properties: Optional['List[ExternalAPIPropertySchema]']
    form_fields: Optional['List[ExternalAPIField]']
    can_enforce_uniqueness: Optional[bool]
    enforce_uniqueness_by_default: Optional[bool]


ExtProviderDTO.update_forward_refs()
