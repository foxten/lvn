from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class ExternalAPIPropertySchema(BaseModel):
    field_name: Optional[str]
    title: Optional[str]
    description: Optional[str]


ExternalAPIPropertySchema.update_forward_refs()
