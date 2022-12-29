from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class ZuoraConfiguration(BaseModel):
    api_key: Optional[str]
    api_secret: Optional[str]
    entity_name: Optional[str]
    entity_id: Optional[str]


ZuoraConfiguration.update_forward_refs()
