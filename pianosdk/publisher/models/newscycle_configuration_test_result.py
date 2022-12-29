from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class NewscycleConfigurationTestResult(BaseModel):
    is_url_valid: Optional[bool]
    is_api_url_valid: Optional[bool]
    is_web_pages_url_valid: Optional[bool]
    is_site_id_valid: Optional[bool]


NewscycleConfigurationTestResult.update_forward_refs()
