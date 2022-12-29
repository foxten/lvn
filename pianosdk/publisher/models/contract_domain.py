from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class ContractDomain(BaseModel):
    contract_domain_value: Optional[str]
    contract_domain_id: Optional[str]
    status: Optional[str]
    contract_users_count: Optional[int]
    active_contract_users_count: Optional[int]


ContractDomain.update_forward_refs()
