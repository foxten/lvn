from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class OneSourceConfiguration(BaseModel):
    onesource_url: Optional[str]
    onesource_username: Optional[str]
    onesource_password: Optional[str]
    onesource_company_name: Optional[str]


OneSourceConfiguration.update_forward_refs()
