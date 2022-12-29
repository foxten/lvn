from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.app import App
from typing import List


class ObiConfiguration(BaseModel):
    configuration_id: Optional[str]
    app: Optional['App']
    source_name: Optional[str]
    source_id: Optional[int]
    title: Optional[str]
    is_editable: Optional[bool]
    is_disabled: Optional[bool]
    is_visible: Optional[bool]
    properties: Optional[str]
    available_countries: Optional[List[str]]


ObiConfiguration.update_forward_refs()
