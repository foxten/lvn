from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from typing import Any
from typing import Dict
from typing import List


class UpdateLinkTermRequest(BaseModel):
    aid: Optional[str]
    term_pub_id: Optional[str]
    rid: Optional[str]
    name: Optional[str]
    description: Optional[str]
    subscription_management_url: Optional[str]
    external_product_ids: Optional[str]
    custom_data: Optional['Dict[str, Any]']


UpdateLinkTermRequest.update_forward_refs()
