from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from typing import List


class ConfigurationPropertyMetadata(BaseModel):
    name: Optional[str]
    attributes: Optional[str]
    validation_rules: Optional[str]
    properties: Optional['List[ConfigurationPropertyMetadata]']


ConfigurationPropertyMetadata.update_forward_refs()
