from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.app import App


class OpenpayConfiguration(BaseModel):
    configuration_id: Optional[str]
    app: Optional['App']
    source_name: Optional[str]
    source_id: Optional[int]
    title: Optional[str]
    is_editable: Optional[bool]
    is_disabled: Optional[bool]
    properties: Optional[str]
    is_visible: Optional[bool]


OpenpayConfiguration.update_forward_refs()
