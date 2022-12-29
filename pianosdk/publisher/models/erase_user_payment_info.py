from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class EraseUserPaymentInfo(BaseModel):
    user_payment_info_id: Optional[str]
    billing_zip_code: Optional[str]
    residence_country: Optional[str]
    provider_fields: Optional[str]
    upi_nickname: Optional[str]
    upi_postal_code: Optional[str]
    funding_source: Optional[str]
    pin_code: Optional[str]
    account_number: Optional[str]
    external_transaction_id: Optional[str]
    upi_ext_customer_id: Optional[str]


EraseUserPaymentInfo.update_forward_refs()
