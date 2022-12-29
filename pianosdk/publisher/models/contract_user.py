from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class ContractUser(BaseModel):
    email: Optional[str]
    last_name: Optional[str]
    first_name: Optional[str]
    contract_user_id: Optional[str]
    status: Optional[str]


ContractUser.update_forward_refs()
