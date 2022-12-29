from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.app import App
from pianosdk.publisher.models.braintree_merchant_account_id_entry import BraintreeMerchantAccountIdEntry
from pianosdk.publisher.models.payee_settings_entry import PayeeSettingsEntry
from typing import List


class BraintreeConfiguration(BaseModel):
    configuration_id: Optional[str]
    app: Optional['App']
    source_name: Optional[str]
    title: Optional[str]
    braintree_merchant_id: Optional[str]
    braintree_client_key: Optional[str]
    braintree_merchant_accounts: Optional['List[BraintreeMerchantAccountIdEntry]']
    braintree_public_key: Optional[str]
    braintree_private_key: Optional[str]
    is_disabled: Optional[bool]
    is_editable: Optional[bool]
    is_paypal_enabled: Optional[bool]
    is_apple_pay_enabled: Optional[bool]
    braintree_descriptor: Optional[str]
    braintree_trial_descriptor: Optional[str]
    braintree_app_name_custom_field: Optional[str]
    payee_settings: Optional['List[PayeeSettingsEntry]']
    is_visible: Optional[bool]
    version: Optional[str]
    version_title: Optional[str]
    use_moto: Optional[bool]


BraintreeConfiguration.update_forward_refs()
