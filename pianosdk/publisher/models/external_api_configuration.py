from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.app import App
from pianosdk.publisher.models.external_api_field import ExternalAPIField
from pianosdk.publisher.models.external_api_provider_property import ExternalAPIProviderProperty
from pianosdk.publisher.models.term import Term
from typing import List


class ExternalAPIConfiguration(BaseModel):
    external_api_id: Optional[str]
    name: Optional[str]
    app: Optional['App']
    form_fields: Optional['List[ExternalAPIField]']
    properties: Optional['List[ExternalAPIProviderProperty]']
    provider: Optional[str]
    description: Optional[str]
    terms: Optional['List[Term]']
    enforce_uniqueness: Optional[bool]
    can_update_fields: Optional[bool]
    force_grace_period: Optional[int]
    external_api_source_id: Optional[int]
    default_verification_period: Optional[int]


ExternalAPIConfiguration.update_forward_refs()
