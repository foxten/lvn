from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class CreditGuardStoredFields(BaseModel):
    terminal_number: Optional[str]
    card_id: Optional[str]
    card_mask: Optional[str]
    card_expiration: Optional[str]
    card_acquirer: Optional[str]
    auth_number: Optional[str]
    slave_terminal_number: Optional[str]
    slave_terminal_sequence: Optional[str]
    shovar: Optional[str]
    cg_uid: Optional[str]
    user_data_1: Optional[str]
    user_data_2: Optional[str]
    user_data_3: Optional[str]
    user_data_4: Optional[str]
    user_data_5: Optional[str]
    user_data_6: Optional[str]
    user_data_7: Optional[str]
    user_data_8: Optional[str]
    user_data_9: Optional[str]
    user_data_10: Optional[str]


CreditGuardStoredFields.update_forward_refs()
