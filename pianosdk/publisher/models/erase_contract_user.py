from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class EraseContractUser(BaseModel):
    contract_id: Optional[str]
    email: Optional[str]
    last_name: Optional[str]
    first_name: Optional[str]


EraseContractUser.update_forward_refs()
