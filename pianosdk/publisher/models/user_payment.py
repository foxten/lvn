from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.credit_guard_stored_fields import CreditGuardStoredFields
from pianosdk.publisher.models.term import Term
from pianosdk.publisher.models.user import User
from pianosdk.publisher.models.user_subscription import UserSubscription
from typing import Any


class UserPayment(BaseModel):
    user_payment_id: Optional[str]
    create_date: Optional[str]
    renewal: Optional[bool]
    refund_amount: Optional[float]
    remaining_amount: Optional[float]
    amount: Optional[float]
    price: Optional[str]
    refund_currency: Optional[str]
    currency: Optional[str]
    refundable: Optional[bool]
    subscription: Optional['UserSubscription']
    term: Optional['Term']
    user: Optional['User']
    tax: Optional[float]
    hst_amount: Optional[float]
    qst_amount: Optional[float]
    pst_amount: Optional[float]
    gst_amount: Optional[float]
    tax_rate: Optional[float]
    hst_rate: Optional[float]
    qst_rate: Optional[float]
    pst_rate: Optional[float]
    gst_rate: Optional[float]
    tax_billing_country_code: Optional[str]
    tax_residence_country_code: Optional[str]
    zip_code: Optional[str]
    tax_billing_zip_code: Optional[str]
    geo_location_country: Optional[str]
    tax_billing_plan: Optional[str]
    billing_plan: Optional[str]
    user_payment_info_id: Optional[str]
    payment_method: Optional[str]
    transaction_details: Optional['Any']
    source_id: Optional[int]
    source_name: Optional[str]
    upi_ext_customer_id: Optional[str]
    upi_ext_customer_id_label: Optional[str]
    external_transaction_id: Optional[str]
    tracking_id: Optional[str]
    original_price: Optional[str]
    status: Optional[str]
    status_value: Optional[int]
    refunded_amount: Optional[float]
    refund_amount_recalculated: Optional[bool]
    invoice_number: Optional[str]
    stored_fields: Optional['CreditGuardStoredFields']


UserPayment.update_forward_refs()
