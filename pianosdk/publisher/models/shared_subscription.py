from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.user_subscription_account import UserSubscriptionAccount
from typing import List


class SharedSubscription(BaseModel):
    subscription_id: Optional[str]
    term_id: Optional[str]
    uid: Optional[str]
    total_tokens: Optional[int]
    unused_tokens: Optional[int]
    redeemed_tokens: Optional[int]
    shared_accounts: Optional['List[UserSubscriptionAccount]']


SharedSubscription.update_forward_refs()
