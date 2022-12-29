from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class TransactionItem(BaseModel):
    user_payment_id: Optional[str]
    name: Optional[str]
    payment_billing_plan: Optional[str]
    amount: Optional[float]
    refund_amount: Optional[float]
    payment_method: Optional[str]
    user_payment_info_id: Optional[str]
    payment_method_type: Optional[str]
    status: Optional[str]
    resource_image_url: Optional[str]
    resource_name: Optional[str]
    rid: Optional[str]
    currency_code: Optional[str]
    customer: Optional[str]
    _date: Optional[datetime]
    external_id: Optional[str]
    refund_external_tx_id: Optional[str]
    uid: Optional[str]
    term_id: Optional[str]
    price: Optional[float]
    price_display: Optional[str]
    currency: Optional[str]
    expires: Optional[int]
    taxed_price: Optional[str]
    upi_ext_customer_id: Optional[str]
    upi_ext_customer_id_label: Optional[str]
    transaction_type: Optional[str]
    currency_symbol: Optional[str]


TransactionItem.update_forward_refs()
