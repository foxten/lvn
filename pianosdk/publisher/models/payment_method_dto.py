from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.user_billing_address import UserBillingAddress


class PaymentMethodDTO(BaseModel):
    user_payment_info_id: Optional[str]
    description: Optional[str]
    upi_identifier: Optional[str]
    upi_nickname: Optional[str]
    upi_cardholder: Optional[str]
    upi_first_name: Optional[str]
    upi_last_name: Optional[str]
    upi_number: Optional[str]
    state: Optional[str]
    upi_expiration_month: Optional[int]
    upi_expiration_year: Optional[int]
    upi_postal_code: Optional[str]
    upi_email: Optional[str]
    upi_card_country_code: Optional[str]
    upi_card_zip_code: Optional[str]
    upi_country_state: Optional[str]
    upi_city: Optional[str]
    upi_street: Optional[str]
    currency: Optional[str]
    next_bill_date: Optional[str]
    readonly: Optional[bool]
    can_be_edited: Optional[bool]
    can_be_deleted: Optional[bool]
    can_be_set_default: Optional[bool]
    source_id: Optional[str]
    source_name: Optional[str]
    upi_ext_customer_id: Optional[str]
    upi_ext_customer_id_label: Optional[str]
    upi_ext_payment_id: Optional[str]
    tax_residence_country_code: Optional[str]
    tax_billing_country_code: Optional[str]
    tax_billing_zip_code: Optional[str]
    user_billing_address: Optional['UserBillingAddress']
    stored_fields: Optional[str]


PaymentMethodDTO.update_forward_refs()
