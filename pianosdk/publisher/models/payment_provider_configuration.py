from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.app import App
from pianosdk.publisher.models.braintree_merchant_account_id_entry import BraintreeMerchantAccountIdEntry
from pianosdk.publisher.models.currency import Currency
from typing import List


class PaymentProviderConfiguration(BaseModel):
    configuration_id: Optional[str]
    app: Optional['App']
    source_name: Optional[str]
    title: Optional[str]
    braintree_merchant_id: Optional[str]
    braintree_client_key: Optional[str]
    braintree_merchant_accounts: Optional['List[BraintreeMerchantAccountIdEntry]']
    mock_currencies: Optional['List[Currency]']
    is_disabled: Optional[bool]
    is_editable: Optional[bool]
    braintree_descriptor: Optional[str]
    braintree_trial_descriptor: Optional[str]
    is_visible: Optional[bool]


PaymentProviderConfiguration.update_forward_refs()
