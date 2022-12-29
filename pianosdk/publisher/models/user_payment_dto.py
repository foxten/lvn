from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.term import Term
from pianosdk.publisher.models.term_conversion_subscription import TermConversionSubscription


class UserPaymentDTO(BaseModel):
    user_payment_id: Optional[str]
    create_date: Optional[str]
    user_payment_state: Optional[str]
    renewal: Optional[bool]
    amount: Optional[float]
    price: Optional[str]
    currency: Optional[str]
    refundable: Optional[bool]
    subscription: Optional['TermConversionSubscription']
    term: Optional['Term']
    tax: Optional[float]
    tax_billing_plan: Optional[str]
    payment_method: Optional[str]
    upi_ext_customer_id: Optional[str]
    upi_ext_customer_id_label: Optional[str]
    external_transaction_id: Optional[str]
    tracking_id: Optional[str]
    original_price: Optional[str]


UserPaymentDTO.update_forward_refs()
