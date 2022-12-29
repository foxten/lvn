from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.link_term_purchase_params import LinkTermPurchaseParams
from pianosdk.publisher.models.link_term_upgrade_params import LinkTermUpgradeParams
from typing import List


class LinkTermSubscriptionParams(BaseModel):
    subscription_id: Optional[str]
    user_id: Optional[str]
    product_ids: Optional[List[str]]
    state: Optional[str]
    upgrade: Optional['LinkTermUpgradeParams']
    valid_to: Optional[int]
    purchase: Optional['LinkTermPurchaseParams']
    custom: Optional[str]


LinkTermSubscriptionParams.update_forward_refs()
