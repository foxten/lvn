from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.app import App


class WorldpayConfiguration(BaseModel):
    configuration_id: Optional[str]
    app: Optional['App']
    source_name: Optional[str]
    source_id: Optional[int]
    title: Optional[str]
    is_disabled: Optional[bool]
    is_editable: Optional[bool]
    properties: Optional[str]
    is_visible: Optional[bool]


WorldpayConfiguration.update_forward_refs()
