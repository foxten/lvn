from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.composer import Composer
from pianosdk.publisher.models.my_account import MyAccount
from pianosdk.publisher.models.redemption_page import RedemptionPage
from pianosdk.publisher.models.subscription_restrictions import SubscriptionRestrictions


class AppFeatures(BaseModel):
    my_account: Optional['MyAccount']
    composer: Optional['Composer']
    subscription_restrictions: Optional['SubscriptionRestrictions']
    redemption_page: Optional['RedemptionPage']
    is_payment_mock_enabled: Optional[bool]
    is_publisher_dashboard_localization_enabled: Optional[bool]
    is_checkout_authentication_in_separate_state: Optional[bool]


AppFeatures.update_forward_refs()
