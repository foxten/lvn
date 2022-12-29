from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class ImportProfile(BaseModel):
    import_profile_id: Optional[str]
    name: Optional[str]
    source_environment: Optional[str]
    source_aid: Optional[str]
    source_url: Optional[str]
    source_api_token: Optional[str]


ImportProfile.update_forward_refs()
