from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.configuration_property_metadata import ConfigurationPropertyMetadata
from typing import List


class PpcWebModel(BaseModel):
    name: Optional[str]
    title: Optional[str]
    source_id: Optional[str]
    properties: Optional['List[ConfigurationPropertyMetadata]']


PpcWebModel.update_forward_refs()
