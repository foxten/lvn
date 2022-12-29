from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.resource import Resource
from pianosdk.publisher.models.term import Term
from pianosdk.publisher.models.user import User
from pianosdk.publisher.models.user_address import UserAddress
from pianosdk.publisher.models.user_subscription_account import UserSubscriptionAccount
from typing import List


class UserSubscriptionListItem(BaseModel):
    subscription_id: Optional[str]
    auto_renew: Optional[bool]
    next_bill_date: Optional[datetime]
    next_verificaition_date: Optional[datetime]
    payment_method: Optional[str]
    billing_plan: Optional[str]
    user_payment_info_id: Optional[str]
    status: Optional[str]
    status_name: Optional[str]
    status_name_in_reports: Optional[str]
    term: Optional['Term']
    resource: Optional['Resource']
    user: Optional['User']
    start_date: Optional[datetime]
    cancelable: Optional[bool]
    cancelable_and_refundadle: Optional[bool]
    user_address: Optional['UserAddress']
    psc_subscriber_number: Optional[str]
    external_api_name: Optional[str]
    conversion_result: Optional[str]
    is_in_trial: Optional[bool]
    trial_period_end_date: Optional[datetime]
    trial_amount: Optional[float]
    trial_currency: Optional[str]
    end_date: Optional[datetime]
    charge_count: Optional[int]
    upi_ext_customer_id: Optional[str]
    upi_ext_customer_id_label: Optional[str]
    shared_account_limit: Optional[int]
    can_manage_shared_subscription: Optional[bool]
    shared_accounts: Optional['List[UserSubscriptionAccount]']
    cds_account_number: Optional[str]


UserSubscriptionListItem.update_forward_refs()
