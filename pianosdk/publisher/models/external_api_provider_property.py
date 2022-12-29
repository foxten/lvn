from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class ExternalAPIProviderProperty(BaseModel):
    name: Optional[str]
    value: Optional[str]


ExternalAPIProviderProperty.update_forward_refs()
