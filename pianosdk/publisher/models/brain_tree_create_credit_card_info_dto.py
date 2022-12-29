from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class BrainTreeCreateCreditCardInfoDto(BaseModel):
    braintree_client_token: Optional[str]
    version: Optional[str]
    braintree_client_key: Optional[str]
    authorization_amount: Optional[float]


BrainTreeCreateCreditCardInfoDto.update_forward_refs()
