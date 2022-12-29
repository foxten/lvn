from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class DnsForwardingConfig(BaseModel):
    aid: Optional[str]
    config_id: Optional[str]
    status: Optional[str]
    cname_status: Optional[str]
    ssl_status: Optional[str]
    content: Optional[str]


DnsForwardingConfig.update_forward_refs()
