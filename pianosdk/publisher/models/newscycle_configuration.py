from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class NewscycleConfiguration(BaseModel):
    url: Optional[str]
    api_url: Optional[str]
    web_pages_url: Optional[str]
    site_id: Optional[str]
    synchronization_url: Optional[str]


NewscycleConfiguration.update_forward_refs()
