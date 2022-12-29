from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.country import Country
from pianosdk.publisher.models.delivery_zone import DeliveryZone
from pianosdk.publisher.models.external_api_field import ExternalAPIField
from pianosdk.publisher.models.resource import Resource
from pianosdk.publisher.models.schedule import Schedule
from pianosdk.publisher.models.term_change_option import TermChangeOption
from pianosdk.publisher.models.vouchering_policy import VoucheringPolicy
from typing import Any
from typing import Dict
from typing import List


class Term(BaseModel):
    term_id: Optional[str]
    aid: Optional[str]
    resource: Optional['Resource']
    type: Optional[str]
    type_name: Optional[str]
    name: Optional[str]
    description: Optional[str]
    product_category: Optional[str]
    verify_on_renewal: Optional[bool]
    create_date: Optional[datetime]
    update_date: Optional[datetime]
    term_billing_descriptor: Optional[str]
    payment_billing_plan: Optional[str]
    payment_billing_plan_description: Optional[str]
    payment_billing_plan_table: Optional['List[Any]']
    payment_allow_renew_days: Optional[int]
    payment_force_auto_renew: Optional[bool]
    payment_is_custom_price_available: Optional[bool]
    payment_is_subscription: Optional[bool]
    payment_has_free_trial: Optional[bool]
    payment_new_customers_only: Optional[bool]
    payment_trial_new_customers_only: Optional[bool]
    payment_allow_promo_codes: Optional[bool]
    payment_renew_grace_period: Optional[int]
    payment_allow_gift: Optional[bool]
    payment_currency: Optional[str]
    currency_symbol: Optional[str]
    payment_first_price: Optional[float]
    schedule: Optional['Schedule']
    schedule_billing: Optional[str]
    custom_require_user: Optional[bool]
    custom_default_access_period: Optional[int]
    adview_vast_url: Optional[str]
    adview_access_period: Optional[int]
    registration_access_period: Optional[int]
    registration_grace_period: Optional[int]
    external_api_id: Optional[str]
    external_api_name: Optional[str]
    external_api_source: Optional[int]
    external_api_form_fields: Optional['List[ExternalAPIField]']
    evt_verification_period: Optional[int]
    evt_fixed_time_access_period: Optional[int]
    evt_grace_period: Optional[int]
    evt_itunes_bundle_id: Optional[str]
    evt_itunes_product_id: Optional[str]
    evt_google_play_product_id: Optional[str]
    evt_cds_product_id: Optional[str]
    evt: Optional['Term']
    collect_address: Optional[bool]
    delivery_zone: Optional['List[DeliveryZone]']
    default_country: Optional['Country']
    vouchering_policy: Optional['VoucheringPolicy']
    billing_config: Optional[str]
    is_allowed_to_change_schedule_period_in_past: Optional[bool]
    collect_shipping_address: Optional[bool]
    change_options: Optional['List[TermChangeOption]']
    shared_account_count: Optional[int]
    shared_redemption_url: Optional[str]
    billing_configuration: Optional[str]
    external_product_ids: Optional[str]
    subscription_management_url: Optional[str]
    custom_data: Optional['Dict[str, Any]']


Term.update_forward_refs()
