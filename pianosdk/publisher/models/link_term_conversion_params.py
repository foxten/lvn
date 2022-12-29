from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.link_term_payment_params import LinkTermPaymentParams


class LinkTermConversionParams(BaseModel):
    conversion_id: Optional[str]
    create_date: Optional[int]
    payment: Optional['LinkTermPaymentParams']


LinkTermConversionParams.update_forward_refs()
