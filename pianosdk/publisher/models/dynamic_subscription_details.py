from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.dynamic_subscription_access_period_info import DynamicSubscriptionAccessPeriodInfo


class DynamicSubscriptionDetails(BaseModel):
    active_period: Optional['DynamicSubscriptionAccessPeriodInfo']
    future_period: Optional['DynamicSubscriptionAccessPeriodInfo']


DynamicSubscriptionDetails.update_forward_refs()
