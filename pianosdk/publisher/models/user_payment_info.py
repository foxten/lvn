from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class UserPaymentInfo(BaseModel):
    user_payment_info_id: Optional[str]
    description: Optional[str]
    upi_nickname: Optional[str]
    upi_number: Optional[str]
    upi_expiration_month: Optional[int]
    upi_expiration_year: Optional[int]
    upi_postal_code: Optional[str]
    upi_identifier: Optional[str]
    payment_method: Optional[str]
    payment_type: Optional[str]


UserPaymentInfo.update_forward_refs()
