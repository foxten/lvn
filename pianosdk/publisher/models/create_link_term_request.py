from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from typing import Any
from typing import Dict
from typing import List


class CreateLinkTermRequest(BaseModel):
    aid: Optional[str]
    rid: Optional[str]
    name: Optional[str]
    description: Optional[str]
    subscription_management_url: Optional[str]
    external_product_ids: Optional[str]
    custom_data: Optional['Dict[str, Any]']


CreateLinkTermRequest.update_forward_refs()
