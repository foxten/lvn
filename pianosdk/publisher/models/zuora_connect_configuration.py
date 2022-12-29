from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class ZuoraConnectConfiguration(BaseModel):
    email: Optional[str]
    zuora_api_token: Optional[str]


ZuoraConnectConfiguration.update_forward_refs()
